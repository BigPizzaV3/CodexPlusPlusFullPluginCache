# Example — forecast calculation and conditional publication

Illustrative workflow, not evidence of an executed test. Use the tools and schemas exposed in the current session.

**User:** Calculate a Q4 2026 forecast for my Deals board. Treat Won and Lost as closed; show the forecast and publication plan first.

1. Run `get_user_context` and resolve the board; read its schema.
2. Resolve Stage, Value, Close Date and Forecast Category by type and meaning. Ask if classifications are unclear. Any new category column needs its own approved proposal and the current column-type schema.
3. Obtain date-filter guidelines. Read the period using a `between` rule with two plain YYYY-MM-DD dates; paginate and disclose any cap.
4. Exclude lost/omit records, then classify each remaining deal once into Closed-won, Committed, Best-case or Pipeline. Report known-value subtotals and missing-value counts; a won record with no value is not zero revenue.
5. Show the calculated table and limitations.
6. Before proposing native publication, obtain `all_widgets_schema` and verify support for the required filters. If unavailable, offer the chat table or a separately approved doc and create no empty dashboard.
7. Search for the exact proposed dashboard title. The current dashboard tool has no description/skill-marker field; stop for user direction if a candidate exists or search is incomplete.
8. Show and approve the concrete dashboard/widget batch. `create_dashboard` uses `workspace_id`, `board_ids`, `name` and optional `kind`. `create_widget` settings must follow the current widget schemas.
9. Report the actual created dashboard/widget count and link. Disclose any unverified rendering, values or filters; do not claim successful publication from a plan alone.

No amount edits, notifications or automatic sharing occur in this example.
