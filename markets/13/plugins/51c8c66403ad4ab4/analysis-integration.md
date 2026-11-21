# Analysis integration

Analysis shares the `extract` registration at `/mcp` with account operations.
Use `insights_start_analysis(question, question_kind, parent_answer_ref?)` with a brief task-specific intent, never
conversation history or prior turns, for task history, company context and eligible
connector discovery, then inspect relevant metadata and run read-only SQL.
Keep history_ref across corrections. Save completed Extract results directly without
a preference precheck; the backend enforces current saving permission. If saving is
rejected or unavailable, deliver the answer without a feedback link. Granular tools
remain available for follow-up calls. Account inventory does not confer SQL access.

See [routing](routing.md) for skill handoffs and [migration](migration.md) for
standalone `/mcp-analyze`, legacy credentials, and client rollout requirements.

## Context updates

The unified endpoint exposes `insights_update_company_context` for account-wide
business context and `insights_update_metadata` for table/column context.
Standalone Insights exposes the corresponding unprefixed names.

Table updates take `account_connector_id`, `database_id`, `schema_id`, `table_id`,
`customer_context`, `expected_revision`, `reason`, and `approval_excerpt`, returning
the structured `MetadataOverrideWriteResult`. Read the current table page with
`insights_get_table`, then call `insights_get_table_context` for editable customer
prose and its revision. Show the full proposed replacement customer context,
preserve unrelated customer definitions, and obtain explicit approval in a later
reply. Submit only customer prose and the exact returned revision; never copy
generated schema or statistics. An empty `customer_context` clears this layer.
On a revision conflict, reread and reconcile before retrying. If `migration_required`
is true, review `legacy_markdown` to extract customer definitions rather than
copying the entire old page. Generated metadata continues to refresh independently;
warehouse schema/data are unchanged.

Both writes allow authenticated MCP users with `mcp:write` in their authorized account. Table writes also
retain connector authorization and catalog validation. Both are non-read-only,
potentially destructive, non-idempotent (audit events), and account-restricted.
The read/approve/preserve workflow is client-enforced: the stateless backend does
not verify a prior read, independently authenticate the approval excerpt, or
compare replacements for preservation. See the [backend trust boundary](../../../dp-backend/app/mcp/README.md#mcp-context-updates).
The merged plugin already requests `mcp:write`; no new scopes or login are needed
for clients with that grant. Deploy the backend and refresh tool discovery and
the analysis skill to use table updates.


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
