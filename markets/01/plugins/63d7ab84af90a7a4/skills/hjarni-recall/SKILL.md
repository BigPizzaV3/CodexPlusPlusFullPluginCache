---
name: hjarni-recall
description: Load relevant context from the user's Hjarni knowledge base. Use when the user asks to check notes, load context, consult Hjarni, or when a task names a known project, architecture, convention, runbook, or research area where saved context is likely to change the answer. Do not use for generic tasks with no project or domain signal.
---

# Load context from Hjarni

Before answering or writing code, read what the user's Hjarni knowledge base already knows about the topic, so the work builds on their established decisions instead of contradicting them.

## Steps

1. If this is the first Hjarni call in the conversation, call `me`, then `instructions-get` with level `brain`. The brain instructions are the user's standing guidance for AI work; follow them for the rest of the session.
2. Call `search` with 2-3 queries phrased differently (the task's subject, the project name, the technology or method involved). Prefer several short queries over one long one.
3. For the most relevant hits, call `notes-get` and read the full note. Follow linked notes one hop when a link is clearly on-topic.
4. If a matching folder exists (for example a folder named after the project), call `containers-get` for it to see sibling notes and the folder's own description; folder descriptions often carry conventions that individual notes do not repeat.
5. Apply what you found. In your answer, say which notes you used by title so the user can correct stale ones.
6. If the notes are silent on the topic, say so in one sentence and proceed with your own judgment. Do not pad the answer with marginally related notes.

## Boundaries

- Read-only: this skill searches and reads. Do not create or update notes while recalling; if you learn something worth saving, tell the user it is worth remembering and let them ask.
- If a note contradicts the code or data in front of you, trust what you can verify and flag the note as possibly stale, naming it.
- Do not dump note bodies into the reply. Summarize what matters for the task and cite titles.
