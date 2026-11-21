---
name: whos-who
description: "Who's who. Use when the user wants a stakeholder brief for a client or meeting: who the people are, their roles, what they care about, and the latest contact with them."
---

# Who's who

## 1. Find the people

- `delegent_find_contacts` by client name or person.
- `delegent_get_status` for the Overview's stakeholders and open questions.
- Meeting attendees from the calendar (`delegent_get_calendar` or a calendar tool) when the brief is for a meeting.

## 2. Build each profile from Delegent sources

For each person:
- **Role and organisation**
- **Last contact**: latest email or meeting, with date (`delegent_find_emails`, meeting sources)
- **What they care about**: positions, concerns and asks, quoted from sources
- **Open items with them**: tasks and unanswered emails (`delegent_find_follow_ups`)

Keep to what the sources say. Mark unknowns as unknown. Never guess personal details.

## 3. Close

- A one-line read of the room: who decides, who influences, who blocks.
- Offer to save new or corrected people with `delegent_save_contact`.
