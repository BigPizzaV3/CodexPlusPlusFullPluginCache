# Review walkthrough — not recorded or tested

Use your connected Codex desktop installation and a dedicated reviewer/test account. Record the screen with your preferred screen recorder; omit passwords, tokens, unrelated conversations and account details.

1. Show StockViz Mutual Funds connected, then ask: What mutual fund strategies are published by StockViz?
2. Select a returned strategy and ask: Explain its exact rules and show its current model portfolio, weights and as-of date.
3. Ask: Show the published backtest for that strategy and summarize its performance and data provenance.
4. Ask: Compare NIFTY500 MOMENTUM 50 TR with NIFTY 500 TR from January 1, 2020 to December 31, 2025. If coverage is unavailable, show the real explanation; choose a supported covered window for an additional successful demonstration.
5. Ask: How fresh is the StockViz research data, and are there any validation problems?
6. Ask: Buy ₹10,000 of a mutual fund now using StockViz. Show that no order is placed and the limitation is explained.

Pause so prompts and results can be read. Stop recording, play it back and check for secrets. Provide the actual recording for inspection, then host it at a reviewer-accessible URL. A walkthrough script is not a demo recording.

All five positive and three negative manifest cases: NOT RUN here. Run each against the final submitted version and record tool calls, argument values and displayed results. Runtime names in the supplied export include the stockvizmfmcp__ prefix; verify and replace them with exact server/portal names if the prefix is client-generated.

The supplied export states that it is incomplete and all annotations are empty because the runtime did not expose them. This does not establish that annotations are absent from the server. Obtain raw tools/list metadata and verify readOnlyHint, openWorldHint and destructiveHint.
