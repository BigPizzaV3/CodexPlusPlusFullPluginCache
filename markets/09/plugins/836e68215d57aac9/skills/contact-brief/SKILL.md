---
name: contact-brief
description: Use when the user wants to prepare for a call or meeting with a customer or lead, or asks "who is X" / "what do we know about X" in Ciarem.
---

# Contact brief

1. Call `search_contacts` with the name, phone or email the user gave. If several match, list them (name, phone, email) and ask which one.
2. Call `get_contact` with that `id`.
3. Call `get_conversation` on the newest of its `recent_conversations` (limit 30).
4. Write the brief:
   - **Who**: name, channels they use, city/country, where they came from (`origin`), funnel stage.
   - **Last conversation**: date, what they asked for, what we answered, anything left open.
   - **Open questions**: things they asked that nobody answered, promises made, objections.
   - **Suggested next step**: one sentence.
5. End with the contact's `url` so the user can open it in Ciarem.

Only state what the tools returned. If a field is empty, leave it out rather than guessing.
