---
name: morning-priorities
description: Build a LinkedIn morning brief from Yadulink. Use when the user asks who to contact today, what is urgent, or what to do first on LinkedIn.
---

# Morning priorities

Help the user start the day with a short, ordered LinkedIn brief. Do not dump raw tool JSON.

## When to use

The user asks for today's priorities, a morning brief, who to contact, or what is stuck in outreach.

## Workflow

1. Call `get_yadulink_capabilities` only if the user is unsure what Yadulink can do.
2. Call `get_today_contact_priorities`.
3. Call `summarize_my_linkedin_inbox` for conversations that need a reply.
4. Optionally call `explain_my_linkedin_progress` or `get_hot_crm_leads` if the brief is thin.
5. Answer in the user's language.

## Output

Return:

- 3 to 7 ordered actions
- why each action matters
- whether it is a reply, a first message, a list cleanup, or a sequence check
- anything the user must confirm before a write

Do not launch searches, import leads, or start sequences from this skill.
