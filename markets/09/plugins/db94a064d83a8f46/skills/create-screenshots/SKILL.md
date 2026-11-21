---
name: create-screenshots
description: Create App Store and Google Play screenshots from app captures. Add headlines, backgrounds, and device frames; preview one image or a series and download full-resolution PNGs in a ZIP.
---

# App Listing Screenshots

Use the connected App Listing Screenshots MCP tools for every render. Do not run a local CLI, draw replacements with Python/Pillow, call image generation, or reuse unrelated previous outputs. If the connection or a required tool is unavailable, report the actual error instead of claiming screenshots were created.

## Conversion-focused screenshot headlines

When drafting or rewriting headlines, act as an expert conversion copywriter and product marketer. Aim to maximize qualified installs through a clear pain → solution → desired outcome story. Preserve exact headlines supplied or approved by the user unless they request a rewrite.

- Infer the audience, concrete frustration and desired outcome from the supplied app context and captures. Tie each promise to a capability the product actually demonstrates; ask only when a missing fact materially changes the claim.
- Lead the first slide with the strongest relevant benefit. Give each subsequent slide one distinct reason to install, connecting a recognizable pain or objection to the useful outcome of the visible feature. Use the sequence to tell the story; every headline does not need to spell out the entire framework.
- Prefer specific, benefit-led language over screen names or feature labels. For an app that provides aquarium care advice, “AI Analysis” can become “Know what your tank needs”; for receipt capture, “Receipt Scanner” can become “Log expenses without typing”.
- Use the requested language and brand voice, direct verbs and concrete outcomes. Aim for 3–7 words and one or two short lines. Shorten the wording before shrinking the font, and check readability in the returned preview.
- Compare a few distinct angles internally and choose the strongest for relevance, clarity, credibility and fit. Deliver ready-to-use headlines without adding an approval round unless the user asks for options.
- Never invent research, numbers, testimonials, urgency, rankings or guarantees. Avoid unsupported health, financial or performance promises. Treat conversion-focused copy as a hypothesis, not a measured conversion improvement.

1. Call `list_screenshot_options` for the actual preset IDs, fonts and complete design schema. Preserve the user's choices. Read [the workflow](references/workflow.md) for sources and series settings.
2. Call `create_screenshot_series` with a name, shared design settings and one or more slides. Use attached captures through the tool's `files` parameter and per-slide `sourceIndexes`. Omit files only when the user authorized using the bundled demo.
3. Call `export_screenshot_series` with the returned `seriesId`. This produces every full-resolution PNG and a ZIP on the server. One slide is valid too.
4. The inline MCP Apps component displays each full-resolution PNG separately, side by side, and provides the ZIP link. Separate image blocks are also model-visible. Large exports use smaller inline previews to keep the tool response bounded; files[].url and the ZIP always contain the original full-resolution PNGs. Do not treat previewAvailable or a successful tool call as proof that the component is visible. For a requested design revision, call `update_screenshot_series` with the affected zero-based slide indexes, then export the same series again. Do not add duplicate Markdown images when the component is visible. If the host does not display the component, show each returned `files[].url` as a separate Markdown image so the user still gets a preview. Provide the exact `downloadUrl` as a Markdown ZIP link. If the host cannot render the component, state the actual limitation. Inspect the component before claiming visual verification. Never invent download URLs or substitute a local archive for the server output.

Do not call `open_screenshot_editor` or tools that automatically open it for this workflow. The expected user experience is a preview in chat and a ZIP download, without a screenshot editor. Explicitly requested design revisions can create a revised series through the same two tools.

All screenshot design settings are available through the schema: presets/custom sizes, layouts, one to three sources per slide, fonts, title/colors/positions, backgrounds, device frames/borders and XYZ rotations. The remote server enforces 9 million pixels per slide, 30 million pixels per series, at most twelve slides, and bounded source/export bytes. Do not imply that every 8192 by 8192 canvas is renderable. Independent slides do not form a seamless panorama.

Use truthful captions and only images authorized by the user. Uploaded source images, projects, and series have no automatic expiration and are stored under an isolated anonymous connection identity. New series PNGs and ZIPs are retained until a deletion request; their signed links have no automatic expiry. Legacy expiring links require a new export. The connection is established automatically: no account login, password or manual key. ChatGPT handles protocol tokens in the background. This identity is a server-generated anonymous connection ID, not the user's verified OpenAI account, name or email. Refreshing the connection token preserves its projects; reconnecting creates a new identity. For a deletion request, direct the user to the support page and ask them to include a series ID when available. Never request credentials in this Skill or messages. Do not publish store listings as part of screenshot creation.
