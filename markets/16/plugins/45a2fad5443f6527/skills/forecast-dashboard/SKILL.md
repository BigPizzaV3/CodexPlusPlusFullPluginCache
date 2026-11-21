---
name: forecast-dashboard
description: Build a Salesforce-style forecast dashboard natively inside monday — closed-won, committed, best-case, and pipeline buckets by close month, rendered as a real monday dashboard with widgets. Use when someone says "build me a forecast", "show me Q2 pipeline", "Salesforce-style forecast view", "forecast dashboard", or "commit vs best-case".
---

# Forecast Dashboard

> **Platform notes (ChatGPT and Codex).** Before any write, show the concrete action or batch and obtain explicit approval. Use only tools exposed in this session; if a named tool is missing, say so and stop that step. Use visible plain-text `monday-crm-skill-id: <skill>` markers; monday Docs can strip HTML comments. Read back newly created documents to verify their marker; dashboard marker limitations are described in Step 6. Before creating documents, search within the relevant workspace and read candidate content; match title, skill marker, board or item, and date or period. Treat surviving legacy `<!-- monday-crm-skill-id: … -->` and `<!-- claude-skill-id: … -->` markers as matches. If a candidate has the right title and generated-by footer but lacks a marker, or matching is ambiguous or incomplete, do not create or update automatically: show the candidate and ask the user. If search or read-back is unavailable, stop the write. For meeting recaps also include and verify a visible `meeting-id: <id>` marker; if either marker is missing, do not infer a match or create a duplicate automatically.

Builds a native monday dashboard that renders the pipeline as a forecast — committed / best-case / pipeline / closed-won, grouped by stage × close month. Replaces the "export to CSV and pivot it" pattern that sales ops leaders do manually every Monday.

Flow: **Trigger → Gather → Synthesize → Show draft → offer publication (α, opt-in) → Share (β, opt-in) → Proactive extension (opt-in, hygiene fix)**.

## Input
- Optional: board name / ID + forecast period (e.g., "Q2 2026", "next 90 days").
- Optional: pre-declared mode (Default / Silent / Proactive).

## Output
- **α (default):** A native monday `create_dashboard` with widgets per bucket + URL.
- **β (Share):** Notify the sales leader with a link via `create_notification`. Granting dashboard permissions has no named monday tool, so the skill tells the user how to share it in monday instead of changing permissions itself.
- **Proactive extension:** Hygiene fix — if a non-closed deal is missing close date, `change_item_column_values` (with batched user confirm) to set a placeholder OR post a prompt update asking the owner to fill it. Missing-amount items are reported in chat and an optional confirmed hygiene update is posted on the item, but the amount column itself is never written (forecast integrity rail).

## Knowledge
- Bucket definitions: closed-won / committed / best-case / pipeline (§ Step 5).
- Shared artifact conventions (see Shared patterns section below).

## Tools (MCP)
- `get_user_context`, `list_workspaces`, `search` — board resolution.
- `get_board_info`, `get_column_type_info` — schema + column types (stage/amount/close-date/forecast-category).
- `get_board_items_page` — paginated pull.
- `board_insights` — aggregate fallback.
- `create_dashboard`, `create_widget` — α publish.
- `create_doc` — fallback for non-admins (see Error handling).
- `create_notification`, `list_users_and_teams` — β share.
- `create_column` — add a forecast-category column only if required to render the dashboard.
- `change_item_column_values` — proactive hygiene fix.
- `update_doc` — doc updates. (No generic GraphQL tool is used.)

## Cross-skill handoffs
- **From morning-briefing:** If the briefing surfaces forecast-hygiene issues (missing close date or amount on >10% of deals), the user may jump here to build the structured view.
- **To board-diagnosis:** If >25% of deals are missing core forecast fields, suggest the `board-diagnosis` skill before publishing.


## Draft first, then offer publication

Use available read-only tools to prepare the complete requested deliverable before asking to publish. Present it as a readable, editable artifact in the host when available; otherwise show the full draft in chat. A native monday dashboard or board cannot be created outside monday: present a concrete preview or blueprint, not a claim that it exists. State meaningful missing data or assumptions. Then ask once whether to publish the displayed draft to the specified monday destination; allow edits or decline. On decline, retain the draft and stop without monday writes. On approval, publish only the shown content and concrete actions the user approved. Separately describe and obtain approval for record edits, notifications, contacts, automations, or other actions not included in that publication. Do not ask to choose a mode before producing the draft; use read-only default behavior. Ask only for information essential to prepare a useful, accurate draft, and state reasonable defaults. This draft-first rule takes precedence over earlier or later mode and publish-first instructions.

---


## Offer a useful next step

At the end of a completed response, offer one specific, relevant next thing ChatGPT can do based on what is actually available: offer to investigate a forecast gap or identify deals needing attention. Ask whether the user wants that help; do not begin it before they respond. Do not repeat an existing unanswered question or make the offer when the task cannot continue because of a connection or permission failure. Do not promise capabilities, events, or results that have not been verified. Approval to explore or draft is not approval to publish, send, or change CRM data.

## Step 0: Connector check

**Goal:** Fail fast if monday connector is missing.

Call `get_user_context`. On success, continue. On connection error / tool not found, print the standard install prompt and stop.

---

## Step 1: Detect mode + confirm forecast period

**Goal:** Know write-confirmation policy AND lock the forecast window.

1. Prepare the forecast read-only; do not ask the user to choose a mode.
2. Use the requested period; if unspecified, use the current quarter and state that assumption in the draft. Store `period_start`, `period_end`.

---

## Step 2: Resolve the deals board (Gather)

**Goal:** Land on one (or user-confirmed multi) board. Same resolution path as morning-briefing Step 2. Use `get_user_context` → `list_workspaces` → `search("deal")`.

---

## Step 3: Read board schema (Gather)

**Goal:** Resolve columns by type — stage (`status`), amount (`numbers` with `$`), close date (`date` with "close"/"expected"), forecast category (`status` with commit/best-case/pipeline labels, if present).

1. `get_board_info(boardId)`.
2. `get_column_type_info` for any ambiguous column.
3. If no forecast-category column exists, explain that the commit/best-case split cannot be verified; prepare the supported forecast without creating a column. If the user later requests a column, show its plan and obtain separate approval before `create_column`.

---

## Step 4: Pull deal data (Gather)

**Goal:** Paginated pull over the forecast window.

Call `get_column_type_info({ columnType: "date", fetchMode: "guidelines" })` first. Use one date-range filter `{ columnId: <resolved close-date column>, operator: "between", compareValue: [<YYYY-MM-DD start>, <YYYY-MM-DD end>] }`; do not add `compareAttribute`. Paginate via `cursor` up to 2K items (same cap as morning-briefing), disclosing truncation. Separately query the same board scope for undated records with `{ columnId: <close-date column>, operator: "is_empty", compareValue: [] }`, with bounded pagination and any truncation disclosed. Report undated records outside period totals: they cannot be assigned to a month or assumed to fall within this period. Same 429 / rate-limit handling.

---

## Step 5: Synthesize (Synthesize)

**Goal:** Group deals into forecast buckets × close month.

Classify each deal once, in this order. Resolve actual labels and meanings from the schema and user instructions; if they are ambiguous, ask before publishing. Recognize board-specific equivalents such as Committed/Commit, Best case/Best-case and Excluded/Omit only when their meanings are established.

- **Excluded** — confirmed lost stages or an explicit omit/excluded category. Report the excluded count separately; these records contribute to no forecast bucket. Surface contradictory won/excluded classifications for review.
- **Closed-won** — a stage label confirmed by the user as won. `is_done: true` alone does not distinguish won from other completed outcomes; if classification is unclear, ask.
- **Committed** — forecast category = Commit OR (probability ≥ 80% AND stage in late-funnel).
- **Best-case** — forecast category = Best-case OR (probability in 50-79% AND stage in mid-funnel).
- **Pipeline** — everything else active.

Group by close month within the period. Sum only known numeric amounts per (bucket × month), showing the record count and count of missing amounts beside each total. A bucket with missing amounts has an incomplete subtotal; never turn a blank amount into zero or claim the subtotal is complete. With no records, a bucket can correctly have zero deals and zero known value.

Within each forecast bucket, show the current stage and owner when available. Apply owner or region segmentation only when requested and supported by real columns. Use the actual dashboard/widget tool schema for formatting; if a widget is unavailable, disclose the limitation and present the calculated table without claiming a dashboard was created.

---

## Step 6: Publish α — build the dashboard (Publish)

**Goal:** First show the calculated forecast and a concrete dashboard preview, including buckets, months, coverage and proposed widgets. Ask whether to create that dashboard in the named monday workspace. Only create after yes; if no, keep the forecast draft.

The currently exposed `create_dashboard` takes `workspace_id`, `board_ids`, `name`, and optional `kind`; it does not accept a description. Search the workspace for the proposed exact title before creation. If a candidate exists or search is incomplete, stop and ask the user which dashboard to use; a title alone is not proof of ownership. Before creating a dashboard, obtain widget schemas with `all_widgets_schema` and confirm that the requested buckets, period and filters can be represented. If that schema tool is unavailable, stop native-dashboard creation and offer the calculated chat table or a separately approved document. For a new dashboard use the approved name and board IDs and the actual widget schemas before `create_widget`. Do not claim a date range, excluded-deal filter, or rendered total unless supported by the widget configuration and verified. If readback of widgets or their values is unavailable, explicitly report that they are unverified. The dashboard has no verified skill marker; do not claim marker-based idempotency or automatically update it on later runs.

### Permission fallback
If `create_dashboard` returns a permission error, report that actual error without inferring the user's role. Ask:
> I couldn't create this dashboard because of the reported permission restriction. Want me to: (a) publish a doc-version with the same forecast (summary tables), (b) stop so you can check workspace permissions, or (c) try a different board?

Route to `create_doc` on option (a).

---

## Step 7: Share β — viewer access for sales leader (opt-in)

**Goal:** Tell the sales leader the dashboard exists. Don't change permissions.

1. `list_users_and_teams` → resolve the sales leader. Confirm the person with the user.
2. The notification tool supports item, board, and post targets, not dashboards. Offer the dashboard link in chat; only send a notification if the user chooses an accessible item or board as its target and confirms the recipient and text. Then call `create_notification({ user_id: <user id>, target_id: <item or board id>, target_type: "Project", text: "Forecast dashboard for <period>: <url>" })`.
3. Tell the user: *"If <name> can't open it, share the dashboard from its Share button in monday (viewer access)."* The plugin doesn't change dashboard permissions: there's no dedicated tool for it, and permission changes should stay with the user.

---

## Step 8: Proactive extension — forecast hygiene fix (opt-in)

**Goal:** Fix hygiene gaps on deals blocking forecast accuracy — WITHOUT editing stage or amount.

Hygiene gap = deal in a non-closed stage that's missing **either** close date **or** amount.

Core pattern:
- For each gap deal with missing close-date: `change_item_column_values` — set a placeholder (e.g., end-of-current-quarter) OR post a prompt update asking the owner to fill it. Stage edits also OK here when a clear signal exists (e.g., user said "move all of these to qualifying"), inside the batched-confirm plan.
- For each gap deal with missing amount: post a prompt update only — **never write to the amount column** (forecast integrity rail).
- If >20 gap deals: batch into one `Forecast hygiene — <period>` review doc (with `monday-crm-skill-id: forecast-dashboard` in body) rather than 20 individual writes.

---

## Step 9: Close the loop

**Goal:** Summary line with dashboard URL + counts.

Report the actual outcome. Use `Published Forecast — <period>. <N> deals, <N> widgets, <N> hygiene gaps flagged.` only when publication succeeded, adding any missing-value or widget-verification limitations. For a chat-only result, say that the calculated forecast was shown and no dashboard was created.

---

## Shared patterns
- **Artifact identification.** Documents use the visible `monday-crm-skill-id: forecast-dashboard` marker and generated-by footer. Dashboard descriptions are unavailable through the current create tool; see Step 6.
- **Idempotency before create.** Search the workspace for the exact proposed title; if it exists or search is incomplete, stop and ask the user. The current create tool cannot store a description marker.
- **Safety rail.** No deletes, no amount-column writes, no cross-workspace moves. Close-date placeholder writes and stage edits OK in a batched-confirm plan.
- **Ask once per session**, not per deal, when entering Proactive mode.
- **Type-based column resolution**, not name-based — global teams have non-English columns.

## Error handling reference
Same table as morning-briefing with additions:
- **Permission error from `create_dashboard`** → report the actual error and ask (a) doc version, (b) stop, (c) different board.
- **Dashboard creation succeeds but `create_widget` partially fails** → keep the dashboard, list failed widgets, let user retry.

---

## Completion criteria

- [ ] Step 0 (connector check) ran and passed.
- [ ] Search was completed before creating; any existing title was resolved with the user.
- [ ] Widget rendering and filters were verified, or their limitations were disclosed.
- [ ] Chat output ends with dashboard URL.
- [ ] Safety rail held: no deletes, no amount-column writes, no cross-workspace moves.
- [ ] Permission fallback reported the actual error and used the user's chosen alternative.
