---
name: posts-ingest-images
description: Save outside images into a PropBot post and rewrite the article to the stored addresses.
---

Use this skill for that request.

Permission: propbot.posts.write.

1. Call posts_private_post_create with text only. Do not put an outside image address in the article.
2. Call posts_private_post_images_ingest with the post id and up to five https image URLs.
3. Call posts_private_post_update so every image address is a URL from replacementMap.
4. Publish only when the person asked. Call posts_private_post_publish, then repeat that call with confirm set to true.

Shared stops:

- One private call is the person, one company, or one group. Take the id from the membership list.
- Do not open another company's private records. Public homes from another company use public search.
- Do not send an invoice, collect payment, accept or reject a quote, write price or status history, or withdraw a listing.
- If the required permission is missing, stop and say that action is not available.
- Follow the person's explicit instruction when it is within these tools.
