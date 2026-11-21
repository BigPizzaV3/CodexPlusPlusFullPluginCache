---
name: get-started
description: Make a short video or image with Dora from a description or a photo, and deliver the result.
---

# Making videos and images with Dora

Dora turns a description or a photo into a short video or an image. Use it when the user wants to create, animate or restyle visual content.

## Before generating

- If the user has not said what to make, ask only: "What do you want to create?" Offer no list of options.
- If it is not clear whether they want a video or an image, ask only that. If it is clear, do not ask.
- Then generate straight away with the tool defaults: for video, vertical 9:16, 8 seconds, 480p, sound on when available; images at 1K. Change a setting only when the user asks.
- If the user attaches a photo, pass it in `photos` so the result keeps the same face, pet or product. Use `image_url` only for a public https link the user gave you; never guess one.

## Generating

1. Call `generate_image` or `generate_video`. It returns a `job_id` right away.
2. Tell the user it is on its way.
3. Call `check_job` quietly with the `job_id`, waiting about 30 seconds between checks, until the status is `done` or `failed`. Do not end your turn before that. If you cannot keep waiting, say plainly that the result is not ready yet and to ask you for it in a little while.
4. When it is done, send one message with the link from `check_job`, as text. Do not embed the file, and repeat only the settings the tool returned. If it failed, say so plainly and offer to try again; the coins for a failed generation are returned automatically.

## When something stops the request

- `CONTENT_POLICY`: Dora does not create sexual content, content involving minors, graphic violence or self-harm. Say that this request cannot be made and offer a different direction. Do not try to rephrase the same request around the filter.
- `INSUFFICIENT_CREDITS`: the user's Dora account does not have enough coins for this generation. Say so and share the link in `plans_url` for information. Do not encourage a purchase.
- `AUTH_EXPIRED`: ask the user to reconnect Dora.

## Series and characters

For a recurring character, ask for one or two clear photos of them and pass them as reference images on every generation, so the face and outfit stay consistent across clips.
