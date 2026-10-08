---
name: get_asana
description: Get step-by-step instructions and benefits for one yoga pose by number
---

## Trigger conditions
Use this tool when the user:
- Names a specific asana (e.g. "how do I do Vrikshasana?" or "teach me Tree Pose")
- Picks a number from the asana list (e.g. "number 3 please")
- Asks about benefits of a specific pose
- Wants to know how long to hold a pose or how many rounds

## Task instructions
1. Map the user's pose name to its id (1–13):
   - 1 Samasthiti, 2 Padahastasana, 3 Vrikshasana, 4 Saral Bhujangasana,
     5 Adho Mukha Svanasana, 6 Baddha Konasana, 7 Janu Sirsasana,
     8 Vakrasana, 9 Dandasana, 10 Supta Dandasana,
     11 Vajrasana, 12 Pawanamuktasana, 13 Shavasana
2. Call `get_asana` with the correct `id`.
3. Display the photo FIRST using the `photo` field from the API response:
   `![{asana name}](https://84asana.com/photos/{photo})`
   Example: photo = "Vrikshasana.png" → `![Vrikshasana](https://84asana.com/photos/Vrikshasana.png)`
4. Present in this order: photo → steps (numbered, verbatim) → benefits.
5. Copy ALL steps VERBATIM from the API response — do not rephrase or summarize.

## Notes
- Asanas 1–13 are FREE — no token needed
- Shavasana (13) is the final resting pose — always include it at end of practice
- This is a general wellness and fitness guide

## Example interaction
User: "How do I do Tree Pose?"
→ id = 3 → Call `get_asana({ id: 3 })` → show photo first → then steps → then benefits.
