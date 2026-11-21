---
name: presentation
description: "Make a presentation or pitch deck with SuperCool, ready to present or download. Use when the user wants slides for a pitch, report, lesson, sales call or talk."
---

# Presentation

Makes a finished, designed slide deck and returns its link.

## The brief

- The topic and audience, and what the deck should achieve (raise money, teach, sell, report).
- Number of slides (default 8 to 10) and the outline if the user has one.
- The facts, numbers and names to use. Don't invent figures: pass on what the user gave and tell them where data is still needed.
- Style or brand colors, logo, and any images or documents to draw from (https URLs).

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
