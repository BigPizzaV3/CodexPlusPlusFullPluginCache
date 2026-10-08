# Visual AI and xKiro
Current path: `Cài đặt` → `API`.
Provider cards currently include:
- `Visual AI` — primary image provider.
- `xKiro AI` — B2 idea/script content.
- `Gemini Backup` — content fallback.
- `OpenAI Backup` — content fallback.
For Visual AI, distinguish endpoint/authentication, model metadata, provider compatibility, and real image-generation capability. Audited statuses include `NOT_CONFIGURED`, `CHECKING`, `READY`, `AUTH_FAILED`, `ENDPOINT_UNREACHABLE`, `MODEL_NOT_FOUND`, `MODEL_UNSUPPORTED`, `PROVIDER_UNSUPPORTED`, `RATE_LIMITED`, `NETWORK_ERROR`, `UNKNOWN_ERROR`, `LIVE`, and `INFERENCE_FAILED`.
Customer-safe checks:
1. Select the exact provider/profile shown in `Visual AI`.
2. Verify the Base URL and model name without asking the user to paste a secret into chat.
3. Use `Kiểm tra kết nối` for connectivity; explain that a separate capability test may consume provider quota when the UI warns so.
4. `LIVE` means compatible metadata without proven image inference; it is not the same as `READY`.
5. If a fallback is configured, it must be a different provider from the primary.
For xKiro, use the exact fields `Kích hoạt`, `API Key`, `Base URL`, `Model Ý tưởng`, `Model Kịch bản`, and `Model Reviewer`, then `Kiểm tra kết nối` and `Lưu cài đặt`.

## Draft versus active configuration

In the Visual AI settings page, provider/mode/model edits are draft changes until the shared `Lưu cấu hình` action succeeds. `Có thay đổi chưa lưu` means the visible selection differs from the persisted active configuration; selecting a value alone does not switch the runtime. After saving, the active configuration is persisted and remains visible after restarting VeTayStudio. If the save fails, keep using the last persisted active configuration and report the exact message instead of assuming the draft is active.
