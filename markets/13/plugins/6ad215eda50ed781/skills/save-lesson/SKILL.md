---
name: save-lesson
description: "Save a practical lesson from a specific experience in Mnemoverse when the user asks to remember what worked, what failed or what to do differently next time. Use for a reusable takeaway, not a generic summary or automatic changes to agent rules."
---

# Save a lesson

Turn an actual experience into a short note the user can find when a similar situation arises. Preserve what makes the lesson useful: the situation, observed result, practical takeaway and limits of applicability.

## Identify the lesson

- Start with the experience the user described or the work visible in the selected conversation. If the request contains no experience, ask what happened and what they want to remember in one question. Do not invent a success, failure or sample lesson for an empty account.
- Separate observations from explanations. “This change fixed the failing test in this environment” is supported by that result; a universal causal rule may not be. Preserve uncertainty, relevant version or date, and conditions under which the takeaway applies when known. Do not manufacture measurements or attribution.
- For several observations, select the durable ones the user wants saved. A reflection request alone does not authorize writing private logs, a full transcript, changing agent instructions, editing repositories, filing issues or sending messages. Use this skill only when saving the lesson is part of the request.
- Reuse an exact personal project domain the user provides. Otherwise use `memory_stats` to identify the relevant existing domain, resolving ambiguous choices; for a clearly named new project, a label such as `project:<actual-project-name>` can begin with the first real write. For a general lesson with no project, use a personal label such as `lessons`. Use a focused `memory_read` in the chosen scope to avoid repeating a known lesson when relevant. Do not copy the lesson into a shared room unless the user separately chooses that sharing scope.

## Preserve the useful outcome

Save with `memory_write`: enough context to recognize the situation, what was observed, the takeaway and its boundary, plus a few relevant `concepts`. Include a supplied source or issue reference when it explains the evidence. Save a distilled lesson rather than raw logs; omit secrets, invitation codes, join URLs, passwords, API keys, payment data, MFA codes, government IDs and health records.

Report a saved lesson only when the result says `stored: true`. For `stored: false`, use the returned reason if present and do not change wording merely to bypass refusal. When a result is missing, unreadable or times out, state that the save is unconfirmed and do not automatically repeat the write. A revised lesson is a new note alongside earlier notes, not proof that the earlier advice was removed.

Finish with the lesson and when to use it in one or two sentences. Do not promise that another assistant has learned it permanently or will apply it without retrieval. If the user also wants rules or code changed, keep that as the separate requested task; this skill does not authorize it.

If tools or authentication are unavailable before any write is attempted, provide the proposed lesson as unsaved and the connection step at https://mnemoverse.com/docs/api/chatgpt. Never request credentials in chat.
