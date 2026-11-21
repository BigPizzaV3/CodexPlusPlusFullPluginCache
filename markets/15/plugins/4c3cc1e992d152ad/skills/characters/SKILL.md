---
name: characters
description: Use when preparing NPCs, monsters or player characters, editing their statistics and descriptions, or keeping DM information hidden.
---

# Characters and NPCs

Look up the campaign and search `list_characters` before creating an NPC. Check `get_character` for existing details. Use the name filter `q` and follow pagination. The `off_screen` scope helps locate a prepared NPC who has yet to enter the encounter. For “prepare the NPCs for the next session,” use the encounter notes or names supplied by the DM. If the encounter is unspecified, ask what the party will face before inventing campaign records.

Use `create_character` or `update_character`. Record the name, description, initiative and passive perception. Owners can set `npc`, `dm_notes` and `legendary_actions`. Put secrets in DM notes. Use `hidden` for a combatant whose identity should stay hidden from the players and `on_screen` for membership in the initiative lineup. For a hidden encounter, create the Lantern Keeper with `name`, `npc: true`, `hidden: true` and the DM's secret in `dm_notes`. A saved character can stay off the lineup until the scene begins. Read back the returned ID before adding a portrait or assigning a condition.

Give each new character a first portrait unless the user asks to skip it. Use supplied artwork or generate an image from the character description. If the appearance is open, ask what the user has in mind or invent a look that fits the setting. Pass the image to `import_upload`, then call `add_portrait` with the new character ID and the returned `signed_id` as `avatar`. The first portrait becomes the default.

Players can edit the characters assigned to them. When player creation is enabled, a character they create is a player character linked to their membership. Use the Avatars skill for alternative portraits and Status conditions for individual assignments.
