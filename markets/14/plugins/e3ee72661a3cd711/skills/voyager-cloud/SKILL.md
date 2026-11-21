---
name: voyager-cloud
description: "Cloud: estimates, references, jobs, results, brand kits and Cast for hosted Voyager generation. Read first for any Voyager image, video, audio or 3D request."
---

# Voyager in the cloud

This plugin generates media on Voyager's servers with the user's existing Voyager
account, selected workspace and credits. It has no access to the user's computer,
editors or project folders. If the local Voyager plugin is also installed and the
work involves files on this computer, a timeline or an editor, use the local plugin
for that part.

Read the family skill before generating: `voyager-cloud-image`, `voyager-cloud-video`,
`voyager-cloud-audio` or `voyager-cloud-3d` (selecting or cutting out objects with
masks is in `voyager-cloud-image`; tracking them in a clip, in
`voyager-cloud-video`). When a skill isn't already loaded,
read it with `load_skill` and its name; a skill's reference files load the same
way with `file` set to the reference's path.

## Account and credits

A plain request needs no account check first: a generation that the workspace
can't run is refused with the reason and a link. Call `account_status` when the
user asks about their account or credits, or after a refusal: it reports the
selected workspace, whether generation is available for this user and the credit
balance.

When the workspace can't run a generation, the tool's error (or an estimate's
reason) says why in one sentence and may include a link. Tell the user what it
says and show its link as given, then ask how to continue. Never retry on another model to get around it without
asking. On `rate_limited`, wait the time the error gives and retry once.

## Models and settings

Models, supported settings, durations and limits change often: never rely on a
model name, cost or limit from memory. Spend at most one discovery call before
the estimate.

- **The user named no model:** generate with the default: omit `model` and the
  generation tool uses it (the result names it). When the request clearly fits a
  recommendation better (a 20-second shot, many references, faces and dialogue,
  clean text in an image), call `list_models` with the `operation` once, use the
  better fit and say why in a few words. With the first result of its kind in the
  conversation, add one line of alternatives from the recommended list, each with
  its reason (for video, for example: "fast and cheap: MiniMax H3 Max Turbo
  · atmosphere and longer shots: Seedance 2.5
  · cinematic realism: FLUX.3 Max Video"). Don't ask the user
  to choose a model first.
- **Common asks switch the model without a question:** cheaper or faster video →
  MiniMax H3 Max Turbo; longer than 15 seconds or many references →
  Seedance 2.5; cinematic realism → FLUX.3 Max Video; faces and spoken
  dialogue → Veo 3.1; clean text, a logo or a transparent background in an
  image → GPT Image 2.6 Flare. Say why in a few words.
  GPT Image 2.6 Flare: Clean text, transparency, careful edits and quick GIFs.
  GPT Image 2.6 Sunburst: Intricate hero art, showcase GIFs and demanding revisions, slower.
  For GIFs, animated stickers, looping reactions or animated logos, default to Sunburst;
  use Flare for quick drafts, many variations or requested faster output. Choose between them by
  speed and detail, not by cost.
  Use 9 frames at 200 ms unless the user asks to change timing.
- Ask at most one question, and only when something you can't sensibly default
  is missing (a reference the user mentioned but didn't attach, for example).
  Don't batch questions.
- **The user named a model:** use exactly that model, and keep using it for
  follow-ups on the same work until the user names another. Find it with one
  `list_models` call with `query` set to the name. When nothing matches, or the
  name fits more than one entry (a family name, a missing version or variant), say
  so, show the closest entries, and ask once which to use. Never pick a near
  match, a newer or cheaper version, or another provider in its place.
- Model IDs are Voyager catalog IDs (`nano-banana-2.1`, `veo-3.1`). The operation
  follows the request: reference images or Cast make an image model edit and a video
  model animate the image (image-to-video); `list_models` shows each model's operations.
- Never page through the whole catalog and never estimate several models to
  compare them. Never invent a model name or ID, and never switch models because
  another one's settings look simpler. Call `list_models` with `model` only when you need settings
  beyond prompt, duration, aspect ratio and audio.
- Name the model with the result. If Voyager refuses the model, or the job
  reports a different one, stop and ask before going further.
- A content refusal whose `details.reason` is `public_figure` means the model
  may refuse a well-known person: never retry that model or reword around it.
  Offer one of `details.suggested_models` (they usually allow public figures for
  the same operation), or switch to it and say so when the user asked you not to
  check in. Without suggestions, say the model doesn't allow it and ask.

Pass only settings that `list_models` reports for that model: the named tool
inputs where they exist, and any other setting in `parameters` under the Voyager
name the model's listing uses (`count`, `duration_seconds`, `images`, `end_image`),
with every media URL imported with
`import_reference` and replaced by its asset ID.
A
requested setting the model does not support (a duration, aspect ratio or audio
option) is also a question for the user, not a reason to switch models.

## Generate

1. For a plain request, call the generation tool directly; everyone expects media
   to cost credits. Call `estimate_generation` first only when the user asks what
   it will cost, gives a budget, or the job is unusually large (several clips, a
   long video, many images): then show the model and estimated credits and wait
   for their go-ahead. An estimate creates no hold and is not the final cost.
2. The generation tool waits up to 20 seconds and returns the job, finished or
   still running.
3. While the job runs, call `get_job` with its ID and `wait_seconds` (up to 25)
   again and again until it succeeds, fails or is cancelled, then show its
   outputs with the model used and the credits charged. Don't end your turn
   while a job you started is still running.

Give every generation call a fresh `client_key`. If a generation call's response
is lost, repeat it with the same parameters and the same `client_key`: Voyager
returns the original job instead of running it twice. Never resubmit with a new key
because a call timed out or a job looks slow: poll the same job with `get_job`. A job in `unknown` state is still being reconciled:
while `get_job` still suggests a poll delay, keep polling the same job. When it
suggests none, stop polling, tell the user the outcome is uncertain, and check
the same job again later. Never start a second attempt that spends credits for it. `list_jobs` finds a job when
the ID is lost. `cancel_job` is best effort: it does not promise a refund, and
credits already spent stay spent. Make no automatic retries that spend credits and no model
switches without the user's agreement; ask before any new attempt that spends credits.

## References and results

References come only from files the user attached in this conversation, HTTPS
URLs they gave you, or a local file the user named when you run on their
computer (a command-line tool with file access). Call `import_reference` for each,
and pass the returned asset IDs to generation tools. For a local file, call
`create_upload` with its name, run the `curl` command it returns with the file's
path, then call `import_reference` with the returned `upload_id`. Never guess
paths on the user's computer, and never look through the user's other files.

Imported references are kept for 7 days and generated results are downloadable
for 30 days. Use `get_asset` for a fresh download link; links expire after a few
minutes, so fetch one when the user needs it instead of pasting an old one.
`delete_asset` deletes an owned asset on request. Give results meaningful
filenames in your reply.

## Brand kits

`list_brand_kits` and `get_brand_kit` read the workspace's brand kits: palette,
typefaces and logo asset IDs. Use them when the user names a brand or asks for
on-brand work: put the palette and type into the prompt, and pass a logo asset ID
as an explicit reference only when the logo should appear. Brand kits are
read-only here; edits happen in Voyager.

## Cast

Cast cards are named, saved characters (or recurring products and props) with a
fixed description and reference images. They persist in the workspace until
deleted and are shared by every connection to the workspace. They are separate from Cast in the Voyager app's local projects.

- Before making a character, `list_cast` and `get_cast` to reuse a fitting card.
- To make one from scratch, `generate_cast` creates its reference images through
  the normal billed image flow.
- To save attached images as a card, import them, then `save_cast` with a short
  fixed description (face, hair, build, wardrobe; never the medium such as
  "cartoon") and the asset IDs. Saving existing images is not billed.
- To change a card, `save_cast` with its ID and the `expected_version` you read; on
  a version conflict, read it again and reapply the user's change.
  `add_cast_reference` and `remove_cast_reference` change its images;
  `delete_cast` deletes the card, only when the user asks.
- Pass Cast IDs to `generate_image` or `generate_video` on every shot with that
  character, including retakes. Write the action, camera and look around the
  character's name.
- Where the generation tools offer `cast_policy` (Voyager's Elements connection),
  `cast` also takes `{id, as, select: {images: [file_…]}}` to send only chosen
  photos of a saved card, and a use-once package `{as, kind, style, name,
  description, images: [{file, role}]}` for an Element that is not saved
  (import its photos first). Write `@as` in the prompt where each Element
  appears; Voyager binds it to the model's own labels and adds each
  description once, so never paste labels or descriptions yourself. When
  photos matter, `estimate_generation` with the same `cast` shows in its
  `cast_usage` what the model would receive before anything is spent.
- The result's `cast_usage` says which photos each Element sent. Relay any
  warning in plain words (for example, photos not sent because the model had
  no room, or only the description used) and offer fewer selected photos or a
  model with more room. `cast_policy: require_images` refuses instead of
  sending descriptions only; pass an estimate's `cast_usage.plan` as
  `cast_plan` to run only if the Elements still match what was estimated.

## Result cards

Results show as cards with previews and downloads where the host supports them;
otherwise give a short text summary with the job ID, filenames and download links
from `get_asset`. Don't autoplay or describe a result you haven't received.
