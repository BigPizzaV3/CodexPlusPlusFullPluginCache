---
name: inbox-configuration
description: Use when tuning existing sending inboxes (daily limits, display names, signatures, reply forwarding, warmup pause/resume). New domains go through infra-planning and domain-selection.
---

# Inbox configuration

Tune existing sending inboxes. These tools cannot read or change inboxes: you bring the judgement and the exact values, and the user makes each change in Kenso on the Email Delivery page, https://app.ken.so/<workspace id>/delivery?tab=inboxes, from the inbox's Inbox actions menu > Edit inbox. New domains and inboxes are sized in `infra-planning` and ordered in `domain-selection`.

Never suggest disconnecting or deleting an inbox, or changing its username, to fix a setting. Restate any change as a short summary and get a yes before the user makes it. Inbox changes need the admin role.

## 1. Read state

Ask the user to open the Inboxes tab and tell you, or paste, each inbox's address, domain, daily limit and display name.

Summarize per inbox: address, domain, daily limit, display name. The inboxes page is https://app.ken.so/<workspace id>/delivery?tab=inboxes.

## 2. Daily limits

- Healthy, warmed inboxes: **30-50/day**
- New or still warming: **5-10/day**, ramp over 2-3 weeks
- Never suggest **more than 100/day** per inbox
- `0` pauses that inbox. No explicit limit means the provider default (Google/Microsoft 25, Azure 5)

Leave create-time limits unless the user asks. Do not raise limits on a domain that is still setting up.

After the user approves a number:
the user opens Inbox actions > Edit inbox, sets Daily send limit to it and clicks Save changes, once per inbox.

Give one sentence on why the limit protects deliverability. Warmup shares the same provider budget, so leave room for it.

## 3. Display names

Edit inbox > First name and Last name, then Save changes. Instant and safe.

## 4. Signatures

Edit inbox > Signature, then Save changes, per inbox.

Draft the signature here first and show it to the user before they paste it in.

## 5. Reply forwarding and warmup

Forward to the client's own external email only:
Edit inbox > Reply forwarding, with the client's external address, then Save changes. Details, plus warmup: `references/forwarding-and-warmup.md` in this skill's folder.

## 6. Boundaries

- **Tuning existing inboxes**: this skill.
- **New inboxes / domains**: `infra-planning`, then `domain-selection`. Do not promise a free domain.
- **Connecting external inboxes / OAuth**: dashboard only.
- **Username changes**: in place on the same mailbox, never a replacement purchase. Not done from this skill.

## Refusal handling

`INBOX_LIMIT_REACHED` is the most common here.

| Code | What to tell the user |
|------|------------------------|
| `PLAN_FEATURE_NOT_AVAILABLE` | Managed sending infrastructure is on paid plans - upgrade at https://app.ken.so/<workspace id>/settings/billing. Show `error.recovery.summary` when present. |
| `INBOX_LIMIT_REACHED` | Show `used` / `limit` / `remaining`. Offer: stay within remaining allocation (or rebalance limits), or upgrade. |

If they need more daily send than they have, load `infra-planning`. When headroom is zero, help them get more from existing inboxes instead of framing it as a system error.
