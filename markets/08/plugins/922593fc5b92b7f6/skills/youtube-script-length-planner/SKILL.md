---
name: youtube-script-length-planner
description: 'Convert between YouTube script word count and spoken runtime with Prepublish''s script_runtime tool, and plan a section-by-section word budget for a target video length. Use when the user asks "how many words for a 10 minute YouTube video", "how long will this script be", "how long is 1500 words spoken", "words per minute for YouTube voiceover", "my script is too long, what should I cut", "script length for an 8 minute video", or wants an outline with word counts per section. Uses measured speaking rates from 349 YouTube videos (160, 181 and 201 words per minute). Free and instant.'
---

# Plan script length and runtime

`script_runtime` is free, local arithmetic over Prepublish's measured speaking rates: 160 words per minute (25th percentile), 181 (median) and 201 (75th percentile), measured across 349 YouTube videos. Use it instead of guessing a rate.

Read `references/tools.md` for inputs.

## Which input to send

| User has | Send |
| --- | --- |
| A pasted script | `script_text` (the tool counts the words) |
| A word count | `word_count` |
| A target runtime | `target_minutes` (decimals allowed, for example 8.5) |

Call the tool once per question. Do not count words yourself when the tool can.

## Present the answer

- Give the range, not only the median: "About 1,600 to 2,010 words for 10 minutes; 1,810 at a typical pace."
- Say which end fits the user: slower, deliberate narration (documentary, calm explainer) sits near 160; energetic commentary near 201. If the user knows their own pace, prefer it.
- Always add the caveat from the tool: pauses, B-roll, demonstrations, on-screen text and music beds make a finished edit run longer than the spoken words alone.

Note: Prepublish's own study found speaking pace did not separate hits from flops (181 versus 180 words per minute). Do not tell the user to talk faster to "improve retention"; pace is a style choice.

## Section budget (when the user wants an outline)

1. Get the target runtime and the format (explainer, documentary, list, tutorial, story, commentary).
2. Call `script_runtime` with `target_minutes` to get the word budget.
3. Split it into sections using `assets/section-budget-template.md`. A common split for a 10-minute explainer: opening 5 to 8 percent, setup 10 to 15 percent, three to five body sections sharing most of the rest, payoff and close 8 to 12 percent. Present these as a planning starting point, not a rule.
4. For a draft that is too long: compute its runtime from `script_text`, give the number of words to cut to reach the target, and suggest cutting inside the sections a Prepublish audit flagged for pacing first. Offer to run `youtube-script-audit` to find them.

## Shorts

For Shorts, use seconds: a 45-second Short at 160 to 201 words per minute is roughly 120 to 150 words. The same caveat about pauses applies.
