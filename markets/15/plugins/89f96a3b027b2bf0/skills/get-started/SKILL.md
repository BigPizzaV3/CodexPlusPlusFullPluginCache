---
name: get-started
description: Show a new Vibestash user what they can do in this chat and capture their first idea.
---

# Getting started with Vibestash

Vibestash is the user's own idea vault. Help them see what it does by doing it, not by explaining it at length.

1. Call `get_profile`. If the profile is empty, ask in one short message how they build (by chatting with AI
   builders, or writing code), how they find customers, and how many hours a week they have, then save the
   answers with `set_profile`. Personal fit is scored against this profile.
2. Ask for one idea they have been thinking about, in their own words. Raw text is enough.
3. Save it with `create_idea`. Tell them its title and that the score and the empty sections fill in within a
   minute.
4. Offer the next step, in one line each:
   - add the riskiest assumption with a cheap test (`add_assumption`);
   - research the market: get the plan with `research_plan`, search the web, then save the findings with
     their sources (`save_assistant_research`);
   - when they have talked to possible buyers, log it as evidence (`log_evidence`).

Keep replies short. Never invent sources for research. Never delete anything during onboarding.
