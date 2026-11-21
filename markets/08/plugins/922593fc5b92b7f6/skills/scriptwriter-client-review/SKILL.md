---
name: scriptwriter-client-review
description: 'Help a freelance YouTube scriptwriter, ghostwriter, editor or small scriptwriting agency quality-check a script before delivering it to a client channel, using Prepublish''s audit, hook and pre-flight tools, then produce a client-ready review note that explains what was checked, what was changed and what remains. Use when the user says they write scripts for a client or channel owner, asks "check this script before I send it to my client", "give me feedback my client will understand", "prepare a script review for a YouTube channel", "QA a ghostwritten script", or needs a second reader for a deliverable. Also use for channel owners reviewing a script a writer delivered to them.'
---

# Client-ready script review

For writers who deliver scripts to someone else's channel, and for channel owners reviewing a writer's draft. The goal is a defensible, neutral second read: specific passages, specific fixes, and an honest statement of what the check covers.

Read `references/tools.md`, `references/report-fields.md` and `references/claims-and-limits.md`. Use `assets/client-review-note.md` for the deliverable.

## Inputs

- The script, verbatim, and the working title the client approved.
- The client's brief if the user has it: target runtime, audience, tone, must-include points. Use only what the user shares.
- Who reads the note: the writer only (internal QA), or the client (external note). Default to internal until the user says otherwise.
- Email for the free audit if the user has no Prepublish account (explain first, never invent).

## Workflow

1. Run `audit_script` with title, script and, when known, `video_duration_seconds`, `category` and `audience` from the brief.
2. If the brief has a target runtime, run `script_runtime` on the script and compare.
3. If the topic is sensitive, run `policy_preflight`. If the channel is faceless or formula-driven, run `check_authenticity`.
4. For internal QA: present the flagged passages with rewrites, prioritised, and offer the `youtube-script-revision-loop` so the writer fixes the draft before delivery.
5. For a client note: fill `assets/client-review-note.md`. Keep it factual, short and neutral. It should help the client trust the draft, not sell a tool.

## Rules for client-facing text

- Describe the check accurately: "a text-level review of the script's hook, structure and pacing, plus a check against YouTube's published policy categories". Never claim it predicts retention or views, and never promise results.
- Do not include internal notes, the writer's private comments, or scores the user asked to leave out.
- Credit rewrites honestly: rewrites from the writer, from Prepublish, or suggested by you are all fine to use, but do not misattribute them.
- If the client's brief conflicts with a flagged issue (for example a required long sponsor read at the start), note the trade-off neutrally and let the client decide.
- Never share the client's script with anyone or anything beyond the checks the user asked for.

## Batch reviews

When a writer has several scripts for the same client, review them one at a time in the order the user gives, and keep a one-line summary per script. Mention the daily free audit limit (3 for users without an account) before starting a batch larger than that.
