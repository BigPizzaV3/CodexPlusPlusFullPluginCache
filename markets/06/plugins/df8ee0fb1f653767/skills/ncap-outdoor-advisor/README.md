# Scouting America Outdoor Programs NCAP Unofficial Advisor

This folder is a reusable ChatGPT Skill package intended to be used directly or leveraged by a Plugin.

## Files

- `SKILL.md` — primary skill definition and operating instructions
- `references/scouting-source-hierarchy.md` — official Scouting America source and version-control workflow
- `references/jurisdictional-research.md` — federal/state/county/local research workflow, including employment law, camp permits, health department, food service, pools/waterfronts, fire, boating, and firearms
- `references/answering-playbook.md` — response patterns and application guidance

## Design choices

The skill is intentionally **NCAP/Scouting America first**. It does not research state/county/local law merely because a camp is named. Jurisdictional research is activated only when the user's question actually turns on employment law, permits/licensing, food service, regulated facilities, fire/occupancy, sanitation/utilities, or another concrete government requirement. When activated, the skill determines the physical jurisdiction and verifies current official government sources at answer time.

The skill also separates four categories that should never be blurred:

1. Scouting America requirements
2. Government/legal requirements
3. Recommended operational practice
4. Interpretation where the sources do not expressly resolve the facts

## Suggested Plugin use

A Plugin using this skill should provide web access for current official-source verification. If it also supplies static reference documents, those should be treated as supplemental unless the current Scouting America landing page or responsible government agency confirms they remain current.
