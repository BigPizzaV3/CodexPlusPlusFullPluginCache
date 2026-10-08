---
name: omneky-billing
description: >-
  Company plan upgrade, Stripe Customer Portal, and prepaid credit balance /
  history for the signed-in Omneky account. Production mcp.omneky.com exposes
  these tools; still confirm they appear on tools/list before calling. Out of
  credits → upgrade plan. Never collect a card PAN. Intent keywords: upgrade
  plan, Stripe portal, invoices, card on file, checkout session, credit
  balance, billing summary.
---

# Omneky billing

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Operational plan / portal / prepaid-credit workflows via cgp-backend-backed
MCP tools. Flow = Stripe Checkout / Customer Portal **URL redirects**. Never
complete Checkout yourself. Never collect a PAN. Never invent Nexus debit or
prepaid-credit purchase tools.

## When to use

- User asks which plan they are on, remaining credits, card on file, invoices,
  or wants to upgrade
- Creative path returned `credit_insufficient`
- Tools below appear on this session’s `tools/list`

## When not to use

- Paid-media ROAS / campaign spend → `omneky-analytics`
- Bank transfers / third-party invoices / general payment rails
- Inventing auto-topup or card-PAN capture

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Approval turns: end the turn after Approve / Deny (host UI or plain chat); mutate only next turn after Approve.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Confirm tool names on `tools/list` before calling. Billing tools may be
  **absent** on some ChatGPT sessions — follow `omneky-failure-modes`
  § Billing tools absent. If absent, tell the user to manage the plan in the
  Omneky app / settings; never invent balance or billing tools.
- Out of credits → **plan upgrade** path (`list_available_plans` +
  `start_plan_upgrade`, or Customer Portal). Do not invent prepaid purchase.
- `list_available_plans` returns lookup keys — Nexus has **no dollar prices**
  here; do not invent a price catalog.
- Owner-only tools may refuse for non-owners — explain; do not bypass.
- After handing `checkout_url` / `portal_url`, wait for the user; poll
  `get_checkout_session_status` **once** after they say they paid (plan-upgrade
  Checkout only). Managed-launch payment uses
  `get_managed_launch_payment_status` instead — do not mix them.
- Credits / deductions: existing MCP balance / history / upgrade tools only
  (cgp-backend path). Never invent Nexus debit routes.
- No subscription promo copy in chat — operational gates only (e.g. image ~5 /
  video ~30 credit callouts belong on creative skills).

## Staged workflow

### Stage 1 — Presence check

1. Confirm allowlisted names exist on `tools/list`. If **absent**, stop —
   do not invent tools or a fake balance; point to Omneky app / settings
   (`omneky-failure-modes` § Billing tools absent). Creative siblings may
   still generate after operational-cost callout and rely on
   `credit_insufficient` as the hard gate.

### Stage 2 — Snapshot

1. `get_billing_summary` — plan + credit snapshot (not a price catalog).
2. Optional: `get_company` for identity / plan fields.
3. Dedicated balance: `get_account_credit_balance` (`credit_balance`,
   `usd_per_credit`).
4. Ledger: `get_credit_history` (capped JSON rows).
5. Card on file: `get_payment_method_summary` (brand / last4 / expiry only).

### Stage 3 — Upgrade / portal

1. `list_available_plans` → keys such as `cgp_standard_monthly`, …
2. Either:
   - `start_plan_upgrade` with a chosen key (saved-card change or
     `checkout_url`), **or**
   - `create_billing_portal_session` → `portal_url` when the user should pick
     a plan / see live prices / invoices.
3. Ask the user to open the URL in the browser. End turn if waiting.

### Stage 4 — After payment

1. User says they finished plan-upgrade Checkout →
   `get_checkout_session_status` **once**.
2. Re-read `get_account_credit_balance` / `get_billing_summary` if useful.
3. Managed-launch `status=payment_required` Checkout →
   `get_managed_launch_payment_status` (not `get_checkout_session_status`).

### Stage 5 — Hand back

Return to `omneky-creative` / `omneky-image-ads` / `omneky-product-video`
when the original intent was generation.

## Allowlisted tools (when listed)

`get_billing_summary`, `get_company`, `get_account_credit_balance`,
`get_credit_history`, `list_available_plans`, `start_plan_upgrade`,
`create_billing_portal_session`, `get_payment_method_summary`,
`get_checkout_session_status`, `get_managed_launch_payment_status`.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Tools missing from `tools/list` | Stop; Omneky app / settings; never invent tools (`omneky-failure-modes` § Billing tools absent). |
| Non-owner on upgrade / portal | Explain owner-only; do not invent bypass. |
| User pastes card PAN in chat | Refuse to process PAN; send them to Stripe portal URL only. |
| Invented prepaid top-up tool | Refuse; use plan upgrade / portal. |
| Tight-loop checkout polling | One `get_checkout_session_status` after user confirmation. |
| Confused managed-launch vs plan Checkout | Use the matching status tool only. |
| `credit_insufficient` mid-creative | If balance/upgrade tools present → upgrade path; else Omneky app; do not retry generate until funded. |

## Sibling map

| Need | Skill |
| --- | --- |
| Balance-only gate | `omneky-credit-balance` |
| Resume image/video after top-up | `omneky-creative` / `omneky-image-ads` / `omneky-product-video` |
| Auth / tool missing | `omneky-failure-modes` / `omneky-getting-started` |

## Never invent

- Prepaid-credit purchase, auto-topup, webhook, or card-PAN tools
- Nexus debit routes or non-cgp balance endpoints
- Dollar prices from `list_available_plans` (keys only)
