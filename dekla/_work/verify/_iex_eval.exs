# Evaluator for verify/iex: one chapter per run. Input: a JSON file
#   {"prelude": path, "modules": [{"line": n, "code": src}], "sessions": [{"line": n, "lines": [...]}]}
# Output (stdout, last line): JSON list of results, one per module and per IEx input.
[file] = System.argv()
data = File.read!(file) |> JSON.decode!()
Code.put_compiler_option(:ignore_module_conflict, true)
{:ok, _} = Application.ensure_all_started(:ex_unit)
{:ok, _} = Application.ensure_all_started(:mix)

quiet = fn fun ->
  # warnings and diagnostics go to stderr; program output is captured separately
  ExUnit.CaptureIO.with_io(:stderr, fn -> ExUnit.CaptureIO.with_io(fun) end) |> elem(0)
end

if data["prelude"], do: quiet.(fn -> Code.require_file(data["prelude"]) end)

module_results =
  for m <- data["modules"] do
    {status, msg} =
      quiet.(fn ->
        try do
          Code.compile_string(m["code"], "book")
          {"ok", ""}
        rescue
          e -> {"error", Exception.message(e) |> String.slice(0, 300)}
        end
      end)
      |> elem(0)

    %{"kind" => "module", "line" => m["line"], "status" => status, "message" => msg}
  end

prompt = ~r/^\s*(?:iex(?:\(\d+\))?>|\d+>)\s?(.*)$/
helper = ~r/^(c |r |h\(|h |i |exports |ls$|pwd$|v\(|Ctrl|cd )/

complete? = fn src ->
  case Code.string_to_quoted(src) do
    {:ok, _} -> true
    {:error, {_, _, ""}} -> false          # the error is at the end of the input: more lines follow
    {:error, {_, msg, _}} ->
      m = inspect(msg)
      not (m =~ "missing terminator" or m =~ "end of file" or m =~ "expression is incomplete" or
             m =~ "unexpected reserved word: end")
  end
end

# split a session into [{line, input, expected_lines}]
split = fn lines, first_line ->
  lines
  |> Enum.with_index(first_line)
  |> Enum.reduce({[], nil}, fn {l, n}, {acc, cur} ->
    case Regex.run(prompt, l) do
      [_, input] ->
        acc = if cur, do: [cur | acc], else: acc
        {acc, %{line: n, input: input, expected: [], open: not complete?.(input)}}

      nil when cur == nil ->
        {acc, nil}

      nil ->
        if cur.open do
          input = cur.input <> "\n" <> l
          {acc, %{cur | input: input, open: not complete?.(input)}}
        else
          {acc, %{cur | expected: cur.expected ++ [l]}}
        end
    end
  end)
  |> then(fn {acc, cur} -> Enum.reverse(if cur, do: [cur | acc], else: acc) end)
end

{session_results, _} =
  Enum.flat_map_reduce(data["sessions"], [], fn s, binding ->
    Enum.map_reduce(split.(s["lines"], s["line"]), binding, fn e, b ->
      base = %{"kind" => "input", "line" => e.line, "input" => e.input,
               "expected" => Enum.join(e.expected, "\n")}

      if Regex.match?(helper, String.trim(e.input)) do
        {Map.put(base, "status", "skipped"), b}
      else
        {res, out} =
          quiet.(fn ->
            ExUnit.CaptureIO.with_io(fn ->
              try do
                {r, nb} = Code.eval_string(e.input, b, file: "iex")
                {:ok, r, nb}
              rescue
                err -> {:error, "** (" <> inspect(err.__struct__) <> ") " <> Exception.message(err)}
              catch
                kind, val -> {:error, "** (#{kind}) #{inspect(val)}"}
              end
            end)
          end)
          |> elem(0)

        case res do
          {:ok, r, nb} ->
            got = out <> inspect(r, pretty: true, width: 80, limit: 50)
            {Map.merge(base, %{"status" => "ok", "got" => got}), nb}

          {:error, msg} ->
            {Map.merge(base, %{"status" => "error", "got" => out <> msg}), b}
        end
      end
    end)
  end)

IO.puts("\n" <> JSON.encode!(module_results ++ session_results))
