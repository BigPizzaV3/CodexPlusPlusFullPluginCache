---
name: get-started
description: Get oriented in a connected Kenso workspace - see the campaigns and where each one stands, then learn what Kenso can help with from the chat, area by area, with one example ask each.
---

# Get started with Kenso

Kenso runs B2B outbound: cold email campaigns to business contacts, their leads, their email sequences and the replies they get, plus the inboxes, accounts, meetings, pages and workflows around them. This skill orients a newly connected user, then shows what else Kenso can help with here.

## Steps

1. Call `list_workspaces`. If it returns more than one workspace, show their names and ask which one to work in, then pass that workspace's id as workspace_id on every later call. With one workspace, skip this and leave workspace_id out.
2. Call `list_campaigns` and summarize each campaign in one line: name, status (draft, active, paused, completed) and whether sending has started. If there are no campaigns, say so and explain that campaigns are created in the Kenso app at https://app.ken.so or by asking here, for example "Create a draft campaign called Q1 agency owners."
3. Offer what Kenso can help with, one line per area with its example ask. Where an ask says <campaign name>, use a real campaign from step 2, or leave that ask out when there is none.
   - **Campaigns and replies**: "Why did replies drop on <campaign name>, and what should I change?"
   - **Workspace setup**: "Please set up my workspace."
   - **Domains and inboxes**: "Help me set up the inboxes I send from."
   - **Deliverability**: "Bounces are up. Are my domains and inboxes healthy?"
   - **Accounts and pipeline**: "Which deals in my pipeline are stuck, and what is the next step on each?"
   - **Meetings**: "Prep me for my next sales meeting."
   - **Studio**: "Help me plan a Studio page for my target accounts."
   - **Workflows**: "Help me plan a workflow that qualifies each new lead and flags the good ones."
4. Only when step 2 listed a campaign, also offer a quick look at one of them, with its real name in the ask: "Show me the leads in <campaign name>." or "Show me the email sequence for <campaign name>."
5. When the user picks an area, follow the Kenso skill for that job. If its text is not already in the conversation, `load_ken_skill` returns it by name.

Some steps happen only in the Kenso app, such as connecting a mailbox, building a Studio template or a workflow, and changing a deal. The skill for that job links the page in the Kenso app (https://app.ken.so) where the user takes that step. Say so plainly; never claim a step was done here when the user has to do it in the app.

## Rules

- Work only in the workspace the user picked. Use only ids `list_workspaces` returned; do not guess workspace or client IDs. When the user names another of their workspaces, switch workspace_id to it.
- Ask the user to confirm before any action that sends email, starts or resumes a campaign, or deletes data. Drafts, reads and blocklist additions do not need extra confirmation.
- Kenso is for outreach to people in their business roles. Honor opt-outs: when someone asks not to be contacted, add them to the blocklist with `add_blocklist_entry`.
- Kenso does not change plans, buy credits or process payments from the chat. Billing is managed by a workspace admin in the Kenso app.
- Report tool errors in plain words and suggest the next step. Do not retry a failed write more than once.
