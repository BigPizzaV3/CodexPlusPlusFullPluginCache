---
name: build-story-bible
description: Save the characters, places, objects and factions discussed in the chat into the World (story bible) of a Musael project, without duplicates. Use when the writer asks to save, record or add story bible entries to Musael.
---

# Build the story bible in Musael

The writer's own instructions come first: if they name exactly what to save, save that.

## When to use

The writer has invented or described characters, places, objects or groups in the chat and wants them kept in their Musael project's World: "save these characters to Musael", "add the places to my story bible".

## Steps

1. Find the project with `list_projects`. If there is more than one likely project, ask which one.
2. List the entries you would save, from the chat only: type (character, place, object or faction), name, other names, and a description of a few sentences with what the writer said (role, look, history, what matters to the story). Merge entries that are the same person or place under one name with the others as other names.
3. Show the list and let the writer correct it. Skip anything they did not settle.
4. Call `add_world_entries` with the confirmed entries. Entries already in the World, by name or other name, are left as they are and reported.
5. Report what was added and what was already there. Offer to set new characters as the point of view of scenes, which `add_to_plan` does for new scenes.

## Rules

- Never invent facts the writer did not give to fill a description.
- This only adds. To change an entry that exists, the writer edits it in Musael.
