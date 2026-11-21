---
name: connect-domains
description: Import customer-owned sending domains onto platform-managed Cloudflare nameservers. Walk capacity, paste names, preview, MX/site confirm, import, registrar NS change, then nameserver check.
---

# Connect domains

Import domains the user already owns onto Kenso. Kenso creates the Cloudflare zone and returns **Kenso Cloudflare nameservers**. The user changes nameservers at their registrar. Kenso owns the zone. Customer Cloudflare API tokens are not supported.

These tools cannot read capacity or billing and cannot import domains. You plan the import with the user, and they run it in Kenso on the Email Delivery page, https://app.ken.so/<workspace id>/delivery?tab=inboxes, with New Inbox > Bring existing domain. Its steps are Capacity, Domains, Settings, Inboxes and Nameservers, and the sections below follow them. Buying new domains (search, checkout) belongs to `domain-selection`.

The import needs the **admin** role on the workspace. Agree the cart with the user before they submit it.

Imported domains get Kenso inboxes, so import is paid like any Kenso inbox. Credit plans pay in credits: 200 credits ($4) per Google / Outlook inbox a month and 2,500 credits ($50) per Azure domain a month (up to 50 inboxes). There is no registration charge. Exempt workspaces (VIP) have mailboxes on the plan.

## 1. Capacity

The app's Capacity step shows the daily send left and the inboxes the workspace has. Ask the user what it shows, and for their plan and available credits (https://app.ken.so/<workspace id>/settings/billing). A white-label child has its credits and its mailbox and domain caps run by its parent workspace.

Done when you know the daily send left, whether the plan is a credit plan, the existing Google / Outlook / Azure counts, the available credits, and the white-label caps when they apply.

Daily-send math:

- The plan's daily send is emails per day. Do not divide a monthly email limit by 30.
- On a credit plan (Platform, Dfy, grandfathered Starter / Growth / Core) the plan's daily send is a planning figure and credits are the limit. Any other paid plan has a hard cap.
- Google and Outlook (MICROSOFT) = 25/day each
- Azure = 5/day
- On a hard cap, mailbox count is the daily send left / that per-inbox daily. Daily send is the plan limit: a mailbox count shown elsewhere does not cap how many they can have.
- Size the cart as `sum(mailboxes * daily)`. On a hard cap, keep it within the daily send left. White-label child only: the parent's caps count every inbox and domain in the workspace, connected ones included (the user counts them on the Inboxes tab), so current plus cart must stay within the parent's mailbox and domain caps.

On a hard cap, the daily send left is the plan cap, not a domain-count allowance.

Ask how many Google, Outlook, and Azure inboxes they want. Derive domain counts:

- Google / Outlook: 1-5 inboxes per domain
- Azure: 1-50 inboxes per domain
- Domain count per platform is between `ceil(inboxes / maxPerDomain)` and `inboxes`
- Every imported domain gets at least one mailbox. Max 50 domains

On a hard cap or a white-label child: if the cart would exceed the daily send left or a white-label cap, shrink inbox counts before the Domains step. Do not submit an over-capacity cart.

## 2. Paste names

Collect apex names into platform pools (Google, Outlook, Azure). Lowercase, no subdomains.

Done when each pool has enough apexes for the inbox counts from step 1.

## 3. Preview

In the app's Domains step the user enters each name with its platform: Google, Outlook or Azure. The app checks each name. What its check can find, and what to do:


| `eligibility` | What to do |
|-------|------------|
| Eligible | Include |
| InUseMx (the domain already receives mail) | Warning. Ask the user to continue on that name. If no, drop it |
| LiveWebsite (the domain serves a live site) | Same as InUseMx |
| LookupFailed | Cannot submit. Check it again later. Keep it off the cart |

If a name cannot take its platform (Google needs Google Workspace availability, Outlook needs Microsoft 365), drop that name or move it to an allowed platform. Azure is allowed unless the lookup failed.

A name refused as blocklisted is on Spamhaus DBL or SURBL. Drop that name and pick another: the import refuses it, and confirming does not lift it.

A warning is not a hard fail. If a pool falls below packing minimum after drops, go back to step 1 or 2.

Paid-plan errors ("A paid plan is required", Forbidden) and over-capacity are hard stops. Import needs Platform, Dfy, VIP, or a grandfathered Starter / Growth / Core plan, with billing Active or Trialing. Free cannot import onto Kenso inboxes: it connects its own inboxes in the app, or upgrades to Platform at https://app.ken.so/<workspace id>/settings/billing. Over-capacity comes only from a hard cap.

Done when every remaining name passed or its warning is confirmed, and packing holds.

## 4. Identities and forwarding

Forwarding URL is required (`http://` or `https://`). Prefill from the workspace website; otherwise ask. The workspace owner email becomes the catch-all; import fails without it.

Per mailbox: `first_name`, `last_name`, `username` (local-part only), optional `profile_picture_url` for Google/Outlook (omit for Azure). Username order and charset: `references/usernames.md`.

On a credit plan, price the cart: 200 credits per Google or Outlook mailbox a month, and 2,500 credits per Azure domain a month. The import needs the first month in available credits. If the user has fewer, shrink the cart or buy credits first at https://app.ken.so/<workspace id>/settings/billing.

**Website question (workspaces with domain pages).** When the app asks what people should see when they open these domains, the answer is the person's, never yours: "A rebuild of your website (recommended) or a redirect to your website?" A rebuild shows a copy of their home page on every one of these domains; a redirect sends visitors to their website, as today.

Show the cart (names, platform, mailbox count, monthly credits on a credit plan, forwarding URL). Get a yes before the user submits it in the app.

## 5. Import

The user enters what you agreed in the app: the Forwarding URL in the Settings step, each mailbox's first name, last name and username in the Inboxes step, then submits.

Partial success is normal. The app's last step, Update nameservers, lists the Kenso Cloudflare nameservers for each domain it accepted. Cloudflare NS are per zone: the user copies them from there, never from memory. A name it refused shows its reason: drop it or fix it and continue.


## 6. Registrar nameservers

Tell the user, registrar-agnostic:

1. Open the domain at their registrar.
2. Replace the current nameservers with the pair the app showed.
3. Save. DNS can take minutes to hours.

If the domain sits on someone else's Cloudflare account, they still point NS at the Kenso pair and leave the old account.

Done when the user says they updated nameservers, or they want to wait.

## 7. Check nameservers

Nameserver status is not readable here. After they confirm, the domain's Nameserver chip on the Inboxes tab shows whether its zone is active.

Kenso polls about every 15 minutes. After about 24 hours without an active zone the status becomes action required (still waiting, NS do not expire). After 14 more days the import is abandoned (`failed`).

Do not have the user check on a timer. Ask them to look again later if they want to know.

## Errors

| Signal | What to tell the user |
|--------|------------------------|
| Paid-plan / Forbidden / `PLAN_FEATURE_NOT_AVAILABLE` | Free cannot import onto Kenso inboxes. Connect your own inboxes in the app, or upgrade to Platform at https://app.ken.so/<workspace id>/settings/billing. Show `error.recovery.summary` when present |
| `INSUFFICIENT_CREDITS` | Not enough credits for the first month of the imported inboxes. Show the message (it carries the credits needed and available). Shrink the cart, or buy credits at https://app.ken.so/<workspace id>/settings/billing and retry. Dfy: the Kenso team adds credits. White-label child: ask the parent workspace |
| `FREE_CREDITS_NOT_ELIGIBLE` | Free and bonus credits can't pay for domains or inboxes, and the bought credits fall short. Show the message (it carries the credits needed, the credits that can pay, and the free part). Buy credits at https://app.ken.so/<workspace id>/settings/billing and retry. Dfy: the Kenso team adds credits. White-label child: ask the parent workspace. |
| Over capacity | Hard cap only. Shrink inbox counts until the cart fits the daily send left. It is not a mailbox-slot limit |
| "workspace mailbox cap" / "workspace domain cap" | White-label child at its parent's cap. Shrink the cart or ask the parent workspace to raise it |
| LookupFailed | Cannot import until the app's check passes the name, or it shows only a warning. Check again later |
| DomainPendingElsewhere | Another workspace's import still holds the name and has not moved its nameservers. The error names a TXT record (name and value): the user adds it at the domain's own DNS (where they edit its records today), waits for DNS to update (it can take minutes, sometimes longer), then retries the import. Only a workspace that controls the DNS can add it |
| ClaimLookupFailed | The TXT record could not be read right now. Retry later. Not the same as LookupFailed |
| ConfirmRequired | MX or live site. Continue or drop that name |
| DomainBlocklisted | On Spamhaus DBL or SURBL. Drop that name and pick another. Retrying or confirming does not lift it |
| PlatformUnavailable | That name cannot take that platform. Drop it or move it to an allowed platform |
| Owner email missing | Set the workspace owner email, then retry |

## Boundaries

- Imports domains the user already owns. Registering new names is `domain-selection`.
- Kenso Cloudflare nameservers only. Never ask for a customer Cloudflare token.
- Existing domains are managed on the Inboxes tab, https://app.ken.so/<workspace id>/delivery?tab=inboxes, not in this cart.
- Inbox tuning after the domain is active belongs in `inbox-configuration`.
