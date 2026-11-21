---
name: workshop-eu
description: Ask sourced questions about Workshop communications, inspect engagement and audiences, and create Workshop email drafts through Workshop's EU service.
---

# Workshop EU

Use `ask_workshop` when the user asks about content, campaigns, engagement, audiences, or other data in their Workshop account.

If `ask_workshop` returns a working result, call `get_workshop_answer` with the returned task ID until the answer is complete. Preserve useful source links in the final response. Do not present progress text as the answer.

Use `draft_workshop_email` only when the user explicitly asks to create a new email draft. Pass a complete, self-contained brief with the intended audience, purpose, facts, tone, and call to action. Return the Workshop editor link and make clear that the tool creates a draft; it does not send or publish the email.

Do not claim support for editing existing emails, sending or publishing emails, or deleting Workshop data.
