---
name: tiktok-hooks
description: Write TikTok hooks, the first one to three seconds of a video, using seven hook types and what already worked on the creator's own public TikTok account. Use when the user asks for TikTok hooks, opening lines, a better first line, "scroll-stopping" openers, or wants an existing hook rewritten. Each hook comes as spoken line, first frame and on-screen text. Not for full scripts (use tiktok-scripts) and it never promises views.
---

Use this skill when the user wants hooks or opening lines for TikTok videos.

## The seven hook types

| Type | Template to adapt | Works for |
|---|---|---|
| Contradiction | "Stop doing [common advice]. Here's why." | Tips, education, myth-busting |
| Specific result | "How I went from [real number] to [real number]" | Case studies, before and after |
| Mid-action | Start at the reveal, explain after | Cooking, DIY, makeovers, edits |
| Direct callout | "If you're a [person] who [problem], watch this" | Niche advice, coaching |
| Open loop | "The reason [problem] happens isn't what you think" | Explainers, storytime |
| Visual pattern-break | Unusual first frame or movement | Faceless, product, visual niches |
| Stakes reversal | "I almost [quit / failed]. Here's what changed." | Personal stories, growth journeys |

## Steps

1. Find out what the video is about. If the user has not said, ask once.
2. If the user gives a TikTok username, call `get_tiktok_script_and_hook_inputs` once and look at the opening lines of `top_videos`. Note which hook types the account's most-viewed videos already use, and lean on those. If the result has `niche_trends`, you may also say how those niche posts open, as an observation; never copy another creator's line. If there is no username, skip this step and say the hooks are not based on their account.
3. Write the payoff of the video in one sentence. Every hook is a short promise of that payoff.
4. Write the number of hooks asked for (5 if not said). Use at least three different hook types and name the type next to each hook.
5. Give every hook in three matching parts:
   - **Say:** one line, about three seconds or less out loud.
   - **Show:** the first frame.
   - **Text on screen:** a few words, placed high, clear of the caption area.
6. Suggest filming two of the openings for the same idea and comparing them by rate (engagement divided by views), not by raw counts.
7. If a tool was called, end with the plain link from its result, once.

## Rules

- Only fill "[real number]" brackets with numbers the user gave or the tool returned. Never invent a result.
- No greetings, no "hey guys", no "wait for it".
- The video must pay off the hook. Do not write a hook the described video cannot deliver.
- Never promise or predict views.
- If the tool cannot read the account, say so in one sentence using its `message` and carry on from the topic alone.
- Explicit instructions from the user come before these guidelines.
