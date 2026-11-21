---
name: get-started
description: Introduce Send & Retain after install or when the user asks what it can do, explain how it keeps sending safe, and suggest a first thing to try. Use when the user asks how to use the plugin, what it manages, or where to begin.
---

# Get started with Send & Retain

Explain the plugin in a few sentences, then offer one concrete next step.
Explicit user instructions take priority over this guidance.

## What to say

- Send & Retain runs a company's **email automation** — transactional and marketing email: the
  templates, the event-triggered automations that send them, the contacts and
  segments they go to, and the sending setup behind them.
- One **company = one project**. Call `email_list_projects` first and pass the
  company's `projectId` to every company-scoped tool.
- Tools are prefixed `email_` and return `{ ok: true, … }` or
  `{ ok: false, error }`. Read the error: it usually says what to do next.

## Check the connection first

Installing the skills does not prove that the MCP connection is authorized.
Call `email_list_projects` before claiming the plugin is ready.

- If no `email_` tools are available, check the host's Send & Retain MCP
  connection. The endpoint is `https://sendandretain.com/api/mcp`; authenticate
  through its browser OAuth flow. Do not ask for a provider key or invent an
  API-key requirement.
- In Codex, use the installed plugin's connection controls first. If its
  connection is unavailable and the user asks you to configure it, a direct
  connection is supported: `codex mcp add sendandretain --url
  https://sendandretain.com/api/mcp`, then `codex mcp login sendandretain`
  if sign-in did not start automatically. Reuse an existing matching connection
  instead of registering a duplicate. After setup, start a fresh chat or reload
  the host's MCP connections, then retry `email_list_projects`.
- On an authentication error, reconnect in the host. On a successful empty
  project list, explain that the account has no companies yet; do not treat it
  as a connection failure or create a company without the user's request.
- Distinguish connection status from sending readiness. A working project list
  proves tool access; `email_get_connection_status` reports the company's
  provider, domains, senders, and sending controls.

## How sending stays safe

Say this plainly whenever sending comes up:

- There is **no bulk send**. Every message has one recipient. Mail reaches a
  list only through an automation a person enabled.
- Automations are **always created paused**. Enabling one is a separate call
  that needs the user's explicit go-ahead in this conversation.
- Each company has a send kill switch and an optional daily cap.
- Bounces and complaints suppress addresses automatically. Complaint
  suppressions can never be removed.
- **Provider API keys never go through chat.** If the user offers one, do not
  repeat or use it. `email_get_connection_status` returns the settings page
  (`settingsUrl`) where they enter it themselves.

## What it can do

- Stand up a company: brand kit, starter templates and paused automations for its
  business type (see the `set-up-a-company` skill).
- Write, render and publish templates in the company's brand
  (`author-a-template`).
- Design and test-drive automations (`design-an-automation`).
- Report on delivery and engagement (`delivery-report`) and triage bounces or
  complaints (`triage-deliverability`).

## What it cannot do

Email only: no SMS, push notifications or social posts. It cannot send to a
whole list in one go. Sending needs a connected provider or platform sending
plus a verified domain, which a person completes once per company.

## Suggested first steps

Offer one of these, adapted to what the user mentioned:

- "Which of my automations are live, and what would block the rest?"
- "Draft a welcome email in our brand voice."
- "How did our emails perform this week, by template?"
- "Set up email for a new company from its website."

Do not call a write tool until the user asks for a change.
