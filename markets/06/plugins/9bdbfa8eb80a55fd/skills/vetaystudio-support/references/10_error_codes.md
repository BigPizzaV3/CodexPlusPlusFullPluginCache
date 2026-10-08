# Audited error-code catalog

Only use a meaning below when the exact code matches. For any other code, state that it is not in the audited catalog and request the complete error text/screenshot.

| Code | Subsystem | Meaning and customer-safe action |
|---|---|---|
| `VOICE_RUNTIME_NOT_READY` | Voice Runtime | Runtime is incomplete. Open `Cài đặt` → `Cài đặt hệ thống` → `Model & Runtime`, use `Repair Runtime`, then retry the model action. |
| `VOICE_MODEL_ROOT_UNAVAILABLE` | Managed voice models | The managed model root cannot be used. Check free disk space and Windows access; do not redirect it to a temporary/test folder. |
| `VOICE_MODEL_INSUFFICIENT_DISK_SPACE` | Managed voice models | Not enough disk space for staged download/validation. Free space safely, then retry. |
| `VOICE_MODEL_DOWNLOAD_CANCELLED` | Managed voice models | Download was cancelled. Retry once when network and disk are stable. |
| `VOICE_MODEL_DOWNLOAD_FAILED` | Managed voice models | Managed download or validation failed. Capture the exact message and model name, then retry once or escalate. |
| `WHISPER_RUNTIME_UNAVAILABLE` | Whisper runtime | Faster-Whisper runtime is unavailable. Repair Runtime before downloading/validating the Whisper model. |
| `MODEL_MISSING` | Whisper model | Whisper model is not configured. Use `Tải Model Whisper`. |
| `MODEL_INCOMPATIBLE` | Whisper model | Selected Whisper model does not satisfy the current contract. Use the managed download or escalate. |
| `VOICE_PROFILE_REQUIRED` | Voice Profile | No usable Voice Profile is selected. Select or create the intended profile. |
| `VOICE_PROMPT_NOT_FOUND` | Voice Profile | The profile has no validated voice prompt. Complete the current profile preparation flow. |
| `VOICE_PROMPT_INCOMPATIBLE` | Voice Profile | The voice prompt belongs to another OmniVoice revision. Revalidate/regenerate through the supported UI. |
| `VOICE_PROMPT_INVALID` | Voice Profile | Profile/prompt metadata or integrity validation failed. Do not modify the file manually; escalate if recreation fails. |
| `AUTH_FAILED` | Visual AI/provider | Credential or permission check failed. Verify the configured credential privately and provider permissions. |
| `MODEL_NOT_FOUND` | Visual AI/provider | The configured model ID was not found. Select a discovered/current supported model. |
| `MODEL_UNSUPPORTED` | Visual AI/provider | The model exists but is not supported for the requested image workflow. Choose another supported model. |
| `PROVIDER_UNSUPPORTED` | Visual AI/provider | The configured provider does not satisfy the current workflow contract. Use a supported provider/profile. |
| `RATE_LIMITED` | Visual AI/provider | Provider quota/rate limit was reached. Wait or check the provider account privately. |
| `ENDPOINT_UNREACHABLE` | Visual AI/provider | Endpoint could not be reached. Check network, proxy, and Base URL. |
| `NETWORK_ERROR` | Visual AI/provider | Network failure occurred. Retry after connectivity is stable. |
| `INFERENCE_FAILED` | Visual AI/provider | Provider/model did not return a valid image. Preserve the exact reason and use configured fallback if available. |
| `ACCOUNT_LOGIN_REQUIRED` | License/account | The current License is account-owned and requires the supported sign-in flow. |
| `ACTIVATION_REQUIRED` | License | This device/session requires License activation. Use the screen shown by the installed version. |
| `DEVICE_MISMATCH` | License | Device identity does not match the bound record. Do not bypass; escalate. |
| `DEVICE_LIMIT_REACHED` | License | Allowed device count is exhausted. Administrative support is required. |
