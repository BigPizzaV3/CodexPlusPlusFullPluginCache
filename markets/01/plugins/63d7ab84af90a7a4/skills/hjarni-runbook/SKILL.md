---
name: hjarni-runbook
description: Save a completed debugging, incident, or setup session as a reusable runbook note in the user's Hjarni knowledge base when they say make this a runbook, save this as a runbook, or document this fix so we can repeat it.
---

# Save a runbook to Hjarni

Convert what just happened in this session into a runbook the user, a teammate, or a future AI session can follow without rediscovering anything.

## Steps

1. Reconstruct the procedure from the session: the symptom or trigger, how it was diagnosed, the fix or procedure itself, and how success was verified.
2. If this is the first Hjarni call in the conversation, call `me`, then `instructions-get` with level `brain`. Follow the user's brain instructions for naming, filing, summaries, and tags.
3. If the user works in a team space and the problem is shared infrastructure, ask whether the runbook belongs in the team folder rather than their personal one before creating or updating a note.
4. Write the runbook so a reader with no memory of this session can execute it:
   - **When to use this:** the symptom or situation, phrased the way someone would search for it (error messages verbatim, observable behavior).
   - **Diagnosis:** the checks that narrow it down, in order, each with the command or place to look and what result to expect.
   - **Fix:** numbered steps with exact commands, files, or settings. One action per step.
   - **Verify:** how to confirm it worked.
   - **Notes:** gotchas hit this session, and what did NOT work, so the next reader skips it.
5. Generalize before saving: replace values specific to this one occurrence with placeholders in angle brackets, but keep real commands and paths that will be the same next time.
6. Title it by the symptom or task ("Restore staging database from a production snapshot"), not by the date.
7. Call `search` for an existing runbook on the same procedure; update it via `notes-get` then `notes-update` if one exists. Otherwise call `notes-create` in a Runbooks folder: use an existing one if `containers-list` shows one (personal or team), or create it and tell the user.
8. Give the note a 2-3 sentence summary: the symptom it covers and the essence of the fix.

## Boundaries

- Exact commands are the point of a runbook, but never include secrets or credentials; reference where they live (vault item, environment variable name).
- If the session ended without a confirmed fix, say so and save it as an investigation note, clearly labeled as unresolved, rather than a runbook that ends in a dead end.
