# Financial document import

## Complete proposals and review transport (#7136)

MCP preview and new apply requests require a separate `completeness` object. The
host records this declaration from the complete extraction and reviewed choices
**before transport**. Never reconstruct it from the received request or response.
It has these exact fields:

```json
{
  "version": 1,
  "document_id": "<proposal document UUID>",
  "file_id": "<immutable proposal file UUID>",
  "source_revision": "<context source revision>",
  "source_line_count": 81,
  "line_decision_count": 0,
  "actualization_count": 0,
  "quote_mapping_count": 0,
  "adjustment_distribution_count": 0,
  "adjustment_targets": []
}
```

Each distribution has one declaration in `adjustment_targets` with its stable
`adjustment_line_id` and `item_line_count`. Use explicit zero counts for absent
optional collections. Their counts need not equal source count. Explicit line
decisions still cover every source row exactly once. All references must retain
valid stable source identities. Count mismatches, including declared 81/received
50 or missing zero-value/offsetting rows, fail closed regardless of matching totals.
The declaration detects transport loss; it cannot prove OCR extracted the PDF
faithfully. Review extraction against the actual immutable source as before.

Capacity is 100 source lines, with up to 100 decisions, actualizations, quote
mappings or distributions, and 100 targets per distribution. The ten-allocation
per-line, uncertainty, 20-budget and 1,500 aggregate operation bounds remain.
Import arguments are limited to 1,048,576 UTF-8 JSON bytes. Oversized proposals
fail explicitly; never split one invoice into fake invoices or substitute a
partial subtotal. The internal AP composition permits 100 allocation targets
within the aggregate import bound; standalone financial-action tools retain
50 allocations and 150 operations.

Small previews return `preview_complete: true`. Larger previews return only
`source_revision`, `preview_time`, `preview_complete: false` and `preview_page`.
A preview page uses the existing JSON-chunk contract: `encoding`, `offset`,
`total_characters`, `json_chunk`, and `next_cursor`. Repeat the unchanged proposal
and completeness declaration, first-page `preview_time`, and `next_cursor` as
`preview_cursor` until null. Check offsets are contiguous from zero and the final
UTF-16 length equals the unchanged `total_characters`; concatenate chunks without
separators and parse once. Restart completely on stale/expired continuation.
Pages are capped at 192 Ki UTF-16 code units and the duplicated MCP response at
480 KiB, leaving JSON-RPC envelope room. A final page alone is not complete review.

The assembled preview contains `completeness.expected` and `.received`, the full
proposal/plan and `review_digest`. Verify counts and every row/decision/adjustment
and operation. To detect output loss or changes, remove only `review_digest` and
`preview_complete` from the complete preview, recursively sort object keys while
preserving array order, JSON serialize without whitespace, and SHA-256 the UTF-8
bytes. Match the lowercase hexadecimal result to `review_digest`. Never simply
echo the server digest without recomputing it from all received output.

After explicit confirmation, apply the unchanged proposal and `completeness`,
`preview_time`, `expected_revision`, stable `request_id`, `confirm_preview: true`
and the locally computed `reviewed_output_digest`. Missing/changed declarations
or review digest cannot authorize a new write. An exact pre-change successful
request can still replay its durable receipt without these fields; a legacy
request with no receipt fails closed. Retrying completed requests does not redo
financial work.

These are server-side contracts. Local unit/HTTP and disposable database evidence
must be distinguished from actual connected-client acceptance after discovery
refresh; server success alone does not establish that the reported connector
clipping boundary is fixed. #7122 context assembly remains independently required.
