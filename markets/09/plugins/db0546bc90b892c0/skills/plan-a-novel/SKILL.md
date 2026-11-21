---
name: plan-a-novel
description: Turn a story idea discussed in the chat into a Musael project with acts, chapters, scenes and the main characters and places. Use when the writer asks to start, plan or save a new novel, story or series in Musael.
---

# Plan a novel in Musael

The writer's own instructions come first. If they ask for a different structure, a different number of parts, or to skip a step, do what they ask.

## When to use

The writer has an idea, often talked through in this chat, and wants it as a project in Musael: "make this a Musael project", "set up my novel in Musael", "save this outline to Musael".

Do not use this skill to add to a project that already exists: use `add_to_plan` and `add_world_entries` on it instead.

## Steps

1. Gather what the plan needs, from the chat first. Ask only for what is missing and matters: the working title, and roughly how the story is divided (acts or parts, chapters). If the writer has not decided, propose a structure that fits the genre and length they mentioned, and say it is a starting point they can change.
2. Draft the plan in the chat before saving it: acts with a one-line synopsis, chapters, and scenes with one or two sentences each saying what happens. Name each scene's point-of-view character and place when the idea makes them clear. Keep the writer's own words and names.
3. Collect the World: the characters, places, objects and factions the plan relies on, each with a short description from the chat. Do not invent backstory the writer did not give; leave the description short instead.
4. When the writer agrees, call `create_project` once with the title, the acts (each with its chapters and scenes), and the entries. Point-of-view and place names must match entry names or other names exactly.
5. Show the result: the Plan appears as an outline with an "Open in Musael" button. Say how many acts, chapters and scenes were created and which names, if any, were left off the scenes.
6. Offer one next step: add scenes to a chapter, save more characters, or open the project in Musael to start writing.

## Rules

- Scenes are created empty. Never put draft prose into synopses; a synopsis says what happens, not how it is written.
- Call `create_project` once per project. If it reports that the project was created a moment ago, do not call it again.
- If the tool says the writer's plan does not allow saving new work, tell them plainly and stop; do not try other tools to get around it.
