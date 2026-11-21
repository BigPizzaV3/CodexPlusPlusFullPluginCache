---
name: weekly-customer-review
description: Review the past week for a Make Agent Fast agent — conversations by channel, new leads, and questions the agent could not answer — and propose fixes.
---

Use this when the user asks how the week went, what customers asked, or for a weekly review.

1. Call `list_agents` and pick the agent the user means. If there are several and it is unclear, ask.
2. Call `get_report` with `days: "7"`. Summarize conversations by channel, leads, bookings, handoffs, and the change from the previous week.
3. Call `list_unanswered_questions` with `days: "7"`. List each question with how often it was asked.
4. Call `list_leads` and show the new leads from the past week: name, what they asked, and whether they are qualified.
5. Call `list_conversations` with `only_unanswered: true` and open the most recent one with `get_conversation` so the user sees a real example of what went wrong.
6. Propose short answers for the unanswered questions. Explain that `save_answer` supersedes the previous answer and can reply to customers waiting for it on connected channels. Save only after the user approves the wording and those effects; do not retry a successful save.

Keep the review to one screen: totals first, then the list of gaps, then the leads. Never contact a customer or change a lead without the user asking.
