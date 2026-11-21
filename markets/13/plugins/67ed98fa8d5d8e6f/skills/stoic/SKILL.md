---
name: stoic
version: 1.0.0
description: Open Stoic to journal with a daily passage from Marcus Aurelius, Seneca or Epictetus, set a morning intention, do an evening review, or sort a worry into what is and is not in your control.
---

# Stoic

Use this skill when the user asks to open, show, or use their Stoic journal, or wants to journal, reflect on their day, set a Stoic intention, do an evening review, work through a worry with the dichotomy of control, or start a Stoic practice.

## How to open it

Call the `show_stoic_journal` tool from the `stoic` MCP server. It renders the interactive journal in the chat.

If the tool is unavailable, direct the user to the hosted app:

https://stoic.host.safrow.com/

## What it does

- Passage of the day from Marcus Aurelius, Seneca or Epictetus, quoted from public-domain translations with author, work, reference and translator
- Morning: intention, what might go wrong, and how to respond (premeditatio malorum)
- Evening: what went well, where I fell short, what I will do differently, plus a 1–5 check on wisdom, courage, justice and temperance
- Control sorter: list worries, sort them into "in my control" and "not in my control", plan a next move
- 7-day Stoic Foundations challenge
- Streak, year heatmap, search, favourite passages, undo/redo, JSON and Markdown export

## Behavior

When the user says things such as "open my Stoic journal", "help me set an intention for today", "I want to do my evening review", "I'm anxious about tomorrow", or "start the 7-day Stoic challenge", open the journal.

The user writes directly in the journal. Their entries stay in their browser, so you cannot see or change them. Do not claim to have read, written or saved an entry, and do not quote their streak or stats unless the user tells you. You may discuss Stoic ideas, explain a passage, or help the user think through what to write.

Never invent quotes. If you paraphrase a Stoic author, say it is a paraphrase. For an exact quote, point the user to the passage in the app.

Stoic is for reflection, not therapy. Do not diagnose or assess the user's mental state. If the user describes being in crisis or at risk of harm, respond with care and point them to local emergency services or a crisis line.

If the journal shows "Not saved", the chat blocked storage; suggest using Backup to export a copy.
