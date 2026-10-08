---
name: get_meditation
description: Deliver the complete 40-minute Dhyana meditation practice in 3 phases
---

## Trigger conditions
Use this tool when the user:
- Asks "how do I meditate?" or "teach me meditation"
- Mentions Dhyana, Bhrumadhya, third eye focus, or breath awareness
- Says "I want to do the meditation practice"
- Asks "what's the 40-minute practice?" or "how long should I meditate?"
- Has finished asanas and wants to move into the sitting practice
- Asks about Chin Mudra in the context of sitting practice

## Task instructions
Call `get_meditation` with no arguments — it is free, no token needed.

1. Display the photo FIRST:
   `![Dhyana Meditation](https://84asana.com/photos/Dhyana.png)`

2. Then present in this order, copying VERBATIM from the API response:
   - **Prepare Your Space** — from `prepare_space` field
   - **Dress Code** — from `dress_code` field
   - **Setting the Ambience** — from `ambience` field
   - **Seeking Permission** — from `seeking_permission` field
   - **Hand Position (Chin Mudra)** — from `hand_position.instruction` field
   - **Phase 1: Breath Awareness (20 min)** — steps from API
   - **Phase 2: Brumadhyam Focus (10 min)** — steps from API
   - **Phase 3: Return to Breath Awareness (10 min)** — steps from API
   - **Closing the Session** — from `closing` field
   - **Tips** — from `tips` array

Copy ALL content VERBATIM from the API — do not rephrase, summarize, or add words.

## Example interaction
User: "Guide me through the 40-minute meditation"
→ Call `get_meditation` → show photo first → then all sections in order verbatim.
