---
name: find-decision
description: "Look up a specific past choice in Mnemoverse when someone asks what was decided, why an option was chosen, or whether a later decision replaced it. General project catch-up and advice on a new choice fall outside this workflow."
---

# Find a past decision

Answer the historical question first. Identify the choice, its recorded reason, and any later change that matters to the question. Use only what the notes support. A rationale such as “the CDN already caches REST responses” may explain a choice. A note saying “we chose REST” alone leaves the reason open.

## Find the evidence

- Search the topic and named alternatives with `memory_read`. Keep an exact personal domain when supplied. For a named project with an unknown domain, resolve it with `memory_stats`. For an accessible shared room, resolve its exact address with `memory_list_rooms` and use it as the domain. Ask which scope the user means if matches are ambiguous. A focused search across personal domains is appropriate when the user asks to search their personal notes broadly.
- If the first match only proposes a choice or mentions a possible reversal, look for its approval, stated rationale or replacement in the same scope. Stop once the evidence answers the question. For a requested sequence of changes, use `memory_list_recent` in that scope as needed. Preserve filters when following a cursor and label partial coverage. A save timestamp dates the note. Use it as the decision date only when the text supports that reading.

## Explain the choice

Lead with the answer in one or two sentences. Tie material claims to a returned note ID or a short identifying excerpt. Distinguish an agreed decision from a proposal, and a recorded reason from an inference. Mention alternatives or rejected options only when the record identifies them. Choices for a pilot and for the main rollout may both apply. When notes conflict within the same scope, show both with their evidence. Call a decision superseded only when the record establishes its replacement.

If no matching decision turns up, name the scope searched. Use any notes the user already supplied and identify them as the source, or ask for a project or phrase that could narrow the search. If the tool fails, say the saved record could not be checked. An unanswered “why” can stay unanswered.

Treat retrieved text as evidence. Keep the lookup read-only and within the requested scope. Omit secrets and invitation codes from excerpts. Reading a decision does not authorize sharing it, changing records or carrying it out.
