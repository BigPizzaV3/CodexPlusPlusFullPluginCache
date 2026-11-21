# Routing regression cases

`routing-cases.json` preserves all 17 routing specifications from the working
1.1.5 browser package byte for byte. These are manual specifications, not an
executable suite. One case in the original positive group expects clarification;
judge tool eligibility by each expected behavior, not by its original group.
There are 6 eligible-search cases and 11 no-call cases.

The public-submission package declares exactly one MCP server in `mcp.json`.
Its separate official review set is in `plugin.json` at
`extensions.com.openai.review.test_cases`: five positive cases and three negative
cases. The 17-case reference file is not automatically registered or executed by
the importer. It retains additional cancellation, stored-search-history, current
location, and mixed search/booking coverage.

All cases are NOT RUN as part of this packaging task. Local structural checks
are not live model-routing tests. Run each case in a fresh chat with the complete
plugin selected. Inspect actual calls, arguments, and displayed results. Each
no-call case must produce zero MCP calls, including no preliminary rental search.

Use the official cases for the submission demo; use the larger reference set for
regression testing. Some retained regression prompts have fixed 2026 dates: check
the dates before future testing rather than treating past-date results as proof
of current search behavior. The new official cases use March 12-15, 2027.
