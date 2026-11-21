---
name: listening-links
description: Use when a parent wants the listening page or podcast feed of their bedtime story series, or wants to change, renew or delete a series ('show my Tucktale series', 'make the episodes shorter', 'give the series a new link'). Manages a Tucktale series and where the family listens.
---

Every Tucktale series has a private listening page and a podcast feed, so the child can listen on a phone, a speaker or a podcast app without ChatGPT. The user's own instructions come first.

## Flow

1. `show_series` shows the series card: the characters, the episodes so far, the listening link (`listening_link`) and the podcast feed (`podcast_feed`). Without a series id, the parent's most recent series is used.
2. `update_series` changes a setting (the episode length, the voice, the values, things to avoid) for the episodes to come, or gives the series a new listening link so an old one stops working.
3. `delete_series` deletes a series with its episodes and audio when the parent asks.

## Scope

- Anyone with the listening link can listen; a new link replaces it at once.
- Changes apply to future episodes; the newest episode can be rewritten through the bedtime-stories skill.
