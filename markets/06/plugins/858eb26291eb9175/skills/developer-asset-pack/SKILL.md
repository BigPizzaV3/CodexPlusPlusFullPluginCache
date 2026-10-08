---
name: developer-asset-pack
description: Use when someone needs several hosted assets prepared for code, documentation, a README, or a website.
---

# Developer Asset Pack

## Purpose

Combine ordered Media2URL publication with ChatGPT’s ability to format structured results for developers. The useful output is a deterministic mapping from each input asset to the requested Markdown, HTML, CSS, JSON, or README representation.

## Trigger examples

- “Host these screenshots and prepare my GitHub README.”
- “Give me HTML for these product images.”
- “Publish these files and return JSON.”
- “Prepare the assets for my website.”

## Do not trigger

- Only one file is mentioned without a hosting or formatting request.
- The user wants a complete website or application built rather than hosted assets.
- The asset bytes or authorized library records are unavailable.

## Allowed Media2URL App actions

- Use `publish_content` or the App’s approved upload flow for each supported asset.
- Use `get_asset_links` for confirmed direct/share URLs and supported output formats.
- Use narrow `search_assets` or `list_recent_assets` calls when the user refers to existing library assets.

## Result interpretation

Keep deterministic input ordering. Map every result to its original filename or logical identifier before producing Markdown, HTML, CSS, JSON, or README content. Prefer direct URLs for code and embed consumers, and use share URLs for human-facing links. Return partial results honestly when the App does not publish every item.

## Missing authorization

Require Media2URL account connection before any storage, publication, or private-library lookup. Do not assume ChatGPT attachments provide binary bytes to the App and do not fabricate a hosted result.

## Plan or quota restriction

Free accounts are capped at 90 uploads per month, roughly 3 per day. Explain the returned plan or quota error, especially for batch publication, large files, persistent hosting, or advanced library search. A paid plan unlocks larger quotas and developer-oriented controls; do not silently publish only a weaker subset unless the user agrees to that change.

## Partial failure

Report successes and failures per input item, keeping filenames and captions matched. A failed item must not receive a copied URL from another item, and the batch must not be labelled fully successful.

## Privacy and destructive actions

Use only assets the connected account/workspace can access. A developer pack does not authorize publication of private assets, remote third-party copying, replacement, or deletion; those actions require explicit intent and the App’s checks.

## Natural-language examples

“I’ll preserve the input order, publish each confirmed asset, and return a README block with the direct URLs. Any failed publication will stay marked as failed.”
