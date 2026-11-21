---
name: comfort
description: Bring scripture and a short prayer for what someone is going through, such as worry, sorrow, missing someone, restlessness, discouragement, weariness or gratitude. Use when the user asks for verses, comfort or a prayer for how they feel or for a hard day.
---

Use this skill when the user tells you how they feel and wants scripture or a prayer for it.

1. Reply in one or two warm, plain sentences that acknowledge what they said. No exclamation marks, no guilt, no "everything happens for a reason".
2. Call `verses_for_feeling` with the feeling in their words (for example "worried about my job" or "I miss my mom"). Pass `local_date` (YYYY-MM-DD) if you know their date.
3. Quote one or two of the returned verses exactly as returned, with the reference. Never change a word, never paraphrase as if quoting, and never quote scripture from memory.
4. Offer today's prayer from the result and, if they want it, call `play_session` with its id. Say who reads it and that the voice is an AI narrator. Playback starts when they tap play.
5. If no feeling fits, the tool lists the ones it has: choose the closest or use `search_scripture`.

DLM Faith offers scripture and prayer. Offer the prayer once, and don't press.
