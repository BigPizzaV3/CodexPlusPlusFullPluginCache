---
name: publish-this
description: Use when someone explicitly asks to publish, host, or put ChatGPT-created content online through Media2URL.
---

# Publish This

## Purpose

Turn an explicit request to publish ChatGPT-created content into a safe Media2URL App action. The goal is a usable result: a live HTML page when a webpage is requested, or structured asset links for supported files and text.

## Trigger examples

- “Publish this HTML and give me a live URL.”
- “Host this SVG.”
- “Put this JSON somewhere I can fetch it.”
- “Turn this image into a URL.”

## Do not trigger

- A file or image is merely mentioned or attached.
- The user asks to explain, edit, summarize, or preview content only.
- The user asks to show a private asset without asking for publication.

## Allowed Media2URL App actions

- Use `publish_content` for supported generated HTML, SVG, Markdown, JSON, plain text, and other App-approved textual content.
- Use the App’s approved upload UI for binary/local media when the App can receive the bytes.
- Use the App’s HTML publication path when the user wants a live webpage rather than a downloadable HTML file.

## Result interpretation

Send the returned public URL first, then useful metadata such as content type, asset/project ID, version, and actual expiration. A successful result must come from the connected Media2URL App; never infer success from a tool call that returned no confirmation. Do not claim to have the actual binary content when the App did not receive its bytes.

## Missing authorization

Before the first storage or publishing action, require account connection through the App. Explain that the user can connect Media2URL, then retry. Do not offer anonymous ChatGPT storage, a presigned destination, or a fabricated URL.

## Plan or quota restriction

Free accounts are capped at 90 uploads per month, roughly 3 per day. Explain the App’s structured reason, such as `UPGRADE_REQUIRED`, `FREE_QUOTA_EXHAUSTED`, `FILE_SIZE_REQUIRES_PLAN`, or `PERSISTENT_HOSTING_REQUIRES_PLAN`. A paid plan unlocks larger quotas and advanced controls; do not silently downgrade a request for persistent hosting, a large file, or a restricted format to a weaker publication.

## Partial failure

For multiple inputs, identify each successful result by its original filename or logical name and list failed items separately. Do not describe the whole request as successful when one publication failed.

## Privacy and destructive actions

Respect the asset’s visibility and workspace authorization. A publish request is not permission to expose unrelated private assets. Publishing is a write action; deletion, replacement, or importing third-party content needs its own explicit intent and App authorization.

## Natural-language examples

“I can publish this as a live HTML page. Connect your Media2URL account first, then I’ll return the confirmed page URL and its actual retention period.”
