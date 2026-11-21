---
name: setup-workspace
description: Set up a workspace end to end - confirm intent, research the website, propose the company profile and logo, suggest teammate invites, explain the blocklist, integrations, and sending infrastructure with links, then hand off to campaign build. The canonical response to "Please set up my workspace". Works on every plan including Free.
---

# Setup Workspace

Onboarding for a new Kenso workspace. Works on every plan, including Free.

Trigger on "Please set up my workspace", "set up my workspace", "onboard me", "get me started", or a fresh workspace with empty company settings.

## Posture

- Conversational and stepwise. Announce the steps once, then work through them in order.
- **Approval gate:** every write is shown first and made only after the user says yes. Reads never need approval. One proposed write at a time.
- Never abort the whole setup because one step failed. Mark it skipped and keep going.

Steps to announce:

1. Confirm intent and workspace
2. Research the website
3. Company profile and logo
4. Invite teammates
5. Blocklist and integrations
6. Sending infrastructure
7. Hand off to campaign build

## Tools

The only call here is `list_workspaces`: the workspaces this user can access, with their ids. These tools cannot read or change the company profile, members, invitations or the plan, so every write in this flow is a page in the app. You draft and propose; the user saves:

| Need | Page |
|------|------|
| Company name, website, LinkedIn page, company context, logo | https://app.ken.so/<workspace id>/settings/company |
| Members, pending invitations, invites | https://app.ken.so/<workspace id>/settings/users |
| Plan and credits | https://app.ken.so/<workspace id>/settings/billing |

Research the website with your own web browsing when you have it; otherwise ask the user to paste the text of their home and about pages. This skill never writes workspace files.

Never buy domains or inboxes, never provision sending infrastructure, never create API keys or webhooks, and never handle credentials (API keys, OAuth tokens, passwords) in chat. Link to the page instead.

**Role:** saving the company profile and inviting teammates need the workspace **admin** role. If the user is a member or view-only, draft anyway, explain what an admin needs to save, and skip the saves.

## Step 1 - Confirm intent and workspace

Confirm the user wants to set up this workspace now and say what you will cover.

Ask once how much cold email they have run, and match your pace to the answer:

- **New to it:** explain each step in a sentence before you act.
- **Has run campaigns before:** skip the explanations and keep each step short.
- **Expert:** offer to jump to the steps they want and skip the rest. The approval gate still applies to every write.

Resolve the workspace before any other call:

1. Call `list_workspaces`. With one workspace, confirm its name with the user.
2. With several, show them and ask which one to set up. Every app link below is for that workspace.

Then ask for the plan, shown on https://app.ken.so/<workspace id>/settings/billing: Free, Platform (the self-serve plan), Core, VIP, or grandfathered Starter / Growth / Dfy. Platform, Core / VIP and the grandfathered paid plans count as paid. If the user does not know, continue with the plan **unknown**. Never block setup on it.

On Free, say early: "You're on Free - the company profile, invites, and guidance all work. Sending domains and inboxes unlock when you upgrade."

## Step 2 - Research the website

Ask the user to open https://app.ken.so/<workspace id>/settings/company and tell you what is in Company Name, Website, LinkedIn Profile and Context, and whether a logo is set. Note which are empty.

If the website is empty, ask for it. Then run the research tool on it. Use only what the research returns plus what the user tells you:

- Prefer facts from the site. A field the sources do not support stays empty - never invent customers, metrics, or product claims.
- The company name is the real company name on the site, not a product name alone.
- The LinkedIn company URL must be a `linkedin.com/company/...` link found on the site (usually the footer). A personal `linkedin.com/in/...` profile is not the company page.

If research fails or returns little, say so and draft from what the user tells you. For a deeper pass later, the `knowledge-setup` skill covers it.

## Step 3 - Company profile and logo

Name, website, LinkedIn company URL, and company context are all part of setup, not extras. Every downstream campaign reads them for research, qualification, and personalization. Fill each one you can and ask once for each you cannot.

Draft the company context with these exact section headers:

**Company / What we do / Who we serve / Value prop & differentiation / Voice & tone / Don'ts (optional)**

Condensed rules (full guide: `references/company-context-guide.md`):

- Extract, don't invent
- Campaign-agnostic: no filters, no numeric disqualifiers, no case studies, no offers or CTAs
- First-person plural ("we")
- Target 400-700 tokens

Show the full proposed profile (name, website, LinkedIn URL, company context) and ask for approval or edits. On approval, the user saves it on https://app.ken.so/<workspace id>/settings/company: Company Name, Website, LinkedIn Profile, and the approved draft in Context, then Save.

Only those four fields belong to this step. Change only the fields that changed, and never clear one unless the user asked. After they save, say which of the four are set and which are still empty, and offer edits to the voice and tone.

**Logo:** saving a Website or LinkedIn Profile on that page fetches the logo when it can. Otherwise the user uploads an image file in the logo section of the same page. Skippable.

## Step 4 - Invite teammates

Ask who is already in: members and pending invitations are on https://app.ken.so/<workspace id>/settings/users. Do not re-invite a member or someone with a pending invite; an expired invite can be sent again.

Suggest inviting the people who will review campaigns or handle replies. Confirm the list of emails, then the user invites each one on that page: Invite Member, Email Address, Role, Send Invitation. Kenso sends the invitation email.

- An admin can change roles later on the same page.
- If the app says the seat limit is reached, relay its message and the upgrade path on https://app.ken.so/<workspace id>/settings/billing, then continue.
- If the invite fails because the workspace is not linked to an organization, do **not** invite as a staff user and do not retry. Tell the user Kenso support needs to link the workspace to its owner's organization first (give them the workspace id and the owner's email), then invites will work.

Invites are skippable.

## Step 5 - Blocklist and integrations

Pure guidance. No writes. Message shapes: `references/setup-messages.md` (unbranded; fill its `<... link>` placeholders with the links in this file).

**Blocklist (state the policy verbatim):**

> Blocklist upload stays in-platform. Do not ask the user to paste their client list or upload a CSV into this conversation - guide them to the blocklist page instead.

Explain that the blocklist keeps current clients, partners, and anyone they cannot contact from ever getting cold email, and that they upload or maintain it themselves at https://app.ken.so/<workspace id>/settings/blocklist. Never ingest a client list, never solicit a paste, and never add entries for them.

**Integrations:** optional and low pressure. Connect when ready at https://app.ken.so/<workspace id>/settings/integrations:

- CRM sync: https://app.ken.so/<workspace id>/settings/integrations/crm
- Calendar: https://app.ken.so/<workspace id>/settings/integrations/calendar
- LinkedIn accounts connect from https://app.ken.so/<workspace id>/delivery?tab=linkedinAccounts
- API keys, when they need them: https://app.ken.so/<workspace id>/settings/integrations/api-keys

OAuth stays in the browser. Never claim setup connected anything.

## Step 6 - Sending infrastructure

Explain, then link. Never buy, import, or provision anything in this flow.

Cold email goes out from separate sending domains (never the main company domain) with a few inboxes on each. A Google or Microsoft inbox sends about 25 emails a day, so volume comes from several inboxes, and new inboxes warm up before they reach full volume.

Branch on the Step 1 preflight:

- **Free:** "Paid plans unlock sending domains and inboxes. Upgrade anytime at https://app.ken.so/<workspace id>/settings/billing, then set them up on the domains and inboxes page." Do not surface any plan error to a Free user; this branch is the graceful path.
- **Paid** (Platform, Core / VIP or a grandfathered paid plan): buy new sending domains, connect ones they own (BYOD), and see inboxes on the domains and inboxes page, https://app.ken.so/<workspace id>/delivery?tab=inboxes. Capacity is daily emails, so do not quote a mailbox count as an allowance.
- **Unknown plan:** give the Free line and the domains and inboxes link in one sentence each.

A paid user who wants help sizing and setting this up can load `infra-planning`, `domain-selection` or `connect-domains` with `load_ken_skill` later. The purchase and import happen in the app.

## Step 7 - Hand off to campaign build

1. Show the steps with **done** / **skipped** for each.
2. Offer the first campaign: "You're ready to build your first campaign." When they agree, create it as a Draft with `create_campaign` and send them to https://app.ken.so/<workspace id>/campaigns to build its audience and copy in Kenso. A Draft sends nothing until a person launches it.

## Plan limits and errors

Plan limits are information, not failure. When the app shows a plan limit (domains, inboxes, seats or AI credits), relay its message and the upgrade path on https://app.ken.so/<workspace id>/settings/billing as friendly next steps, and continue.

If `list_workspaces` fails, retry once, then continue with the workspace the user names. If a page refuses the user, that part is not available to their account: continue without it.

## Free-plan success bar

A Free user reaches the hand-off with the company profile and context drafted and saved in the app, the logo set (if they had one), invites sent within seats, blocklist and integrations guidance given, and an upgrade pointer for sending infrastructure, with zero error-shaped plan output.
