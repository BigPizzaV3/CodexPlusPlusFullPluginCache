---
name: nacre
description: Use Nacre when the user asks to save what they learned to Nacre, asks to be quizzed or tested on what they saved, or asks what's due in Nacre or how their streak is going.
---

# Nacre

Nacre helps the user remember what they learn. It turns key ideas from a chat into short review questions and brings them back at the right time. The questions are answered in the Nacre app, not in the chat. Keep every reply light, short and encouraging.

## When to use each tool

| The user says something like | Call | Then |
| --- | --- | --- |
| "Save this to Nacre", "add that to Nacre", "remember this in Nacre" | `save_to_nacre` | Say in one sentence that it's saved and give the link to their questions in Nacre |
| "Quiz me from Nacre", "test me on what I saved" | `quiz_me` | Say how many questions are ready and give the link that opens them in Nacre |
| "What's due in Nacre today?", "how's my streak?" | `nacre_today` | Say how many questions are due and the streak in days |

## Saving

- Nacre saves only when the user asks, for example "save this to Nacre". It's fine to mention once that they can say that.
- One save per request. `summary` is a short list of the key facts they're learning, one line each, about 3 to 8 lines. Nacre writes the questions itself.
- Nacre is for things being learned, such as ideas and facts. Passwords, health, money, relationships and contact details don't belong in it; for a password, a password manager is the right place.
- Add a short `title` when the user names the topic, and set `source_app` to `chatgpt`.
- After saving, give the link from the result. The questions are ready about a minute later. Don't invent a number of questions.

## Quizzing

- Never write or ask quiz questions in the chat yourself, even if the user asks to be quizzed "here". Call `quiz_me` and give its link: the questions are answered and marked in Nacre, where the streak is kept.

## If something isn't possible

- If a tool says nothing was saved (for example the account is not finished, saves are used up for now, or Nacre is invite only), pass that on in one kind sentence with the link it gives. Don't mention plans, prices or upgrades.
- Each save adds a new set; Nacre never changes or deletes what's already saved, so don't retry a save that succeeded.
