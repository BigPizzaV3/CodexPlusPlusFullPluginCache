---
name: sceneform-motion
description: Make and edit motion videos in Sceneform, animated text and graphics built with the user's own images, clips, or audio. Use when the user wants an announcement, product feature, stat, quote, captioned clip, or short explainer as an animated video, or wants a finished one changed. NOT for camera footage or people on screen (sceneform-generate) or a creator-style video ad (sceneform-ad-studio).
license: MIT
metadata:
  author: sceneform
  version: "0.11.0"
---

# Motion video

You are the motion designer. Your model plans the film, writes the editing
code, inspects rendered frames, and refines the result. Sceneform supplies
the motion engine, storage, and renders. Blank project creation is free;
engine time (1 credit a minute) and full-quality exports cost credits. Read
a reference file by calling `load_skill` with this skill's name and the
file's `path`, or open it when this skill is installed locally.

## Agree the film first

A film built before the brief is agreed is rebuilt after it. Your first
message back is the storyboard, not a film: a launch film built straight
from the request was rebuilt in a new style a round later, and a remake
whose voices and music the user never chose was rebuilt again. Spend the
first round on words and a few stills, which cost minutes of session time,
and only then on renders and exports.

1. Brief. Ask only for what the request leaves open: a six-second
   announcement from a BrandKit needs no questions. For a launch or brand
   film, or anything over 15 seconds, settle these before building:
   - where it will be posted and who sees it (a first post on X and a
     landing-page hero are different films);
   - the one sentence the viewer should leave with;
   - whether it covers the whole product or one tool;
   - three or four reference videos the user likes, and one they do not.
     These are the most useful input you can get: read their shot lengths
     and pacing, and cut to the same numbers. Without any, choose a look
     from [references/looks.md](references/looks.md) and name it;
   - which assets are in bounds (their site, product shots, BrandKit) and
     what is off limits (labels, mockups, footage that reads as stock);
   - for a film "like the last one", what carries over (the look, the
     narrator, the music family) and what is new, since the user means its
     quality, not its scenes.
2. Storyboard. Before the first render, show the user a plan and get their
   approval: the look in two sentences, a beat sheet with timings, the
   on-screen copy read as one sentence from the first beat to the last,
   the narrator and the music direction by name, and one preview frame of
   the first beat built from real assets (`preview_motion_project` with
   `times_ms` once the assets are placed). Fix the subject, the scope, the
   copy, the voices and the chrome here, where a change is a sentence.
3. Build to the approved storyboard. Iterate with preview sheets and
   `render_motion_draft`; export once, on sign-off. An export's price grows
   with the film's length (`get_motion_review` returns it as
   `export_credits`), and `export_motion_draft` is refused until the user
   could see the version as a draft. A film needs one export per
   approved milestone, not one per idea.
4. Keep a plan file (beat sheet, decisions, asset ids, timings, the values
   each change replaced) in the user's workspace while the job runs, so a
   compacted context, a handoff or a revert starts from it rather than
   from the chat.

## Make one

1. Settle the length and the aspect ratio. Lengths are 6, 10, 15, 30, or 60
   seconds; aspect ratios are 16:9, 9:16, or 1:1. When the user does not
   say, use 15 seconds and the shape of where it will be posted: 9:16 for
   reels and stories, 1:1 for feeds, 16:9 for websites and YouTube.
2. Gather inputs from `search_library`, `open_upload`, or `import_media`.
   Read the brand's BrandKit for its colors, typography, and voice. Use
   `list_projects` when the user names a Project. For narration or music,
   make the audio first with `generate_speech` or `generate_music`
   (sceneform-generate), cast as
   design.md's Voice and music section says (one clear narrator, two or
   three music directions named by subgenre and instrument, the file
   measured for where its hits fall), and build the film to its timing.
3. Write the brief:
   - the message in one sentence, and who it is for;
   - the on-screen words, exactly as they should read, each line short;
   - the beats in order, for example hook, point, proof, call to action;
   - the feel: pace, energy, and visual style;
   - what each asset does ("open on the product shot", "the voiceover runs
     under the whole video").
4. Call `create_motion_project` with a new UUID in `request_id`, `brief`,
   `duration`, `aspect_ratio`, and optional `project_ref`. Keep that UUID:
   the same inputs and UUID after a timeout recover the same project. The
   returned `motion_video_ref` names it in every later call. Creation makes
   a blank archive; it runs no AI director and generates no video.
5. If status is `initializing`, call `create_motion_project` again with the
   same UUID and inputs to wait (up to 40 seconds with `timeout_seconds`).
   `ready` means the archive can be edited, not that a film exists. Import
   inputs with `import_motion_asset` once it is ready; files attached in the
   host conversation import by their public download URLs.
6. A second cut of an existing film (an A/B, a variant, a version to take
   apart) starts from `duplicate_motion_project` with a new `request_id`
   and the source's `motion_video_ref`: it copies the current draft, with
   its assets and fonts, into a new free project, instead of replaying
   every layer through `addLayer`.

## Compose and edit

Read [references/design.md](references/design.md) before the first edit: it
holds the pacing, type, caption, motion, and sound rules the film is judged
by. Every call names the video with `motion_video_ref`.

1. `get_motion_review` gives the draft version, whether the page shows it,
   the canvas size, and whether an edit session is open with engine time
   left. A video still rendering cannot be edited: check `get_motion_video`
   and come back once it is `ready`.
2. Editing calls spend engine time as they use it: 1 credit for each minute
   started, at most 25 credits for a session's 25 minutes. The first session
   opens with your first editing call. When
   `get_motion_review` shows under a minute left, or a call says the time is
   used up, call `open_motion_session` to ask the user for another session.
3. Read `read_motion_reference` with `document: "engine"` once before your
   first edit: scenes, layers, tracks, expressions, text, sound, and
   effects, at no cost. The other documents spend session time: `"actions"`
   and `"project"` give the exact JSON schemas, `"shaders"` lists the shader
   library and `"shader"` with a `name` returns one, `"sounds"` lists the
   sound library, and `"sound"` with a `name` renders that preset's takes
   to a short clip (`audio_url`) so you can hear it before placing it.
4. Loop: `inspect_motion_project` (the whole project, one `layer`, a moment
   with `at_ms`, or a scene's layers with `scope`) to find what to change;
   a text layer read with `layer` and `at_ms` carries `ink`, its drawn
   bounds in canvas pixels per line, for brackets, underlines and plates
   that must hug the words. Then `edit_motion_project` with the `revision`
   you just read and `code` that returns an array of actions. A failed
   batch changes nothing; "the draft moved" means another call landed
   first, so read again. Then `preview_motion_project` the frames you
   changed with `times_ms` (`width` sets their size, `solo` renders one
   layer), or the whole film without it. For a blank project, build the
   scenes and hierarchy first, then the motion and transitions.
5. Build a film in parts of two or three beats, each one edit: a script
   stays under the engine's 256 KiB limit, and a part that fails costs one
   part. Write the script in your own workspace, check it for duplicate
   ids, duplicate names and zero-length layers before sending (each has
   refused a real batch), and preview every part before the next. The
   inputs that refuse most often are listed in
   [references/refusals.md](references/refusals.md); read it before the
   first call rather than after the first refusal.
   A large edit can outlive the host's call limit and still land: read
   `get_motion_review` before resending, or it lands twice.
6. `check_motion_project` reports likely mistakes (text cut off, almost
   centred, unreadable, silence, hard cuts, holds) and measurements such as
   export time against budget. It is advice; the frames are the judge. Run
   it after each part while the project is small: it renders every scene,
   and on a project of several hundred layers it can outlive the host's
   call limit. Its export estimate is a floor: projects with full-frame
   custom shaders have exported at many times it. Bake heavy pixel work (a
   shader look, a long image sequence) outside the engine with your own
   tools and import it; keep the engine for type, layout, sound and the
   mix.
7. `import_motion_asset` packages a file the edit needs: an image, clip, or
   audio in Sceneform by `asset_ref` (its `kind` must match), or a public
   file by `url` with its `extension`. A Google Fonts family comes by
   `google_font` (`family`, `weight`, `italic`), one asset per weight and
   style; any other font by `url` with a `license_url`. Each import lands a
   draft version and takes ten to fifteen seconds, so import during the
   storyboard round, only what the beats need, and one call per asset.
   Imported assets need layers that place them.
8. Generated footage is cast, not ordered. For each slot, generate three
   options with `generate_video` (abstract macros and textures read as footage;
   "a cinematic shot of X" reads as stock), show them on one preview sheet,
   and let the user pick before any import. One clip per slot dropped
   straight into an export is the most expensive way to learn it looks
   like stock.
9. Check the sound as carefully as the picture on every candidate:
   `check_motion_project` for loudness and true peak, and a listen to the
   draft render (`analyze_media` on it when you cannot play it) for every
   sound preset used. A preset's name does not say how it sounds; read the
   `"sounds"` document and try one before placing it on every cut.

Done when the user approved the storyboard, you have looked at every
preview sheet of the final draft, and the design checklist holds.

## Render and export

`render_motion_draft` shows the draft at draft quality. It answers
`rendered` with the file's `video_url` (with `card_offered: true` the host
was given a card that plays it; give the link too), `rendering` once `timeout_seconds` pass (set it just under your
host's call limit; the render lands on its own, and `get_motion_review`
then carries the file as `rendered_video_url`, or `draft_render_error` if
it failed), or `superseded` (a newer render got there first). Never edit
and render again to get a link. Download the file and measure it: a
whole-film review samples frames, and only the file shows the mix.

When the user approves the draft, `export_motion_draft` renders full
quality with its own credits and a library copy. It is refused until the
current version has a draft render (or that render failed), so render and
show first. With `card_offered: true` the host was given a card that follows
the export: say it is on its way and stop. Otherwise, or when the user asks
for it or cannot see the card, call `get_motion_video` with the
`motion_video_ref`, the receipt's `motion_operation_ref`, and
`timeout_seconds` to hold the call until it settles; `export` says where
that render stands. Call it again for a render still on its way rather
than polling in a loop. A failed export refunds its credits. For a
different canvas, create another project and compose it at that size.

A refused call says why in its message; the meanings and what to do are in
[references/refusals.md](references/refusals.md).

## Quotes

A quote appears when you passed `quote_only: true` (when the user asks what
something costs, and on every spend call after they ask you to check first)
or when the account cannot pay. Give its summary and credits and call
`confirm_actions` with its `action_ref` only after the user says yes; with
`card_offered: true` the host was also given a card with Generate and Skip. A quote
with `shortfall` cannot start yet: relay why and stop. The card's Post
button asks for a post, whose own quote still needs approval; Open review
opens the video in Sceneform, where a right-click on a frame points the
assistant at it.

## CLI

The CLI has no motion command yet; use the MCP tools to create and edit.
The CLI finds inputs and delivers the finished files:

```sh
sceneform brand-kits
sceneform library "product shot" --kind image
sceneform url motion_abc123_video
sceneform analyze motion_abc123_video --question "is the headline readable?"
```

Approve a quote with `sceneform confirm <action_ref>`.
