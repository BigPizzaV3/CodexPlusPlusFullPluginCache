---
name: get-started
description: Set up agent-swarm.dev in ChatGPT. Ask whether the user already runs an Agent Swarm at a public HTTPS URL, then either point them to the waitlist or the Codex install line, or connect their swarm and suggest a first task.
---

# Get started with agent-swarm.dev

agent-swarm.dev connects ChatGPT to an Agent Swarm that the user runs on their own infrastructure. This skill runs when the user selects **Set up** after installing the plugin.

Rules for this skill:

- Make **no tool call** until the user says they have a swarm.
- Never ask the user to paste a swarm token (`aswt_…`) or any other secret into the chat. The token is entered only on the agent-swarm.dev connections page.
- Do not mention prices, plans, subscriptions, free trials, discounts or promotions.
- Keep each reply short. Offer the options below; do not invent other ones.

## Step 1: ask

Ask exactly one question:

> Do you have an Agent Swarm running at a public HTTPS URL?

If the user already has a linked swarm (a previous `list_swarms` call in this conversation returned one), skip to **Step 3**.

## Step 2a: the user says No

Say that there are two options and show both:

1. **Managed, later.** "We don't run a hosted Agent Swarm today. Leave your email here if you'd want one: https://mcp.agent-swarm.dev/r/waitlist"
2. **Self-host now.** "Paste this line into Codex (the app or the CLI prompt box). It installs Agent Swarm on your infrastructure with a public HTTPS URL and mints your personal token:"

   ```
   Read https://mcp.agent-swarm.dev/r/install and help me install and operate Agent Swarm on our infra with a public HTTPS URL (the skill's HTTPS step). Then mint me a personal aswt_ token for /mcp-user (POST /api/users, then POST /api/users/{id}/mcp-tokens). Ask about my setup before running anything.
   ```

   In a terminal the same text works as `codex "<the line above>"`.

Then say: "When Codex is done you will have two things: your swarm's HTTPS URL and a token that starts with `aswt_`. Come back and tell me you have a swarm." Stop and wait. Do not call any tool.

While they wait, the user can still try the read-only demo: "list my tasks" works without signing in and shows the demo swarm's tasks.

## Step 2b: the user says Yes

Say: "You'll sign in and paste your swarm URL and a personal `aswt_` token on our page, never in this chat."

Then call `list_swarms`.

- **ChatGPT asks the user to connect or sign in.** Tell the user to follow the Connect prompt and sign in with Google, GitHub or an email code. After sign-in, call `list_swarms` again.
- **The tool says no swarm is linked.** Give the user the link from the tool result, or https://mcp.agent-swarm.dev/connections if none is given, and say: "Open this page, enter your swarm URL and your `aswt_` token, and select Link. Tell me when it says Linked." When they confirm, call `list_swarms` again.
- **The page or the tool reports a link error.** Repeat the error in plain words. The usual fixes: the URL must be public `https://` (not localhost or a private IP), `GET /health` on the swarm must answer, the swarm must be recent enough, and the token must belong to an active user.
- **`list_swarms` returns a swarm.** Go to Step 3.

## Step 3: linked

Confirm which swarm is linked (host only), then propose one first task, for example:

> Your swarm is connected. Want me to send it a first task? For example: "Send a task: summarize the README of our main repository."

Only call `send-task` after the user confirms the task text.
