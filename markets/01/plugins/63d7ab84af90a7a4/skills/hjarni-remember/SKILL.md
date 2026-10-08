---
name: hjarni-remember
description: Save decisions, findings, preferences, and conventions to the user's Hjarni knowledge base when they say remember this, save this, note this down, or add this to my notes. Updates an existing note when one covers the topic instead of creating a duplicate.
---

# Save knowledge to Hjarni

Capture what the user asked to remember as a durable, well-filed note in their Hjarni knowledge base, using the Hjarni MCP tools.

## Steps

1. If this is the first Hjarni call in the conversation, call `me`, then `instructions-get` with level `brain`. Follow the user's brain instructions for naming, filing, summaries, and tags. If the user is near their note limit, prefer updating an existing note over creating a new one and tell them why.
2. Distill the thing to remember into one clear fact, decision, or procedure. Strip conversation-specific detail (file paths from a one-off session, timestamps like "today") unless it is the point of the note. Convert relative dates to absolute dates.
3. Call `search` with 1-2 queries for the topic. If an existing note covers it:
   - Call `notes-get` to read the current version.
   - Call `notes-update` with a targeted edit that adds or corrects the fact. Do not rewrite unrelated sections.
4. If no note covers it, call `notes-create` with:
   - A short, searchable title stating the fact, not the category ("Deploys go through Kamal, never direct SSH", not "Deployment notes").
   - A markdown body with the fact first, then why it matters, then any how-to detail.
   - A summary of 2-3 sentences. Always include a summary; it is what future searches surface.
   - The most fitting folder. Call `containers-list` if you have not seen the folder tree this conversation. Only create a new folder when nothing fits and say so.
   - Existing tags where they fit (`tags-list`); create a tag only for a genuinely new cross-cutting theme.
5. Confirm to the user in one sentence: what was saved or updated, and in which folder.

## Boundaries

- Never save secrets, credentials, API keys, or tokens, even when asked. Offer to save where the secret lives instead (for example, the vault item name).
- Do not save things the project's repository already records (code structure, git history, README content). Save the non-obvious context around them instead.
- If the user's request is ambiguous between updating their brain-level instructions and saving a note, save a note. Only call `instructions-update` when the user explicitly asks to change how their AI behaves, and read the existing instructions first.
