---
name: temporary-secure-share
description: Use when someone asks to share a Media2URL asset for a limited time or with a supported access restriction.
---

# Temporary Secure Share

## Purpose

Create or apply only the temporary sharing settings that Media2URL confirms for the asset, account, and workspace. A time limit is not automatically a password or download-control feature.

## Trigger examples

- “Make this available for 24 hours.”
- “Share this until tomorrow.”
- “Let this file expire after the review.”
- “Create a temporary link for this asset.”

## Do not trigger

- The user only wants the ordinary direct URL or share page.
- The requested asset is not identified or authorized.
- The user asks for password protection, one-time viewing, or download limits without confirming that Media2URL supports it.

## Allowed Media2URL App actions

- Use `create_temporary_link` with the exact asset ID and supported expiry.
- Use `get_asset_links` to return the resulting link formats and actual expiration.
- Use `get_asset` to confirm the asset’s current status and visibility.

## Result interpretation

Report the expiration returned by the App, plus whether the link is temporary and which access controls are actually active. Do not call a link permanent, password-protected, one-time, or download-limited unless the structured result says so.

## Missing authorization

Require a Media2URL account connection before changing sharing rules or accessing a private asset. Do not create anonymous hosted storage or use a public URL as proof that the requester owns the asset.

## Plan or quota restriction

Free accounts are capped at 90 uploads per month, roughly 3 per day. Explain the App’s actual restriction, such as `CUSTOM_EXPIRY_REQUIRES_PLAN`, `FEATURE_REQUIRES_PLAN`, or `UPGRADE_REQUIRED`. A paid plan unlocks larger quotas and advanced sharing controls. If only a fixed supported free expiration is available, offer that exact alternative rather than inventing a custom date.

## Partial failure

For several assets, report each confirmed temporary link and identify assets whose rule was not changed. Never reuse one asset’s expiration or URL for another item.

## Privacy and destructive actions

Keep private and workspace-only assets within their existing authorization boundary. Changing access can affect recipients, and deletion is a separate destructive action that must not be bundled into temporary sharing.

## Natural-language examples

“Media2URL confirmed this link will expire at the returned time. It did not confirm password protection, so I’m not describing the link as password-protected.”
