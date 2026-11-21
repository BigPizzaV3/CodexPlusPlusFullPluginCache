---
name: manage-grigora
description: Build or manage websites in Grigora through its connected MCP server, including website drafts, CMS posts, directory content, SEO, assets, analytics, and store catalogs. Use when the user chooses Grigora or is continuing work on a Grigora site.
---

# Work with Grigora

Use the Grigora MCP tools available in the current connection. Account permissions and enabled features determine which operations are available. If disconnected, direct the user to connect their Grigora account through the plugin's OAuth flow; do not request raw API keys in chat.

## Connect the account

The registered Grigora app is required. If its tools are unavailable or authentication is required, direct the user to the Grigora connection inside this plugin and complete the host OAuth flow. Never ask the user to paste a password, access token, or API key into chat. After connecting, call `list_projects` as a read-only connection check. If website creation tools are missing, explain that an account connection is required and ask the user to reconnect through Grigora account sign-in. Do not substitute a legacy project token or claim a website was created without a successful tool result.

## Select the site

For an existing site, use `list_projects` and reuse returned identifiers. Resolve the site from the user's request and prior context; ask only when the target remains ambiguous. Read existing content or settings before applying a partial update. Distinguish saved changes, completed builds, and published content in the result.

## Build and edit

`create_website` creates a new unpublished site and consumes AI credits and plan capacity. Call it once for each requested new site. `edit_website` modifies an existing AI-built site and also consumes credits. Combine related edits in one prompt. Explain credit use before starting when the user has not already acknowledged it.

Use the returned project and build IDs with `get_website_build_status`. A running build is not completion. If `build_in_progress` is returned, wait for that build before starting another edit. If the response contains a question without starting a build, relay it to the user. Do not blindly repeat a create/edit call after an uncertain response: a new invocation can create another billable build. Inspect existing sites or build status first.

For attachments, supply public URLs supported by the tool. For a user-authorized local upload, use `get_attachment_upload_url` and its returned upload instructions; do not put file bytes in the build prompt. Return the actual editor URL from the server. Publish with `publish_project` only within the user's requested scope; a request for a draft does not authorize publication.

## Content and settings

- CMS: inspect posts and relevant categories before creating or updating. Preserve existing structure when editing; `content_blocks` is a JSON string and overrides HTML `content` when supplied. Publishing and unpublishing are separate tools.
- Directories: inspect the collection's field definitions before writing items; use the actual collection and item IDs.
- SEO: use `get_seo_settings`, then patch only changed keys through `update_seo_settings`. When required, pass the returned mutation version and a unique idempotency key. Preserve the same arguments and key for a retry of the same operation. Empty strings clear text; `false` clears toggles; empty arrays clear lists. Arrays replace the entire list; null and unknown fields are rejected. Saving may still require publication.
- Commerce: amounts are integers in the currency's smallest unit. Read the currency and product/variant identifiers before changing prices or stock. Product options support up to three axes, twenty values per axis, and one hundred variants. Respect commerce-access errors. Payment gateway credentials are configured in the dashboard and cannot be read or changed through MCP.
- Domains and redirects: custom-domain setup returns DNS instructions for the owner to apply; report the actual verification status. Redirect creation and editing require a connected custom domain.
- Newsletter support is limited to signup-list discovery and custom-field tools. Contact exports and campaign sending are not exposed.

Use the server's returned errors to explain unavailable features or missing permissions. Do not fabricate successful changes, links, or identifiers.
