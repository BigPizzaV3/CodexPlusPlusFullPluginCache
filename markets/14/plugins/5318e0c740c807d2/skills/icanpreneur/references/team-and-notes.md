# Notes, exports, invitations and seats

## Notes

Notes hold decisions, research plans, client briefs and meeting notes in Markdown.

- `list_notes` (with `filter`) before creating, so you do not duplicate a note. `get_note` returns the full text.
- `create_note(ideaId, title, text)` saves a new note. Ask for or propose a short title.
- `update_note` replaces the **whole** text if you send `text`. Call `get_note` first, edit, and send the complete result.
- `duplicate_note` copies a note to explore an alternative. `delete_note` and `restore_note` follow the deletion rules.
- Saving a note is free. Offer it once at the end of a piece of work when the conclusions would help the team. Save only if the user agrees or already asked.

A decision note works well in this shape:

```markdown
# <Decision in one line>

**Date / context:** <what was discussed and why>
**Decision:** <what was agreed>
**Evidence behind it:** <research and persona used, with the persona version if known; the source research held N completed interviews at the time, X real or imported and Y synthetic; analysis as of <updatedOn>>
**Not yet supported:** <assumptions with no real-customer evidence>
**Open questions:**
**Next steps:** <owner, what to test or build>
```

Do not put anything in a note that the conversation did not establish. Mark an unknown as unknown.

## Exports

`export_canvas`, `export_research` and `export_buyer_persona` return the platform's standard Markdown (`text`). They are free, read-only and are not rewritten, summarized or translated.

- Use them for client handovers, sharing, or passing context to another tool. Hand the text over unchanged. Summarize only if asked.
- For a handover, export the Canvas, the relevant research and the persona, and say which workspace and which items each came from.
- Documents (positioning, landing page, sales deck) and notes are read with `get_buyer_persona_document` and `get_note`; they have no export tool.

## Inviting people to a workspace

`invite_idea_member(ideaId, emailAddress, role, expirationInDays)` sends a real email.

- If the user gave an unambiguous address and role and asked you to invite them, send it; do not ask for the same authorization again. Ask only for what is missing (address, role `Viewer` or `Editor`, expiry in days). If the user tells you to decide, choose a value, say what you chose, and mention that an active invitation keeps its original expiry when resent. An expired invitation is replaced with a new three-day invitation. `expirationInDays` is an integer of at least 1 with no declared maximum; use a sensible duration the user authorizes. To change it, an Administrator revokes the invitation and invites again.
- Check `list_idea_members` and `list_idea_invites` first. A duplicate invitation returns an error and is not resent. Use `resend_idea_invite` (Administrator) to resend.
- Keep invitation IDs from invite/resend responses: `list_idea_invites` excludes expired invitations. Resending an expired invitation returns a replacement with a new ID.
- The person joins only after accepting. An invitation does not give them a license seat.

## License seats and credits

- `get_license_team` shows the owner, seat capacity, active and inactive users.
- `invite_license_members(emailAddresses)` uses seats that already exist. If there are none left it returns an error. It never removes, replaces or reactivates anyone, and it never buys seats. Do not suggest that it does.
- Everyone on a license shares one credit pool. Any seat holder can top it up.
- There are no tools to remove or reactivate a license member. Direct the user to the Icanpreneur app for that.
