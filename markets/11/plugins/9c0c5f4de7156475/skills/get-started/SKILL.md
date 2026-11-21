---
name: get-started
description: Explain what Sayli can do in this assistant and help someone reach a first useful result. Use when a person has just added Sayli, asks what Sayli can do here, or has no calls in Sayli yet.
---

Sayli is the user's meeting memory: briefs, decisions, action items and transcripts of calls they recorded with the Sayli desktop app or imported into Sayli. Here it is read-only. It does not listen to calls, record, send or change anything.

## What to offer

Three things work well. Offer them in one short list, in the user's language:

1. Prepare for a call: "Help me prepare for my call with <company or person>."
2. Draft a follow-up: "Draft a follow-up from my last call."
3. Review open commitments: "Which commitments are still open?"

Then do whichever the user picks, with the matching skill.

## When there is nothing to read yet

If `show_open_commitments` or `prepare_call` returns status `no_meetings`, the workspace has no calls. Say so plainly and give the next step the tool returned: record a call with the Sayli desktop app, or import past transcripts in Sayli. A brief is ready a minute or two after a call ends. Do not make up an example result with invented names.

## Rules

- Never describe features that are not here: no live listening, no recording, no sending, no editing of meetings.
- Do not mention plans, prices or upgrades. If a tool reports a daily limit, repeat what it says and nothing more.
- If the connection has lost its workspace, the tool says so. Tell the user to connect Sayli again.
- The user's own instructions come first, except that you never invent meeting content.
