---
name: create-slideforge-presentation
description: Create and export a SlideForge presentation from a user's topic using the connected SlideForge MCP tools. Use when a user asks to generate a slide deck, PowerPoint, PDF presentation, or slide-image package.
---

# Create a SlideForge Presentation

Use the connected SlideForge tools to turn a topic into a presentation and, when requested, provide a short-lived download link.

## Prepare the Request

- Preserve the user's intent, requested language, audience, tone, and slide count.
- Ask one concise clarification only when a missing detail would materially change the deck. Otherwise use sensible defaults.
- Do not send private source material, secrets, or unrelated conversation content as the topic.
- Before generating, use `get_account` when the available slide balance is unknown. If the requested count exceeds the balance, explain the shortfall instead of starting a generation that cannot succeed.
- Treat a clear request to create a deck as authorization to call `generate_presentation`. Do not create duplicate presentations when retrying status checks or exports.

## Generate and Monitor

1. Call `generate_presentation` once with the finalized topic, slide count, tone, language, audience, and the default `split` layout.
2. Tell the user that image-rich presentation generation is asynchronous and may take several minutes.
3. Use `check_presentation_status` with the returned presentation ID. Poll at reasonable intervals rather than issuing rapid repeated requests.
4. Stop polling when the status is `completed` or `failed`.
5. If generation fails, report that outcome clearly and retain the presentation ID for support or a later status check. Do not automatically start a replacement deck.

## Export

- Export only after status is `completed`.
- Use `pptx` for an editable PowerPoint, `pdf` for a fixed-layout document, or `images` for a ZIP of rendered slide images.
- If the user did not specify a format, ask which format they want after generation completes; prefer `pptx` only when they explicitly asked for PowerPoint or an editable deck.
- Call `export_presentation` once for each requested format and immediately present its download link. Explain that the link expires in five minutes and is intended for one download.
- If a link expires or has already been used, create a fresh export link rather than reusing it.

## Existing Presentations

- Use `list_presentations` to find presentations belonging to the connected account.
- When titles are similar, confirm the presentation ID before exporting.
- Use `list_templates` only to describe templates currently available. The present MCP contract cannot apply a template to a deck.

## Capability Boundaries

Do not claim that these tools can upload documents, edit individual slides, apply templates, delete presentations, or modify billing. Direct users to the SlideForge web application when they request those actions.
