# TranscriptLab for ChatGPT

This private Agent Plugin connects ChatGPT to the TranscriptLab MCP server at
`https://api.transcriptlab.dev/mcp`.

## Sign in

Connect through the Clerk OAuth prompt and sign in with your TranscriptLab account using the
sign-in method configured for that account. No TranscriptLab API key is needed. Review the consent
screen before granting `transcriptlab:read` and `transcriptlab:write` access.

The production Clerk instance must publish CIMD support and make the `transcriptlab:read` and
`transcriptlab:write` OAuth scopes available to the ChatGPT client. ChatGPT may also request the
OIDC scopes advertised by Clerk, including `offline_access` for refresh. The MCP tools do not use
Clerk `public_metadata` or `private_metadata`. The API enforces the read/write scopes per tool and
requires the token audience/resource to match `https://api.transcriptlab.dev/mcp`.

For ChatGPT on the web, create the custom MCP connection from ChatGPT Plugins using the server URL
above. The folder's bundled MCP configuration is also used when the package is installed in Codex;
that local plugin launch link does not create a ChatGPT web connection by itself.

## Credit behavior

- The first delivery of a transcript variant may spend credits. Later deliveries of that variant
  are free.
- Caption discovery is free in credits and subject to a monthly limit.
- Cached transcript search, job status, usage, and library listing do not deliver a transcript.
- YouTube links use captions. Attached files, media links and uploads use speech-to-text, billed per audio minute.

## Available tools

- Get a transcript from existing YouTube captions, or transcribe an attached file or media link with speech-to-text.
- Retrieve a completed transcript after a job finishes.
- Discover available caption tracks.
- Search or chunk cached transcript text.
- Check job status, account usage, and the transcript library.

## Composer at-mentions

The server implements the OpenAI `mentions/search` extension (`openai/mcp-extensions`): typing
`@TranscriptLab` in the composer searches the account's transcript library and inserts a resource
link. The `transcriptlab_mentions` tool carries `ui.visibility: ["app"]`, so it serves the picker
without appearing in the model's tool list.

## Attached files and media links

Without opening any view, the model can transcribe media directly:

- **A file attached to the chat** goes to `transcriptlab_transcribe_file`. The tool declares
  `_meta["openai/fileParams"]: ["file"]`, so ChatGPT passes a temporary `download_url`. The server
  downloads it (https, public host, size checked against the 300 MB chat-attachment limit before storing; larger files use the launcher, up to 2 GB),
  streams it into R2 through the signed-upload pipeline, and starts speech-to-text. No browser
  upload and no R2 CORS rule are involved.
- **A direct media link** (not YouTube) goes to `transcriptlab_transcribe_media_url`, which uses
  `POST /v1/media`.
- Both return an id to poll with `transcriptlab_get_speech_transcript`.
- If a file is too large, unreadable, or the user wants to pick it from disk, the model calls
  `transcriptlab_open` with `tab: "upload"`, which opens the launcher on the Upload tab.

## Audio file upload

Opening an audio or video file with the plugin (file-extension entrypoint) launches a sandboxed
audio uploader: it reads the file through ChatGPT, uploads the bytes to TranscriptLab's signed
direct-upload URL, then starts and polls the transcription inside the conversation.

Deployment prerequisite: the R2 bucket must allow `PUT` from any origin in its CORS policy —
ChatGPT's app iframes run as an opaque origin (`Origin: null`), which hostname rules cannot
match. Restrict methods to `PUT` and headers to `Content-Type`, `Content-Length`,
`x-amz-meta-upload-source`; the presigned URL is the actual credential. The view's declared
CSP still limits network destinations to `https://*.r2.cloudflarestorage.com`.

## Launcher

`transcriptlab_open` opens a four-tab launcher view (Riso theme, light and dark):

- **Paste link** — fetches a YouTube transcript; "Languages" lists caption tracks (free) first.
- **Upload file** — drag-and-drop or pick a file (up to 2 GB), with real upload progress and retry.
- **Batch** — paste URLs (validated and de-duplicated), submit one job, watch per-video progress,
  search the results, and send them to chat as one combined message.
- **Library** — reopen any delivered transcript for free, filter it, and search across the listed
  videos.

Every source opens in one shared viewer with find-in-transcript, "Download" (TXT, SRT, VTT, Markdown; a 10-minute signed link opened in your browser, because ChatGPT's view sandbox blocks direct file saves) and "Open in TranscriptLab" for the web app,
Copy, "Discuss in chat", and quick actions (Summarize, Chapters, Key quotes, Blog post). A credits
chip shows the remaining balance. The view loads its fonts from Google Fonts via
`resourceDomains` and falls back to system fonts if the host blocks them.
