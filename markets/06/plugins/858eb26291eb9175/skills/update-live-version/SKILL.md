---
name: update-live-version
description: Use when someone asks to update, replace, or restore an already published Media2URL asset or HTML page.
---

# Update the Live Version

## Purpose

Change an identified managed asset or HTML project while preserving its existing public URL where Media2URL supports that workflow. Treat an update as different from creating a new asset.

## Trigger examples

- “Update the live page with this new copy.”
- “Replace the screenshot but keep the URL.”
- “Publish this version instead.”
- “Restore yesterday’s version.”

## Do not trigger

- The user wants a second, unrelated upload.
- No immutable asset/project identifier or confirmed library result exists.
- The user only wants a link copied or content edited in the conversation.

## Allowed Media2URL App actions

- Use `update_published_content` with the exact asset/project ID.
- Use `replace_asset` for an authorized managed file replacement.
- Use `rollback_version` only with an exact asset/project ID and version ID returned by the App.
- Use the App upload UI for local binary replacement when it supports that flow.

## Result interpretation

Confirm the same public URL, the new version identifier, the previous version when returned, and the updated timestamp. If the App reports that the operation creates a new asset or new URL, say so plainly; never represent a new asset as a preserved URL.

## Missing authorization

Require a connected Media2URL App account before reading private library details or changing hosted content. Ask the App to resolve the current workspace and ownership; do not accept a public URL alone as proof of control.

## Plan or quota restriction

Free accounts are capped at 90 uploads per month, roughly 3 per day. Explain errors such as `VERSIONING_REQUIRES_PLAN`, `FEATURE_REQUIRES_PLAN`, or `UPGRADE_REQUIRED`. A paid plan unlocks larger quotas and versioning controls; do not silently turn a request to preserve the URL into a new free upload.

## Partial failure

If a replacement or publication fails after staging, report that the existing live version remains unchanged only when the App confirms that state. Never invent a version number, rollback entry, or recovery result.

## Privacy and destructive actions

Only update assets in the authorized account/workspace. Rollback changes what recipients see and delete is destructive; keep those actions distinct and follow the App’s confirmation and permission requirements.

## Natural-language examples

“I found the managed project. I’ll use its update action so the same URL remains active, then report the new version that Media2URL confirms.”
