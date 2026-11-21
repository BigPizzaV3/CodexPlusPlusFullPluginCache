---
name: notes
description: "Save notes to beckett, filed by topic and linked to the people and places they mention, and find saved notes. Use when the user asks to remember or save something, shares a lasting fact about themselves or someone they know, or asks what they saved about a person or topic."
---

# Notes

- If beckett's tools aren't available, beckett isn't connected yet. Say so once, give the step below, keep what they asked for, and offer to finish it once beckett is connected. Don't say anything was saved to or found in beckett.
  - In ChatGPT, open **Plugins**, choose **beckett**, and connect a beckett account. Connecting creates one for anyone who doesn't have an account yet.
- When beckett is connected, follow the shared rules in the use-beckett skill.
- To save something the user wants kept, use `beckett_store_notes`. beckett files the note by topic and links the people and places it mentions.
- To find notes, search their saved notes. For notes about a person, look the person up first, then read the notes linked to them.
