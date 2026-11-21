---
name: project-brief
description: "Save a concise project brief in Mnemoverse so the user can resume in another connected AI tool. Use when asked to remember project context, prepare a memory handoff or save a brief; ordinary summaries do not require saving."
---

# Continue a project in another AI tool

The user's request defines what to save. A project handoff carries selected useful context, not their entire conversation, files or automatically discovered private information.

## Prepare the brief

- Start with the project facts already supplied in this conversation or the documents the user selected. If a new account has no context, ask for the project name and what the next assistant needs to know in one short question. Do not create a fictional sample project or a placeholder memory.
- Include the goal, confirmed decisions and constraints, relevant current status and next step when supplied. Distinguish decisions from suggestions and date status that can change. Keep only details needed to continue the project. Do not invent missing sections to fill a template.
- If the user supplies an exact personal project domain, use it as given without `memory_stats`; that label does not need to exist before the write. Use `memory_stats` only when choosing or disambiguating an existing project domain. Use `memory_read` for relevant earlier project context when needed; do not enumerate all personal memories. A domain is a label on records, not a separately created empty project. For a clearly named new project, choose a simple domain such as `project:<project-name>` on the first real write.
- If existing notes contradict the current account, keep the disagreement visible and resolve any ambiguity that would change the brief. A new write does not edit or remove an earlier note.

## Save and hand off

1. Save the brief with `memory_write` in the chosen personal project domain, using self-contained statements and a few relevant `concepts`. Independent decisions can be separate notes. Include sources for material facts when known. A request to use another AI under the same account does not authorize putting the brief in a shared room.
2. Report only notes whose result says `stored: true`. For `stored: false`, report the returned reason if present and distinguish already known content from new facts that were not saved. Do not retry the same fact with cosmetic rewording. If the result is unreadable, state that the save is unconfirmed.
3. Give a short handoff prompt containing the project name and exact domain, for example: “Read my Mnemoverse notes in project:<actual-name> and help me continue from the saved next step.” Use the actual saved scope, never the example placeholder.
4. Explain that the other AI tool must support Mnemoverse and be connected separately to the same Mnemoverse account. It can retrieve the saved brief; this does not transfer the whole chat, modify that tool's built-in memory or prove the other tool has already read it.

Do not include passwords, API keys, payment data, MFA codes, government IDs or health records. If Mnemoverse tools are unavailable, show the concise unsaved brief and explain the connection step without claiming it is in memory. In ChatGPT, point to https://mnemoverse.com/docs/api/chatgpt; use https://mnemoverse.com/docs/api/install-by-host for another host. Never request credentials in the conversation.
