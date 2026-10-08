# Auditing a chapter against its sources

An auditor is a fresh agent that did not write the chapter: a writer who knows what a source "means" reads over what it actually says. The coordinator starts one per `AUDIT` line of a class agent's phase C report and passes it this instruction with the three paths of that line.

> Audit one chapter of a study book against its sources. Chapter: `<chapter path>`. Sources: `<excerpt path>`, which holds the source units that feed this chapter. Class profile: `<profile path>` (if not "none", read it first for the course's terms and conventions). Change nothing.
>
> Read the excerpt in full, then the chapter. For every unit of the excerpt, find each definition, rule, statement of fact, condition or exception, example, code example with its output, formula, table and figure, and check that the chapter carries it with the same meaning. The chapter is an explanation, not a copy: other wording, another order, merged examples and silently fixed typos are fine, and so is code shown in a newer version's output format.
>
> Do not report: anything a unit marks as "partly cut on purpose"; course administration, installation steps, link lists; style. If a unit "also feeds" other chapters, the item may be there: still report it, marked `(maybe elsewhere)`.
>
> Report one line per problem, nothing else:
> `<unit>: missing: <the item, in a few words>`
> `<unit>: differs: <what the source says> / <what the chapter says>`
> If there is no problem, report `no problems`.

Cost: the excerpt holds only the units that feed the chapter, and for an extended chapter only this run's units (`cover.py excerpt --pending`), so an audit costs about one chapter plus its new sources, however large the book has grown.
