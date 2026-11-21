---
name: tubegrade-get-started
description: Start here with TubeGrade — what it can research on YouTube, how credits work, checking the balance, and fixing errors (not enough credits, indexing, missing fingerprints, tracking not available). Use for "what can TubeGrade do", "how many credits do I have", or when a TubeGrade call fails.
---

# TubeGrade — get started

Read `references/tubegrade-tools.md` before answering anything about tools,
costs or errors.

## When this applies
- The user is new to TubeGrade or asks what it can do.
- They ask about their balance or what something costs.
- A TubeGrade call failed and they want to know why or what to do next.

## What TubeGrade is for
YouTube research grounded in real numbers: which videos broke out (beat their
own channel's normal views) and why, the title and thumbnail formats behind
them, how channels are growing, what viewers say in comments, and what was
actually said in videos (transcripts). Thumbnails come back as real images.

Offer the workflows that fit the user's goal:
- New ideas from breakout videos → **tubegrade-video-ideas**
- Choosing the single best next video for their channel → **tubegrade-next-video-planner**
- Titles and thumbnails for a video → **tubegrade-packaging-studio**
- A researched script with cited sources → **tubegrade-script-writer**
- Studying a rival channel → **tubegrade-competitor-breakdown**
- Why one video worked → **tubegrade-video-teardown**
- What viewers want, in their own words → **tubegrade-comment-insights**

## Balance and costs
1. Call `tubegrade_balance` (free) and report the number.
2. If they plan something specific, estimate its cost from the table in the
   tool notes and say it before running anything. A typical research session
   is 30–80 credits; bulk transcripts are the expensive part (10 each).

## Fixing errors
Match the error to the tool notes' **Errors** section and give the concrete
next step. Specific cases:
- **Not enough credits** — report the call's cost and the balance, then
  suggest the cheapest way to still answer (fewer videos, `limit` lower,
  `tubegrade_search_videos` instead of bulk transcripts). Do not retry the
  same call.
- **Sign-in problems** — the user signs in with their TubeGrade (Google)
  account when the connection is first made; reconnecting the TubeGrade
  plugin/connector in the assistant's settings re-runs sign-in.
- **Anything else** — point to https://www.tubegrade.com/support/ (support
  email is listed there).

## Don't
- Don't run paid research just to demonstrate the tools — ask what they
  want to find out first.
- Don't describe plans, prices or ways to get more credits; if asked, point to
  https://www.tubegrade.com/support/.
