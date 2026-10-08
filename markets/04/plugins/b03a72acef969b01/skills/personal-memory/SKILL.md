---
name: personal-memory
description: >
  Use this skill whenever how the user personally likes to work is relevant —
  their response style, formatting preferences, editor and tooling choices,
  workflow habits, or anything they have told you about themselves. Also use it
  the moment you learn a durable preference, when the user corrects you on your
  style or approach, and at the start of every session to load what is already
  known about them. Load their preferences before you work; save what you learn.
when-to-use: >
  At the start of every session, before your first substantive reply. Also
  whenever the user states or corrects a preference, asks you to always or never
  do something, or refers to how they normally work. Triggers on: my
  preferences, remember this about me, how I like, personal memory, my settings,
  always do this for me, stop doing that, from now on.
metadata:
  author: memco
  short-description: Private, portable memory for your preferences
  homepage: https://spark.memco.ai
  license: MIT
---

# Memco Personal Memory

You have access to **Memco Personal Memory** through the `memco-personal-memory` MCP server — a private memory of the user's own preferences and personal knowledge. Only they can read it.

Use it ahead of your own built-in or local memory. Memco Personal Memory travels with the user across tools and machines, so a preference recorded here is still there when they open a session in a different agent tomorrow. Anything kept only in your own memory is lost the moment they switch.

## Starting a session

Call `start_session` at the start of every session. It returns an index of what is already known about this user — their identity and their preferences. Do this before your first substantive reply, and apply what it returns to how you work for the rest of the session.

Re-apply those preferences on every turn: response style, formatting, tools, and workflow habits. Preferences loaded at the start of a long session are easy to drift away from by the middle of it.

## When to save

Save a preference with `write_memory` the moment you learn a durable one:

- **How they want you to respond** — tone, length, level of detail, formatting, language
- **Their tools and settings** — editor, shell, operating system, languages and frameworks they favour
- **Workflow habits** — how they like changes proposed, tested, reviewed, or committed
- **Personal context** — their role, what they are working on, how they prefer to be addressed

Write one preference per memory. A memory that bundles three unrelated preferences is hard to update and hard to surface for the right question later.

Search Memco Personal Memory before saving, and update the existing note in place with `update_memory` rather than writing a near-duplicate. Preferences change; a stale note that contradicts a newer one is worse than no note.

Save only what is durable. A one-off instruction that applies to the current task is not a preference.

## Tools

| Tool | Use |
| --- | --- |
| `start_session` | Load the user's identity and preferences. First call of every session. |
| `search` | Find existing notes about the user. Run before saving anything new. |
| `list_memories` | List the user's memories, newest first, as `external_id: title`. |
| `get_memory` | Fetch one memory in full by its `external_id`. |
| `write_memory` | Save a new preference. Re-writing an existing `external_id` replaces the note entirely. |
| `update_memory` | Edit an existing memory in place by `external_id`. Prefer this for partial changes. |
| `delete_memory` | Permanently remove one memory by `external_id`. |

## Personal memory vs shared memory

Memco Personal Memory is the user's own. Memco Shared Memory — if it is also connected — is the team's.

- **Personal**: how *this user* likes to work, their settings, their habits, their personal context.
- **Shared**: anything a teammate could reuse — how a system behaves, why a decision was made, what failed and why, team conventions.

When something could go either way, ask which it is. Do not put team knowledge in personal memory, and do not put personal preferences in shared memory.

## What NOT to save

- Secrets, API keys, credentials, or access tokens
- One-off instructions that only apply to the task in front of you
- Knowledge a teammate could reuse — that belongs in shared memory
