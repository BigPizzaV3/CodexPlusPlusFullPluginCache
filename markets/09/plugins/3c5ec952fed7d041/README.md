# Anime Style

**Upload status:** This package is prepared for a draft upload to OpenAI Platform.
It is not ready for review submission until the publishing identity,
country targeting, commerce declaration, reviewer access, and required portal checks
are complete. Five positive and three negative review cases are included; the complete
set has not yet been run in the submission host. A verified public walkthrough recording is
included in the manifest; it demonstrates image conversion and result controls. Video conversion
and the full review-case set are not shown in that recording.

- Product: https://firemoon.studio/anime-style
- Support: https://firemoon.studio/support
- Privacy policy: https://firemoon.studio/privacy
- Terms: https://firemoon.studio/terms

A separate Firemoon plugin for converting images and videos into anime.

- Image conversion: Nano Banana Edit, 1–4 PNG variations.
- Video conversion: Gemini Omni Flash 1.1 Edit, 720p.
- Presets: classic, cinematic, retro-90s, chibi, manga.
- Results: inline image previews or a video player, with Open and Download actions.
- Authentication: existing Firemoon OAuth or a Firemoon full_access key configured in the host's secure connection settings.

## Connection

The dedicated Streamable HTTP server is `https://mcp.firemoon.studio/anime-style/mcp`.
The portable manifest uses `mcp.json`; `.codex-plugin/plugin.json` and `.mcp.json` support older Codex clients.

**Release status:** Firemoon and the MCP server are deployed in production. Both conversion tools, the result resource, a real image conversion, a real video conversion, image delivery and ranged video playback have passed live verification. Host installation and OAuth consent are still required for each user.

## Limits and billing

MP4/MOV video, up to 10 seconds and 50 MB. Source duration is read from the movie header before charging credits, at $0.10 per second. Video resolution is fixed to 720p. No new Google key is needed: the backend uses Firemoon's existing fal credentials.

Prompts request preservation of identity, composition, movement, timing and audio; results can differ. Generated media is available through public result links. Original files and prompts are sent to Firemoon and its generation provider.

## Backend source

The source is in the Firemoon repository:
- `mcp-vercel/lib/anime-style-mcp.mjs` and `api/anime-style.mjs`.
- `mcp-vercel/widget/anime-results.js` and its generated resource.
- `models-config/google/gemini-omni-flash-v1.1-edit.json`.
- `app/api/generate/route.ts` validates source duration, reserves/refunds credits, and stores the output.

Run `node --test mcp-vercel/tests/anime-style.test.mjs` for the local integration suite. Local checks mock paid generation; they do not prove provider access or visual quality. Deploy Firemoon before the MCP service. See the repository deployment guide.
