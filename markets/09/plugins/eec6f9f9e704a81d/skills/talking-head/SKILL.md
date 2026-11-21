---
name: talking-head
description: "Make a talking-head video with SuperCool: an AI presenter who speaks a script to camera, for explainers, product walkthroughs, UGC-style reviews and lessons. Use when the user wants someone on camera saying something."
---

# Talking-head video

Makes a video of an AI presenter speaking to camera, with a consistent face and voice across videos.

## The brief

- The script, or the topic and key points so the agent can write it (say which).
- Length (default about 30 seconds), shape (vertical 9:16 or 16:9) and language.
- The presenter: age range, look, voice and setting, or "the same presenter as last time".
- Captions, b-roll or a call to action at the end.

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
