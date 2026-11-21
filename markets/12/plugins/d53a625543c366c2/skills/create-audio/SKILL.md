---
name: create-audio
description: Create narration or a scripted multi-speaker podcast with a connected Unicorn AI Studio account, or check and retrieve a prior Unicorn audio job.
---

# Create with Unicorn

Unicorn renders approved scripts to audio. Prepare a script from the user's supplied content, then show it and the voice choices before starting a generation that consumes their Unicorn allowance. Use `list_voices` for actual IDs. Do not invent a voice, project, or saved My Voice profile.

For narration, call `generate_speech` with an approved script, a listed voice or owned cloud `voice_profile_id`, and a stable `request_id`. For a podcast, write bounded `Speaker 1:` and `Speaker 2:` turns, choose two listed studio voices, and call `create_podcast`. The assistant prepares source material and facts; Unicorn's tools render the script.

Generation is asynchronous. Preserve the returned `job_id`, use `get_generation_status` for actual progress, and call `get_audio` only after completion. `list_generations` can recover recent job IDs. An audio link expires; fetch a fresh one with `get_audio` if needed. For saved jobs that need resuming, explain the state and use `resume_generation` only when the creator requests it. If a hosted attempt is uncertain, ask the creator before setting `confirm_uncertain_remote`.

The MCP connection runs on Unicorn-managed infrastructure. Do not claim that a desktop-local voice runs inside ChatGPT or Claude, or silently substitute another voice or execution location. Voice enrollment, editing, versions, and billing remain in Unicorn Studio. The tools do not create video, clone an unconsented third-party voice, purchase credits, or publish media. For billing questions, explain that purchases are unavailable through this connection and direct the creator to Unicorn Studio; do not propose adding an in-chat purchase flow.
