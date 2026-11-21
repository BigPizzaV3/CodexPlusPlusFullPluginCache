---
name: soemind-get-started
description: How to create marketing videos, images and voiceovers with the connected SoeMind account: the price-first rule, using files the user attaches, and the standard workflow.
---

# Getting started with SoeMind

SoeMind is an AI content operating system: it generates marketing videos,
images, voiceovers and music inside the user's own projects, edits and
converts their media, and publishes to Facebook, Instagram and TikTok.
Everything runs on the user's SoeMind account and credits.

## The one rule that always applies

**Never spend credits without telling the user the price first.**

1. Call the matching estimate tool (`estimate_image`, `estimate_video`,
   `estimate_voiceover`, `estimate_music`, or the `estimate_*` tool paired
   with an edit tool) with the same arguments you will generate with.
2. Tell the user the credit price and wait for their OK.
3. Call the generate or edit tool with `confirmCredits` set to that price.
   The server refuses the call if the live price is higher than what was
   confirmed. That is a guardrail, not an error to work around.

## Plans, workspaces and credits

- Generating needs an active SoeMind plan, or membership of an active
  workspace (Business). Without a plan, only the 100 free trial credits can be
  spent, on the lower-cost models.
- A workspace member generates inside that workspace's projects, and the
  workspace's credits pay. If the user has no personal plan, pick a workspace
  project from `list_projects`; a personal project will be refused.
- If a tool answers `plan_required`, tell the user plainly and point them to
  soemindai.com/pricing (or their workspace admin). Do not retry.

## Standard workflow

1. `whoami`: confirm the account and credit balance.
2. `list_projects`: every generation targets a project (`projectSlug`).
3. Estimate, then the user approves, then generate (`generate_image`,
   `generate_video`, `generate_voiceover`, `generate_music`).
4. `job_status` with the returned jobId until it succeeds. Video takes 1 to
   5 minutes; poll patiently and do not resubmit.
5. `list_recent_outputs` and `get_file_url` to give the user a link to view
   or download the result.

## When the user attaches a file

If the user attaches an image, video or audio file in this chat and wants
SoeMind to use it, call `import_attachment` first with the attached file and
the project. It returns a `fileId`. Then pass that fileId to the tool that
needs it, for example:

- `edit_image` (put their product or logo into a scene), `remove_image_bg`,
  `vectorize_image` (logo to a clean SVG)
- `animate_image` (bring a photo to life)
- `caption_video`, `dub_video`, `trim_clip`, `transcribe_media`
- `clone_voiceover` (speak a script in the voice from their recording)

Importing is free. Do not ask the user to upload the file somewhere else.
The attachment link expires after a few minutes, so import it right away.

## Useful generate arguments

- `generate_image`: `prompt`, optional `aspectRatio` ("1:1", "4:5", "16:9",
  "9:16"), optional `imageSize` ("1K" or "2K"). Text-to-image only: to use a
  real product, person or logo, import the photo and use `edit_image`.
- `generate_video`: `prompt`, `durationSeconds` (keep 4 to 8).
- `generate_voiceover`: `script` (about 1,000 characters is about 1 minute).
- `generate_music`: `prompt` (style and mood).

Use `get_prices` for the live per-unit rates when the user asks about costs
in general.

## Publishing

`list_social_accounts` shows the connected pages. A post prepared from chat is
saved as a draft; it is published only after the user approves that specific
post.

## What to refuse or redirect

- Anything that would spend credits without the user approving the stated
  price.
- Content that impersonates real people without consent, or that breaks
  SoeMind's content policy. The server's moderation blocks these; do not
  retry around a moderation refusal.
- Account changes (plan, billing, refunds, deletion): send the user to
  soemindai.com, Settings.
