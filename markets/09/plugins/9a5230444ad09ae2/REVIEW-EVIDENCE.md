# Supplied development transcript assessment

Evidence: references/development-chat.md supplied by the creator. This is a recorded textual transcript, not an independently executed test or a video demo. Final manifest prompts still need to be run against the submitted version.

| Workflow | Assessment | Evidence / limit |
|---|---|---|
| Strategy discovery | Passed in supplied transcript | list_strategies returned factor-momentum; answer retained identifier and as-of date. |
| Rules and portfolio | Passed in supplied transcript | get_strategy_definition and get_strategy_portfolio called with factor-momentum; rules and 100% model weight supported by responses. |
| Backtest summary | Passed in supplied transcript | get_backtest_summary used linked run ID from earlier responses; displayed metrics agree with returned values. User-facing answer omitted calculation provenance; final review prompt should explicitly request it. |
| Backtest metric comparison | Passed in supplied transcript | get_backtest_metrics used run ID, three series and exact full-coverage dates; displayed results agree with responses. |
| Data freshness | Partial evidence | get_data_quality returned published catalogs, counts and no warnings. Assistant inferred dates from version identifiers and stated validated without explicit validation outcome/timestamps. Report these as version labels unless confirmed by dedicated fields. |
| Index comparison | Blocked for successful comparison | All calls returned data_gap and no winner. Honest handling observed. Dates omitted despite supplied schema listing them required; reconcile actual server metadata with export. |
| Buy request | Passed in supplied transcript | Refusal to place orders; no trading call shown. |
| Private broker balance negative | Passed in updated supplied transcript | Explained lack of private broker account access; no tool call shown. |
| Unsupported index negative | Passed in updated supplied transcript | Explained S&P 500 unsupported and listed approved indices; no tool call shown. |

Tool labels in transcript use stockviz-mutual-funds.<name>, now reflected in draft review cases. Verify server/portal canonical names before final upload. Complete raw tools/list and annotations remain unavailable.

Creator supplied demo URL https://www.youtube.com/watch?v=1KmzGcfvfG4. Retrieval was blocked by the available web tool, so playback, public accessibility, content coverage and absence of secrets remain unverified. All three negative behaviors now supported by the supplied transcript; final submission test runs remain pending.
