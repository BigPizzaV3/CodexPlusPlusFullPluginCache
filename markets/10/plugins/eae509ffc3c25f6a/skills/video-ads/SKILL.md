---
name: video-ads
description: Create, revise, and inspect UGC-style AI video ads through Retiplex. Use for product ad projects, product media, actors, scripts, storyboards, rendering progress, and supported generation recovery on a connected Retiplex account.
---

# Retiplex video ads

Use the connected Retiplex MCP tools. Every operation acts on the account that
signed in through OAuth. The endpoint is `https://app.retiplex.com/mcp`.

Read the MCP resource `retiplex://guide` when costs, media rules, or a less common
operation need clarification. Live tool schemas, server instructions, and
returned project state supply the current requirements; use those instead of
assuming a saved project is still at the same step.

## Account and scope

- Call `get_account` first and before spending credits. Respect
  `canGenerateVideos`, `creditsBalance`, and `maxScriptSeconds`.
- If the connection is missing, ask the user to connect Retiplex and complete
  OAuth themselves. A new user can sign up at
  `https://app.retiplex.com/sign-up`. Do not request their password or tokens.
- For an existing project, use `list_projects` and the user's selection, then
  `get_project`. Clarify an ambiguous choice before modifying a project.
- For a new project, get a product URL or a product name and factual description.
  Reuse campaign details already supplied; clarify only consequential gaps.
- Follow the user's requested stopping point. A request to inspect or write a
  script does not authorize generating a storyboard or video.

## Credits and review

Generative operations spend Retiplex credits. Explain a step's cost before
running it, using current server guidance and available estimates. Label an
approximate price as approximate; do not invent an exact quote. Respect spending
limits and previously granted authorization.

Before `start_video_generation`, read `estimatedVideoCredits` from a fresh
`get_project`, show the estimate, and obtain the user's acceptance unless their
existing authorization already covers that estimate. Pass the approved amount
as `max_credits`. If the estimate exceeds the approved limit, stop and ask; do
not raise the limit automatically. A final-render estimate does not include
credits already spent preparing the project.

Show the script and storyboard at their review checkpoints. Wait for review
when requested; otherwise follow the user's authorized workflow. Regeneration
can replace existing work and spend credits again.

When `canGenerateVideos` is false, explain that video generation is not included
in the account's current plan. Product, brief, actor, and script setup can still
be available. In ChatGPT, report plan or credit limitations neutrally without
upgrade prompts or checkout links.

## Create or revise an ad

Use `get_project` and its `nextTool` to determine the next valid operation. The
usual sequence is:

1. `create_project` imports the product URL, or saves its name and description.
   Classify any imported media before the storyboard needs it.
2. `list_formats` returns current narrative formats; `set_creative_brief` sets
   the format, audience, benefit, goal, and funnel stage. For `custom`, use `idea`
   to describe the intended ad. Missing campaign facts can be generated at a cost.
3. `set_actor` casts the narrator and renders a portrait. Show `previewUrl`.
   Omit `archetype` for automatic casting; use its current schema to design or
   update the actor. Each call renders another portrait.
4. If requested, add extra cast with `add_subject` and required scenes with
   `add_moment` before writing the script. Use names from the returned cast in
   `@[Name]` tags. These additions are optional unless using uploaded footage.
5. `generate_script` writes the voiceover, or saves the user's supplied `script`
   without script-generation charges. Respect the account's duration limit.
6. `generate_storyboard` starts scene planning in the background. Check
   `get_project` every 20–30 seconds while pending; inspect `storyboard.job` for
   failures and review the returned `scenes` when complete.
7. After reviewing readiness and credit authorization, use
   `start_video_generation`. Check `get_video_status` about every two minutes.

For edits, `set_product`, `set_creative_brief`, `set_actor`, and
`generate_script` update the corresponding project content. Changing the script
after storyboarding requires another storyboard; inspect `storyboard.stale`.
Use `remove_subject`, `remove_moment`, or `update_product_media` with
`remove: true` only when the requested edit includes that removal. Do not edit a
project while its video is generating.

## Product photos and footage

`get_project` lists media and what each item still `needs`. Inspect the images
before using `update_product_media` to assign angles or descriptions. If the
environment cannot inspect an image, ask the user for its description and view.
Physical product photos need view angles. Detail shots, videos, and photos of
digital products or services need descriptions. Use the live schemas and guide
for accepted formats, dimensions, file sizes, duration, and description limits.

- Public media URLs can be passed through `create_project` or `set_product`.
- For local files, `create_media_upload` returns a one-time `upload_url`. Upload
  only the intended file's bytes with HTTP PUT and its Content-Type, then call
  `finalize_media_upload`. Confirm success before treating the file as attached.
  If local-file upload is unavailable in the host, use a public URL or `appUrl`.
- Uploaded videos appear in the ad only through `add_moment` with
  `type: "custom-footage"` and `footage` containing `media_id`, `start_seconds`,
  and `duration_seconds`. Clips play muted. Uploading alone does not include them.
- An `add_subject` image uses exactly one source: `image_url`, `upload_id`, or
  `generate: true`. A generated person also needs an `archetype`.

## Progress and recovery

Use `get_project` for storyboard and subject-image progress; use
`get_video_status` for video progress. Explain meaningful status changes and
include the returned `appUrl` so the user can review the project in Retiplex.
If the current host cannot keep waiting, share the project link and current
state; do not promise an ongoing monitor that has not been set up.

On a failed video, read `nextAction`. Use `resume_video_generation` only when
that action recommends it and the user's authorization covers the recovery.
Incomplete scenes and failed exports may require finishing in the app. Do not
retry a credit-spending operation blindly after an unclear response: read the
project and status first to check whether it already started.

Share `finalVideoUrl` when returned for a completed render. Distinguish an
actor preview, storyboard, or pending render from the finished video. Retiplex's
tools create video assets; publishing campaigns or uploading to social accounts
requires a separate integration and user authorization.
