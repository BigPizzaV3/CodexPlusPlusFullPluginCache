# Whisper
Whisper is used for subtitle timing/transcription support and is separate from OmniVoice speech synthesis.
Current path: `Cài đặt` → `Cài đặt hệ thống` → `Model & Runtime`. The Whisper area includes `Tải Model Whisper` and uses a Faster-Whisper model path.
Audited statuses include:
- `READY` / `● Sẵn sàng`
- `MODEL_MISSING` / `⚠ Chưa cấu hình model`
- `MODEL_INCOMPATIBLE` / `✕ Model không tương thích`
- `WHISPER_RUNTIME_UNAVAILABLE` / `✕ Thiếu Whisper Runtime`
- `RUNTIME_CHECK_PENDING` / `○ Đang kiểm tra Runtime…`
Customer-safe sequence:
1. Read the exact Whisper status and tooltip/message.
2. If the runtime is unavailable, repair the Voice Runtime first.
3. If the model is missing, use `Tải Model Whisper`.
4. If incompatible, do not rename files or substitute an arbitrary model; redownload through the managed action or escalate.
5. Validate again after the operation completes.
A Whisper problem does not automatically mean OmniVoice or a Voice Profile is broken.
