# Voice Runtime
Current path: `Cài đặt` → `Cài đặt hệ thống` → `Model & Runtime`.
The page separates:
- `Runtime`
- `OmniVoice`
- `Whisper`
It includes `Tải Model Giọng nói`, `Tải Model Whisper`, and `Repair Runtime`.
Do not treat one missing component as proof that every voice component is broken.
Customer-safe sequence:
1. Read the `Runtime`, `OmniVoice`, and `Whisper` status lines separately.
2. If the runtime is incomplete or the code is `VOICE_RUNTIME_NOT_READY`, use `Repair Runtime` first.
3. Download only the missing model with its matching button.
4. Wait for the background operation to finish; do not close the application during an active repair/download.
5. Recheck readiness after completion and restart the app once if the persisted status is unclear.

Managed runtime and model locations are auto-detected on later launches. Runtime, OmniVoice, and Whisper readiness are persisted and evaluated independently, so a restart should rediscover completed managed installs without downloading them again. If one component remains unavailable after restart, troubleshoot that component instead of reinstalling everything.

The runtime/model manager intentionally rejects temporary/test model paths in production. Do not instruct customers to point production settings at `%TEMP%`, pytest folders, or developer caches.
