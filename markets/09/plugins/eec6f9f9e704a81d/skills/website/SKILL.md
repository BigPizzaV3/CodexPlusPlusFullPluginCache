---
name: website
description: "Build and publish a website or landing page with SuperCool, then change it by asking. Use when the user wants a site, landing page, portfolio or simple web app for a business, product, event or person."
---

# Website

Builds a real, published website and returns its live link. The user can keep changing it by asking.

## The brief

- What the site is for and who visits it.
- The pages or sections (default: one page with hero, about, services or products, and contact).
- Real details to include: business name, location, prices, hours, contact details, links. Never make these up: leave placeholders and tell the user which ones to fill in.
- Style, colors, logo or photos (https URLs), and any form (contact, booking, signup).

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
- Connecting a custom domain or handling payments happens in the user's SuperCool account; pass on what the agent says about it.
