---
name: update
description: >-
  Update the user's TAOS profile: expertise changes, new goals, or calibration
  tweaks like "coach me harder on X", "never automate Y", "move Z to speed".
  Invoke when the user reports a change or asks to adjust how TAOS treats them.
---

Update the user's Talent Augmentation OS profile through the connected `taos` MCP
server.

1. Understand the change: a new or changed expertise rating, a new goal, a
   calibration preference, or a red line.
2. Call `talent_preview_profile_update` with the proposed change to produce a diff
   for the user.
3. Show the diff and get an explicit yes. Never change the profile without
   confirmation.
4. On confirmation, call `talent_save_profile` to persist it, then restate what
   changed in one line.
