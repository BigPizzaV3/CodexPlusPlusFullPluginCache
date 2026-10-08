---
name: working-with-slidely
description: Create, import, review, and edit PowerPoint presentations with Slidely. Use this whenever the user wants a deck built from a topic or outline, wants an existing .pptx improved or redesigned, or asks to continue work on a presentation they already have in Slidely.
---

## Slidely is a stateful presentation agent, not a set of one-shot tools

Slidely builds and edits PowerPoint decks. You work with it through a chat that remembers everything in it — the uploaded files, the chosen design, the approved storyline, the slides it has proposed and the feedback you gave. A message asks it to do something; it decides the next useful step and may ask a question before acting.

The user owns the presentation. Slidely proposes, the user approves, and slides only enter the deck through an explicit review.

## Read the working instructions before you start

The detailed workflow — how to initialize a presentation, when to involve Slidely, how design systems and layouts are chosen, how to answer the cards it raises, and who decides what — is served by two tools:

1. Call `list_skills` and read the descriptions.
2. Call `read_skill` for the one that matches what the user is asking for, and follow it.

Do this before the first Slidely tool call of a conversation, not after. The instructions cover which tool answers which card, and getting that wrong strands the user's work — accepting slides, choosing layouts and setting a design each have one correct tool, and a message is not a substitute for any of them.

A skill may list further files under `files`; read one with `read_skill` when the instructions point you at it.
