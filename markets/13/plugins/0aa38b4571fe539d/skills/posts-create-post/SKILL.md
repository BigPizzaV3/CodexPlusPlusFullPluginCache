---
name: posts-create-post
description: Create a PropBot post for the person or one company or group.
---

Use this skill for that request.

Permission: propbot.posts.write.

1. Call posts_private_post_create on the hat they named. Show the saved title and status. There is no separate post publish permission.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
