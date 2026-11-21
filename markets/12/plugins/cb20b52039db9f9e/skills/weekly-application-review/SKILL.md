---
name: weekly-application-review
description: Summarise the user's Tradermaths application board for the week, grouped by stage, with suggested next actions. Use when the user asks for a review, status update or overview of their graduate applications.
---

1. Call `board_summary` to get counts of tracked roles by status (saved, applied, online test, interview, offer).
2. Call `list_board` to fetch the roles. Page with `cursor` if more results exist. Use `role_status: "Open"` when the user only wants roles still accepting applications.
3. For any role the user asks about in detail, call `get_board_role` with its `role_ref`.
4. Reply with:
   - A one-line headline (e.g. "12 tracked: 5 saved, 4 applied, 2 online tests, 1 interview").
   - A short list per stage, most advanced stage first.
   - Suggested next steps: saved roles that are still open and worth applying to, and online test or interview stages that need prep.
5. The board is read-only. If the user asks to move or edit a role, tell them to do it on tradermaths.com.
