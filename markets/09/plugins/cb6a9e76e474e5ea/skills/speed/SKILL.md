---
name: speed
description: >-
  Ship mode. Run the next task fast, without coaching friction, for when the user
  just needs it done. Invoke on "ship mode", "just do it", "skip coaching", "I
  need this fast", "don't coach me on this one".
---

The user wants speed on this task, not coaching.

1. If you have not already, call `talent_get_coaching_layer` and adopt it; it
   defines ship mode, including the one rule that still holds under speed.
2. Execute the task efficiently. Skip the hypothesis check and the probing. Annotate
   the key decisions so the user can verify them.
3. Follow the operating layer's instruction for what ship mode still owes the user
   in coach and protect domains; do not drop it.
4. Ship mode is per task. Return to normal TAOS coaching on the next task, and do
   not edit the profile.
