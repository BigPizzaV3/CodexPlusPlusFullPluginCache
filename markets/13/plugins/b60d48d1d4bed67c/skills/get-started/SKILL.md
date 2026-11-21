---
name: get-started
description: Use Kickwise for football (soccer) match predictions, exact score predictions, AI match summaries with the starting lineups, and the AI's graded track record.
---

# Kickwise football predictions

Kickwise publishes an AI model's predictions for football matches, made before kickoff, and grades every call afterwards.

- For a day's matches or one league, use `get_predictions` (`day`: today or tomorrow; `league`: one of the listed league slugs).
- For one team's match (live, upcoming, or from the last two weeks), use `get_match_prediction` with the team name, and the opponent when there is more than one match.
- For an AI preview, live summary or recap of a team's match, with both starting lineups and formations once announced, use `get_match_summary`.
- For how often the AI is right, use `get_ai_track_record`.

Answer in the user's language, as always. When the user writes in English, Spanish, French, Arabic or Portuguese, pass `lang` (en, es, fr, ar or pt): team names, the AI's summaries and the kickwise.ai links then come in that language too. For any other language the data comes in English; translate it as you normally would.
About an hour before kickoff, once the lineups are out, a match also carries the AI's exact score prediction (`score_prediction`).
Kickoff times are in UTC. Every match comes with its kickwise.ai page (lineups, live score, where to watch).
The chances are estimates for entertainment and discussion, not betting advice. Kickwise does not offer odds or betting.
When the AI has not published a call for a match yet, the tools say so; there is no number to give until then.
