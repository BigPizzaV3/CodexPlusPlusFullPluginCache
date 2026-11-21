---
name: posts-delete-post
description: Delete a PropBot post the person asked to remove.
---

Use this skill for that request.

Permission: propbot.posts.write.

1. Delete only when they asked to remove that post. Call posts_private_post_delete. Show what was removed.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
