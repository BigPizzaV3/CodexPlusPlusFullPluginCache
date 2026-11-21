---
name: podcasts
description: Find and play podcasts on Spinn Radio, by show name, host or topic, or from the podcast charts. Use when the user asks to play, find or recommend a podcast or an episode ("play the latest Daily", "top true crime podcasts", "a podcast about space").
---

Use this skill for podcasts.

1. Find the show:
   - A show, host or topic: call `search_podcasts` with it in `query`.
   - "Top", "popular" or "best" podcasts: call `top_podcasts`, with `category` when the user names one (news, comedy, truecrime, business, sports, history, science, technology, health, education, society, tv-film, kids, fiction, arts, religion).
2. To play, call `play_podcast_episode` with the `show_id`. Leave out `episode_id` for the newest episode.
3. For a particular episode ("the one about the midterms", "last week's"), call `get_podcast_episodes`, pick the matching `episode_id`, then `play_podcast_episode`.
4. After the player opens, say in one sentence which episode you chose. Playback starts when the user taps play; the player has a seek bar, skip buttons and Next for the following episodes.

Only use shows, episodes and ids returned by Spinn tools. Don't summarise an episode's content beyond its returned title and description.
