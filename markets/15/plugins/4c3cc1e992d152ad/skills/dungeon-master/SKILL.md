---
name: dungeon-master
description: Use when a DM sets initiative order, starts or ends combat, hides combatants, advances a turn, or skips to a new round.
---

# Dungeon Master

Read `get_combat_state` to see the DM’s ordered lineup, active character, round and turn token. Use `update_character` to record initiative and `screen_position` to set the actual order. Changing initiative alone leaves the lineup order intact. Set `on_screen: true` to add a character and `on_screen: false` to remove them. Use `hidden: true` to keep an upcoming combatant in the order but concealed on the player screen.

Start or end combat with `update_campaign` and `in_combat`. Starting requires at least one character in the lineup. It begins at round zero with no active character. For “start combat and take the first turn,” start combat, read the fresh state, then use `advance_combat_turn` with its `turn_token`. Use `forward` for the next turn, `backward` for the previous step, or `next_round` when the DM wants to skip the remaining turns and start the next round. A forward step from the last character ends the current round. The next forward step starts the next round with the first character. Activating a hidden character reveals it.

Changing the lineup needs Write access and the DM’s character permissions. Starting, ending or advancing combat needs Maintain and the DM’s campaign permissions. If another participant already changed the turn, read the state and report where combat is before advancing again.
