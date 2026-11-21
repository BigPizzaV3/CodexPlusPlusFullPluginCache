---
name: send-email
description: Draft, test, and send a SendFox email campaign safely. Use whenever the user wants to write, schedule, send, or resend an email to their SendFox list or tags.
---

# Sending a SendFox email

Sending reaches real people and cannot be undone. Follow these steps in order, and never skip the confirmation in step 4.

1. **Pick the audience.** Use `list-lists` and `list-contact-tags` to turn the names the user gives into IDs. If the user hasn't said who it goes to, ask. Don't guess "everyone".
2. **Write a draft.** Call `create-campaign`. It only makes drafts. The HTML must include `{{unsubscribe_url}}`. Use `get-account` for the sender name and email unless the user gives others.
3. **Send a test.** Offer `send-test-email` to the user's own address so they can check it in their inbox. This never reaches the audience.
4. **Confirm before it goes out.** Show the subject, the audience, and roughly how many people it will reach (`list-contacts` with `count_only: true` and a `filter` of `in_list_ids` / `tag_ids`, minus any excluded tags). Ask: "Send this to about N people now?" Go on only after an explicit yes in the current conversation.
5. **Send or schedule.** Call `send-campaign` to send now. For a later time, call `update-campaign` with `scheduled_at` (ISO-8601). Both need the step 4 confirmation.
6. **Report back.** Say whether it was sent or scheduled, and when. If SendFox returns an error (plan limits, an unverified account, a large send already queued), pass the message on plainly. Don't retry or work around it.

## Resending to non-openers

`resend-campaign` copies a sent email into a new draft aimed at its non-openers, openers, or clickers. Leave out `scheduled_at` so the copy stays a draft. Then report `estimated_recipient_count` and confirm as in step 4 before sending.

## Never

- Send, schedule, or resend without the step 4 confirmation, even if the user asked for something earlier in the conversation.
- Pass `scheduled_at` to `update-campaign` or `resend-campaign` before the user has confirmed: it sends at that time.
- Import or email contacts the user didn't collect themselves (bought or scraped lists).
