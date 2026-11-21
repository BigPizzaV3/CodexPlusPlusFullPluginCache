---
name: capture
description: Save something to Notii as a clear, well-structured note, such as the outcome of this conversation, meeting notes, a decision, a plan, research findings, a code snippet or a list of to-dos. Use when the user says "save this", "capture this", "note this down", "remember this", "add to Notii" or similar.
---

# Capture to Notii

1. **What to save.** If the user said what (words after the command, or "this"), save that. Otherwise save the substance of the conversation so far: conclusions, decisions, facts and next steps, without the back-and-forth and the dead ends.
2. **Where.** If the user named a notebook or project, find its id with `list_notebooks`. Otherwise leave `notebook_id` out and the note goes to their default notebook. If a note on the same topic exists (a quick `search`), offer to add to it with `update_note` and `append_markdown` instead of making a second one.
3. **Shape it** in Markdown:
   - A specific, searchable title (for example "Pricing decision for the Pro plan, Oct 27"), never "Notes" or "Summary".
   - A short summary paragraph first.
   - `##` sections as the content needs them, such as Decisions, Details, Open questions, Next steps.
   - Action items as `- [ ]` checklist items, with the owner and the date in the text when known.
   - Code in fenced blocks with a language, and links as `[text](url)`.
4. **Save** with `create_note`: the title, the Markdown and, when it's obvious, one to three tags (reuse existing tags; `list_tags` shows them).
5. **Dated to-dos.** If there are to-dos with dates the user will want on their daily note, offer to add them with `add_task` and `due`, in the user's time zone.
6. **Confirm** in one line with the link: Saved "Title" to Notii ([open](url)).
