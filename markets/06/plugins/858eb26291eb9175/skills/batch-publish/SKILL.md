---
name: batch-publish
description: Use when someone explicitly asks to publish several files or prepare multiple hosted assets together.
---

# Batch Publish

## Purpose

Publish several authorized assets while keeping deterministic input ordering and an honest per-item result map. Batch publication is a workflow, not permission to bypass limits or validation.

## Trigger examples

- “Host these ten screenshots.”
- “Give me URLs for all these images.”
- “Create a Markdown gallery from these files.”
- “Publish this folder of assets in filename order.”

## Do not trigger

- The user mentions several files but does not ask to host, publish, or link them.
- The App cannot receive the binary bytes or identify authorized library assets.
- The user asks for a bulk action that would silently replace or delete existing assets.

## Allowed Media2URL App actions

- Use repeated `publish_content` calls or the App’s approved multi-file upload flow.
- Use `get_asset_links` for confirmed output URLs.
- Use `search_assets` only when the user explicitly refers to existing library assets.

## Result interpretation

Preserve input order and map each result to its original filename or logical identifier. Return direct URLs for code and embed output, share pages for human sharing, and structured Markdown/HTML/CSS/JSON only from confirmed results.

## Missing authorization

Require a Media2URL account connection before the first storage action. Do not offer anonymous ChatGPT uploads, presigned destinations, or a batch result before the App confirms each publication.

## Plan or quota restriction

Free accounts are capped at 90 uploads per month, roughly 3 per day. Explain `BATCH_REQUIRES_PLAN`, `FREE_QUOTA_EXHAUSTED`, `FILE_SIZE_REQUIRES_PLAN`, or the App’s actual entitlement error. A paid plan unlocks larger quotas and batch controls. Do not silently publish only some items or downgrade a batch into unrelated individual behavior without telling the user.

## Partial failure

Report successful and failed items separately, preserving input order and source names. A failed item must not receive another item’s URL, and the batch must not be described as fully successful. Do not retry indefinitely.

## Privacy and destructive actions

Every item must pass the App’s workspace, file, abuse, and plan checks. Batch publication does not authorize private-asset exposure, third-party importing, replacement, rollback, or deletion; those are separate actions.

## Natural-language examples

“Three files were published and two were rejected by Media2URL. I’ll return the three confirmed URLs in the original order and list the two failures separately.”
