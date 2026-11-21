---
name: pick-costume
description: Find a DIY Halloween costume from materials the user already owns. Use when the user needs costume ideas, wants to know what they can make, or asks about Halloween costumes.
---

# Pick a Costume

Help the user find a DIY Halloween costume they can actually make from what they already own.

## How to use the tools

1. Ask who the costume is for (kid, adult, couple, family, pet) and what materials they already have on hand.
2. Call `pick_costume` with the audience, owned materials, and any vibe or interest preferences.
3. Present the top 3 matched costumes with their match reasoning.
4. When the user picks one, call `get_build_guide` for the full materials list and step-by-step build instructions.
5. If they want ideas based on a specific item they own (e.g. "I have a cardboard box"), use `search_by_owning` with that material.

## Guidelines

- Prioritize costumes with the highest material coverage from what they own.
- Always mention the estimated build time and effort level.
- Flag any safety notes from the build guide (especially for kids).
- Keep suggestions practical: no shopping required unless the user asks.
