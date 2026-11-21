---
name: editor-overview
description: "How Donkey Cut works inside ChatGPT: cloud projects, the editor card, shared undo history, and which tools read or edit. Use at the start of any Donkey Cut editing session."
---

# Donkey Cut in ChatGPT
ChatGPT plans the edit and interprets the footage with the user. Donkey Cut imports media, measures it, applies editing commands, and renders the result.
Work on the connected account's cloud projects. Use list_projects or create_project, then open_project once. Keep that card throughout inspection, imports, edits, previews, undo and redo: reopening starts a fresh editor with empty history. The existing card shows edits immediately; render_preview and get_preview_status verify the saved preview. Recover a missing card with open_project and resume when ready. Local projects become accessible after the user saves them to cloud in Donkey Cut.
Read inspect_project for current assets, selection, tracks, captions, notes and settings. An editor_state mentioned in these guides is that returned state. Times are seconds and ids come from tool results.
Every editing operation is its own tool taking projectId. Each write is one undo step; the user's manual edits share that history. Read each result before continuing.
The card offers the timeline, preview and inspector. ChatGPT provides the conversation and calls the media and caption commands. When a required asset is missing, ask the user for a file or link, or discuss suitable stock. Ask about creative choices when the answer materially changes the requested result.
