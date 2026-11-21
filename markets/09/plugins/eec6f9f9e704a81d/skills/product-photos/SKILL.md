---
name: product-photos
description: "Create product photos, image ads and branded visuals with SuperCool, from a description or the user's own product photos. Use when the user wants images for a product, ad, store listing or social post."
---

# Product photos and image ads

Makes finished images: product shots, image ads with headlines, lifestyle scenes and branded visuals.

## The brief

- The product or subject, and the user's product photo if they have one (https URL). With a photo, the agent keeps the real product's look.
- How many images (default 4) and the shape: square 1:1, portrait 4:5, vertical 9:16 or landscape 16:9.
- Style and setting: studio, lifestyle, flat lay, bold graphic, a mood or a reference.
- Any headline, offer or brand colors to put on the image.

## How to run it

1. Collect the brief above from what the user has already said. Ask one short question only if something essential is missing; otherwise go ahead with sensible defaults and say which you chose.
2. Call `message_agent` once with the complete brief in plain language: every detail, style, length and format the user gave, and any files as public https URLs. Send a fresh `request_id` with each new message; reuse one only to retry that same message.
3. Pass on the agent's reply in a sentence or two. If it started work, call `wait_for_updates` with the returned cursor. Keep calling while `done` is false (right away when `more` is true).
4. Results appear in the SuperCool card as they arrive (images, video posters with a play link). Don't embed them again as images in your reply; describe them briefly and share their links. Websites, documents and decks are links.
5. For changes ("shorter", "warmer colors", "swap the music"), send them to `message_agent` as a follow-up about the same work. To show a finished result again, use `get_work` with its `work_id`.

## Rules

- Never describe, link or claim a result you haven't received from `wait_for_updates` or `get_work`.
- Don't quote prices, credit amounts or how long it will take unless the agent said so. If the agent says the user is out of credits, tell them plainly and pass on any link it gives.
- Explicit instructions from the user come before this skill's suggestions.
- Don't make content that shows a real, identifiable person (a celebrity, public figure or private individual) saying, doing or endorsing something, unless it's the user themselves or they confirm they have that person's consent. Decline briefly and offer an original character instead.
