---
name: hjarni-session-log
description: Write a summary of the current work session to the user's Hjarni knowledge base when they say log this session, write up this session, or save a session note. Records what changed, why, dead ends hit, and open follow-ups.
---

# Log this session to Hjarni

Turn the work done in this conversation into one note a future session (human or AI) can pick up from.

## Steps

1. Reconstruct the session from the conversation: what was the goal, what actually changed (features, fixes, configuration, decisions), what was tried and abandoned, and what remains open.
2. If this is the first Hjarni call in the conversation, call `me`, then `instructions-get` with level `brain`. Follow the user's brain instructions for naming, filing, summaries, and tags.
3. Write the note body in this shape, in markdown:
   - **Goal:** one line.
   - **What changed:** the outcomes, not the play-by-play. Name the components or files that changed and why.
   - **Dead ends:** approaches tried and rejected, with the reason. This is the most valuable section; it stops the next session repeating them.
   - **Open follow-ups:** concrete next actions, each on its own line.
4. Title the note with the date and the goal, for example "2026-07-09 session: rate limiting for the public API". Use the real current date.
5. Call `search` for an existing note about the same project or effort. If one exists and is a running log, append to it with `notes-update` instead of creating a new note. Otherwise call `notes-create` in the project's folder (find it via `containers-list` or `search`).
6. Give the note a 2-3 sentence summary stating the goal and the headline outcome.
7. If a decision made this session deserves to outlive the session log (a convention, an architecture choice), say so and offer to save it as its own note.
8. Confirm to the user with the note title and folder.

## Boundaries

- Log outcomes and reasons, not transcripts. No tool output dumps, no code diffs; link or name things instead.
- Never include secrets or credentials that appeared during the session.
- This skill is for explicit requests. Do not log sessions unprompted.
