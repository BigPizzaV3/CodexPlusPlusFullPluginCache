# Collection tools in functions.exec

- When functions.exec is available, never call a collection-returning research tool directly. Treat search, list,
  feed, crawl, and other array-returning tools as collection-returning. Invoke
  them only as nested tools inside functions.exec, keep their full responses in
  JavaScript, and never pass a raw collection to text() or notify(). This rule
  overrides general advice to emit each completed nested tool result.
- Each functions.exec call has fresh JavaScript state. In the same invocation,
  await the collection calls, unwrap their MCP CallToolResult envelopes, do the
  deterministic work below, and call text() with the compact result. Never call
  a paid retrieval again merely to process a response from an earlier
  functions.exec invocation. Follow the tool's documented output contract.
  Marble plugin tools return their JSON payload in structuredContent; their
  content[].text completion message is not JSON. For get_data_operation, read
  structuredContent.results when the operation is complete and require an
  array before projecting records. Composio tools retain the upstream MCP
  response contract; unwrap their actual response instead of assuming they
  use Marble's envelope.
- Parsing is not projection. Unwrapping a response only extracts its records; it does not filter records or remove fields. Never emit its return
  value directly, even when the gateway has already normalized the records.
  Build new, smaller objects containing only fields needed for relevance
  judgment and the widget. Do not copy whole records with object spread or
  hide them in nested objects or serialized strings. Omit unused fields and
  nested data, but preserve the evidence needed to judge every candidate.
- Use that JavaScript only for deterministic work: enforce unambiguous structured
  constraints, remove exact duplicates, normalize and sort fields, and project
  each remaining record to the fields needed for relevance judgment and the
  widget. Projection must not remove records. A hard-constraint filter may
  remove a record only when a present structured field directly contradicts
  that constraint; keep records whose field is missing, unfamiliar, or
  ambiguous. If the response cannot be unwrapped confidently, emit a bounded
  description of its shape and do not retry the retrieval. Emit only the compact
  records plus kept and removed counts. Do not encode semantic relevance,
  inferred categories, or keyword heuristics in the code. Keep every record
  that requires model judgment.

Use only APIs and output-budget options documented by the current host. Marble’s native runtime token budget does not configure ChatGPT. If functions.exec is unavailable, use the available host tools with bounded pages; do not invent an execution tool or drop candidates to hide output limits.
