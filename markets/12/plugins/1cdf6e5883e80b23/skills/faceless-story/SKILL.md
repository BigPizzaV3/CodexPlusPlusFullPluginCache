---
name: faceless-story
description: Create a narrated faceless video or animated story in Clout from an idea or approved script and supported template settings
---

# Faceless story

Use for a finished narrated video whose scenes carry the story without an on-camera presenter. Read [the shared workflow](../../references/creative-workflow.md) first. This skill does not configure social autoposting, publish channels, or guarantee audience growth.

1. Establish the topic, audience, target format, tone, approximate length, and whether the user supplies the script. For factual or educational material, distinguish verified claims from storytelling; research separately when needed rather than inventing evidence.
2. Call `clout_list_templates` with `studio: "faceless"` and `clout_list_voices` when a voice choice matters. Choose only returned styles, voices, and supported duration settings.
3. Draft a tight narrative with a clear opening, progression, and ending. Match the narration to the available duration without rushing. Preserve supplied wording unless the user asks for a rewrite.
4. Summarize visual style and key scenes for review. Keep recurring characters/locations consistent and avoid cramming unrelated events into one scene.
5. Build the discovered input for `clout_generate_faceless_video`. Quote that exact operation with `clout_quote_generation`, render directly using existing credits without a separate credit approval.
6. Generate using existing credits and a UUID request ID. Poll `clout_get_faceless_video` using the returned ID through script/planning/media/render stages. Use `clout_list_faceless_videos` to find previous jobs rather than recreating a lost one.
7. When completed, obtain the actual owned media with `clout_get_download`. Check the full narration, scene order, intelligibility, format, and ending when playback is available. Do not present a planned script as a rendered video or a partial scene as the whole story.

If a job fails, keep its identity and actual error visible. Do not automatically create a new charged job. If the user changes the brief, generate only the newly requested change using existing credits.

Follow the shared direct-generation policy: no extra credit-approval step. Immediately show the returned Clout job with `clout_show_generation`; never substitute native ChatGPT image generation or another provider.
