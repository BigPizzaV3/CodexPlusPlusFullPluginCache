---
name: delivery-setup
description: Set up a workspace's sending - read its inboxes, domains and capacity, pick a path (claim warmed inboxes, order or connect domains, connect Google or Microsoft mailboxes, import SMTP inboxes, or a sending provider), set the link host and connect LinkedIn accounts, routing each step to the infra skills.
---

# Delivery setup

This is the front door for sending setup: "set up my sending", "I need inboxes", "connect my Google mailboxes", "add my LinkedIn". These tools cannot read or change inboxes, domains, LinkedIn accounts, sending providers or credits, so every step happens in the Kenso app, on the Email Delivery page, https://app.ken.so/<workspace id>/delivery. You find out what the user has, pick a path with them, and walk them through each step there. Four skills hold the deep steps; load the one a step names with `load_ken_skill`:

| Step | Skill |
|---|---|
| How many domains and inboxes for a daily volume | `infra-planning` |
| Search and buy new domains | `domain-selection` |
| Bring domains the user already owns | `connect-domains` |
| Daily limits, display names, signatures, forwarding, warmup on existing inboxes | `inbox-configuration` |


## The rules

- **Paid steps need a yes with the price the app shows.** New domains and Kenso mailboxes cost credits (or a Stripe checkout on some workspaces). The app shows the price before it charges. Never quote a price from memory, and never call a paid step free.
- **The owner connects their own account.** A mailbox or LinkedIn account is connected by the person who owns it, signed in to Kenso in this workspace. Never offer to sign in for them.
- **Secrets stay in the app.** A mailbox password or a provider key is entered in the app only. Never ask the user to paste one into this chat; if they do, tell them not to share it here and to enter it in the app.
- **Setup is not sending.** Nothing here launches a campaign. Launches, and limit or pause changes on a client's campaign or inboxes, need a person's yes, and on a client's workspace that yes names the client.

## Step 0 - Read what the workspace has

Ask the user to read you:

1. From https://app.ken.so/<workspace id>/delivery?tab=inboxes: how many inboxes are active and how many are warming, their daily limits, and the sending domains with their status.
2. From https://app.ken.so/<workspace id>/delivery?tab=linkedinAccounts: the LinkedIn accounts.
3. From https://app.ken.so/<workspace id>/settings/billing: the plan and available credits, for the paid paths.

New domains and warmed inboxes need a paid plan. On a Free workspace, say so and point to https://app.ken.so/<workspace id>/settings/billing.


Tell the user what they have in one short block: active inboxes and domains, inboxes still warming, the daily capacity (the daily limits of active inboxes added up), LinkedIn accounts, and credits.

## Step 1 - Pick the path

Ask what they have and what they want, then pick:

| The user has or wants | Path |
|---|---|
| Nothing yet | `infra-planning` to size it, then `domain-selection` to buy, or connect mailboxes they already have (Steps 3 to 5) |
| New domains of their own | `infra-planning` to size it, then `domain-selection` to buy |
| Domains they already own | `connect-domains` |
| Google Workspace or Microsoft 365 mailboxes | Connect by sign-in (Step 3) |
| Mailboxes at another host, with SMTP and IMAP details | Import them (Step 4) |
| An account with a sending provider | Connect the provider (Step 5) |

When they name a daily volume ("2,000 a day"), load `infra-planning` first to size it.

## Step 2 - Claim warmed inboxes

Claiming Kenso's pre-warmed inboxes is not available from this chat. Offer the other paths in Step 1.

## Step 3 - Connect Google or Microsoft mailboxes

On https://app.ken.so/<workspace id>/delivery?tab=inboxes, the mailbox owner clicks Connect Inbox, picks Gmail or Outlook, and signs in with that mailbox. They must be signed in to Kenso, in this workspace.

- When the company blocks new apps, a Google Workspace or Microsoft Entra admin approves the Kenso app first.
- Repeat per mailbox. Each one shows on the Inboxes tab once it is connected.

## Step 4 - Import SMTP and IMAP mailboxes

On the Inboxes tab, Connect Inbox > SMTP connects one mailbox at a time: the user enters its address, its password, and the SMTP and IMAP host and port from their mail host, in the app.

- First name, last name and daily limit are set afterwards with `inbox-configuration`.

## Step 5 - Connect a sending provider

On the Inboxes tab, Connect Inbox > Sending provider, where it is on for the workspace.

1. The user picks the provider and enters its key in the app.
2. Some providers' terms forbid cold outreach on the user's own account. If the user is not sure about theirs, have them check the provider's terms before they connect it, and suggest another path when it does.
3. They add each sending address with its display name. When the provider sends from its own inboxes, the address must already exist in the provider account.

## Step 6 - Domain orders already open

An open domain order shows as a banner on the Inboxes tab: Domain purchase in progress, waiting on external approval, or finished with issues. An order waiting on payment has Continue, which reopens checkout. Cancel an order only when the user asks. New searches and orders go through `domain-selection`.

**Website question (workspaces with domain pages).** When the app asks what people should see when they open these domains, the answer is the person's, never yours: "A rebuild of your website (recommended) or a redirect to your website?" A rebuild shows a copy of their home page on every one of these domains; a redirect sends visitors to their website, as today.

## Step 7 - The link host

The link host (for example `go.acme.com`) serves Studio pages and the open pixel from the workspace's own domain. These tools cannot read or set it, so skip this step here.

## Step 8 - LinkedIn accounts

1. On https://app.ken.so/<workspace id>/delivery?tab=linkedinAccounts, the account owner clicks Connect LinkedIn Account and signs in. An account that dropped is reconnected from the same tab.
2. A campaign sends on LinkedIn when its Sequence tab has the LinkedIn channel on, and needs a connected account before launch. Choosing which accounts a campaign uses is not available from this chat.

## Step 9 - Check and hand over

- Each new inbox warms before it sends at volume: plan on two to three weeks before full volume. Its warmup state shows on the Inboxes tab.
- Each new domain, once its DNS is in: its SPF, DKIM, DMARC and Nameserver chips on the Inboxes tab show whether its records pass.
- Report: what is connected, what is warming and until when, what the user still has to do (DNS records, sign-ins, admin consent, payments), and the daily capacity now and once warm.
- Next: `inbox-configuration` for names, signatures, forwarding and limits; `deliverability-guard` once mail is flowing.

## What this skill cannot do yet

- Read or change inboxes, domains, LinkedIn accounts, sending providers or domain orders from this chat. Every step above happens in the app.
