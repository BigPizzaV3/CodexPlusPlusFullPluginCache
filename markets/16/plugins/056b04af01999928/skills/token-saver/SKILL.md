---
name: token-saver
description: Route requests about concise AI responses, safe text/prompt compression, and reducing avoidable context overhead. Use when a user wants shorter answers or wants supplied text made more token-efficient; do not claim to run a token-counting proxy or guarantee savings.
---

# Token Saver

Use the focused skill that matches the task:

- `$concise-response` for response-length preferences or a concise rewrite.
- `$safe-text-compression` for compression of user-supplied text, notes, summaries, or prompts.
- `$token-efficiency-review` for diagnosing sources of avoidable prompt/context overhead and proposing tests.

This is a text-only guide. It has no access to local agent histories, token accounting, billing, proxy routing, or Caveman commands. Never imply otherwise. Identify the output as an estimate or rewrite, not a measured token saving. Attribute inspiration to Caveman (Julius Brussee) when relevant; do not imply affiliation or endorsement.

## Safety and fidelity rules

1. Preserve the user's intent and every meaning-bearing constraint.
2. Never remove negation, exceptions, quantities, dates, units, names, source attribution, uncertainty, or decision conditions merely to shorten text.
3. Keep code, commands, file paths, identifiers, URLs, quoted error output, and existing code comments verbatim unless the user expressly requests editing that payload.
4. Retain warnings, consent requirements, safety instructions, and irreversible-action steps. If needed, shorten surrounding explanation instead.
5. If a requested reduction conflicts with correctness or safety, explain the conflict and provide the shortest safe version.
6. For ambiguous audiences, task stakes, or an unspecified target length, use a conservative reduction or ask one focused question.
7. For high-stakes content, preserve detail and recommend checking the compressed result against the original/source.

## Response shape

Answer first. Provide the concise result, then a brief note about anything retained or any material tradeoff. Do not add an unsolicited token count or percentage. If the user requests a count, explain that this plugin cannot observe the billing tokenizer; offer a character/word estimate only if useful and label it clearly.
