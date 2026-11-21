---
name: teleprompter
description: Show a live script reader, calculate speech timing with pause cues, and plan script length for a target duration.
---

Use show_teleprompter when the user wants to read a supplied script in a live scrolling reader. Include the script and either speed or target duration. Use [PAUSE] for one second and [PAUSE 3] for three seconds. Numeric cues accept whole seconds from 1 to 86,400 per cue; values outside that range produce a plain error.

Use estimate_speech_time for a script or known word count. It returns named pace timing and timing for sections separated by blank lines or headings.

Use plan_script_length with a target duration and speed to calculate words to write. Include a script too when the user needs the required speed and words to cut or add.

Numeric speeds must be whole numbers from 60 to 300 wpm. Target-derived paces are reported as a fraction, with the nearest whole-number reader speed and its actual duration.
