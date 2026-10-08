---
name: pps-trailer
description: Create cinematic movie-style trailers or product demo hype videos using PPS footage, music, and audio with agent-directed motion graphics. Use for story teasers, product launches, and feature reveals; adapt to the rendering tools actually available.
---

# PPS Trailer

Direct a trailer as one audiovisual composition: a compelling hook, a developing question, escalating reveals, memorable animated titles, and a satisfying payoff. The music score is the structural foundation: plan its progression, then coordinate footage, speech, typography, and transitions around its actual phrases and accents. Aim for attention, rewatching, and sharing; never promise virality. The subject is the hero. Motion-design virtuosity must amplify its story rather than become an unrelated showreel.

The server exposes this direction through `pps_get_workflow` with workflow `make-a-trailer`. When available, read that recipe for current execution details and workspace rendering availability, carrying existing answers forward.

These instructions are portable between agents with the PPS MCP. Tool prefixes may differ; use the exposed PPS tool descriptions and schemas. Reading this skill for explanation, review, or editing does not authorize creating a trailer.

## Establish the brief and rendering path

Offer two creative modes when the user has not already chosen or clearly described one: **Cinematic trailer** (story, characters, stakes, anticipation) or **Product demo / hype trailer** (a strong hook, real product demonstrations, bold motion graphics, and music-driven feature reveals). Ask which they want before detailed intake. Infer an explicit product-hype or movie-trailer request without asking again. Creative mode and rendering capability are separate choices.

Read [references/trailer-modes.md](references/trailer-modes.md) for the chosen mode. Product hype should feel like a tightly directed modern music video about the product: catchy, upbeat, cinematic music drives the edit; risers prepare major transitions and impacts punctuate reveals. Preserve moments where viewers can understand the product. Cinematic mode builds story and score together toward a climax and payoff, using stillness, dialogue, and suspense to make the final release stronger. Read [references/cinematic-score.md](references/cinematic-score.md) when directing that mode.

Use what the person already supplied. Ask for missing essentials one question at a time: what is being teased and for whom; desired feeling or reveal; duration and destination; usable footage/cast and mandatory title, date, or CTA. Use reference format and destination to inform duration and shape; the supplied product-hype references are landscape films around a minute long. Default to a 15-second vertical teaser only when they delegate those choices and no stronger context exists. Read the saved PPS brand kit before asking for branding; change or save it only as requested.

References are helpful, not a prerequisite. When provided, inspect accessible video and audio, and record timestamps for the opening hook, title entrances, cuts, acceleration, music changes, pause, and final reveal. Translate those mechanics into a new visual language. If only a thumbnail or inaccessible link is available, say what was actually inspected; do not invent a timing analysis.

Read current PPS capabilities and call `pps_plan_trailer` without a spec BEFORE pricing. PPS hosts the trailer compositor: ChatGPT and Claude do not need their own Node runtime or local renderer.

- **Hosted trailer (preferred):** `pps_plan_trailer` checks availability and validates a supplied timeline. `pps_render_trailer` renders it to a project MP4; follow `pps_wait_job`. Supports 5–60 seconds at 30 fps, free cut points, layered text/shapes/screenshots/video/cursors, pose keyframes, reveals, crossfades, source trims and audio envelopes. Read [references/hosted-timeline.md](references/hosted-timeline.md).
- **PPS ad:** The existing `make-an-ad` route remains available for its fixed ad grammar.
- **External composition:** Only needed for a requirement beyond the hosted schema or when the hosted renderer is unavailable. Verify that environment before spending. Do not assume that a chat without a local renderer cannot make a custom trailer.

If no suitable route is available, explain the verified limitation and offer a supported treatment before spending.

## Direct the trailer before generating

Write one central promise and one emotional progression. Avoid a succession of interchangeable epic shots. Choose a visual motif related to the subject (a fracture, a threshold, a pulse, a gathering light) that recurs across footage and titles.

Build a timed treatment showing each interval's footage/action, exact title copy, motion behavior, transition, music cue, and voice/dialogue. Mark timings as provisional until an actual score is available. Keep generation source durations separate from edit durations. Use a few legible title phrases; avoid dense explanation. Include at least one contrast in scale, speed, density, or sound. Open with a striking action or unresolved image while reserving the main payoff for the ending; a hook need not be the largest spectacle. A seamless loop is useful for social when it fits the message.

For each generated shot specify subject/action, foreground and background, camera movement, light/material palette, a concrete change within the shot, and the final composition that motivates the next cut. Carry exact cast names and approved references consistently. Match the PPS ad prompt rules when using that renderer; custom cinematic trailers may use restrained movement, held tension, profiles, or environmental shots when creatively justified.

Design music in phases, describing instruments, mood, tempo, and development rather than named artists or franchises. Specify an identifiable motif, escalation, room for important speech, the intended climax, and a resolving tail. Sparse voiceover should add stakes or meaning without repeating every title. Use verified PPS voices and supported audio tags. Use dialogue generation for multiple speakers where supported. Do not invent a dedicated PPS sound-effects endpoint: integrated percussion/impacts may be requested in music, but separately timed effects require an available source and mixer.

Show the treatment and chosen production path before pricing. Ask whether to change anything; reuse existing authorization when the person explicitly delegated creative choices.

## Produce, assemble, and inspect

Read [references/pps-production.md](references/pps-production.md) for PPS-specific execution and limitations. Quote only after the treatment and source mapping are coherent. Respect the PPS member approval flow; a request to make a trailer is not approval of a quoted credit charge.

For hosted trailer rendering, establish the usable score before locking shot lengths and generating duration-dependent footage. Reuse an approved track when available; otherwise quote/generate the score through PPS's approval flow, inspect its actual phrases and accents, and refine the treatment before quoting the remaining assets. Batch independent remaining assets where supported. If the user already has footage, edit it around the score without unnecessary regeneration. The native PPS ad route retains its documented batching and fixed grammar; do not claim it offers the same timing freedom.

Use clean PPS footage without generated title text; compose exact copy in the graphics layer. Maintain an asset manifest with beat, source ID, generation duration, chosen in/out points, audio ID, and render path. Time motion to the actual returned music and speech, not assumed generated timestamps. If a renderer cannot perform a planned effect, revise the treatment and disclose material changes before further spending.

Review the finished artifact visually and audibly when tools permit: title spelling and legibility at phone size, hook timing, purposeful cuts, continuity, correct branding/CTA, sync and voice clarity, intentional ending, and expected aspect ratio/duration. For custom animation inspect representative transition frames as well as title holds; check for unintended blank frames or clipped text. If video/audio playback is unavailable, state that limitation; metadata checks alone do not establish creative quality.

Deliver the MP4 through its supported Save/download link, and give a short repeatable creative preset. For hosted rendering also preserve the timeline spec; for external rendering preserve editable source when available. Distinguish a finished trailer from a draft, storyboard, or render-ready plan. Retries, replacement generations, finalization, and upscaling follow the current PPS consent rules; explain failures and let the person choose the next paid attempt.
