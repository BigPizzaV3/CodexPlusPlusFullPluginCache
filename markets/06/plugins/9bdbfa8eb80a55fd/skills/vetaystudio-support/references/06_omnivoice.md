# OmniVoice
OmniVoice guidance must separate four things:
1. Voice Runtime — Python/native packages required to run voice workers.
2. OmniVoice model — the managed model snapshot used for synthesis.
3. Voice Profile — customer voice reference/profile metadata.
4. Voice prompt — the validated `voice_prompt.pt` generated for a compatible profile/model revision.
Current customer path for runtime/model readiness is `Cài đặt` → `Cài đặt hệ thống` → `Model & Runtime`.
Customer-safe checks:
- If Runtime is not ready, use `Repair Runtime` before model download.
- If OmniVoice is missing, use `Tải Model Giọng nói` and wait for validation.
- If the model is ready but synthesis fails, inspect the selected Voice Profile and exact error code.
- `VOICE_PROFILE_REQUIRED`, `VOICE_PROMPT_NOT_FOUND`, `VOICE_PROMPT_INCOMPATIBLE`, and `VOICE_PROMPT_INVALID` are profile/prompt issues, not proof that Whisper is broken.
- Do not move, rename, or delete managed model directories as a first-line fix.
Escalate persistent native/runtime failures with the exact status, app version, and screenshot.
