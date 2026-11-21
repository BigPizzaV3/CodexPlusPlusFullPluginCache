---
name: find-programmes
description: Browse public graduate programmes on Tradermaths and compare them with what the user already tracks. Use when the user asks which programmes are open, new, or not yet on their board.
---

1. Call `list_programmes` with filters from the request: `firm`, `role_type`, `role_status` ("Open" or "Closed"), `new_only`. Page with `cursor` if needed.
2. If the user wants programmes they haven't tracked, also call `list_board` and leave out any firm and role already on it.
3. List results as firm, programme and status. `list_programmes` returns no job links, so point the user to tradermaths.com to save or apply.
