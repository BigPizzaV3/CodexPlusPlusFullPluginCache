---
name: creative-reference-watchlist
description: Build a YouTube reference watchlist from a creative brief, with a distinct reference purpose for each video and viewing questions that turn user-reported reactions into creative directions. Use for documentary, filmmaking, animation, presentation, or other creative-project inspiration. Select from metadata without claiming to inspect visual style. Do not use for automatic scene analysis, image generation, or a general entertainment recommendation.
---

# Creative Reference Watchlist

## Inputs

Establish the project, audience, intended effect, and decisions the user needs
references to inform. Use any stated constraints or existing reference links.
Ask one focused question if the brief lacks a clear project or creative purpose.
Default to three reference needs rather than a large inspiration catalog.

## Workflow

1. Break the brief into distinct reference needs, such as an opening structure,
   interview approach, or pacing. Give each need a decision it should help the
   user make; avoid several videos serving the same purpose without explanation.
2. Call `search-videos` with `{ query, reason? }` for needs without supplied
   references. Read `results` and shortlist candidates based on titles,
   descriptions, channels, and publication dates. Deduplicate IDs. Explain what
   the metadata suggests and what the user still needs to assess while watching.
   Refine an unsuitable search once; leave a need open if no plausible fit appears.
3. Return a compact watchlist containing the reference need, selected title,
   channel, returned `watchUrl`, selection rationale, and two targeted viewing
   questions. Phrase questions as prompts to inspect the work, not assertions
   that it contains a particular shot, palette, editing rhythm, or performance.
4. Call `display-video` with `{ videoId, reason? }` for the reference the user
   wants to view, or the first selection when they ask to begin. Extract an ID
   from a supplied YouTube URL. Accept only `status: ready` with a video; explain
   `invalid_video_id`, `video_not_found`, or a tool error and offer a returned
   alternative. Open further references individually when requested.
5. Invite the user to report what they liked, what they would avoid, and why.
   Wait for these reactions before describing the reference's actual execution.
   Keep metadata, user observations, and assistant suggestions distinguishable.
6. Translate the reported reactions into two or three creative directions for
   the user's project. For each direction, name the underlying principle,
   a possible original application, and the next decision or small experiment.
   Attribute the reference to the user's account and keep unviewed aspects open.

## Deliverable

Provide a purposeful reference watchlist and viewing questions. After the user
shares reactions, provide a short creative-direction brief tied to their project
and supported by those reactions.

## Boundaries

- Work through ordinary playback and chat. Do not require tags, observation
  logs, transcripts, private widget state, or automatic viewing detection.
- Do not infer visual or audio execution from thumbnails, titles, or popularity.
  Do not claim the model watched scenes or measured pacing.
- Keep the watchlist and brief in chat; do not promise a saved mood board,
  downloadable clips, a YouTube playlist, or editing and generation features.
- Use only the registered tool arguments. Express preferences through `query`
  without inventing style filters. If the user explicitly requests text only
  or no video display, call neither tool and organize their supplied references.
