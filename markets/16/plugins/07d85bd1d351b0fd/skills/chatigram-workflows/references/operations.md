# Resource operations

Use the selected organization's current tool schemas and authorization. Resolve real resource IDs through list/read tools. Counts and permissions are point-in-time; writes may still be rejected. Report the actual reason rather than bypassing a limit. Missing OAuth scope consent uses the existing connection. Chatigram has no purchasing or plan-changing tools; return the billing link when needed.

## Databases and records

Use list_databases, list_tables and inspect_table to resolve column IDs, names and types. create_database takes an explicit organizationId, name and requestId; preview then commit the same request. inspect_database reads its metadata and tables; rename_database retains identity and configuration. Use supported create_table, create_column and record tools for the selected database.

Preview schema changes and describe affected columns or data loss. Table/column deletion previews include conservative stored-reference counts for saved workflows, active MCP drafts/runs and current Page drafts/publications. Known references block commit; removing a draft reference does not remove a published reference. Resolve dependencies through the corresponding authorized tools and create a fresh preview. Counts disclose no protected configuration or resource identities from another scope. Computed resource IDs are outside this scan; it is not a global referential lock. Table deletion requires the separate structural-deletion confirmation in the main skill. Do not invent a missing database-deletion tool.

read_records uses 1-based pages. Use actual column IDs or supported system keys _id and _createdAt for filters/sorts. Record writes map actual column UUIDs to supported strings, numbers, booleans or null. IMAGE values refer to an existing owned image. Read the returned shape: unfiltered rows can expose id, createdAt and values; filtered/sorted rows can use column UUID keys.

Record operations can trigger enabled workflows and webhooks. Operate only within the user's authorized scope. Routine record operations inside an approved automation do not require structural-deletion confirmation.

## Lines and channels

Use list_lines, inspect_line and compatible_workflows. Assignment modes are ALL, SOME and NONE; ALL includes future eligible workflows. Preserve unrelated IDs and their order when editing SOME. Preview set_line_assignment and commit the identical reviewed request when authorized. add_line_workflow/remove_line_workflow change one assignment.

create_livechat_line creates a disabled Line without assignments. inspect_line_settings exposes editable fields; update_line_settings changes only requested supported values. rename_line changes the internal name. Preserve logos, protected account settings and unrelated configuration. line_share_links returns the actual public URL/embed snippet; share it only with the intended audience and report readiness alongside it.

Use set_line_enabled for the authorized enable/connect or disable/disconnect action. reconnect_line reuses the selected Line's stored account. Review channel-specific effects: connecting Telegram replaces its webhook, and disabling disconnects it. Never change another Line's account to work around duplicate-account errors.

Use begin_connection_setup for supported new channel/provider connections and send the trusted setupLink to the user. Credentials are entered in that authenticated form, never in chat or tool arguments. Check connection_setup_status using the original setupId and organization. Setup is scoped to the initiating user and expires. New channel setup creates a separate disabled Line without workflows; assignment and connection need authorization.

LINE_ACCOUNT_IN_USE includes disabled Lines; disabling does not release the account. Prefer reusing the existing Line. Recreation can require removal of its Inbox conversations and original Line. Never delete conversations automatically; conversation removal requires separate authorization in the application. delete_line does not remove conversations or disconnect a bot. Preview its canDelete/reason and conversationCount. Meet returned prerequisites, obtain the separate structural-deletion confirmation and commit the exact reviewed request. Re-preview when prerequisites or state change.

## Inbox

list_conversations and read_conversation resolve the actual recipient, Line, history and reply eligibility. Use draft_reply, then send_reply only for the explicitly authorized sending scope and reviewed text. Retain requestId, organizationId, conversationId, lineId, message and eventTriggered across preview, send and retry.

ACCEPTED is channel acceptance, not proof that a recipient read the message. If the outcome is unknown, check Inbox before deciding what to do; never automatically resend with a fresh ID. Private AI conversations are unavailable through these Inbox operations.

Use list_conversation_statuses for real status IDs, then preview set_conversation_status before committing. A status change can trigger enabled workflows.

## Connections and usage

Use list_integrations for supported services and their protected setup links, integration_accounts after setup, and bind_connection for the explicitly selected account. list_connections/list_native_connections provide safe connection identifiers and labels. Do not infer account selection from list order, copy credentials from another system or rebind existing resources silently.

organization_capabilities and organization_usage report current access, plan and usage. Report the returned timezone and completeness when relevant.

For attachment access or optional processing, follow [attachment access and consent](attachments.md).

## Reviewed changes and retries

Keep requestId paired with the exact operation and inputs. A stale preview requires reading the target and producing a fresh preview. An initial request can authorize creation, saving, assignment and activation together. Structural deletion still requires a later separate explicit confirmation; sending and paid services retain their own authorization rules. Unknown outcomes must be inspected before any retry.
