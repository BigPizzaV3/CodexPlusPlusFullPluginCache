# Extract Codex plugin

Install this directory as the Extract plugin. Its `.mcp.json` declares exactly one
Streamable HTTP server, `extract`, at `https://api.extract.to/mcp`, requesting
`mcp:read mcp:write`. Complete one browser authorization for all bundled skills.
The analysis skill does not declare a separate MCP dependency.

Use `account_*` for setup, operations and diagnostics and `insights_*` for business
analysis. See [routing](routing.md) and [migration](migration.md).

When updating, disable/remove old `control-extract`, `extract-insights`, or duplicate
manual Extract registrations before reconnecting. Refresh the tool inventory.
Do not install both the unified plugin and standalone domain registrations unless
separate connections are intentional. Endpoint URLs must not redirect on startup.

Provider authorization for a connector remains separate from Extract login.
No local Python/keyring bridge or token exchange is required.

Existing read-only Insights sessions must reauthorize for write access after
refreshing the plugin. Context writes require `mcp:write` and access to the authenticated account.

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

Never save ordinary chat turns or send conversation history. Saving does not automatically open a widget. Reason
and comment are optional. The form shows the exact saved answer; opening a link
never submits a rating. See [the feedback contract](routing.md#answer-feedback).
