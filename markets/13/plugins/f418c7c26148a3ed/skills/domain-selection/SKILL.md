---
name: domain-selection
description: Use when reviewing sending domains or ordering new ones on a paid workspace, paid in credits or through Stripe checkout.
---

# Domain selection

Review live sending domains. On a paid plan, search names and order them. Credit plans pay registration and inboxes in credits; exempt workspaces pay the search hit `price` for one year through Stripe checkout. Never present names as ordered before the order is paid. To import domains the user already owns, load `connect-domains` (BYOD is live).

These tools cannot read domains, plans or credits, and cannot search or buy names. You bring the naming rules and the judgement; the user searches and buys in Kenso on the Email Delivery page, https://app.ken.so/<workspace id>/delivery?tab=inboxes, with New Inbox > Purchase Domain. Its steps are Calculator, Search, Settings and Charge.

## 1. Paid plan, credits, and capacity

Before any search or order:

1. Ask the user for their plan, on https://app.ken.so/<workspace id>/settings/billing. Plans that buy Kenso domains, with billing Active or Trialing: Platform, Dfy, grandfathered Starter / Growth / Core (all credit plans), and VIP (exempt). If Free, stop adds: Free cannot buy Kenso domains or inboxes and connects its own inboxes in the app, or upgrades to Platform on that page. A white-label child has its credits and caps run by its parent workspace.
2. Ask for their available credits, on the same page.
3. The daily send left on the plan is not readable here. The app's Purchase domains flow checks it, and the credits, before it charges.
4. On a credit plan credits are the limit. Any other paid plan has a hard daily send cap: when none is left, stop new orders and work with existing domains.

Mailbox count on a hard cap is the daily send left / per-inbox daily (Google/Microsoft 25, Azure 5). Daily send is the plan limit: a mailbox count shown elsewhere does not cap how many they can have. White-label child only: the parent's caps count every inbox and domain in the workspace, connected ones included, so current plus cart must stay within them. Otherwise there is no domain-count allowance.

## 2. Naming rules (advice only)

- Never cold-send from the naked brand or primary company domain.
- Prefer `get{brand}.com`, `try{brand}.com`, `{brand}hq.com`. Short, pronounceable, no hyphens or numbers.
- Search offers `.com`, `.net`, `.org`, `.shop`.

Advice is not an order. Search before claiming a name is free.

## 3. Read existing domains

Existing domains are not readable here. Ask the user to open https://app.ken.so/<workspace id>/delivery?tab=inboxes and tell you the domains they have, with their status.

Summarize names, status, tracking posture. Domains and inboxes page: https://app.ken.so/<workspace id>/delivery?tab=inboxes.

## 4. Search

Needs a paid plan, the admin role on the workspace, and some daily send left when daily send is a hard cap.

The user searches in the app's Search step: Keyword, with the words you suggest, or Exact name for one name. Search more shows more names.

Each name the search returns has its first-year price. Banned names are left out. Premium is allowed if they pay it.

What the user pays for the first year:

- Credit plans: (ceil(registrar quote x 1.03) + 1) x 50 credits, as the app shows it. A renewal is charged each year after.
- Exempt workspaces: the price at Stripe checkout. It already includes Kenso's markup, so show it as is.

Have the user read you the names, their first-year prices and which platforms each can take, then help them pick. Do not put Google inboxes on a name that is not Google-available.

## 5. Checkout

Requires workspace admin (backend FullAccess). After the user confirms names, platforms, mailbox identities, forwarding URL, and the total:

On a credit plan, add the cart up first: the registrations, plus the first month of the order's inboxes (200 credits per Google or Microsoft inbox, 2,500 credits per Azure domain). The order needs that in available credits. If the user has fewer, shrink the cart or buy credits first.

**Website question (workspaces with domain pages).** When the app asks what people should see when they open these domains, the answer is the person's, never yours: "A rebuild of your website (recommended) or a redirect to your website?" A rebuild shows a copy of their home page on every one of these domains; a redirect sends visitors to their website, as today.


The user enters the order in the app's Settings step: Sender name (First and Last, with Apply to all inboxes), Forwarding URL, and for each mailbox its First, Last, username and an optional Profile picture URL. The Charge step then shows the total, and Pay N domains places the order.

For each domain, agree with the user:

- the name and its platform: Google, Microsoft or Azure
- its mailboxes, each with a first name, last name, username and an optional profile picture: Google/Microsoft 1-5, Azure 1-50, one platform per domain. Usernames: real name, first.last first, no role names

Forwarding URL defaults to the workspace website (add `https://` if missing). The workspace owner email is the catch-all; checkout fails without it.

On a credit plan the order is paid from credits at once; otherwise the app sends the user to Stripe checkout. The new domains then show on the Inboxes tab while they set up, until each is active, needs action, or failed. An order paid but waiting for the client's approval is still in flight.

Mailboxes on credit plans: 200 credits ($4) per Google/Microsoft inbox a month and 2,500 credits ($50) per Azure domain a month (up to 50 inboxes). On exempt workspaces they are on the plan.

## 6. Present live inventory

| Domain | Status | Notes |
|--------|--------|-------|
| send.example.com | Active | tags / tracking host |

## 7. Mutations on existing domains

Changing or deleting a domain happens in the app, after the user confirmed the exact domain and change here. A domain's site redirect is its forwarding URL: on the Inboxes tab, select the domain's inboxes, then Set forwarding URL. Leave MX/SPF/DKIM/DMARC alone. Turning on click rate tracking does not publish the click host; that provisioning is a staff step.

## 8. Refusal handling

The app shows these when the user checks out. What each means and what to tell the user:

| Code | What to tell the user |
|------|------------------------|
| `PLAN_FEATURE_NOT_AVAILABLE` | Free cannot buy Kenso infrastructure. Connect your own inboxes in the app, or upgrade to Platform at https://app.ken.so/<workspace id>/settings/billing. |
| `INSUFFICIENT_CREDITS` | Not enough credits for the registration plus the first month of the order's inboxes. Show the message (it carries the credits needed and available). Shrink the cart, or buy credits at https://app.ken.so/<workspace id>/settings/billing and retry. Dfy: the Kenso team adds credits. White-label child: ask the parent workspace. |
| `FREE_CREDITS_NOT_ELIGIBLE` | Free and bonus credits can't pay for domains or inboxes, and the bought credits fall short. Show the message (it carries the credits needed, the credits that can pay, and the free part). Buy credits at https://app.ken.so/<workspace id>/settings/billing and retry. Dfy: the Kenso team adds credits. White-label child: ask the parent workspace. |
| `INBOX_LIMIT_REACHED` | Show what the message says is used, the limit and what is left. Rebalance existing mailboxes, or upgrade. |
| "exceeds your daily send capacity" | The cart exceeds remaining daily send on a plan with a hard cap. Shrink it. It is not a mailbox-slot limit. |
| "workspace mailbox cap" / "workspace domain cap" | White-label child at its parent's cap. Shrink the cart or ask the parent workspace to raise it. |

If checkout fails because too little daily send is left on a hard cap, shrink the cart.

## Boundaries

- Inbox tuning belongs in `inbox-configuration`.
- Sizing against daily send and credits belongs in `infra-planning`.
- Importing owned domains belongs in `connect-domains`.
