# Croatian provision context

This optional workflow applies only to deployments that expose
`get_legal_context` in the connected tool list. It is disabled in the submitted
1.1.2 deployment; use the article, structure, chapter, and related-document
tools there instead.

When available, use `get_legal_context` for `@hr` when a question depends on a
provision's definitions, scope, conditions, exclusions, or references
elsewhere in the act.

1. Pass the retrieved document URI and article. For a historical question pass
   the relevant `as_of`, or the selected `version_id`; use the returned
   `regulation_version_id` to pin subsequent calls in this act.
2. Start with `max_depth=1`. Increase to 2 or 3 only when unresolved local
   references matter to the question. Depth controls traversal, not text length.
3. Read `article.text` and the relevant `related_provisions[].text` in full.
   Inspect `relationships`, evidence segments, `unresolved_references`, and
   `coverage`. Candidate roles such as definition, limitation, or exception
   are suggestions for review; a citation edge does not prove a legal effect.
4. Retrieve material external acts or annexes separately when supported. Each
   different act needs its own version for the relevant date; do not reuse
   one act's version identifier for another act.
5. If `coverage.ready_for_conclusion` is false, resolve the material gaps or
   explain why the retrieved evidence cannot settle applicability. A true flag
   is retrieval metadata, not a legal determination. Empty candidate lists
   never prove that no exceptions or limiting rules exist.

Keep each quote linked to its own source and version. Explain the relationship
only when the wording supports it, and distinguish explicit conditions from
your interpretation.

If this tool is unavailable, use supported article/structure retrieval to
inspect explicit references and state the remaining coverage limit. `@eu` and
`@fr` do not support this context tool; do not imply that their full context
was checked by calling it on another jurisdiction.
