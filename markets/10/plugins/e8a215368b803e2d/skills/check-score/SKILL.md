---
name: check-score
description: Review and fix the "things to check" PlayableNotes reports after reading sheet music (measures that don't add up, unreadable lines, suspicious notes).
---

# Checking a score after reading

Reading printed music is very accurate but not perfect. PlayableNotes lists "things to check": measures whose voices don't add up to the time signature, lines it couldn't read, and similar problems. Review them only when the teacher asks; the card has a "Review with ChatGPT" button for this.

1. Call `get_score`. The things to check are listed with their measure numbers.
2. For each one, look at the measure and its neighbours:
   - **Too long or too short**: usually a duration misread (an eighth read as a quarter, a missing dot, a triplet without `t3`), or a rest or spacer missing in a second voice. Fix the smallest thing that makes it add up and keeps the musical sense, such as matching the rhythm of a parallel measure.
   - **Pickup or final measure**: an incomplete first measure is a pickup and is fine. A last measure that completes it is also fine. Leave both alone.
   - **Unreadable line**: rebuild it from the other staff and the harmony only if you're confident. Otherwise, say which measure needs the teacher's eye.
   - **Wrong-sounding notes**: a common cause is an accidental that should carry through the measure, or a clef change that was missed (`{G}` and `{F}`).
3. Send only the fixed measures to `edit_score`, with a summary such as "Fixed rhythms in measures 12 and 30".
4. Report what you fixed and what you left for the teacher, with measure numbers. Suggest comparing with the original pages (the "Original" button in the PlayableNotes studio) for anything uncertain.

Never "fix" a measure by inventing music. If you can't tell what was printed, say so.
