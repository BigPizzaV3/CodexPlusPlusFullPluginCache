---
name: bandicam-narration
description: Turn a script or brief into spoken narration with Bandicam AI. Use for voiceovers, spoken introductions, or supported multi-speaker dialogue, including voice selection and delivery guidance.
---

# Bandicam AI narration

Produce spoken audio with `generate_speech`. Script drafting alone does not authorize audio generation. This workflow does not promise video assembly, subtitle timing, or a cloned voice.

1. Use the supplied script verbatim when the user asks to read it. Change wording only when they request writing or editing. For a brief, draft narration in the requested language, preserving names and facts. Treat a requested running time as a target, not a guaranteed duration; do not invent an exact duration control.
2. Call `list_models` with `category: "audio"`, then with the chosen text-to-speech model ID to get its full defaults, controls, and capabilities. Follow the control `field` names for language, speed, voice, and other options. Select `variant` verbatim from the current `generate_speech` schema. Some enums use full model IDs (currently `elevenlabs-ai-voice-generator`, `elevenlabs-ai-multivoice-generator`, and `google-ai-voice-generator`); others may use shorter aliases. The live enum determines the accepted value.
3. When the user wants to choose or hear voices, call `list_voices` with an ISO language code. Its card contains the list and free samples; use `preview_ids` for requested samples instead of generating a paid sample. Match voice IDs to a compatible voice-library model. For a different model, use its catalog voice choices rather than assuming the same voice IDs work everywhere. If no particular voice was requested, a supported default avoids an unnecessary selection question.
4. Add audio direction tags only if the current tool guidance explicitly supports them for the chosen variant. Use the returned tag list and its placement rules. Unsupported variants may speak bracketed tags literally, so omit them there. Keep delivery directions separate from the script when the user asks for an exact reading.
5. For explicitly requested multi-speaker audio, select a supported dialogue variant. Follow the tool's format, such as `A: ...` and `B: ...` lines with `options.speakers` entries containing `id` and compatible `voice_id` values. Do not convert a one-voice request into dialogue.
6. For a price-first request or budget ceiling, call `quote_job` with the full model ID, voice/language options, and the exact script (including supported tags or dialogue formatting) in `options.prompt`. This tool has no top-level `prompt`; omitting the script produces an unrelated default estimate. Re-quote changes. Stop for estimates alone, a failed quote, insufficient credits, or a quote above budget.
7. For an authorized audio request, call `generate_speech` once without a separate quote unless requested or needed for a budget, passing the same script as its top-level `prompt` and the voice settings in `options` (remove the quote-only duplicate `options.prompt`). Report returned credit information rather than guessing it.

## Results and recovery

- Let displayed cards track progress. Use `wait_for_job` for dependent steps, requested completion checks, or clients without cards. Keep polling the same ID through `running`, `processing`, or `deadline_reached`, within host limits; disclose unfinished work.
- Never resubmit an uncertain job. For `recovery_required`, call `resume_generation` with its ID. Without an ID, disclose uncertainty. Stop on failure or insufficient credits without purchase suggestions.
- `credits_quoted` is an estimate; `reserved` is not consumed. Report final `credits_cost` with `credit_status` for usage/refunds.
- Do not duplicate cards or call `show_creations` for new jobs. Otherwise use returned previews/`view_urls`; refresh expired links with `get_creation`. Claim content quality only after inspection, not from `completed` status alone.
