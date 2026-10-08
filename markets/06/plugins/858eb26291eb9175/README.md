# Media2URL

Publish media, files, and generated web content from ChatGPT to usable Media2URL links. Use the direct URL for code and embeds, the share page for people, or the managed update workflow when an existing URL must stay the same.

This package is the workflow layer for ChatGPT and Codex. It contains instructions and listing metadata only. Real publication, upload, import, search, diagnosis, updates, versioning, sharing, and deletion require a connected Media2URL App and its server-side authorization.

## What it helps with

- Publish generated HTML, SVG, Markdown, JSON, text, and App-supported media after an explicit request.
- Choose the right direct URL, share page, Markdown, HTML, CSS, or JSON representation.
- Update a managed asset or HTML project without silently creating a new URL.
- Prepare ordered asset packs, temporary shares, Link Doctor checks, and narrow library searches.

The plugin does not activate just because a file or image is mentioned. It also does not assume ChatGPT can pass binary attachment bytes to an external App. Account connection is required before a storage or publication write; the plugin never offers anonymous ChatGPT hosting.

## Account-only freemium access

Every upload, publication, import, and managed update requires a connected Media2URL account. The Free plan is capped at 90 uploads per month, roughly 3 per day. Paid plans unlock the remaining advanced workflows, including larger quotas, batch publishing, private links, replacement/versioning, and richer library controls when the connected App supports them.

## Included skills

| Skill | Use it when |
| --- | --- |
| Publish This | Someone explicitly asks to publish or host content. |
| Update the Live Version | An existing managed URL should be preserved. |
| Get the Right Link | The destination needs a direct URL or share page. |
| Developer Asset Pack | Several hosted assets need code or README output. |
| Temporary Secure Share | A confirmed asset needs supported limited-time sharing. |
| Link Doctor | A URL redirects, opens HTML, expires, or fails in code. |
| Media Library Reuse | An existing authorized library asset should be found. |
| Batch Publish | Several assets must be published in deterministic order. |

## Media2URL website and trust

- [Media2URL website](https://media2url.com/)
- [Pricing](https://media2url.com/pricing)
- [Privacy Policy](https://media2url.com/privacy)
- [Terms of Service](https://media2url.com/terms)
- [Contact and support](https://media2url.com/contact)
- [Report abuse](https://media2url.com/report-abuse)
- [Security](https://media2url.com/security)

## Media2URL tool pages

- [All tools](https://media2url.com/tools)
- [Link Doctor](https://media2url.com/tools/link-doctor)
- [Image to Link](https://media2url.com/image-to-link)
- [Video to Link](https://media2url.com/video-to-link)
- [GIF to Link](https://media2url.com/gif-to-link)
- [PDF to Link](https://media2url.com/pdf-to-link)
- [Audio to Link](https://media2url.com/audio-to-link)
- [File to Link](https://media2url.com/file-to-link)
- [HTML to URL](https://media2url.com/html-to-url)
- [Media Library](https://media2url.com/features/media-library)
- [Expiring Links](https://media2url.com/features/expiring-links)
- [Private Links](https://media2url.com/features/private-links)
- [Custom Domains](https://media2url.com/features/custom-domains)
- [Media Processing](https://media2url.com/features/media-processing)
- [PDF Workspace](https://media2url.com/features/pdf-workspace)

The tool pages describe the corresponding Media2URL website workflows. They are not claims that every website feature is available inside ChatGPT.

## App dependency

Phase 1 intentionally has no `.app.json` and no App ID. Once the real Media2URL App exists, create `media2url-chatgpt-plugin/.app.json` using the then-current OpenAI app-reference schema and the real Media2URL App ID. Add the manifest’s `apps` field only at that time; do not replace it with a guessed identifier or duplicate MCP configuration inside the plugin.

## Install and test

1. Validate the package locally with `python3 /Users/sagarkumarsahu/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py media2url-chatgpt-plugin`.
2. Run `npm run test:plugin` from the Media2URL repository.
3. In Codex, make the repository plugin available through the plugin controls, then start a new task and use Sources → Use plugins where that control is available.
4. In ChatGPT, use the Plugins directory or the available Apps/More control to import or enable the package. A workspace administrator may need to approve it.
5. Test intent boundaries with the prompts in `submission/test-matrix.md`. Until the real App is connected, verify that skills explain the required connection and do not claim a publication occurred.

OpenAI account, workspace, Developer Mode, App authorization, and App publication controls are external to this repository. This package has not been registered, deployed, or published to OpenAI.
