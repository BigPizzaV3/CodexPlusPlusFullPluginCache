---
name: dice-rolling
description: Use to roll on the live game screen, express advantage, damage or modifiers in dice notation, or check a pending public result.
---

# Dice rolling

MCP sends dice to the table. Check `get_game_screen` for a live screen whose `active_components` include `overlay`. A private check belongs in the dice drawer on the player's or DM's own browser. If someone asks for a private roll, direct them there and keep their check off the table.

Pass one `dice` string and the campaign ID to `roll_dice`. The basic die term matches `/^(\d*)d(4|6|8|10|12|20|100)(kh|kl)?$/i`. Omit the count for a single die. Join dice terms and flat modifiers with `+` or `-`. Roll up to 100 dice. The screen understands the same Roll20 expressions as the web roller.

| Requested roll | Dice input |
| --- | --- |
| Advantage, Bless and a +10 modifier | `2D20kh+1d4+10` |
| Disadvantage with a -2 penalty | `2d20kl-2` |
| Weapon damage plus fire | `1d8+3+2d6` |
| Roll four d6 and drop the lowest | `4d6dl1` |

Submitting creates one public roll. The screen can take up to 10 seconds to return its total. Check `get_dice_roll` with the original roll ID. If the result is still pending, report that and keep the ID. Another call to `roll_dice` starts a new roll.
