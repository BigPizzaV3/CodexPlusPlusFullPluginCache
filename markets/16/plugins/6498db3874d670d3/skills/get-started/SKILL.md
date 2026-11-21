---
name: get-started
description: Set up Blindspot after installing the plugin. Checks that the Blindspot account is connected, shows what is already saved, and agrees how the user wants to learn in chat. Use when the user runs plugin setup, asks how to start with Blindspot, or Blindspot tools are not connected yet.
---

# Get started with Blindspot

Blindspot is the user's personal English-learning storage: saved words with
translations and examples, vocabulary topics, and personal grammar rules. You
provide translations, explanations and exercises; Blindspot keeps what you save
so it shows up in the Blindspot app and in later chats.

Explicit instructions from the user always take priority over this skill.

## 1. Check the connection

Call `list_topics`. It is read-only and cheap.

- If the tool is unavailable or returns an authentication error, stop and ask
  the user to connect Blindspot: enable the Blindspot plugin for this chat and
  complete the Blindspot sign-in when prompted. A free account can be created
  at https://blindspot.study. Do not call other Blindspot tools until the
  connection works.
- If it succeeds, continue.

## 2. Show what is already saved

1. Call `list_vocabulary` with `limit: 5` to read the `total` word count and
   the `target_language` / `native_language` of recent words.
2. Call `list_grammar_rules` with `limit: 1` to read the `total` rule count.
3. Summarize in two or three lines: number of saved words, topic names with
   word counts (from step 1), number of saved grammar rules.

If nothing is saved yet, say so plainly; that is normal for a new account.

## 3. Agree on how to work

Ask, in one short message:

- Which language they are learning and their native language, only if this is
  not clear from saved words. Use ISO 639-1 codes internally (for example
  `en` and `ru`).
- Whether you should save useful new words automatically during this chat, or
  only when they ask. Default to "only when asked" if they do not answer.

## 4. Suggest a first step

Offer up to three concrete options that match what they have, for example:

- "Paste a text or write a few sentences in English, and I'll correct it and
  save the new words."
- "Quiz me on my weakest words" (only if they have saved words).
- "Practice one of my grammar rules" (only if they have saved rules).

## Limits

- Saved grammar rules can be read but not created or edited from chat.
- Billing, subscriptions and account settings are managed only in the
  Blindspot app; point the user to https://blindspot.study/support.
