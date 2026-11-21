---
name: contact-lookup
description: Find a Vixiees contact and explain what has happened with them — stage, calls, WhatsApp and email messages, tasks, comments. Can leave an internal comment or set a reminder. Use when the user names a person, phone number or email and asks about them.
---

# Contact lookup

## Steps

1. Find the contact with `search_contacts_tool` using the name, phone or email the user gave. If several match, list them (name, phone, current stage) and ask which one.
2. Call `get_contact_tool` for the contact's current playbook, stage and fields.
3. Call `get_contact_feed_tool` (default limit 20) for the recent timeline. If the user asks about something specific ("did they reply on WhatsApp?", "what did they say about price?"), use `search_contact_feed_tool` instead.

## Output

- One line: who they are, which playbook and stage they're in, and since when.
- A short timeline of the most recent meaningful events, newest first. Skip system noise.
- What's next: open tasks or reminders on this contact, if any.
- Answer in the language the user wrote in.

## Writing

- To leave a note for the team, use `create_contact_comment_tool`. Show the user the exact text and confirm before posting.
- To follow up later, use `create_reminder_tool`. Confirm the date and time with the user first.
- Don't move contacts between stages or change their fields from this skill.
