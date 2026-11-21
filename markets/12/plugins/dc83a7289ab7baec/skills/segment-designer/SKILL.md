---
name: segment-designer
description: Create, edit, inspect or count Reteno dynamic segments with live account definitions and the bundled Segment Designer SDK. Use for audience conditions, exclusions, event windows, segment changes and unsaved audience calculations. Does not require a browser or a saved segment for counting.
---

# Segment Designer

Read [OPERATING_MANUAL.md](OPERATING_MANUAL.md) before building a segment. The local runner
validates and prepares a request; the host calls the selected authenticated Reteno MCP.
Use the installed skill directory, not a path relative to the user's project.

1. Resolve the selected organization through MCP. Fetch `list_segment_definitions(for_sdk=true)`;
   for an edit pass the target `segment_id`. Save the manifest and download its `catalogRef`
   with `<plugin-root>/scripts/transfer.py`. Keep its SHA-256, expiry and account binding.
2. Read the relevant definitions and [SDK reference](references/client/SDK_API_REFERENCE.md).
   Resolve exact field, event, application and option IDs through live MCP. Never invent them.
3. For an edit, call `get_segment(segment_id=..., include_schema=true)` and save the complete
   result. The runner hydrates its backend schema before applying a bounded SDK mutation.
4. Write a JavaScript module using the supplied `segment` handle, check each mutation result,
   and return `segment.finish()`. Run the command in the manual. Review diagnostics and the
   formula, including include/exclude logic and date interpretation.
5. Call the tool and arguments from the generated request file through the same MCP connection.
   Local `persisted:false` is preparation only. Verify the response with
   `python3 <plugin-root>/scripts/receipts.py segment --response <receipt> [--expected-id <id>]`.
   The backend verifies retrievability, not byte equality of its normalized schema. Inspect
   fresh conditions and explain that distinction when exact semantic verification is unavailable.
6. Retain the destination ID. On an ambiguous create, find the exact name before any retry;
   never create duplicates because read-back failed. On edit, re-read and reconcile intervening
   changes rather than overwriting them from an old export. There is no server hash precondition.

For audience size only, use `--mode count`; call `count_segment_contacts` and verify with
`receipts.py count`. Never save a segment merely to count. Use `get_segment_contacts` for an
existing saved segment. Read [audience guidance](../reteno-analytics/references/audience-counts.md)
for population scope, rate limits, unknown outcomes and partial comparisons.

Reteno channels only. Viber and Telegram are unavailable even if a generic upstream catalog
mentions them. Do not import private warehouse data or change contacts.
