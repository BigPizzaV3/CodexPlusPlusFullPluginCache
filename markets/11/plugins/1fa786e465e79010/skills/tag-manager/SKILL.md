---
name: tag-manager
description: Google Tag Manager with Opus Growth - accounts, containers, workspaces, tags, triggers, variables, built-in variables, previewing pending changes, publishing, version history, rollback and user permissions. Use when installing or fixing tracking tags (Google Ads, GA4, Meta, TikTok, LinkedIn and others) through Tag Manager. Covers working in a workspace, publishing only on approval and rolling back safely.
---

# Google Tag Manager

Follow the `opus-growth` skill for preview and confirm, and the `measurement` skill for what to
track. Tag Manager changes reach every visitor of the site the moment they are published.

## Find the right container

`list_gtm_accounts` → `list_gtm_containers` → `list_gtm_workspaces`. Confirm the container is the
one the site loads (`wordpress_tracking` on WordPress, or `site_read_url` / `seo_audit` to see the
GTM-XXXX id in the page). A site can load more than one container.

## Build in a workspace

1. Read what exists: `list_gtm_tags`, `list_gtm_triggers`, `list_gtm_variables`. Do not add a
   second tag for something that is already tracked; that doubles conversions.
2. Work in a dedicated workspace for larger changes (`create_gtm_workspace`), so unrelated
   pending edits by someone else are not published with yours.
3. Create what is needed: `create_gtm_trigger` (page view, click, form submit, custom event),
   `create_gtm_variable`, `create_gtm_tag`. Built-in variables such as Click URL, Click Text or
   Form ID must be enabled first: `enable_gtm_builtin_variables`.
   - Google Ads conversion tag: tag type `awct` (Google Ads Conversion Tracking), with the
     conversion id and label from `google_ads_get_conversion_tags`. Type `sp` is the Google Ads
     remarketing tag and counts no conversions. A Conversion Linker tag (type `gclidw`) must fire
     on all pages, unless the container already has one, so the ad click is kept for the
     conversion tag.
   - GA4 event tag: measurement id from `ga4_list_data_streams`.
   - Custom event triggers fire on `dataLayer.push({event: "name"})` from the site; the event
     name must match exactly, including case.
4. Edit or remove with `update_gtm_entity` / `delete_gtm_entity`.

## Publish only on approval

- `gtm_workspace_status` lists every pending change in the workspace. Show it to the user.
- `publish_gtm_container` makes it live immediately, after the user approves.
- After publishing, verify: GA4 `ga4_realtime`, the platform's pixel or conversion status, or the
  page itself.
- Something broke: `list_gtm_versions` shows which version is live; `rollback_gtm_version`
  returns the site to an earlier version.

## Consent

Tags that require consent fire only after the visitor accepts. Fewer tag hits than sessions is
expected with a consent banner, not a broken tag.

## Access

`list_gtm_permissions` and `manage_gtm_permissions` grant or revoke access. Never remove the
user's own admin access. `delete_gtm_container` permanently deletes a container and everything in
it; only on an explicit request, after confirming the container is not live on any site.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
