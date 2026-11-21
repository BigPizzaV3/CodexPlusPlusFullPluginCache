---
name: get-started
description: How to work with a local business's Kadaleo account — bookings, customers, messages, website, posts and payments — and which actions the owner must confirm in Kadaleo.
---

# Working with Kadaleo

Kadaleo runs one local business: its website, bookings, customer inbox, customers, social posts and invoices. The person
connected is the business owner.

- Start with `today` for "how is my day / week", then `list_bookings`, `list_conversations` or `search_customers`.
- Read before you write: look up the booking, conversation or service and use its id.
- Anything a customer would see (a reply, a booking change, a booking or payment link, a post, new hours or prices) is
  only **prepared**. Show the owner the confirmation link the tool returns and say that nothing has changed until they
  press Confirm on the Kadaleo page. Never claim it was sent.
- To plan posts from the owner's photos and videos: `upload_media` (ChatGPT passes attached files in `files`; pasted public
  links go in `urls`; 1-10 per call) or `list_media` for what is already stored, then `plan_posts` with one item per post
  (`social_account_id`, `caption`, `media_urls`, `scheduled_for`). One confirmation link schedules the whole plan; until
  the owner presses Confirm the new posts are only drafts. `draft_post` makes a single draft (several photos or one video).
- Website edits (`site_*`) go live at once and return a preview link; `site_undo` reverts the last one.
- There are no tools for refunds, deleting customers, bulk changes, campaigns or account settings: say these are done in
  the Kadaleo dashboard.
- If a tool refuses (for example the WhatsApp 24-hour window), explain the reason in plain words and suggest the next step.
