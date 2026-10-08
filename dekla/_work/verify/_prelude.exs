# Modules the slides use in IEx sessions without showing them as one piece (fpea.ex of the
# lectures, assembled from dp26a-fp1ea s37 and dp26a-fp2ea s8, s9, s37, s38).
defmodule Fpea do
  def fac(0), do: 1
  def fac(n), do: n * fac(n - 1)

  def sum_of_squares(a, b), do: sqr(a) + sqr(b)
  defp sqr(a), do: a * a

  def sum_of_sqrs_b5(a, b \\ 5), do: sqr(a) + sqr(b)
  def sum_of_sqrs_a6b5(a \\ 6, b \\ 5), do: sqr(a) + sqr(b)

  def sum([]), do: 0
  def sum(xs), do: hd(xs) + sum(tl(xs))

  def append([], ys), do: ys
  def append(xs, ys), do: [hd(xs) | append(tl(xs), ys)]

  def revapp([], ys), do: ys
  def revapp(xs, ys), do: revapp(tl(xs), [hd(xs) | ys])
end

