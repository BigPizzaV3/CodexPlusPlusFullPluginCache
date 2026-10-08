# PPS execution and integration

Read live tools first. `pps_plan_trailer` checks the hosted renderer and validates custom timelines; `pps_render_trailer` returns a job for a finished project MP4. Follow [hosted-timeline.md](hosted-timeline.md). ChatGPT and Claude do not need a local compositor. `pps_plan_ad` / `pps_render_ad` retain the separate fixed ad grammar; read `make-an-ad` for that route.

Create an appropriate Director Mode project with one numbered shot per needed source, cast/location/object references and the requested aspect ratio. Read the project back and map real shot IDs to intended actions. Validate generation durations against live capabilities; a brief edit interval does not imply PPS can generate a source that short. Reuse suitable existing footage and score.

Establish the score, then map actual musical cues before locking the trailer edit. Batch the remaining footage and audio with pps_quote_batch, at most 12 items per batch. All paid generations require the existing member approval flow. Retain source audio by default; turn it off only if requested. Do not silently retry, upscale or finalize. Explain failed results and follow the person's choice. Translate musical/style references into descriptive qualities for generation prompts.

For interface scenes, import genuine screenshots using pps_import_image, or build a verified representation from editable primitives. Label invented UI conceptual. Preserve exact titles with compositor text layers, never generated-video text. Construct a full timeline using completed IDs and source in-points; validate with pps_plan_trailer, render with pps_render_trailer, follow pps_wait_job and deliver its Save link. Preserve the spec so the user can revise timing, graphics or text without buying replacement footage.

Existing scene-audio takes can carry ambience/effects; the trailer compositor mixes them but does not add a dedicated SFX generation provider. Narration uses voiceover IDs, music uses music IDs. Exact source lengths are checked before rendering. No arbitrary host code is uploaded.

The self-contained make-a-trailer workflow and optional pps_make_trailer prompt expose this across clients. Development connections refresh tools after new tool definitions are deployed. The downloadable pps-trailer-skill.zip contains the skill and canonical kit, including TrailerComposition. An external renderer is an alternative for requirements beyond the hosted contract, and its capability must be verified separately.
