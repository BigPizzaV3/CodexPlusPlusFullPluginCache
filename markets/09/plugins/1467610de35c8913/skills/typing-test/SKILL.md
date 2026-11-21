---
name: typing-test
description: Run a live typing speed test (WPM, accuracy, consistency) in the chat with show_typing_test, score typed text exactly with calculate_typing_score, and build weak-key practice drills and challenge links.
---

# Zovo Typing Test

Use `show_typing_test` whenever the user wants to take a typing test, check their typing speed or WPM, practice typing, or be tested on a specific paragraph.

1. Map the request to settings and call the tool right away (no questions needed):
   - Length: `duration_seconds` 15, 30, 60 (default) or 120; job tests often use 60, 180 or 300. "Full passage" or "this paragraph" means `mode: "passage"`.
   - Style: `difficulty` `words` (default), `sentences` (punctuation and capitals, good for job or data-entry tests), `numbers`, or `code`.
   - Their own text: pass it verbatim as `custom_text` (5-3,000 characters); the test defaults to a full passage.
   - Practice: pass weak keys from a previous result as `focus_keys`, e.g. `"eth"`.
   - Retake or fair comparison: reuse the `seed` from an earlier test.
2. The widget times the test from the first keystroke and scores it with `calculate_typing_score` automatically. Do not ask the user to paste what they typed.
3. Call `calculate_typing_score` yourself only when the user gives the target text, what they typed, and the time. Never estimate WPM by hand.
4. After a result, report WPM, accuracy and errors, mention the weakest keys, and offer a drill (`show_typing_test` with `focus_keys`). Share the card or challenge link only if the user asks.

Scoring is word by word: WPM = (correct characters / 5) / minutes, where spaces between correctly reached words count as characters; accuracy = correct / (correct + errors).

Do not use this skill for internet speed tests, reading-speed tests, word counts, or typing lessons that do not involve a test.
