---
name: infra-planning
description: Use when sizing sending domains and inboxes against daily send and credits on a paid plan, or when the user asks how much infrastructure they need.
---

# Infra planning

Review existing sending domains and inboxes, then size a cart against daily send and credits. New domains and Kenso inboxes are paid: in credits on credit plans, through Stripe checkout on exempt workspaces. Never invent domains or inboxes that are not already in Kenso. Never say domain registration or Kenso inboxes are free. To import domains the user already owns, load `connect-domains` (BYOD is live).

These tools cannot read billing, credits, sending capacity, domains or inboxes, and cannot buy anything. You size and price the cart from what the user reads you; the user buys it in Kenso on the Email Delivery page, https://app.ken.so/<workspace id>/delivery?tab=inboxes, with New Inbox > Purchase Domain.

## 1. Preflight

Ask the user for their plan and their available credits: both are on https://app.ken.so/<workspace id>/settings/billing. A white-label child workspace has its plan and credits run by its parent workspace: send purchase and credit questions there.

Plans that buy Kenso infrastructure, with billing Active or Trialing:

- Credit plans pay in credits: Platform (`planType` Platform, the public plan: 200,000 sends and 5,000 credits a month), Dfy (the Kenso team adds its credits), and grandfathered Starter / Growth / Core.
- VIP (`planType` Premium) is exempt and staff-sold: it pays new domains through Stripe checkout, and mailboxes are on the plan.

Free (or `PLAN_FEATURE_NOT_AVAILABLE`): Free cannot buy Kenso domains or inboxes. It connects its own inboxes in the app, or upgrades to Platform at https://app.ken.so/<workspace id>/settings/billing (surface `error.recovery.summary` when present). **STOP** any request to add Kenso capacity. You may still list what they have.


The daily send left on the plan is not readable here. The app's Purchase domains flow checks it, and the credits, before it charges, and says so when a cart does not fit.

- Credit plans (Platform, Dfy, grandfathered Starter / Growth / Core): the plan's daily send is a planning figure. A cart may go above it; credits are the limit.
- Any other paid plan: daily send is a hard cap. When none is left, stop new orders.

There is no domain-count allowance.

## 2. Read current state

Ask the user to open https://app.ken.so/<workspace id>/delivery?tab=inboxes and tell you how many domains and inboxes they have on Google, Outlook and Azure, and each inbox's daily limit, or paste the list.

Summarize: domain count and names, inbox count and limits, and the daily send they add up to.

## 3. Size a cart

Size from the daily volume the user wants, in emails a day.

New-inbox daily: Google (`GOOGLE`) or Microsoft (`MICROSOFT`) **25/day**, Azure (`AZURE`) **5/day**.

`cartCapacity = googleCount*25 + microsoftCount*25 + azureCount*5`

Hard cap (a paid plan that is not a credit plan), with the daily send left that the user reads from the app as `remaining` and the plan's daily send as `planDaily`:

- Google/Microsoft: `floor(remaining / 25)`
- Azure: `floor(remaining / 5)`
- Require `existingCapacity + cartCapacity <= planDaily`.

Credit plans: size from the daily volume the user wants. The credit total below is the gate.

Daily send is the only plan limit on Kenso mailboxes: a mailbox count shown elsewhere does not cap how many they can have.

White-label child only: the parent workspace's caps on mailboxes and domains count every inbox and domain in the workspace, connected ones included. Ask the parent workspace for them, and keep current plus cart within each, with counts from step 2.

Hard-block carts that exceed remaining daily send or a white-label cap. On a credit plan, only the white-label cap and credits block.

Starting mix (easy to change): about 40% Azure / 40% Google / 20% Microsoft of daily volume. On a white-label child, clamp that mix to `caps.mailboxes - currentInboxes` and pack so new domains stay within `caps.domains - currentDomains`. Then 3 inboxes per Google/Microsoft domain (clamp 1-5) and 50 per Azure domain (clamp 1-50; Azure is priced per domain, so fill each one). Checkout `platform` is `GOOGLE` | `MICROSOFT` | `AZURE`.

Steady-state caps: healthy inboxes 30-50/day, new or warming 5-10/day, never above 100/day. Warmup shares the same provider budget as cold. If the target does not fit even at healthy caps, the answer is more mailboxes, not higher caps. What the app's Purchase domains flow accepts is the source of truth.

## 4. Price the cart (credit plans)

Credit prices:

| Item | Credits |
|------|---------|
| Google / Microsoft inbox | 200 credits ($4) per inbox a month |
| Azure domain (up to 50 inboxes) | 2,500 credits ($50) per domain a month |
| Domain registration | (ceil(registrar quote x 1.03) + 1) x 50 credits, first year upfront |

Add the cart up from the table: one line per item, then the total, which is the first month of the inboxes plus the first-year registrations.

A registration needs the registrar's quote, which the app's domain search shows (`domain-selection`). Until the user has it, give the inbox part and say the registrations come on top. Buying needs the registration plus the first month of the order's inboxes in available credits. If the total is more than the credits the user has, shrink the cart, or buy credits at https://app.ken.so/<workspace id>/settings/billing (Dfy: the Kenso team adds credits; white-label child: ask the parent workspace). The app shows the exact charge on its Charge step before anything is paid.

Exempt workspaces skip this step: they pay each domain's price as the app's search shows it (it already includes Kenso's markup) for one year at Stripe checkout, and mailboxes are on the plan.

## 5. Hand off

- Inspect names or tags, search, or buy: load `domain-selection`.
- Import owned domains: load `connect-domains` (BYOD is live).
- In a workspace with domain pages, buying or importing asks the website question first (`domain-selection`, `connect-domains`): "What should people see when they open these domains? A rebuild of your website (recommended) or a redirect to your website?" The answer is the person's, never yours.
- Limits, display names, signatures on existing inboxes: load `inbox-configuration`.

## Refusal handling

The app shows these when the user checks out. What each means and what to tell the user:

| Code | What to tell the user |
|------|------------------------|
| `PLAN_FEATURE_NOT_AVAILABLE` | Free cannot buy Kenso infrastructure. Connect your own inboxes in the app, or upgrade to Platform at https://app.ken.so/<workspace id>/settings/billing. Show `error.recovery.summary` when present. |
| `INSUFFICIENT_CREDITS` | Not enough credits for the order. Show the message (it carries the credits needed and available). Shrink the cart, or buy credits at https://app.ken.so/<workspace id>/settings/billing and retry. Dfy: the Kenso team adds credits. White-label child: ask the parent workspace. |
| `FREE_CREDITS_NOT_ELIGIBLE` | Free and bonus credits can't pay for domains or inboxes, and the bought credits fall short. Show the message (it carries the credits needed, the credits that can pay, and the free part). Buy credits at https://app.ken.so/<workspace id>/settings/billing and retry. Dfy: the Kenso team adds credits. White-label child: ask the parent workspace. |
| `INBOX_LIMIT_REACHED` | Show metrics. Offer upgrade or rebalance limits on existing inboxes. |
| "exceeds your daily send capacity" | The cart exceeds remaining daily send on a plan with a hard cap. Shrink it. It is not a mailbox-slot limit. |
| "workspace mailbox cap" / "workspace domain cap" | White-label child at its parent's cap. Shrink the cart or ask the parent workspace to raise it. |

When no daily send is left on a hard cap, say so. Offer to work with existing infrastructure.

## Boundaries

- Changing or removing a domain happens in the app, on the user's explicit choice (admin). Search and checkout live in `domain-selection`. Import is `connect-domains`.
- Connecting external inboxes / OAuth is a dashboard flow, not this skill.
