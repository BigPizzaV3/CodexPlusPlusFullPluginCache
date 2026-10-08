---
name: get_warmup
description: Deliver the complete warm-up sequence — Arrival & Centering, 15 Joint Rotations, Surya Namaskar
---

## Trigger conditions
Use this tool when the user:
- Asks "how do I warm up?" or "how do I start my practice?"
- Says "I want to begin yoga" or "what do I do first?"
- Asks about Surya Namaskar, joint rotations, or Chin Mudra
- Wants to do today's practice and hasn't started yet

## Task instructions
Call `get_warmup` with no arguments — it is free, no token needed.

For each section, display its photo first, then the steps verbatim:

1. **Arrival & Centering** (3 min)
   - Photo: `![Arrival and Centering](https://84asana.com/photos/Arrival and Centering.png)`
   - Then copy the 8 steps VERBATIM from the API response

2. **15 Joint Rotations** (10 min)
   - Photo: `![Joint Rotations](https://84asana.com/photos/Joint Rotations.png)`
   - Then list all 15 joints in order with exact instructions from API

3. **Surya Namaskar** (7 min)
   - Photo: `![Surya Namaskaram](https://84asana.com/photos/Surya Namaskaram.png)`
   - Then show both "Right Leg Back and Front" and "Left Leg Back and Front" with exact breath cues from API

Copy ALL steps VERBATIM — do not rephrase, summarize, or add words.
After presenting, ask if the user is ready to move into the asana sequence.

## Example interaction
User: "I'm ready to start. What should I do?"
→ Call `get_warmup` → show photo then steps for each section → offer to proceed to asanas.
