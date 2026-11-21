---
name: bedtime-series-setup
description: Use when a parent or caregiver wants to start a bedtime story series for their child, for example about a favourite stuffed animal or toy ('start a bedtime story series about my kid's rabbit'). Sets up the characters, world, values, age band and length once.
---

A Tucktale series is set up once, then continues every night. The parent or caregiver describes it; the child only listens. The user's own instructions come first.

## Inputs

- Two or three main characters: the child's toys, animals or made-up friends, each with what they are (a stuffed rabbit, a brave little turtle).
- Where the stories happen (`setting`).
- One to three values to weave in, such as kindness, courage or trying again.
- The listener's age band (`age_band`: 3-4, 5-6, 7-8 or 9-10) and the episode length (`length`: short, medium or long, about 3, 6 or 10 minutes).
- Optional: a title, a narration voice, episodes per season (5 to 14) and things to keep out of the stories (`avoid`).

## Flow

1. Ask only for what is missing; sensible defaults are fine for the optional parts.
2. `create_series` saves the series and returns its private listening link (`listening_link`) and podcast feed (`podcast_feed`). It writes no episode yet.
3. The first episode comes from the bedtime-stories skill, the same night or the next.

## Scope

- Tucktale keeps no real child's name, age, school, town or photo; a made-up hero or "the listener" stands in for the child.
- Characters from books, films, shows or games are outside Tucktale; the family's own toys and invented friends are the heart of it.
- Narration is in English and AI-generated.
