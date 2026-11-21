---
name: setup
description: Set up Vinktar product analytics and error tracking in this codebase end to end, from picking the SDK to checking the data arrives and saying where each environment variable goes. Use when asked to install, set up, configure, audit or extend Vinktar, to add error tracking or product analytics to an app, or to add or change tracked events.
---

# Set up Vinktar

Vinktar is product analytics and error tracking. You set it up in this codebase through the
Vinktar tools on the MCP connection this plugin adds.

## 1. Get connected

Look for the Vinktar tools (`get_install_guide`, `list_projects`, `get_project_keys`). Their names
carry a prefix that differs from app to app. This plugin adds one connection, `vinktar`, which works
before anyone has signed in and asks for sign-in at the first call that reads data. The tools are
listed before sign-in, so being there is not enough: call `list_projects`.

- **It answers:** go to step 2.
- **A Vinktar tool whose name ends in `authenticate` is there instead:** call it. It returns a
  sign-in link. Give the link to the person, wait until they say they approved, then go to step 2.
- **It fails for want of sign-in, or only `start_project` and `get_install_guide` are there:** do
  not stop and do not wait. Call `start_project` with the app's name (and its stack as `platform`).
  It returns a write key and a claim link. Go to step 2 with that key in place of
  `get_project_keys`, and give the person the claim link once the first event has arrived: opening
  it signs them in, or makes them an account on the spot, and keeps the project with its data.
  Until they have claimed it, skip `define_event`, `set_project_notes` and `get_setup_status`
  (check arrival with `get_start_status`), and keep a list of the events you add so you can define
  them after.
- **There are no Vinktar tools at all:** what is missing is the connection. Say exactly where, for
  the app you are running in, then wait:
  - Claude Desktop and Claude on the web (chat, Cowork, the Code tab, Claude Code on the web): open
    the Vinktar plugin's Connectors tab, or https://claude.ai/customize/connectors. If Vinktar is
    not listed there, add it (Add custom connector, address `https://mcp.vinktar.com/mcp`). Choose
    Connect. Then start a new chat and ask again: one that was already open may not pick the
    connection up.
  - Claude Code in a terminal or an editor: `/mcp`, pick `vinktar`, choose Authenticate.
  - Codex: `codex mcp login vinktar`. Cursor asks on its own.
  - Anything else: add `https://mcp.vinktar.com/mcp` as an MCP server. It finds the sign-in itself.

  In the browser they sign in to Vinktar, or make an account right there (nobody has to register
  first), leave Build and Configure switched on, and approve. Then carry on from step 2 without
  being asked again.
- **No codebase is open** (a chat with no project, a phone): do not stop there. `get_install_guide`
  starts with what to do: the person opens the project in the Code tab or in Claude Code and asks
  again, or they do the typing while you hand them each file and variable ready to paste. If their
  app already reports to Sentry or Bugsnag, `get_project_keys` has the line that points it at
  Vinktar.

Never ask for a key to paste, and never write a key into the code by hand.

## 2. Follow the guide

Call `get_install_guide` and follow it from start to finish. It is kept current on the server: the
SDKs that exist and their versions, the layout to install in, how to define each event as you add
it (`define_event`), the notes to write about the product (`set_project_notes`), the check
(`get_setup_status`), and the handover. Where this skill and the guide differ, the guide wins.

## 3. Finish with the handover

End with the guide's handover: what was installed, what is tracked, what the check says, and a
table of every environment variable with where it goes locally, in production and in CI, plus the
steps only the person can do.

## Later

The guide has you leave a Vinktar block in this repository's `AGENTS.md`, which is what tells the
next agent any of this is here. Keep it: when you add or change a `track()` call, call
`define_event` in the same step, and when asked what is happening in the product, start with
`whats_changed`.

Before adding an event to an app that is already set up, call `get_install_guide` with
`section: "conventions"`. The short version: event names and property keys are `snake_case`, object
then past-tense action (`report_exported`); a description is one sentence; a name never changes its
meaning, so a new meaning gets a new name.
