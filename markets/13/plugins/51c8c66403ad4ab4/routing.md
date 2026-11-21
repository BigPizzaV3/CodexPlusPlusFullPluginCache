# Extract routing contract

All bundled skills share the `extract` MCP at `https://api.extract.to/mcp` and
one OAuth authorization. Skills are procedures, not separate connections.

| Skill | Owns | Handoff |
| --- | --- | --- |
| Setup | Authentication, connector/configuration, streams, mappings, connection setup | Diagnostics for failed execution; operations for ongoing management |
| Operations | Inventory, health summaries, schedules, enablement, requested runs | Setup for configuration; diagnostics for failure investigation |
| Diagnostics | Failed syncs, run errors, stale ingestion | Setup for an authorized fix; analysis for business interpretation |
| Analysis | Warehouse queries, business metrics, company context | Diagnostics when evidence indicates stale or failed ingestion |

Use `account_*` for pipelines and `insights_*` for warehouse/business analysis.
Resolve any host-added namespace from the actual tool inventory. Never invent a
missing tool or bypass missing permissions using another endpoint.

“Why did revenue fall?” starts with analysis. Stale data can justify a read-only
handoff to diagnostics. “Why did this sync fail?” starts with diagnostics.
“Show failing connections” starts with inventory; explaining a failure uses
`account_diagnose_connection`. “Connect Google Ads to Snowflake” starts with setup.

Multiple skills may cooperate within one task; no exclusive domain selection or
routing call is required. Carry explicit connector/connection IDs and history
references, but IDs do not grant authorization. Ask a focused question only if
unresolved ambiguity changes the target or action. Never guess among warehouses.

Investigation does not authorize writes or reruns. Preserve explicit confirmation
for creation, schedule changes and manual runs. Read-only handoffs need no extra
approval. Prefer MCP configuration tools; credentials/provider consent use secure
browser links, never chat. Use native forms or guided input when widgets are absent.

Start each analytical question with `insights_start_analysis`, reuse `history_ref`
for corrected queries. Save the current result directly; the backend enforces current saving permission. Follow result pagination and
report incomplete history or truncated results. Task `next_step` gives a status
tool and terminal states; it is not permission to retry a failed mutation.

## Answer feedback

Save completed Extract results directly without a preference precheck or repeated
consent prompts. The user approves answer saving when connecting; the backend checks
current permission on every save and rejects disabled or unavailable permission.
If saving is rejected or unavailable, deliver the answer without a feedback link.
Use get_answer_saving_preference only when the user asks to view or change saving
settings, or needs a settings_url to enable feedback links. Only the user may change
that setting in the authenticated browser; a chat reply, rating, or tool result cannot
enable it. If the user says stop saving, stop immediately in this chat and use
get_answer_saving_preference to provide settings_url to disable future saves across chats.
After saving, show only the returned non-null feedback_url. Never invent a link.
If already rated, submit the explicit rating with the returned answer_ref without
another invitation; otherwise show a “Leave feedback” link once after the answer.
The link opens a form; users choose Helpful or Not helpful there and submit.
Consent to saving is never a rating. No prompts on intermediate steps, clarifications,
feedback receipts, or sample-data downloads requiring only “Saved to <path>”.


For completed Extract results, use
`insights_save_answer(history_ref, question, answer, source_account_connector_ids)` for analysis with that result
and the exact question used to start it, or
`save_response(domain, question, answer, submission_id, history_ref?)` for setup,
operations, and diagnostics. Start a new analysis for a different question; reuse
its history reference only for corrections. Use a brief task-specific intent as question.
Never transmit conversation history, raw transcripts, prior turns, unrelated messages,
credentials, or authentication links. Do not save every chat turn automatically.

Feedback links require a valid Extract browser session authorized for the saved
answer's account. The session's active account and the authenticated user's original
account are eligible; impersonating another account does not require switching back
or signing in again to rate an answer owned by the original account. Let the browser
form check authorization rather than blocking or redirecting eligible sessions.
Include `feedback_url` only if non-null; otherwise relay explicit ratings through
`submit_feedback` using `answer_ref`. Sample-data download responses must contain
only `Saved to <path>`; do not append feedback invitations or URLs.
Users can choose 👍 helpful or 👎 not helpful; reason and comment are optional. The link opens a form, and opening it never submits a rating. Show the complete answer before the feedback invitation and link. Saving does not
automatically open a widget or browser preview; the user opens the linked form.
Tools and the browser form work without widgets or skills. The form/widget displays the exact rated answer.

Call `submit_feedback(answer_ref, rating, submission_id, reason?, comment?)` only
for an explicit user judgment about an identifiable saved answer. Keep the original
`answer_ref` when a user rates an earlier revision. Ask if the target is ambiguous.
Never invent satisfaction or turn an observed query/tool failure into a user rating.
Use a fresh UUID `submission_id` for each deliberate submission; reuse the same ID
and arguments on transport retries. Do not request feedback on intermediate steps,
clarifications, or feedback receipts. If saving fails or returns no `answer_ref`,
do not invent a feedback target or link.

### Analysis relationship and source arguments

Every analysis start (including granular `insights_record_question`) requires
`question_kind="new"` for an independent question, even in the same chat, or
`question_kind="follow_up"` with the exact saved `parent_answer_ref` when the
question depends on an earlier answer. Independent questions must omit the parent.
Each question gets a new history reference; only retries/corrections reuse it.
Every analysis save requires `source_account_connector_ids`: list all connector
IDs used, including metadata-only sources, or `[]` if none were used. Use discovered
IDs, never guesses. Refresh tool definitions after deployment.
