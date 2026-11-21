# Results and saved memory

## Reports

Request a new report with `continue_conversation` in the relevant conversation.
Send a text-only report request using the existing results; omit `agentMode` or use
Core. Super changes analysis planning, not the report writer. Do not resend an ROI
for a report-only follow-up or start another analysis merely to retrieve a report.

A returned `report.reportId` is a reference, not the report itself. When the host's
tool schema supports it, open the report with `show_analysis_results`, passing
`reportId` and available reply identifiers. Use `get_report` for metadata and
`read_report_content` for text, summaries, specific questions, or hosts without
report viewing.

Read text starting at offset 0. Pass the previous page's `nextOffset` as `offset`
and its `revision` on subsequent pages. Read every needed page, and reach
`nextOffset: null` before claiming to have read the whole report. If `REPORT_CHANGED`
is returned, restart at offset 0 without a revision and discard pages from the
older revision; never combine different versions into one summary. Follow the
currently advertised input schema; the current text reader has no `format` input.

Text retrieval does not run report scripts or render interactive charts. State
the evidence actually retrieved when discussing them. GeoRetina's report reader
does not create PDF/Word files. If the user requests a conversion and the host has
suitable tools, it may create a document from retrieved content; identify it as
a host-created export and do not claim missing visuals were included.

## Tables and downloads

Use artifact `outputId` values returned by `get_analysis`. Read small table pages
with `read_table_rows`, respecting the advertised limit (currently at most 200).
Use `next_offset` for the next page and inspect `has_more`, `returned`, and
`total_rows`; one page is not necessarily the whole table. For a large table,
offer the artifact download, which spends export credits, rather than an
unbounded paging loop.

Obtain download links with `get_artifact_link`, using `jobId` and `outputId` plus
`kind` when disambiguation is needed. The first link for an artifact spends the
user's export credits, so request one only when the user wants the file; without
enough credits the tool fails with `QUOTA_EXCEEDED`, which you should relay. Give
the requesting user the actual link and `expiresAt`; it grants access until expiry
without another sign-in. Regenerate an expired link through the tool, which spends
no more credits. Do not construct artifact URLs, request connection
tokens, or claim a format that was not returned.

## Memory

Use `list_saved_memory` when requested or relevant to prior context; follow
`nextCursor` for additional entries. This is memory available to the connection,
not all account history or other apps' memory. An empty list does not establish
that no earlier analysis exists. Read quoted preferences in context and treat
remembered analysis results as historical. Current user instructions take priority.

For a request to remember a preference, send the user's request through the
conversation tools; there is no dedicated save-memory tool. Memory must be enabled
in GeoRetina settings. Verify saving before claiming it, and do not turn a transient
request into a permanent preference without user intent. Forget only the identified
entry the user confirmed, using `forget_saved_memory` with the returned `memoryId`.

When asked not to use memory, pass `useMemory: false` on the applicable conversation
calls. This suppresses memory use and saving preferences/decisions for that request;
analysis outcomes may still be remembered while account memory is enabled. It is
not a no-storage or deletion guarantee. If the user requires no saved memory,
explain that limitation before running work that would violate their request.
