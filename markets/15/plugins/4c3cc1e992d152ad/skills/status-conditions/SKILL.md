---
name: status-conditions
description: Use when defining a campaign status condition, choosing its icon and reminder, or adding or removing it on a character.
---

# Status conditions

Search `list_conditions` in the selected campaign. Use `create_condition` for a new definition or `update_condition` to change its name, color, icon or reminder text (`prompt`). A definition can be shared by several characters. For a new Stunned condition, set a recognizable color such as `#E0A100`, choose a Font Awesome icon such as `fas fa-bolt` and write the DM’s reminder in `prompt`. For custom artwork read `get_condition_icon_guide` and pass the allowed inline markup in `icon_svg`.

Find the character with `list_characters`. To apply Poisoned, pass that character’s ID, the existing Poisoned condition ID, and `assigned: true` to `set_character_condition`. Set `assigned: false` to remove just Poisoned. Use `get_character` to check the result. The `status_condition_names` field on `update_character` replaces the entire list, so reserve it for explicit replacements.

Renaming a shared definition changes its label for every character who has it. Removing it from one character leaves the definition available to everyone else.

Owners manage campaign definitions. A player’s ability to edit definitions and to change another character’s assignments depends on the campaign settings. Assignments may trigger an avatar or sound automation on the game screen.
