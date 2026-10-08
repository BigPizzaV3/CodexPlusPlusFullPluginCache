---
name: vitals
description: Read the connected person's VITALS personality profile and adapt how you work with them. Use this whenever they ask how you should work with them, ask about their own traits, patterns, or motivations, ask about their career fit, a relationship, or their 360 feedback, or whenever a task turns on their preferences for tone, detail, pace, or how they decide. Use it even when they never say the word VITALS.
---

# VITALS

VITALS is a personality profile the person completed themselves. Every tool is
read-only and returns only their own data.

## Which tool, and when

- **Once per working session, before style starts to matter:** `get_collaboration_directives`.
  These are written for you, not for them. Apply them to your tone, detail, and
  pace, and do not read them back.
- **They ask about themselves, their traits, or their patterns:** `get_personality_profile`.
- **Work, roles, environments, or motivation:** `get_career_profile`.
- **A named person or a working relationship:** `list_relationships`, then
  `get_relationship_read` or `get_relationship_tendencies`.
- **Two people side by side:** `list_profile_comparisons`, then `compare_profiles`.
- **What other people said about them:** `get_360_feedback`.

Leave the tools alone when the person did not ask about themselves and the task
does not turn on how they work. A profile read they did not want reads as
surveillance, which costs more trust than the personalization gains.

## How to speak about the results

- Bands are tendencies, not scores, strengths, or weaknesses. Each pole has a
  cost and a use, so "leans toward planning" is true where "scores high on
  planning" invents a ranking that the instrument does not produce.
- Say only what the profile says. Percentiles, rankings, and comparisons to other
  people are not in the data, and inventing them makes the rest untrustworthy.
- Do not diagnose. This describes how someone tends to work, not what they are
  capable of, and it is neither clinical nor predictive.
- Prefer the profile's own words. They were written for this person to recognize
  themselves in, and a paraphrase usually loses that.

## When a tool returns no content

- `status: no_profile`: they have not completed the assessment. Send them to
  https://app.vitals.me.
- `status: not_generated`: that part is not built yet. Tell them to open it in the
  VITALS app. Nothing you call will build it.
- An error saying a feature is not turned on: tell them what it said and move on.
  Retrying returns the same error.
