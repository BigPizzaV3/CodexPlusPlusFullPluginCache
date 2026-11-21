# unsketch for ChatGPT

MCP endpoint: `https://unsketch.io/mcp`. Transport: Streamable HTTP. Anonymous template/model search and local editing; OAuth required for account data, generation and temporary export uploads.

## Connect

Add the MCP URL in ChatGPT's plugin development connection flow, then refresh tools after server changes. OAuth uses the existing unsketch login, CIMD, PKCE S256 and explicit consent. No client secret is required. The exact resource audience is `https://unsketch.io/mcp`.

For package distribution, ZIP the contents of this directory with `plugin.json` and `mcp.json` at the archive root. Public directory listing requires OpenAI's review and publication flow. Uploading the package is not evidence of approval.

## Behavior

- Templates and model consultation are free. Model metadata comes from the live catalog.
- Image and video generation uses the connected account's existing balance. `prepare_image` and `prepare_video` make quotes without generating. Only the widget's priced confirmation button invokes the corresponding app-only `generate_image` or `generate_video` tool. Quotes restore their inputs in the widget and can be refreshed after expiry.
- Each quote has one Studio request ID. Retries use that same request ID. Results remain in the normal Studio conversation.
- The player uses a one-hour, per-media capability URL. URLs stay in widget metadata, not model-visible results. Ownership and account status are checked on every media request.
- Editing runs locally. Users import video/images, trim, reorder, add timed SRT/VTT captions or fixed text, mute and export MP4 (H.264/AAC) or WebM at up to 1920 pixels on the longest side. Recording runs in real time; keep the card open. Projects are stored in the browser's IndexedDB and can be explicitly deleted. The model receives clip names, IDs, durations and edit settings, not the local file bytes.
- Hosts with file-download support save the exported MP4/WebM directly. Other hosts show an explicit upload-and-save button: connect a free unsketch account, upload only the rendered result (up to 32 MiB), and download through a one-hour link. Files expire through a one-day storage lifecycle. Up to six export links per account per hour; no credits are charged. Original editor source files stay local except when the user explicitly selects automatic transcription.
- A new card can restore the exact local project ID in the same browser. Other devices need the original files again.
- Images and videos run in the widget. Image outputs can be revised or animated using their exact owned conversation/message/index. Source-video models accept a user-selected MP4/WebM/MOV through a single-use upload capability (100 MB, 30 seconds, 20 preparations/day); Studio validates and stores the video using its existing source-upload path. Some provider/model combinations remain unavailable and return the normal Studio error before charging.
- History lists conversations and paginates their image/video outputs. Output saving preserves the actual MIME type and file extension.
- Source files added to the local editor stay local except for the audio range the user explicitly sends for automatic subtitles. Images added for AI generation and source videos are uploaded only after the user selects them. Source videos follow Studio's existing 30-day upload lifecycle.
- The plugin does not sell digital credits, launch checkout or include a ChatGPT-specific surcharge.

- `import_chat_images` accepts ChatGPT file params (host-issued HTTPS capabilities only, no redirects, bounded 8 MiB images). The widget can also select existing ChatGPT images when its host exposes the optional file picker. Reference thumbnails use owner-bound capability URLs.
- The home screen offers product ads, image-to-video and captioned-video workflows. The package includes three corresponding skills. Skills require updating/importing the plugin package; deploying the server does not update installed skill snapshots.
- Automatic subtitles send a mono 16 kHz WAV of the selected clip range to fal Whisper only after the explicit button. Up to 60 seconds and six new clips per account per day are included, with a global 120/day cap. Audio uses a one-hour capability URL and is deleted after a terminal result; the existing one-day export storage lifecycle is the fallback. Hash-bound jobs recover without duplicate submission. A confirmed legacy unsupported-data-URL failure can retry once through the corrected HTTPS transport. Captions remain editable; transcription is not guaranteed accurate.

## Verification

Run from the repository root:

```sh
node tools/build-chatgpt-plugin.mjs
npm run studio:typecheck
node tools/test-chatgpt-plugin.mjs
node tools/test-chatgpt-exports.mjs
node tools/test-chatgpt-generation.mjs
node tools/test-chatgpt-uploads.mjs
node tools/test-chatgpt-production-flows.mjs
node tools/test-chatgpt-transcription-media.mjs
node tools/verify-chatgpt-plugin.mjs
```

The browser check uses the existing Antigravity Chrome on port 9222 and a mock host. It makes no paid provider calls. Production OAuth, the actual ChatGPT host and live generation are separate checks; see the release report for their status.

## Review preparation

Before submitting publicly, supply an authorized reviewer account and a real walkthrough recording, verify the domain challenge issued by the developer dashboard, and confirm the publisher information. Credentials must never be included in this ZIP. Do not create or impersonate reviewer credentials automatically.

## Installed development release

The existing private ChatGPT connection was updated to 1.2.4 with all three skills. `node tools/package-chatgpt-plugin.mjs` builds both the portable archive and an archive preserving that development connection’s registered identity. The latter references its existing canonical app and omits a second MCP declaration. Public directory publication remains separate.
