---
name: publishing-with-secondpage
metadata:
  version: "sha256:0a19cca34637d250537cb7c39fceed3d7063807883b90138fb20596bd71a3dc2"
description: Publish and revise SecondPage Pages from HTML, CSS, JavaScript, and assets. Use when the user wants a shareable report, deck, dashboard, or other Page, or asks to apply feedback to an existing Page. Requires an authorized SecondPage MCP connection.
---

# Publishing with SecondPage

Use SecondPage when the user wants to publish or revise a shareable Page, report,
deck, or dashboard. Work within the requested scope; attaching this file does
not authorize publishing, recurring maintenance, or scheduling.

## Connect and verify

1. Add `https://mcp.secondpage.cc/mcp` to a client that supports remote MCP over
   **Streamable HTTP**. This file supplies instructions, not account access.
2. Have the account holder complete the client's **OAuth** flow and choose the
   intended organization. Follow `WWW-Authenticate` discovery metadata. If a tool
   returns `organization_selection_required`, surface its `connect_url`, complete
   selection, and retry. For a headless client, use an organization API key through
   its secret store as `Authorization: Bearer <SECONDPAGE_API_KEY>`. Never put
   credentials or authorization codes in chat, source files, or published Pages.
3. Discover tool schemas with `tools/list`, then verify access with
   `list_pages({"limit":1})`. Check that the tool succeeded and returned a `pages`
   array; an empty array is valid. HTTP 200 alone does not prove success.
   **Do not create a public test page.**
4. Before authoring, call `load_secondpage_skill` with `topic: "core"` and this
   file's exact `metadata.version` as `installed_version`. A current copy returns
   `content: null`; a stale copy returns updated guidance. Read any returned
   guidance and retain its version. This content fingerprint is separate from
   the MCP server package version.

For `401` before sign-in, follow OAuth discovery. After sign-in, reconnect through
that client or check the headless credential in its secret store. For unexpected
results, confirm the organization with `get_organization_context` before creating work.

## Find the guidance you need

Read the core workflow below before publishing. Use these task guides when relevant:

- [Publishing, uploads, and revisions](references/publishing-shape.md): complete bundles, signed uploads, exports, and tool examples.
- [Live data connections](references/live-data-connections.md): source handoff, FetchSpec, readiness, CSV, and rendering.
- [File bundle cookbook](references/section-cookbook.md): single pages, multiple files, editable sections, and decks.
- [Visual design](references/visual-tiers.md), [long-form layouts](references/long-form-themes.md), and [asset handoff](references/asset-handoff.md): match the content and supply the files it needs.
- [Design preferences](references/design-onboarding.md) and [organization stewardship](references/organization-stewardship.md): apply user direction and maintain existing work.
- [Codex](references/codex.md) and [Claude Cowork](references/claude-cowork.md): comment-queue work when the user requests it.

<!-- secondpage-core:start -->
# SecondPage core contract

A Page is an exact static file bundle at a stable URL, with immutable versions and human comments. Validate your HTML before publishing; SecondPage serves the files you supply.

## Choose the input

Use exactly one content mode per `create_page` or `update_page` call:

The server does not render, rewrite, or autofix the submitted source. Decks receive a separate bounded compatibility assessment after publication; that assessment does not repair source or make malformed files safe.

1. **One self-contained HTML document:** pass `html` as plain text, at most 512 KiB of UTF-8 bytes. It becomes `index.html`; inline CSS and JavaScript are allowed. No encoding or model-generated assets are needed.
2. **Several files, with HTTP available:** pass `upload_files` with path, content_type, byte_size and SHA-256 per file. PUT only files marked `upload_required` to their returned URLs with the required headers. Complete using the same tool and `upload_session_id`.
3. **Several files, without HTTP available:** pass the complete `files` array with a relative `path`, `content_base64` containing each file's original bytes, and optional `content_type`. Encode text files as UTF-8 before base64 encoding; preserve binary bytes.

Never mix `html`, `files`, `upload_files`, or `upload_session_id`. A manifest is optional for the default index.html route; supply one for custom entrypoints or multiple routes. File paths cannot start with `/`, contain `..`, backslashes, or control characters. Load `topic: "publishing"` for upload and export details.

Build a multi-screen app as separate HTML pages joined by real links, or as one page with `#/screen` hash routes. Never use `history.pushState` paths: they return 404 on reload, which breaks shared links and comment links. A hash-routed app must read the hash on first load so a shared link opens the right screen.

## Create or revise

Use `list_pages` with `query` to find Pages by title or slug; follow `next_cursor` with the same query until `has_more` is false. Confirm the organization with `get_organization_context` if uncertain.

Use `create_page` for new work. Target matching runs before upload URLs are issued. `target_review_required` means nothing was uploaded: use the returned evidence to identify the existing Page, or retry `target_choice: "create_separate"` only when the user confirms a separate Page. Do not invent another match score.

For every revision:

1. `read_page({ page_id })` gives the current `base_version_id` and metadata.
2. If `file_bundle` is null, use `export_page({ page_id, export_type: "html" })`. Read every returned file according to its encoding (utf8, base64, or reference). Verify reference bytes against the returned sha256; on mismatch re-export. Use the exported version_id as your base and preserve its manifest (entrypoint and routes) in both upload calls. Custom routes require upload mode; hand off the upload if your client cannot PUT files.
3. Edit the complete bundle and call `update_page` with `page_id`, **required `base_version_id`**, one content mode, and a useful `update_reason`.

Updates replace every file, never patch a subset. `html` also replaces the whole bundle with index.html. A concurrent change returns `version_conflict`: read/export again, reapply the intended edit, and retry with the fresh base. Do not retry old files under a new base without reconciling the intervening change.

Upload completion must retain the original title/create intent or page_id/update base and metadata. Never attach a new base to an old update upload session. `no_change` means the effective content and requested Page state already match; return the existing URL. A rename with identical files is still a real update.

## Visibility and handoff

New Pages default to `organization` (workspace members); use `public` for external sharing or `private` for a draft. Pick the audience on create; on updates omit visibility or repeat its current value. Change an existing Page with `set_page_visibility`, which works on Pages this agent created: narrowing applies immediately, and widening returns `human_approval_required` with an `approval_url` for a person to confirm. Ask a person to change any other Page, or to add or remove individual people.

Return the Page URL and who can see it. If publishing returns warnings, resolve them before calling the Page finished.

## Errors and pending work

Check `isError` and branch on the stable JSON `error` code. Follow `recovery` when present, or the existing `next_action`. Do not match message wording. Fix invalid fields; wait for `retry_after_seconds` for throttles. Reopen expired upload sessions. Shrink bundles that exceed returned limits. Do not blindly retry permanent failures.

For newly authored slides, call `prepare_deck` with the title, ordered `{ id, html }` slides, optional shared CSS/assets, and optional canvas. It returns a normal inline bundle and does not publish, call a model, or prove readiness. Publish the returned bundle with `presentation: { "intent": "deck" }`; assemble larger decks locally and use signed uploads.

For an existing deck export, preserve its files and publish them directly with deck intent. Publication and presentation readiness are separate: only `ready` verifies controls for that exact version. Follow pending `presentation_follow_up` guidance with a compact version-bound `read_page`, and stop on a terminal status. Creation may set presentation policy; updates preserve policy, which a Page manager changes in Share settings.

Queued uploads or refreshes are pending, not completed. For live data load `topic: "live-data-connections"`: configure a spec, keep its revision identity, and preview that revision only when ready. CSV is refreshed by human upload.

## Comments and decks

Read a specific Page's queue with `read_comments({ page_id, queued_only: true })`. Read/export its latest bundle, revise it, then reply with `add_comment` to close the loop. Call `read_page_analytics` only when the user explicitly asks for readership, views, or reading performance of a specific SecondPage Page. It reads existing Page-view statistics under organization privacy controls; it does not collect ChatGPT conversations or activity. Do not call it for routine publishing, background analytics, or inferred user profiling.

Only slide-based documents use `<html data-sp-document-type="deck">` and stable `data-sp-frame` attributes on slide roots. Ordinary scrolling Pages do not use deck markers. When generating new markup, give major editable regions stable `id` and `data-review-target-id` values. Preserve exact user-supplied files when that was requested. Report publishing warnings and, for decks, the separate presentation status; a live URL proves publication, while `ready` proves presentation compatibility.
<!-- secondpage-core:end -->
