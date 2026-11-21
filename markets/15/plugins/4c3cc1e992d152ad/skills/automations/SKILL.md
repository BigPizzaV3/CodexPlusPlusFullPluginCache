---
name: automations
description: Use for campaign-member rules that switch a portrait or play a sound when a character becomes active or gains a status condition.
---

# Automations

Call `get_automation_options` for the campaign. If the rule belongs to another member, request options again for their `campaign_user_id`. Read the returned authoring guide, eligible characters, condition IDs, effect targets and limit. Use `list_automations` for that member and update a matching rule before creating another.

Each rule has one JSON Logic condition and one effect. For a battle portrait, match the character’s `active_turn`. For a poisoned portrait, test membership of the condition ID in `status_condition_ids`. Use the guide’s boolean templates and returned fact paths. Choose `character_avatar.show_on_character` and the target portrait ID, or `sound_effect.play_once` and the member’s eligible sound ID. For a new cue, create it on that member's own soundboard and refresh options before selecting it. Submit with `create_automation` or `update_automation`.

For example, when a character gains Poisoned, use the discovered character’s status-condition fact and the numeric Poisoned ID from the options. A portrait effect’s target is the portrait ID. Build the missing-fact guard from the returned template so an offscreen character cannot trigger a rule by accident.

Rules are evaluated in the game-screen browser. A sound plays once when its rule becomes true and rearms after it becomes false. The member’s allowance and rule position determine which rules are eligible. Later matching portrait rules take precedence and a manual active portrait overrides them. `reorder_automation` changes precedence. `delete_automation` removes a rule. Edits can affect an already open screen.
