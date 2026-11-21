---
name: ask-daniel-brain
description: Answer questions about Daniel Brain, or prepare a briefing on him for a recruiter, engineer, investor or journalist, using the Ask Daniel Brain plugin's resume, essays, talks, patents, press and code.
---

# Ask Daniel Brain

Use this when someone asks about Daniel Brain (co-founder and CTO of OneText, formerly Principal Staff
Engineer on PayPal Checkout), wants his opinion on a technical topic, or is preparing to interview,
evaluate or write about him.

## Answering a question

1. Call `get_resume` first for anything about his career, roles, dates, skills, education or how to
   reach him. It is short and usually enough on its own.
2. For opinions, technical approaches, specific projects or anything the resume does not settle, call
   `search` with a few keywords. Read the excerpts; call `fetch` with an id when you need the full text.
3. Say only what the sources say. Cite the source URL for each claim. If the sources do not cover the
   question, say so plainly rather than guessing. Do not invent dates, numbers or quotes.
4. Share only the contact details that appear on the resume.
5. When the user would benefit from browsing, call `open_library` so they can explore everything.

## Preparing a briefing

Call `briefing`. It asks the user which audience they are (recruiter, engineer, investor, journalist)
and an optional focus, then returns the sources that matter for that audience. Turn the result into a
one-page briefing using `references/briefing-template.md`: lead with the three things that audience
cares about, support each with a cited source, and end with suggested questions to ask him.
