---
name: analyze-reel
description: Diagnose why a specific short-form video underperformed by analysing the video itself. Use when given an Instagram, TikTok or YouTube Shorts link and asked why it flopped, how to fix the hook, or where viewers dropped off.
---

# Diagnose a reel from its link

Runs the video through Reelyze: frame-by-frame vision, transcript, scene cuts,
and a predicted retention curve. Returns where viewers are predicted to leave
and what to change.

## Tools

| tool | cost | returns |
|---|---|---|
| `get_transcript(url)` | free, metered | the spoken words |
| `analyze_reel(url)` | **paid plan, spends one analysis** | full report |
| `explain_drop_off(analysis_id)` | paid plan | per-moment retention diagnosis |
| `check_job(job_id)` | free | poll a running job |

`get_transcript` and `analyze_reel` are **asynchronous**. They return a
`job_id`; poll `check_job` until `status` is `completed` or `failed`. A full
analysis takes minutes, not seconds. Tell the person it is running rather than
polling in silence.

## Spend the paid call deliberately

`analyze_reel` consumes one analysis from the person's plan allowance, the same
allowance the Reelyze dashboard spends. Before calling it:

- confirm this is the video they want analysed, if more than one link is in play
- if they only asked what was said, `get_transcript` is free and sufficient
- if the call returns 402, their plan has not billed yet. Say so and link
  https://getreelyze.com/billing rather than retrying.

## Read the report in the order that matters for reach

This order is not cosmetic. It is the order these levers actually move
distribution, and a report read out of order sends people to fix the wrong
thing.

1. **Skip rate, the hook, first 3 seconds.** The single biggest lever. If the
   opening loses people, nothing later in the video gets a chance.
2. **Watch time, retention through the rest.** A *separate* lever, not a
   restatement of the hook. A video can survive the first 3 seconds and still
   collapse at 5 to 8 seconds, and low average watch time stops the algorithm
   expanding reach even though the opening worked.
3. shares
4. likes
5. saves
6. reposts
7. comments

Lead with whichever of 1 and 2 the report actually implicates. Do not invent a
mid-video problem for a video that holds its middle.

## One caveat you must not get wrong

The reported `skip_rate` is **not** a 3-second measurement despite the name.
Instagram's API exposes no true 3-second skip rate, so it is derived from
average watch time across the whole video. That one number therefore spans both
levers 1 and 2 and cannot separate "left at 2 seconds" from "left at 15
seconds". Only the retention graph from `explain_drop_off` shows the shape of
the drop.

So never assert that a high skip rate proves the opening was weak. It is
consistent with a weak opening and equally consistent with a strong opening and
a collapse at 8 seconds.

## Give fixes that can be executed while editing

A diagnosis the person cannot act on is half an answer. For each moment, name
the concrete on-screen change: the exact caption words to overlay and where, a
hard cut or zoom, a progress cue, b-roll, a pattern interrupt. "Improve the
hook" is not a fix; "put 'I lost $4,000 on this' on screen at 0:00 and cut the
establishing shot" is.

## Links this accepts

Instagram reels, TikTok, YouTube Shorts. Share strings are tolerated: a pasted
TikTok link with the trailing "This post is shared via TikTok" caption is
normalised before download, so pass the string as given rather than editing it.
