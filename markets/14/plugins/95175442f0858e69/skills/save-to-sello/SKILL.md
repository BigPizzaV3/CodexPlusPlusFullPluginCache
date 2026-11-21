---
name: save-to-sello
description: "Prepare drafts for Sello only when a user requests to save or send supplied content, a summary, or conversation notes to their Sello journal."
---

# Save to Sello workflow

- Invoke `prepare_sello_entry` when the user explicitly asks to save, send, or prepare notes, a summary, or conversation content for their journal or Sello. Do not invoke for general journal advice or unsupported entry operations.
- Draft a concise, faithful title of at most 200 characters, or honor the user's shorter supplied title. Provide a Markdown `text` string of at most 50,000 characters. Do not invent personal events, facts, sentiments, dates or details. Ask only if vital source content is missing.
- The MCP tool is read-only. It prepares text and returns a card containing `Guardar en Sello` / `Save to Sello`; it does not save a journal entry.
- Never claim anything has been saved. In Spanish, tell the user: "Toca Guardar en Sello para revisarlo y guardarlo." In English: "Tap Save to Sello to review and save it."
- The external Sello page handles user review and saving. Do not automatically follow the button or imply a ChatGPT login, account connection, or access to the journal.
- Do not invoke the MCP tool to read, search, edit, delete, or publish entries. Explain those operations are unavailable via this plugin.
- The tool arguments contain plaintext from chat. Never claim the information is end-to-end encrypted inside ChatGPT or while passed to the MCP server. Sello encrypts journal entries on the user's device when they save them there.
