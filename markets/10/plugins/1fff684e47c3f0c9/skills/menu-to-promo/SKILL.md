---
name: menu-to-promo
description: Turn a real dish from a connected restaurant's menu into marketing — Studio designs, then (optionally) a social post — with the credit cost and the post shown before anything is spent or published.
---

1. `get_studio_options` for the dishes; pick one with the owner (dishes with a photo work best). Use real dishes, prices and offers only.
2. `estimate_creative` and tell the owner the credit cost and what it will make. Wait for yes.
3. `create_creative` with `max_credits` = that estimate and a new `request_id`. Then `get_creative` every ~30 seconds until done; show the images.
4. If they want to post: `get_social_accounts`, draft a caption with them, then `create_social_post_draft` with the chosen image's `asset_id`. Show the draft (text, image, accounts).
5. Publish or schedule with `publish_social_post` only after an explicit yes. Report the result per platform with `get_social_post`.
6. Never claim a post went out unless `get_social_post` says published. If an account needs reconnecting, say so and share where.
