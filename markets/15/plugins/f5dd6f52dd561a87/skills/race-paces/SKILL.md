---
name: race-paces
description: Give road runners their training paces, the pace and splits of a goal time, and the time left before a dated road race, with the 7Running tools. For road races from 5K to marathon. Not for pain, injury, nutrition, heart-rate zones or trail races.
---

# Road race paces with 7Running

Use this skill when a runner asks for running paces, or for the time left before a specific road race.

1. Collect what the runner gave: recent road race results (distance and finish time), a known VMA in km/h, a goal distance and time, a race date.
2. Write times as h:mm:ss, or mm:ss under one hour (a 3h30 marathon is 3:30:00), and dates as YYYY-MM-DD.
3. For training paces, or the pace and splits of a goal time, call `get_training_paces`.
4. For a specific road race with a date, call `race_countdown`.
5. If nothing usable was given (no race time, VMA, goal or date), ask one short question instead of guessing.
6. Report the paces, splits and dates as the tool returns them. Do not recompute them and do not change the ranges.
7. If a tool returns an error message, show it and ask for the missing or corrected value.

Present paces as training guidance, not as a promise of a finish time. Answer in the runner's language. Explicit instructions from the user take priority over this skill.

Do not use the 7Running tools when the runner mentions pain, injury or a medical condition: suggest seeing a health professional instead. Do not use them for nutrition, hydration, heart-rate zones or trail races with elevation. 7Running does not write training plans: if the runner asks for a plan for a dated road race, you may call `race_countdown` for the time left and the goal pace, and write the rest of the answer yourself.
