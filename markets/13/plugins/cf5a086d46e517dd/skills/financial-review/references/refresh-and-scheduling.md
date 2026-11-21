# Refresh and scheduling

Fina supplies financial data. The host owns artifact creation, scheduling and delivery. The same financial workflow applies in every host; no schedule API name is assumed here.

Read [host capabilities](host.md). Use the actual host Scheduled tasks or automation tool to create or update the routine; do not stop at giving instructions for the user to schedule it if the host exposes the authorized action. If it does not, explain the specific incomplete portion and the supported host setup path. A reminder to update the dashboard is not an updating dashboard.

## Establish the durable target

Before scheduling, verify that the host can read the connected Fina account on future runs and edit the exact dashboard artifact. Discover the actual scheduler and artifact tools available in this session. A download-only file or a chat preview does not establish durable edit access.

Keep a small private update descriptor next to the artifact, or in its supported persistent metadata: artifact ID/path, style preferences, timezone, reporting-currency choice, period rules, data sections and last-successful refresh. It contains no passwords, OAuth tokens or embedded private tool responses. Do not place financial facts or account identifiers in a public repository or shared task template. The descriptor is not a substitute for an executable schedule.

If scheduled sessions cannot reopen the chosen artifact, use another supported private durable format within the user's request, or explain the limitation. Do not silently replace an updating dashboard with new unrelated reports.

## Set up the requested routine

1. Honor the requested cadence. If the user accepted daily updates without specifying a time, use 08:00 in their saved profile timezone and state this default in the completion message. Do not ask for a technical timezone when a reliable saved one exists. If no timezone can be resolved, ask the minimum necessary location/time question.
2. Reuse an existing schedule for this dashboard when accessible. Do not duplicate it on refresh, restyling or retries. Use the host's required approval flow without inventing approval or overriding its permissions.
3. Save instructions that tell each future run to reopen the descriptor, resolve the period anew, fetch fresh authorized Fina facts using the financial-facts reference, update the same artifact while preserving design, and record successful data-refresh time. Include enough workflow guidance for a new run if the host does not automatically load the skill. Never embed an access token.
4. Updates should be financial reads only. Do not modify accounts, dismiss suggestions, import transactions or change subscriptions as a side effect. Read-only Fina permission is sufficient for financial reads; artifact editing and scheduling are separate host actions.
5. Keep unchanged successful maintenance quiet unless the user requested a report or notification at every run. Notify on a material failure or action required. A requested daily report is delivered on its requested cadence. Delivery occurs through the host's supported destination; Fina provides no proactive WhatsApp delivery.
6. Verify creation from the scheduler's successful response. Perform an immediate supported refresh to verify artifact access and updated data. Record whether an unattended scheduled run has actually succeeded; successful creation or a manual refresh alone does not prove unattended execution. Never backdate verification.

## Instructions to save in the scheduled task

Adapt the following workflow to the actual durable target, period rules and supported scheduler. Resolve every target reference before creating the task; do not save placeholders. Include the stable private artifact identity/path and private descriptor location, not financial data or secrets. Preserve existing permissions; do not create a public task-share link.

> Open the existing private Fina dashboard at the saved target and its update descriptor. Use the authenticated Fina connection for this user. Resolve the reporting period afresh in the saved timezone. Read current account summaries and financial context, the requested period's spending and received-income aggregates, relevant commitments, dated card obligations and bounded recent activity using the live tool schemas. Preserve currencies, dates, coverage and the distinction between cash, credit, assets, expected income and payments due. Update this same artifact while preserving its design and user edits. Do not import data, change Fina records, move money, publish or send data to another destination. Preserve the last valid data if access or a section fails; show the actual last successful refresh per section. Report a failure or required action through the authorized host channel; remain quiet for unchanged successful maintenance unless the user requested a report every run. Never substitute a reminder, new dashboard or stale snapshot for this update.

For a recurring financial review rather than a dashboard, replace artifact-edit steps with the explicitly requested private report destination and comparison window. Never infer permission to email, message WhatsApp or post publicly from permission to schedule.

## Failure and cancellation

If Fina is disconnected, authorization is revoked, analysis access is denied, or a provider is unavailable, keep the last valid dashboard. Preserve its last successful refresh timestamp; do not replace unknown or failed results with zeros or claim current data. Tell the user how the specific access or execution issue can be resolved, without checkout promotion or bypasses.

If a source returns partial data, update only coherent sections and label the section's coverage and date; a complete-refresh timestamp must not suggest failed sections are current.

When the user asks to stop updates, pause or remove the corresponding host schedule and verify that action. Keep the dashboard unless they separately request its deletion. Changing or removing a host schedule does not cancel a Fina membership or delete financial records.
