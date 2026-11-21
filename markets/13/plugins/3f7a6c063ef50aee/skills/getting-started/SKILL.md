---
name: getting-started
description: How to use HolyCRM, a church management app, to answer questions about a church's people, visitors, small groups and events, and to add or update visitors with the user's confirmation.
---

# Using HolyCRM

HolyCRM is a church management app. These tools act as the signed-in person, with their own
permissions in their church: they only see what that person's role can see in the app, and
records of children are never returned.

## Which church

- Call `list_churches` when you don't know the church yet. A person can belong to several.
- A church may show `ai_allowed: false` with a note: its administrator has not turned on AI
  assistants (or has blocked this person). Tell the user the note; do not retry.
- When the person belongs to more than one allowed church, pass `church_id` to every tool, or
  ask which church they mean.

## Answering questions

- Visitors (first-time guests): `search_visitors`. "Not contacted yet" is `contacted: false`.
  Dates are `YYYY-MM-DD`; compute ranges such as "last month" from today's date.
- People (adult members): `search_people`.
- Who is missing from small groups: `group_absences`. Groups that met without taking attendance
  are listed separately; say so instead of guessing.
- Events: `list_events`. Times are UTC; convert them to the user's time zone when you show them.

## Making changes

Changes always take two steps:

1. Call the prepare tool (`create_visitor`, `log_visitor_followup` or `set_visitor_stage`).
   It changes nothing and returns a `summary`, the exact `changes` and a `confirmation_token`.
   For a new visitor it also lists possible duplicates: mention them.
2. Show the user the summary and changes, and ask them to confirm. Only after they clearly say
   yes, call `confirm_change` with the token. Never confirm on your own initiative.

Tokens expire after 10 minutes and work once; if one fails, prepare the change again.
Turning a visitor into a member, and deleting anything, are done in the HolyCRM app, not here.
