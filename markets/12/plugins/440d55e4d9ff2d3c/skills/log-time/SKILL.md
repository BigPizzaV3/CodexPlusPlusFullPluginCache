---
name: log-time
description: Log time in TimeTackle from a plain description - turn "I spent 2 hours on the Acme proposal this morning" into one or more manual time entries with the right tags, confirmed before saving, and fix or remove entries just created. Use when the user wants to log, record, add, correct or delete their time.
---

# Log time

Create manual time entries for the connected user from what they describe. Entries always belong to the connected
user. Explicit instructions from the user take priority over these steps.

## Input

- What they worked on, when (date and start time), and for how long (or an end time).
- Optionally tags or property values (for example Project: Acme, or Development).

## Steps

1. Work out each entry: title, `startDateTime` in `YYYY-MM-DD HH:mm:ss`, and either `durationMinutes` or
   `endDateTime`.
   - Resolve relative dates ("this morning", "yesterday at 3") against today in the user's timezone (theirs if stated,
     otherwise their own calendar's `timezone` from `get_imported_calendars`).
   - If the start time or the duration is missing, ask. Do not guess times.
2. Resolve tags: call `get_properties` with `search` for each tag or property the user mentioned.
   - Use `"key"` for a tag on its own, or `"key:value"` for a property value (for example `"Project:Acme"`).
   - If a name matches nothing, or several things, ask the user; do not invent tags.
3. Confirm before saving: list every entry (title, date, start–end, duration, tags) and ask the user to confirm.
   For a single, fully specified entry, a short confirmation is enough.
4. After confirmation, call `create_manual_entry` once per entry with `title`, `startDateTime`, `durationMinutes` or
   `endDateTime`, and `tagNames`.
5. Report each created entry with its time and tags, and keep its `eventId` for corrections.

## Corrections

- To change an entry, call `update_manual_entry` with its `eventId` and only the fields that change. `tagNames`
  replaces all of the entry's tags, so pass the full list. Start and end times must be given together.
- To remove an entry, confirm with the user first, then call `delete_manual_entry` with its `eventId`.
- Only manual entries can be changed or deleted, not calendar meetings from Google or Outlook.

## Do not

- Do not create entries for someone else; to log time for another person, they connect their own TimeTackle account.
- Do not create, change or delete anything without the user's confirmation.
- Do not split, round or merge the user's times unless they ask.
