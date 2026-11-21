---
name: setup
description: "First-run setup for the monday CRM plugin. Checks the monday MCP connection, walks through OAuth if needed, then detects whether the user already has CRM boards and routes to the right next skill. Say 'connect my monday account', 'set up monday CRM', 'monday CRM setup', or 'get started with monday CRM'."
---

# monday CRM — Setup

Guide the user through first-run connection of the bundled monday MCP connector, then triage whether they are an existing CRM user or a new one.

**This skill is read-only.** It never writes to monday — only checks the connection and reads board metadata.

---


## Offer a useful next step

At the end of a completed response, offer one specific, relevant next thing ChatGPT can do based on what is actually available: offer to help with a suitable first CRM task based on the connection and available boards. Ask whether the user wants that help; do not begin it before they respond. Do not repeat an existing unanswered question or make the offer when the task cannot continue because of a connection or permission failure. Do not promise capabilities, events, or results that have not been verified. Approval to explore or draft is not approval to publish, send, or change CRM data.

## Step 1: No-account detection

Before attempting the MCP connection, ask the user:

> **Welcome to the monday CRM plugin.**
> This plugin connects ChatGPT and Codex to your monday.com CRM boards via the official monday MCP connector.
>
> Do you have a monday.com account? (yes / no / not sure)

- **yes** → continue to Step 2.
- **no** →

  > Don't have a monday account yet? monday CRM has a free tier — start at **https://monday.com/crm**.
  > Once your account is set up, come back and run the `setup` skill to connect it here.

  Stop.
- **not sure** →

  > No worries — let's try connecting. If you have an account, the OAuth flow will find it.

  Continue to Step 2.

---

## Step 2: Check connector status

Call `get_user_context`.

- **Success** → the monday MCP connector is already connected. Continue to Step 4 (Triage).
- **Connection error / tool not found** → the monday MCP connector is not yet connected. Continue to Step 3.

---

## Step 3: Prompt OAuth connection

Print:

> The monday CRM plugin needs its monday connection to work.
> ChatGPT or Codex will prompt you to authorize monday.com via OAuth when the plugin is installed or first used.
>
> **What to expect:**
> 1. A browser window opens to monday.com.
> 2. Sign in (or approve if already signed in).
> 3. Grant access to your workspaces.
> 4. You return to this conversation.
>
> If no prompt appeared: in ChatGPT, open **Plugins → monday CRM** and select **Connect**. In Codex CLI, open `/plugins`, select monday CRM, and complete the connection.

Ask the user: "Ready to connect? (1) yes (2) I need help (3) skip for now"

- **yes** → call `get_user_context` again. If it succeeds, continue to Step 4. If it still fails, go to Step 5.
- **I need help** → go to Step 5.
- **skip for now** → print: "No problem. Ask me to run monday CRM setup whenever you're ready." Stop.

---

## Step 4: Triage — existing CRM user or new user?

**Goal:** Detect whether the user already has CRM-shaped boards and route to the right next skill.

1. Call `search` with query terms: `deals`, `pipeline`, `leads`, `contacts`, `opportunities`, `accounts`, `sales`.
2. Also call `list_workspaces` to enumerate workspaces.
3. Evaluate the results:

**If CRM-shaped boards are found** (boards whose names contain deal, pipeline, lead, contact, opportunity, account, sales, or similar CRM terms):

> monday MCP is connected. You're signed in as **{user.name}** ({user.email}).
>
> I found existing CRM boards in your workspace:
> {list board names with item counts}
>
> You're all set. Here are the skills that work with your existing boards:
> - the `my-focus` skill — your main tasks and signals: what to follow up on, what's blocking, with a draft next step
> - the `morning-briefing` skill — daily pipeline digest
> - the `forecast-dashboard` skill — commit / best-case / pipeline view
> - the `board-diagnosis` skill — structural audit of your CRM board
> - the `bulk-data-hygiene` skill — clean and normalize your CRM data
> - the `update-crm` skill — review customer conversations and propose updates to one record or a batch
> - the `subscribe-to-events` skill — request ChatGPT notifications for customer follow-ups or blockers when event monitoring is available; otherwise, ask for a scheduled check or check My Focus now (also supports board-change options)
>
> Want to start with your morning briefing, or check what needs follow-up in My Focus?

Stop.

**If no CRM-shaped boards are found** (the user has a monday account but no CRM setup):

> monday MCP is connected. You're signed in as **{user.name}** ({user.email}).
>
> I didn't find any CRM boards in your workspace yet. Would you like to:
> - **Build a CRM from scratch** — run the `workspace-builder` skill to set up deal boards, contacts, and pipeline stages tailored to your business.
> - **I already have CRM boards** — tell me the board name and I'll find it.
> - **Just exploring** — no problem. Run any skill when you're ready.

Stop.

---

## Step 5: Troubleshoot

Print:

> **Troubleshooting the monday connection:**
>
> 1. **Plugin not connected** — in ChatGPT, open **Plugins**, find monday CRM under **Installed**, and select **Connect**. In Codex CLI, run `/plugins` and check the plugin is installed and turned on, then start a new session.
>
> 2. **Authorization failed** — your monday admin may need to allow AI connectors: monday **Admin → Permissions → AI Connectors**. If your company uses a ChatGPT workspace, a ChatGPT admin may also need to enable the plugin.
>
> 3. **OAuth didn't open a browser** — in a headless or remote environment, complete the connection from ChatGPT on the web or the ChatGPT desktop app instead.
>
> 4. **Workspace not visible** — your monday account must have access to the boards. Ask the board owner or your admin.
>
> 5. **Still stuck** — check the [monday MCP repo](https://github.com/mondaycom/mcp) for known issues or contact monday support.

Stop.
