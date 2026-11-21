---
name: get-started
description: "Start here with SuperCool: what the user's SuperCool agent can make in ChatGPT, how a request runs, and how results come back. Use when the user first connects SuperCool, asks what it can do, or asks how it works."
---

# Get started with SuperCool

SuperCool connects ChatGPT to the user's own SuperCool agent. The agent makes finished work in their SuperCool account: videos and video ads, images and product photos, talking-head presenter videos, websites, presentations, research reports, music and voiceovers. It remembers their earlier work across SuperCool, so "the logo from last week" or "make yesterday's ad shorter" work.

When the user asks what SuperCool can do, answer in a few lines from the list above and suggest one or two concrete things to try, based on what they've told you about themselves. Don't call a tool just to describe SuperCool.

When they ask for something to be made, use the matching SuperCool skill if one fits (video ad, product photos, talking-head video, website, presentation, research report, music). Otherwise follow the steps below with whatever they asked for.

## The brief

What they want made, who it's for, and any style, length, format or files they gave.

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

## When not to use SuperCool

Answer quick questions, arithmetic, and writing you can do yourself in the chat without SuperCool. Don't send account changes such as deleting work, cancelling a subscription or changing billing to the agent: tell the user to do that in their SuperCool account settings at supercool.com.
