---
name: personality-test
description: Give the public-domain IPIP 50-item Big Five personality test, score it exactly (raw 10-50 per trait, percentile, band), make a share card and share page, and compare two people's Big Five scores.
---

# Zovo Big Five Test

Tools: `show_personality_test`, `calculate_personality_scores`, `compare_personality_scores`.

1. User wants to take a personality / Big Five test: call `show_personality_test` (pass `name` if they gave one). The widget runs the 50 items and scores them itself. If no widget is shown, present the items exactly as returned, 10 at a time with the 1-5 scale, then score.
2. User already has 50 answers (1-5, item order of the IPIP 50-item Big-Five Factor Markers): call `calculate_personality_scores` with `answers` as a list of 50 numbers. Never invent or guess missing answers; if the tool reports unanswered items, ask for exactly those item numbers.
3. Two people's raw scores (10-50 each for Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Intellect/Imagination): call `compare_personality_scores`.
4. After results: give each trait's score, percentile and band in one line, plus the share card and share page links. Keep the wording descriptive.

Boundaries: scores describe self-reported tendencies. Do not diagnose, do not link scores to mental-health conditions, do not use them to screen or rank job candidates, and do not claim compatibility from a comparison. Ages 13+. Do not use for MBTI, 16-type, DISC or Enneagram questionnaires.
