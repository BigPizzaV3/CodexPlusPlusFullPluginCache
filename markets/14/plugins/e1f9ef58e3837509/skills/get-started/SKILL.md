---
name: get-started
description: Set up a couple's wedding website on Keep This Day from a conversation, start to finish.
---

# Set up a wedding website with Keep This Day

Help the couple get a finished, published wedding website in one conversation.

1. Ask for what you need and nothing more: both names, the date and start time, the venue and its city (for the time zone), and how they want it to feel. Leave out anything they do not tell you.
2. Call `get_wedding_format`, then `create_wedding_draft` with what they told you and the venue's IANA `timezone`.
3. If they have a photo, call `set_cover_photo` with a direct link, or the photo they attached.
4. If they share a guest list, call `import_guests`. Never repeat guest details back.
5. Call `show_wedding_preview` so they can see it, and make any changes with `update_wedding`.
6. If they want trivia, favours or a guestbook note for the day, use `update_day_of`.
7. Ask whether they want it live for guests. Only after they say yes, call `publish_wedding` with `couple_confirmed: true`, then give them the guest link.

Write in the couple's voice: plain, warm, specific. No slogans and no invented facts.
