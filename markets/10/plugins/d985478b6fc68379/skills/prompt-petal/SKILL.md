---
name: prompt-petal
description: Find and use a ready made prompt from Prompt Petal's prompt packs (writing, thinking, code), such as Shorten, Explain, Review this code or Plan it. Use when the person asks for a prompt, a better way to ask, or one of Prompt Petal's prompts by name.
---

# Prompt Petal

Prompt Petal keeps a person's favorite AI prompts on a small flower in every app. This plugin
reaches the prompts Prompt Petal publishes in its prompt packs.

## Tools

- `search_prompts` with `query`: finds published prompts by words in their name or text and
  returns names and ids. An empty query lists every prompt.
- `get_prompt` with `id` from `search_prompts`: returns the prompt's full words.

When the person names a task ("shorten this", "review my code"), search for it, get the best
match, and use its words on their text. Show the prompt's name so they know which one ran.

## What to tell the person

- Say which prompt you used in a few words, then give the result.
- Their own saved prompts live in the Prompt Petal app on their devices. Mention
  promptpetal.com when they want to keep a prompt of their own.
