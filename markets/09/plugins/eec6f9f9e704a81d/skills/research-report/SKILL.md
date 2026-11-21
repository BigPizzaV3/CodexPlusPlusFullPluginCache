---
name: research-report
description: "Get a research report from SuperCool that reads the web and cites its sources, delivered as a document. Use when the user wants a deep, sourced report on a market, competitor, topic or question, beyond a quick answer."
---

# Research report

Runs a multi-step web research job and returns a written report with sources.

## The brief

- The question, and what the user will use the answer for.
- Scope: region, time period, sources to prefer or avoid, and the depth they need.
- The format: report, comparison table, brief or slides, and the length.

Answer simple factual questions yourself; use this skill when the user wants a sourced report or the question needs real digging.

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
