---
name: omneky-failure-modes
description: >-
  Recover from Omneky MCP failures: JWT re-OAuth, missing brand_id, empty
  reporting, timeouts, launch 400s, needs_user_decision, credit_insufficient,
  billing tools absent from tools/list, approval plain-chat fallback,
  ambiguous paid-submit recovery, disconnected connectors, and pending
  scrapes. Intent keywords: unauthorized, reconnect, empty metrics, timeout,
  400, credits, billing absent, needs_user_decision, pending scrape, failure
  playbook.
---

# Omneky — failure modes (shared playbook)

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Cross-cutting recovery rules other skills point to by section (§). Encode
recoveries with **exact** public tools. Do not invent SQL, auto-topup,
card-PAN, Nexus debit, Central-only tools, fake widgets, or shared files
outside skill folders.

## When to use

- A tool returned 401 / unauthorized / invalid token
- `brand_id` missing or unresolvable from user language
- Metrics look empty or “zero”
- `status=timeout` / `status=pending` / `status=needs_user_decision`
- Launch 400s (locations, LinkedIn start_date, Reddit microcurrency)
- `credit_insufficient` on creative submit
- Billing / balance tools missing from this session’s `tools/list`
- Approval UI needed and no host widget / `request_user_decision` is available
- Ambiguous paid submit (timeout / transport error after a possible charge)
- Connector disconnected mid-workflow
- User asks “what went wrong?” after an Omneky tool error

## When not to use

- Not a substitute for happy-path skills (`omneky-getting-started`,
  `omneky-analytics`, `omneky-creative`, `omneky-launch-manage`, …)
- Not a license to invent tools absent from `tools/list`

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) **when that tool is on tools/list**.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval / Generate turns: follow **§ Approval / plain-chat fallback** below — never invent a fake “summary widget” tool; never stall waiting for a widget that did not appear.
- Never invent tokens; OAuth is host-managed. Never ask the user to paste a JWT or API key into chat.

## Non-negotiable output / safety contract

- Credits / deductions / balance: **cgp-backend path only** via existing MCP
  tools when present on `tools/list`. Never invent Nexus debit routes or
  prepaid-purchase tools. When billing tools are absent, follow **§ Billing
  tools absent**.
- Never dump raw `clarification_needed` JSON into chat — present plain
  questions / host UI.
- Never identical tight-loop retries in one turn for timeout / pending.
- Prefer pause over delete when a mutate failed mid-flight and the user
  only wanted to stop spend.
- Point siblings back here by name + section from other skills’ failure tables.

---

## § Billing tools absent / tools/list gating

Billing tools (`get_account_credit_balance`, `get_billing_summary`,
`list_available_plans`, `start_plan_upgrade`, `create_billing_portal_session`,
`get_credit_history`, …) may be present on some connectors and **absent** on
some ChatGPT / host sessions (smaller tool snapshots).

1. **Before calling**: check whether the tool appears on the host’s
   `tools/list` / available tools.
2. **If present**: call balance before paid gen when unknown; on low balance
   offer upgrade / portal tools **only if those are also present**.
3. **If absent**:
   - Do **not** call balance / billing tools.
   - Do **not** invent a balance number or a billing tool name.
   - State operational cost (~**5** credits per image job / ~**30** credits
     per multi-scene video job when submitted).
   - Proceed to generate after the user confirms intent (Generate / Cancel
     via host UI or plain chat).
   - Rely on the generate tool’s `credit_insufficient` (or equivalent) as
     the hard gate.
4. Same gating for plan / portal tools: if absent, tell the user to manage
   plan / credits in the Omneky app / settings — never invent Checkout tools.

Creative skills should say: “follow `omneky-failure-modes` § Billing tools
absent” rather than duplicating divergent copy.

## § Approval / plain-chat fallback

Do **not** require an unimplemented custom “summary widget” binary. Contract:

1. Prefer host-native decision UI when available: OpenAI/ChatGPT confirmation
   cards, MCP Apps UI, or MCP `request_user_decision` when that tool is on
   `tools/list`.
2. If **none** of those exist: **plain-chat fallback** — send a one-card
   summary in chat (`Brand · Channel · Objective · Budget · Paused|Live ·
   Creative`) with explicit options **Approve / Deny / Edit**, then **end
   the turn** and wait for the user’s reply text; mutate only after an
   affirmative Approve (or clear yes).
3. Never invent a fake widget tool. Never stall waiting for a widget that
   did not appear.
4. Same pattern for Generate / Cancel credit callouts when no host widget
   is available: plain-chat Generate / Cancel, end turn, wait.

Launch / pause / budget skills should say: “follow `omneky-failure-modes`
§ Approval / plain-chat fallback”.

## § Ambiguous paid submit recovery

Paid submits (`generate_image_ad` with `gpt_ad_gen_id`, optional video
`job_id` you supplied) can fail clearly **or** leave the outcome unknown.

**Clear failure** before accept (`credit_insufficient`, validation error,
explicit reject): a **new** key / new attempt is OK.

**Ambiguous** (timeout / transport error / unknown **after** you may have
already submitted):

1. Do **not** immediately resubmit with a new `gpt_ad_gen_id` (duplicate
   spend risk — commit lag can still mean charged). Remember the intended
   key.
2. On the next turn call `get_generation_status(job_id=<that gpt_ad_gen_id>,
   kind="image")` **once**. For images, the status `job_id` arg accepts the
   same `gpt_ad_gen_id` used at submit.
3. If status shows running / complete → continue that job (do not re-mint).
4. If `not_found` **or** `queued` with `source=not_found`: **WAIT ~30–60s
   and/or ask the user** before any new paid submit. Do **not** auto-mint a
   new key and resubmit — a missing status row often means commit lag, not
   a safe never-started.
5. New key / resubmit only after:
   - a **clear pre-accept failure**, or
   - **explicit user OK** after the wait still shows never-started /
     `not_found`.
6. If still ambiguous after wait → ask the user before a second paid submit.

Same spirit for video when you supplied a client `job_id`: one status peek
with `kind="video"`; on `not_found` / queued+source not_found wait/ask —
do not auto-resubmit. Widget hosts: leave in-flight polling to the MCP Apps
widget; do not loop status in one turn.

Creative / image / video skills should say: “follow `omneky-failure-modes`
§ Ambiguous paid submit recovery”.

## § Resize / edit charge (follow live tool text)

Public tool text for `resize_ad` / `resize_image`: **resizes are not
charged** — they adapt an already-paid creative. Synchronous; no status
poll. Do **not** invent “premium resize tiers” or require balance-before-
resize.

- `edit_image` may still be a separate paid path — check live tool text on
  `tools/list` for that tool only.
- If a future `tools/list` description changes charge language, **follow the
  live tool text** over any skill copy.

Edit-resize / creative skills should say: “follow `omneky-failure-modes`
§ Resize / edit charge”.

---

## Staged workflow (other recoveries)

### Stage A — Auth / JWT

1. Send the user through **host OAuth** for Omneky again.
2. Optionally `health_check` after reconnect.
3. Re-run `get_current_user` before brand-scoped calls.
4. Never ask them to paste a Nexus JWT or API key into chat.

### Stage B — brand_id

1. `list_brands` + confirm (host UI / plain chat / one question).
2. Prefer numeric `brand_id` when thumbnails matter.
3. Do not guess.

### Stage C — Empty reporting

1. Call `check_reporting_data_available` (not deprecated `data_available`)
   for brand + date range + channels **before** treating empty as zero.
2. If coverage is missing, say so; do not invent metrics.
3. Never sum `selected_conversion_metric_value` across channels.

### Stage D — Timeouts / pending

| Signal | Response |
| --- | --- |
| `get_recommendations` → `status=timeout` | Narrow date window; do not identical retry this turn. |
| Unscoped `get_ad_groups` → timeout | Pass `campaign_id` (and ids when known); retry once narrowed. |
| `scrape_product_from_url` → `status=pending` | Retry later same `brand_id` + url; no tight poll this turn. |
| Async gen still running | On widget hosts, let the widget poll; on text hosts call `get_generation_status` **once** next turn — never loop in one turn. |

### Stage E — Launch / targeting 400s

- LinkedIn: `search_ad_targeting` with `types=["locations"]` and a
  `urn:li:adTargetingFacet:locations` entry; `start_date` required when
  creating a new campaign group.
- TikTok: `get_tiktok_location_ids` then pass `location_ids` on the ad group.
- Google Demand Gen: `search_google_countries` → `targeting_fragments`.
- X Ads: wire name `twitter`, never `x`.
- Reddit: `bid_value` is microcurrency (dollars × 1,000,000).
- Meta leads: `lead_gen_form_id` on ad specs for native forms.
- Disconnected channel: `omneky-self-connect` /
  `get_channel_connect_url` → link → re-check.

### Stage F — needs_user_decision

1. If `request_user_decision` is on `tools/list`, call it (not deprecated
   `ask_user`).
2. Else use plain-chat questions (§ Approval / plain-chat fallback).
3. Never dump `clarification_needed` JSON.
4. Never auto-retry the failed write in the same turn.

### Stage G — Credits / plan

1. `credit_insufficient` means the render **did not start**.
2. If balance tools are on `tools/list`: `get_account_credit_balance` (and
   optional `get_credit_history`).
3. If upgrade / portal tools are present: `list_available_plans` +
   `start_plan_upgrade`, or `create_billing_portal_session`. Hand Stripe URL;
   never collect a PAN.
4. If billing tools are **absent**: follow **§ Billing tools absent**; do not
   invent balance; point to Omneky app / settings for plan management.
5. After user finishes Checkout (when those tools exist):
   `get_checkout_session_status` **once**. Details: `omneky-billing` /
   `omneky-credit-balance`.

### Stage H — Connector disconnected mid-flow

1. `get_channel_connection_status` / `list_connector_statuses`.
2. Hand off to `omneky-self-connect` / `omneky-channel-connect`.
3. Do not invent alternate launch endpoints.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| 401 / unauthorized | Host re-OAuth; never pasted JWT. |
| Unknown brand | `list_brands` + confirm. |
| Empty metrics | `check_reporting_data_available` first; never invent. |
| Cross-channel conversion sum temptation | Group by channel or named metric only. |
| `status=timeout` | Narrow scope; no identical retry this turn. |
| `status=pending` scrape | Later retry same args; no tight loop. |
| `needs_user_decision` | `request_user_decision` if listed; else plain chat; no auto-retry. |
| Launch location 400 | Channel pre-call (LinkedIn / TikTok / Google DG). |
| `credit_insufficient` | Did not start; upgrade path if tools present; else Omneky app; no retry. |
| Billing tools missing | § Billing tools absent — operational cost + `credit_insufficient` gate. |
| No approval widget | § Approval / plain-chat fallback — never invent widget tools. |
| Ambiguous paid submit | § Ambiguous paid submit recovery — status once; on not_found wait/ask — never auto new key. |
| Resize charge guess | § Resize / edit charge — follow live tool text (uncharged today). |
| Missing tool on `tools/list` | Say unavailable; do not invent. |
| Delete urge after error | Prefer `set_ad_entity_status` pause; deletes need dual confirm. |
| Widget poll tools called by model | Do not call `poll_image_generation` / `poll_video_generation` / `sync_generation_group` as the agent on widget hosts. |

## Sibling map

Other skills should point here for recovery, then return to:

| Domain | Skill |
| --- | --- |
| Session / brand | `omneky-getting-started` |
| Connectors | `omneky-self-connect` / `omneky-channel-connect` |
| Analytics empty | `omneky-analytics` |
| Credits | `omneky-credit-balance` / `omneky-billing` |
| Creative async | `omneky-creative` |
| Launch 400s | `omneky-launch-manage` / `omneky-meta-launch` |
