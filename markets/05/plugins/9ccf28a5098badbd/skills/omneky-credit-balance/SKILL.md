---
name: omneky-credit-balance
description: >-
  Check prepaid creative credit balance and history before paid generation.
  Keywords: credits, credit balance, out of credits, credit history,
  usd_per_credit, credit_insufficient.
---

# Credit balance

## Activation analytics

If the host exposes a skill-activation / analytics hook, call it once per new user request with this skill name; otherwise skip silently. Never invent a tracking tool. Omneky MCP does **not** expose `track_skill_activation`.

## Purpose

Lightweight prepaid-credit gate before image / video generation. Balance and
history only; upgrades live in `omneky-billing`.

## When to use

- Before `generate_image_ad` / `generate_product_video` / paid `edit_image`
  (not for uncharged `resize_ad` / `resize_image`)
- After `credit_insufficient`
- User asks “how many credits do I have?”

## When not to use

- Full plan / portal / checkout flows as the primary task → `omneky-billing`
- Campaign budgets / media spend → `get_channel_budget` via analytics /
  launch-manage (different concept)

## OpenAI runtime contract

- Use only tools from the current OpenAI host + Omneky MCP (`https://mcp.omneky.com/mcp`). Never invent tools.
- Prefer native ChatGPT / host widgets and question UI for decisions. Use MCP `request_user_decision` for missing structured fields (not deprecated `ask_user`) when listed. Else `omneky-failure-modes` § Approval / plain-chat fallback.
- When intake is incomplete, ask **one** concise chat question. Never invent a question tool.
- Generate / Cancel turns: end the turn after the choice UI (or plain chat); mutate only after affirmative Generate.
- Never invent tokens; OAuth is host-managed.

## Non-negotiable output / safety contract

- Confirm `get_account_credit_balance` (and related) appear on `tools/list`
  first (`omneky-failure-modes` § Billing tools absent).
- **If present**: call balance before paid creative jobs when unknown.
- **If absent**: skip the balance call; state operational cost (image ~5 /
  video ~30); proceed after user confirms intent; rely on
  `credit_insufficient` as the hard gate. Never invent a balance number.
- Operational credit callouts are OK — not subscription promo copy.
- On `credit_insufficient`, the job **did not start** — do not retry generate;
  hand off to `omneky-billing` only when upgrade/portal tools are listed;
  else point to Omneky app / settings.
- Never invent Nexus debit / auto-topup tools. Never collect a PAN.
- Resize is not charged — do not gate `resize_ad` / `resize_image` on
  balance (`omneky-failure-modes` § Resize / edit charge).

## Staged workflow

### Stage 1 — Presence + balance

1. If `get_account_credit_balance` is **absent** from `tools/list`: state
   operational cost (~5 image / ~30 video), return to creative skill after
   user confirms intent; skip Stages 2–3 balance reads.
2. If present: call it → report `credit_balance` and `usd_per_credit` when
   present.

### Stage 2 — Optional history

1. Only if `get_credit_history` is listed: recent grants / usage (capped
   rows).

### Stage 3 — Gate or upgrade

1. If balance tools were absent: creative path uses operational callout +
   `credit_insufficient` hard gate.
2. If balance is sufficient for the intended job, return to
   `omneky-creative` / `omneky-image-ads` / `omneky-product-video` /
   `omneky-edit-resize` with a credit callout (Generate / Cancel; host UI
   or plain chat) before submit. Do not gate uncharged resizes.
3. If insufficient and upgrade tools are listed: `omneky-billing`
   (`list_available_plans` + `start_plan_upgrade` or
   `create_billing_portal_session`). If upgrade tools absent: Omneky app /
   settings.

## Failure boundaries

| Failure | Required response |
| --- | --- |
| Tool missing | Say unavailable; Omneky app / settings; never invent balance (`omneky-failure-modes` § Billing tools absent). |
| `credit_insufficient` | No retry; billing upgrade path if tools present; else Omneky app. |
| User confuses credits with ad budget | Clarify prepaid creative credits ≠ channel budget. |
| Balance gate on resize | Forbidden — resizes not charged. |
