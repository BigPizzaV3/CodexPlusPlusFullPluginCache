# Host tools: ChatGPT

Which ChatGPT tool builds each format, and how the result gets into OptiSigns. Check what this session
actually offers; tools, export options and public Sites vary by plan and workspace.

| Format | ChatGPT tool | Into OptiSigns |
|---|---|---|
| Slides (default) | The code sandbox. ChatGPT on the web has no slide app in chat; the sandbox builds PPTX or PDF pages at 1920×1080 with real text | PDF (PPTX if they'll re-edit) → upload below |
| Pixel-exact image | Image generation | PNG per slide → upload below |
| Web page / dashboard | **Sites** | Public URL → `optisigns_asset_create{url, name}` |
| Kiosk | **Sites** (the Worker holds shared state) | Public URL → `optisigns_asset_create{url, name}` |

## Slides

ChatGPT on the web has no slide-deck app in chat; the code sandbox is the slides tool. Build each page at
1920×1080 with real text and export **PDF**, one page per slide; PPTX only when the user will edit it in
PowerPoint. Show the rendered page before asking for the OK. The upload takes the file from the sandbox;
if it lands only as a download for the user, say: "download the PDF and drop it here, I'll upload it."

## Image

Image generation returns a photo-sized image (about 1672×941, not 1920×1080) and can misspell words, so it
is for a background or illustration placed under real text on a 1920×1080 page, not for the text of a sign.

## Web page

Build it as a Site. Facts that matter for a signage player:

- Simple pages default to buildless HTML/CSS/JS served as static files. Follow `references/web-app.md`.
- A Site can run a Cloudflare Worker with D1 (SQL, SQLite semantics, 10 GB per Site) and R2 (files).
  The Worker can fetch live data from HTTP APIs and serve it to the page, so the page shows live data
  to an anonymous viewer without any sign-in.
- **The audience must be public.** New Sites start owner-private, and deploying does not change the
  audience. The player loads the URL as an anonymous browser; a private or workspace-only Site shows a
  sign-in page on the TV. Ask the user before making it public. Public access may be off by workspace
  policy; then the user's admin must allow it.
- Unattended refresh: a linked schedule (`create_schedule`) runs an authorized writer that updates the
  Site's stored data while nobody has it open, without republishing. The page then polls the Worker.
- Saving a version and deploying it are separate steps; the URL shows only what is deployed.
- Connected apps run with the visitor's own connection. A TV has no visitor connection, so never build
  a signage page that depends on one; fetch from the Worker with its own credentials instead.
- Keep secrets in the Site's runtime environment variables, never in page source.

## Kiosk

Also a Site; read `references/kiosk.md`. Shared results (answers, sign-ups, a leaderboard) go to the
Worker and D1, written through the Site's own API. A public write endpoint needs its own protection
(rate limit, input validation, duplicate-submission guard), because anyone with the URL can call it.
Per-device state stays in `localStorage`.

## Export → upload

- PDF / PPTX / PNG files, attached or made in this sandbox → `optisigns_asset_upload_from_url` with the
  file as `file`, one call per file. The sandbox cannot reach the upload service, so
  `optisigns_asset_upload_begin` → POST fails here.
  If the file exists only as a user download, ask the user to drop it into the chat.
- Site → copy the deployed public URL → `optisigns_asset_create{url, name}`. Open the URL once signed out
  (or in a private window) before publishing; it must load without a sign-in.

## Brand storage

No brand store on this host. Ask the user to paste the brand card into the chat, or keep it in the
project's instructions or files so every chat in the project has it. Never save it anywhere silently.

## Limits

- Worker memory 128 MB per isolate (server side; the player limits in `references/web-app.md` still apply).
- HTTP, HTTPS and WebSockets only.
- No native queues, cron triggers or durable objects confirmed; use the linked schedule for refresh.

