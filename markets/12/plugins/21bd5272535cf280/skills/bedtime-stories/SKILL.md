---
name: bedtime-stories
description: Use when a parent wants tonight's bedtime story, read aloud, or wants last night's story continued ('tonight's Tucktale episode'). Writes and narrates the next episode of the family's series.
---

Tucktale keeps a family's bedtime story series: the characters, the setting, what happened in every episode so far, and an audio narration of each episode. The parent or caregiver sets it up and asks for each night's episode; the child listens. This skill covers setting up a series, tonight's episode and changes to it. The user's own instructions come first.

## Inputs

- **A new series** (`create_series`): the main characters (toys, animals or made-up friends, each with what they are), where the stories happen (`setting`), one to three values such as kindness, courage or trying again, the listener's age band (`age_band`: 3-4, 5-6, 7-8 or 9-10) and the episode length (`length`: short, medium or long, about 3, 6 or 10 minutes). Optional: a title, a narration voice, episodes per season (5 to 14, 10 by default) and things to keep out of the stories (`avoid`).
- **Tonight's episode**: a request such as "tonight's Tucktale episode", "tonight's bedtime story" or "continue last night's story". Without a series id, the parent's most recent series is used.

## Flow

1. `create_series` saves the series once and returns its private listening link (`listening_link`) and podcast feed (`podcast_feed`). It writes no episode.
2. `get_episode_brief` returns what tonight's episode is written from: `episode_number`, the characters and setting, `story_so_far` (a recap of every earlier episode this season), `earlier_seasons`, `facts`, `last_hook`, `tonights_value`, `target_words` for the chosen length, the age band's `style` and the bedtime `rules`.
3. The episode is written to that brief, and `save_episode` stores it once with its title, the full text in paragraphs, a 2-3 sentence summary and any new facts. Tucktale checks the text, then narrates it on its own server; the audio is ready in a minute or two in the card, on the listening page and in the podcast feed. The result's `summary` says which episode to ask for the next night.
4. `rewrite_episode` replaces the newest episode (for example calmer, shorter or without something) and records its narration again. `show_series` shows a series and its listening link, `update_series` changes its settings or gives it a new listening link, and `delete_series` deletes it.

## Scope

- Characters are the family's toys, animals or invented friends. Tucktale keeps no real child's name, age, school, town or photo; when the parent mentions their child, a made-up hero or "the listener" stands in. Characters from books, films, shows or games are not accepted.
- Narration is in English, read by one of four voices on Tucktale's own server; the narration is AI-generated.
- Only the newest episode can be rewritten, so the story stays consistent.
- A one-off story that isn't part of a series is outside Tucktale; ChatGPT tells it itself.
