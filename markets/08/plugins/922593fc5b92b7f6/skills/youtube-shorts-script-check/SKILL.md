---
name: youtube-shorts-script-check
description: 'Check a YouTube Shorts, TikTok or Reels script before filming with Prepublish: score the first line or two as the hook, check that the spoken length fits the target duration, and audit the full short script for attention risk with rewrites. Use when the user shares a script for a Short, a vertical video, a 15, 30, 45 or 60 second video, or asks "is my Shorts hook good", "how many words for a 60 second Short", "will people swipe away", "make my Short script tighter", or "check my TikTok script". Not for long-form scripts (use the full audit) and not for predicting views, swipe rate or viewed-versus-swiped-away figures.'
---

# Check a Shorts script

A Short has seconds to earn attention and no room for setup. This skill runs the three checks that matter most, cheapest first.

Read `references/tools.md` and `references/claims-and-limits.md`.

## Inputs

- The script verbatim and the target length in seconds (ask once; default to 45 seconds if the user has no target and say so).
- A working title or topic line (needed for the full audit).
- Email for the full audit if the user has no Prepublish account (explain first, never invent).

## Workflow

1. **Length**: `script_runtime` with `script_text`. Convert the minutes to seconds. Compare with the target: at 160 to 201 words per minute, 30 seconds is about 80 to 100 words, 45 seconds about 120 to 150, 60 seconds about 160 to 200. If the script is over, say how many words to cut.
2. **Opening line**: `audit_hook` on the first one or two sentences. In a Short the opening line has to do the job a whole intro does in a long video. Present the score, the weakest line and the rewrites.
3. **Full script**: if the script is at least 50 characters, `audit_script` with the title and script. In a Short, focus on flagged passages that delay the payoff or repeat a point; mention the attention-risk map only if it shows a clear dip.
4. **Tighten**: offer one revision that applies the hook rewrite, cuts to the target length and fixes the top flagged passage. Keep the creator's voice. Offer one re-check of the hook.

## Shorts-specific guidance you may give (as craft advice, not predictions)

- Put the payoff or the promise in the first line; setup that a long video can afford usually does not fit.
- One idea per Short. If the script has two, suggest splitting it into two Shorts.
- If the Short is meant to loop, make the last line lead naturally back into the first.
- On-screen text should reinforce, not repeat, the spoken line.

Never quote viewed-versus-swiped-away rates, retention percentages or view forecasts as outcomes of these checks. The tools read text only.
