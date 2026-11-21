# MCP errors

Use these recovery rules for YouCam MCP failures.

- **Authentication required or expired:** Ask the user to connect or reconnect
  YouCam. Never request, print, or expose an access token. Retry only after
  authentication succeeds.
- **Insufficient credits** (`error_type=insufficient_credit_error`,
  `error_code=VL-UN-NA-07`, or upstream type
  `Validation.Internal.InsufficientCredit`): Do not retry the failed request.
  Tell the user they have reached their usage limit and must check their plan
  or top up credits before continuing. Do not mislabel this as an
  authentication, upload, or network error.
- **Attachment upload failed:** Ask the user to reattach the affected image.
  Retry `upload-file` once only when the failure is clearly transient.
- **Invalid tool arguments:** Correct the MCP arguments locally. Do not expose
  internal field names unless the user must change an attachment.
- **Processing still running:** This is not an error. End the assistant turn
  and let the App retrieve the result. Never submit the request again.
- **Widget reports a terminal processing error:** Explain the reported failure.
  Do not start a duplicate generation or request another upload without the
  user's approval.
- **Upstream or network failure:** Retry one clearly transient failure. If it
  persists, state that YouCam is unavailable and offer a later retry or clearly
  labeled general guidance.
- **Invalid result resource:** Preserve the textual specialist answer and
  explain that the generated file could not be opened.
