---
name: reteno-email-editor
description: "Import packaged Fiteno templates into a Reteno organization as Saved Templates or regular emails. Read a Reteno email or template export manifest and clone, update, or translate it through Reteno MCP while preserving Reteno's original verbose builder HTML. Owns message-level work — translation and localization (translate a template, add a locale or language variant, including saved language-specific module replacement), subject, Reply-To, clones and copies, saved static module placement in HTML, and bounded visible-text or existing-image edits, including on an email that exposes no JSON model. Native preheader changes use email-model-editor; HTML localization owns its existing hidden preheader. Customising content or style on a model-bearing email is email-model-editor. New email creation uses email-from-reference."
---

# Reteno Email Editor

## Import Fiteno templates

When the user asks to add, upload, install, or copy the Fiteno library or a named Fiteno
template into a Reteno account, follow [Fiteno import](references/fiteno-import.md).
This imports the packaged native model unchanged; it uses its own create-and-verify
workflow and defaults to Saved Templates. Do not run HTML clone/edit steps or recompose
the model for this request. Resolve sender and existing copies separately per organization.

## Overview

Use explicit `read`, `clone`, and `update` modes:
- `read`: call `get_email_message_export(message_id)`, download the exported files through `python3 <plugin-root>/scripts/transfer.py download`, and write local files only.
- `clone`: duplicate the base email and all existing language variants by default, using their exported HTML and CSS. Only an explicit language restriction narrows the copy.
- `update`: update an existing Reteno email message by uploading the local HTML and CSS into a short-lived upload session, then finalizing the update.

This skill handles narrowly scoped copy edits, existing-image replacement, saved static module placement in existing emails, and message-level subject and Reply-To work. Keep the original verbose Reteno builder HTML. Do not rewrite the email as a new simplified document. For metadata-only requests, use the metadata tools below without downloading or uploading HTML/CSS.

## MCP callable discovery

Names in this skill identify MCP operations, not guaranteed callable tool names. A long
organization namespace can make the runtime shorten a callable and append a hash, removing
words such as `message` or `translation`. Use the exact name and schema advertised by the
current tool catalog; never construct a callable by joining the server and operation names.

Use tool discovery scoped to the selected organization's advertised MCP server, then
search names and descriptions with operation concepts such as localization or translation.
Print candidate names first and inspect the selected descriptor, keeping output small enough
to avoid truncation. If that search is empty, inspect the complete selected-server name list
and relevant descriptors before declaring the operation unavailable. Do not infer absence
from an exact-name or name-only search, or search other organizations to bypass the selected one.
Resolve the finalizer before preparing an upload. After compaction or resumption, rediscover
any callable whose exact advertised name and schema are no longer in context.

An unavailable local tool binding is not an MCP rejection. Rediscover the tool and
continue with the same target, original inputs, and operation ID; reuse the upload session
if still usable. Do not report a backend outage or missing MCP capability from that error.
If a request may have reached MCP, follow the live read-back and bounded recovery rules below
instead of assuming no write occurred. Never bypass the catalog with a raw content API call.

## Native preheaders

Native preheaders use `metadata.preheader` (`text` and boolean `fillSpace`) in the actual target's
current JSON model through `email-model-editor`. For text-only changes preserve `fillSpace`;
clear with `{text: "", fillSpace: false}`. Preserve unrequested preheaders. Never pass flat
`preheader` or `preHeader` fields to message metadata, creation, or translation tools.

Before a native write on a copy or translation, establish that the current target model matches
its latest exported body. Never write a base/source or stale model over translated content, or
rebuild the layout just to change a preheader. Native preheader writes require exact saved JSON
text/fillSpace and durable compiled-preheader verification. A native-only edit with a missing,
stale, or incompatible model remains incomplete unless the HTML localization path below applies.

## HTML localization preheaders

A full HTML translation/localization includes the existing natural-language hidden preheader.
Translate it together with the body through the HTML upload and translation finalizer, including
when completing an earlier partial localization. This is the scoped exception to native-only
preheader editing: it changes the durable HTML used for that locale and does not claim to refresh
its separate native editor model. Do not require editor hydration or recompile a native model
just to finish an HTML localization.

Use a fresh export of the actual locale (or base when first creating it). Require exactly one
canonical `span.esd-hidden-preheader` directly under `body`, containing the expected source copy.
Use the HTML helper's `block_type:"hidden_preheader"` with `match_mode:"single"`,
`expected_blocks:1`, and `expected_matches:1` to replace only that copy. HTML-escape the new text;
preserve the span, attributes, filler, CSS, links, merge tokens, and already-correct body bytes.
Do not insert a missing span, guess around duplicates/nested markup, or use this path for native
creation, native preheader-only work, or unrequested metadata changes. An already-correct value
is a verified no-change success.

Finalize with the same language-bound upload and Reply-To/sender recovery contract as the body.
Use a new logical operation ID for this new edit; retain it across identical retries. Require all
four translation receipt checks, then obtain a new export. Check that the single canonical
preheader equals the requested copy after decoding entities and ignoring only invisible filler;
check the entire requested body and subject, not only the replacements made in this retry. Run
`verify_reteno_email_translation.py <saved.html> --include-preheader --replacements <checks.json>`
on the fresh saved HTML, with source HTML/CSS checks as below. Do not scan an unrelated stale
native model as if it were the saved HTML result. Screenshots cannot verify a hidden preheader.

## Workflow

Resolve `<plugin-root>` and `<skill-dir>` from this installed skill location. Read [HOST.md](HOST.md) for transfers and image jobs. Host-native MCP owns OAuth; local helpers never load tokens.

For `clone`, resolve the source-to-copy mapping and language scope under "Clone scope and completion" before creating or uploading anything.

1. `read`: call the MCP tool `get_email_message_export(message_id=<ID>)` to fetch the source message export manifest by ID.
2. Use the manifest download links to retrieve the source files without pulling the full email body into the MCP tool response.
   - For every artifact download, run `python3 <plugin-root>/scripts/transfer.py download --url <manifest-url> --output <local-path>`.
   - Use the transfer helper, which binds signed tickets to the installed MCP origin and writes downloads atomically.
3. Write local files under a fresh run directory for image replacement, or under `output/reteno` for ordinary read/text workflows:
   - For existing-image replacement, create `output/reteno/runs/email_<ID>_<UTC_TIMESTAMP>/` and write all source artifacts, downloaded original images, generated replacements, and manifests inside that run directory.
   - Do not reuse existing `output/reteno/email_<ID>.*`, `output/reteno/runs/...`, or `output/images/...` artifacts for a new Reteno image replacement.
   - `email_<ID>.json`: full normalized email JSON from the export.
   - `email_<ID>.html`: the editable HTML from the export, when present. This is the file to edit.
   - `email_<ID>.css`: the dedicated Reteno `css` field from the export, when present.
   - `email_<ID>_<LANG>.json`, `email_<ID>_<LANG>.html`, and `email_<ID>_<LANG>.css`: per-translation artifacts when the export includes language variants. Treat each language variant as its own HTML/CSS artifact pair, not as a lightweight copy of the base message.
4. Edit the run-local `email_<ID>.html` file in place with the appropriate validated helper.
   - For visible text/button/menu copy and full-localization image `alt`/`title`, use `<skill-dir>/scripts/edit_reteno_email_html.py`.
   - Run `python <skill-dir>/scripts/edit_reteno_email_html.py --html <path> --replacements <json-path>`.
   - Run `python <skill-dir>/scripts/edit_reteno_email_html.py --html <path> inventory` FIRST, before writing any replacement JSON. It prints the editable-block census by type, every visible text run that no block covers (with a context excerpt), and the swept regions. Re-run it with `inventory --replacements <json-path>` to audit each `old`: `occurrences` counts the whole file, `document_sweep_matches` counts what a sweep would actually rewrite, and each listed match carries its offset, a context excerpt, and `in_document_sweep`. Read those excerpts and copy `document_sweep_matches` into `expected_matches`; do not echo a count back out of an error message.
   - The replacements JSON must contain objects shaped like `{"block_type":"text"|"button"|"menu"|"image","old":"...","new":"...","match_mode":"auto"|"single"|"responsive_pair"|"all","expected_blocks":2,"expected_matches":2}`. Omit the last three fields for the safe `auto` default.
   - Default `text_mode:"text"` treats `new` as literal visible text and escapes HTML characters. Supply ordinary text, not pre-encoded entities or markup. `old` still matches the exact serialized source. Use the explicit inline mode below only when preserving existing inline markup.
   - In `auto` mode, one match is edited normally. Exactly two matches are edited together only when their effective visibility is a complementary responsive pair: one desktop-only branch (`es-mobile-hidden`) and one mobile-only branch (`es-desk-hidden`). The visibility class may be on the block or any ancestor.
   - Treat that complementary pair as one logical block represented twice by Stripo. Preserve both branches and every `es-mobile-hidden`/`es-desk-hidden` class; never collapse the pair into one branch.
   - Use `match_mode:"responsive_pair"` to require the complementary pair explicitly. Use `match_mode:"all"` only with `expected_blocks` to authorize an exact larger count. Other duplicate matches remain ambiguous and fail closed.
   - `expected_blocks` counts BLOCKS. `expected_matches` counts MATCHES: visible text occurrences for `text`/`button`/`menu`, and matching `alt`/`title` values for `image`, so one image carrying the same value in both attributes counts as 2 and a responsive image pair counts as 4. Add `expected_matches` whenever `old` is short enough to recur inside one block, which no block count can see; the helper then fails closed on any other total. Omitting it keeps the existing behaviour of replacing every match in every selected block.
   - Use `block_type:"text"`, `block_type:"button"`, or `block_type:"menu"` to change only visible text inside exact `esd-block-text`, `esd-block-button`, or `esd-block-menu` class tokens. A nested `esd-block-menu-item` is not a separate editable block.
   - `block_type:"document"` sweeps the whole rendered `<body>` instead of one block, for email whose copy sits outside every `esd-block-*` td — an email not authored in the Stripo/eSputnik block editor keeps its copy in, say, a `div.esd-text`, which no block-scoped replacement can reach. The sweep replaces text through the same visible-text walk, so markup, attributes, `href` URLs, image URLs, plain comments and every byte outside a text node stay untouchable by construction; only the SCOPE widens.
   - A document sweep is authorized ONLY for full translation/localization of a language variant. NEVER use it for a bounded copy edit, a subject fix, or a single-phrase correction — use the block types for those, and if a bounded edit cannot reach its target, stop and report that instead of sweeping. Block scoping exists to bound PARTIAL edits; in a full locale creation every visible run is in scope by definition, which is the only reason the bound can be dropped.
   - A document replacement requires the `--allow-document-sweep` CLI flag: `python <skill-dir>/scripts/edit_reteno_email_html.py --html <path> --replacements <json-path> --allow-document-sweep`. Without it the run is refused. The flag makes sweeping a deliberate act visible in the command line and in the logs; it authorizes `block_type:"document"` only and never widens a block-scoped replacement.
   - Every document replacement REQUIRES `expected_matches`. Without block scoping there is no ambiguity partition left, so the occurrence count is the only bound on the edit; a document replacement without it is refused, and so is any count that does not match exactly. Take the number from `inventory --replacements`, field `document_sweep_matches`.
   - No document `old` may contain another document `old`. `"Order"` alongside `"Order summary"` is refused, because whichever runs first silently changes the other's count. Re-scope to phrases that do not overlap. The remaining document replacements apply longest-`old` first, so the result does not depend on the order they were written in.
   - A sweep does NOT reach `esd-hidden-preheader` spans. They are carved out of the swept region and must remain unchanged.
   - Every existing guard still applies inside a sweep: the `style`/`script`/`noscript`/`head` skip set, the Velocity/merge-token multiset check, the unbalanced-skip-markup and conditional-comment refusals, the enclosing-skip-markup entry check, and the nesting check. A sweep widens what the editor may reach, not what it may break.
   - Treat `<a>` anchor text inside editable text/button/menu blocks as translatable visible text, but preserve `href` URLs unless the user explicitly requests URL localization.
   - For full email translation/localization, inventory every non-empty `<img alt>` and `<img title>` value. Add `block_type:"image"` replacements for natural-language values on every image. One image replacement changes exact matching decoded values in both `alt` and `title` together, preserving `src`, `href`, classes, IDs, tracking attributes, and every unrelated attribute.
   - Preserve empty image attributes, dynamic/template expressions, filenames, technical labels, and product or brand names unless the user explicitly requests their translation. Image attribute replacements are exact-value matches; do not use them for substring rewrites.
   - The helper never rewrites text inside `style`, `script`, `noscript`, or `head`, even when that markup sits inside an editable block. That tag set is exactly the one `verify_reteno_email_translation.py` skips. Do not try to reach CSS or JS text through a copy replacement.
   - The two surfaces agree on that TAG SET ONLY, not on the whole notion of visibility. They still diverge in two places: the editor deliberately edits inside `<!--[if mso]>` conditional comments while the verifier treats the entire comment as invisible, so the phrase scan cannot catch a bad Outlook-branch translation and the merge-token check is the only net there; and a block commented out with a plain `<!-- -->` is still discovered and edited, while the verifier sees nothing there — harmless for rendering, since no client renders a comment, but the phrase gate cannot vouch for it either. Read a translated MSO branch yourself; no gate proves it. Ordinary body checks exclude hidden preheader text; explicit HTML localization preheaders use --include-preheader, and native changes use Native preheaders above.
   - A conditional comment must leave `style`/`script`/`noscript`/`head` balanced inside itself. The helper refuses one that opens such an element without closing it, because Outlook parses that region and every other client treats it as a comment, so the two client models genuinely disagree. Real builder markup keeps it balanced; if this fires, read the source region instead of retrying.
   - An editable block must leave that same markup balanced too. An unclosed `style` inside a block used to make the rest of that block invisible, so its tail shipped in the source language at exit 0 whenever another block satisfied the replacement. The helper now refuses instead; nothing is written.
   - A block must also START outside that markup. A `style` opened earlier in the document makes the block's own text stylesheet content, which the per-block walk cannot see; the helper checks the document-global depth and refuses, naming the block's offsets.
   - When a translated sentence changes word order around inline formatting, use `text_mode:"inline"` on a text/button/menu replacement (or an authorized document sweep) with `expected_matches`. Supply the complete exact source fragment and complete translated fragment, e.g. `Start at <strong>$!{levelText}</strong>` → `<strong>$!{levelText}</strong>から始める`. The helper preserves every tag/attribute byte and order, balanced inline markup, and each merge token's formatting/link context. It may redistribute copy before/inside/after those unchanged tags, including a previously empty text position. It cannot change structure, links, attributes, comments, or Velocity directives. Do not delete the source prefix and then drop an unsupported translated suffix.
   - Build final verification from every complete source/target copy entry supplied by the user, not just the subset emitted by an edit script. Preserve complete sentences, including text after closing inline tags. Recheck already-saved locales against those complete entries when recovering a partial batch; helper success alone does not prove that the translation plan included all requested copy.
   - Velocity/merge tokens stay BYTE-EXACT. Before and after every replacement the helper extracts the whole document's token multiset — `$name`, `$!name`, `${name}`, `$!{name}` with `.member` chains and `(...)` call syntax, plus `#set`, `#foreach`, `#if`, `#end` and the other VTL directives — and fails the whole run, writing nothing, when it changes. A raw substring edit such as `old:"Price"` over `$!formattedCardPrice` mints a dead token that renders empty at send time; work around the token, never through it.
   - That guard proves token PRESENCE, never PLACEMENT. A positional swap inside one edit — `"Use $!a then $!b"` rewritten as `"Use $!b then $!a"` — leaves the multiset equal and passes both the editor and the verifier. When a translation reorders a sentence that carries two or more tokens, read the result and confirm each token still sits with the phrase it belongs to.
   - An argument-free directive (`#end`, `#else`, `#stop`, `#break`) counts as a token only in a document that also opens a real VTL block with `#if(`, `#foreach(`, or `#macro(`, so prose like `#end of season sale` is editable in a template that carries no Velocity. In a document that carries both, that prose is indistinguishable from a directive and the edit fails closed; re-scope `old` to exclude the `#` word.
   - If the helper refuses a replacement for changing merge tokens, do not retry with a narrower substring that still straddles the token. Re-scope `old` to a phrase that excludes it, or leave that copy untranslated and report it.
   - Translate product and tool labels during translation/localization unless the user explicitly asks to preserve English brand labels.
   - For existing image replacement, first run `python <skill-dir>/scripts/edit_reteno_email_images.py --html <path> inventory`.
   - Replace exactly one existing image with `python <skill-dir>/scripts/edit_reteno_email_images.py --html <path> replace --index <one-based-index> --expected-src <old-src> --new-src <reteno-asset-url>`.
   - Add `--new-alt <text>` only when the user explicitly asks to change alt text during an image-source replacement. Full translation/localization uses `block_type:"image"` instead and does not replace the image source.
   - Keep base-message `subject` updates outside the HTML edit path. Write them only with `update_email_metadata(message_id=..., subject=...)`; no model upload is required for a subject-only change.
   - Preserve unrequested `esd-hidden-preheader` HTML. For full HTML localization, use the explicit HTML localization preheaders workflow above.
   - Do not change any HTML text, attributes, classes, IDs, language tags, `href` URLs, image URLs, image `alt`/`title`, comments, tracking markup, or block metadata outside the selected validated text, localization attribute, or image-source replacement.
   - Do not replace the file with a newly authored HTML document.
   - Do not remove Reteno wrappers, table structure, tracking markup, inline styles, conditional comments, or other verbose builder output.
   - If the helper reports a missing, unrecognized ambiguous, count-mismatched, or out-of-scope replacement, stop and report that validation failure instead of retrying with `apply_patch`.
5. If replacing an image, resolve and verify its hosted replacement before editing HTML:
   - For a generated replacement, follow the MCP image-job workflow in [HOST.md](HOST.md) with the selected current asset URL, intended changes, and source message/image identity. Use MCP `edit_image` with `size: "source"`, `textPolicy: "preserve"`, and compression by default.
   - Preserve the original image layout, composition, approved embedded text, dimensions, crop, and transparent alpha channel unless explicitly requested otherwise.
   - Require a completed `get_image_job` result and inspect the actual image. Record the jobId, final `image.url`, dimensions, and sha256 with the selected source. Do not require a local generator manifest, reupload, or recompress a completed MCP image.
   - For a user-supplied local replacement, call `prepare_image_upload(name=<asset-filename>)`, PUT that file through `python3 <plugin-root>/scripts/transfer.py upload`, and finalize with `upload_image(uploadSessionId=<same-ID>, name=<same-asset-filename>)`. Preserve the exact name. This manual upload path is separate from completed MCP image jobs.
   - Use only the verified final hosted image URL as `--new-src`. A pending or failed image job leaves the source image unchanged; report the missing replacement instead of substituting another asset.
6. `clone` or `update`: read the edited `html` file, prepare a Reteno upload session, upload `html` and the current exported `css` with `python3 <plugin-root>/scripts/transfer.py upload` to the returned signed HTTP endpoints, then finalize through Reteno MCP.
   - Use `python3 <plugin-root>/scripts/transfer.py upload --url <signed-upload-url> --input <local-path> --content-type <mime>`.
   - The helper defaults to `PUT`. Keep that default for Reteno email HTML and CSS uploads unless the upload session explicitly says to use another method.
   - For HTML uploads use `text/html; charset=utf-8`. For CSS uploads use `text/css; charset=utf-8`.
   - Do not send signed upload URLs through `/mcp`, and do not append synthetic `path=` query params.
   - Always upload the current exported message `css` field as the session's `css` artifact unless the user explicitly provides replacement CSS. After module placement, use its fresh export, including the saved module styles.
   - Never send empty CSS unless the source message CSS is actually empty.
   - Never extract, infer, rebuild, or synthesize CSS from the HTML document, `<head>`, or `<style>` tags.
   - When translations are present or requested, upload each language variant's HTML and CSS from that variant's exported artifacts. Do not silently reuse base-message CSS for translations.

Reteno MCP email upload manifests and successful finalizers expose a structured
`writeOperation` receipt.

- Keep the prepare receipt's `operationId` and use that exact value as the
  finalizer's `uploadSessionId`.
- Treat a finalizer as accepted only when its receipt has `status: "succeeded"`
  and its target ID and variant identify the requested message.
- `evidence: "readback_verified"` means Reteno MCP read the saved message back
  and matched it to the submitted content.
- `evidence: "upstream_ack"` means only that Reteno acknowledged the write. When
  final stored state matters, perform a fresh export and verify the requested
  content before reporting the overall execution as succeeded.
- If any requested write is missing, rejected, or cannot be verified, return a
  failed execution outcome even when other requested writes succeeded.
- Translation finalizers also require the Reply-To verification contract below;
  an acknowledgement or a matching content export alone cannot complete them.

## Reply-To

Reply-To is message metadata, separate from sender (`from`), subject, and HTML.

- Read `get_email_message_export` for the base and each requested locale. `messageId` is the actual private message ID; `originMessageId` identifies its base. `replyTo` is the stored value. When `replyToMetadata.available=true`, `effectiveReplyTo` inside that object is the effective value and `inherited` explains whether it comes from the base. `contentShared` and `baseContentShared` describe sharing; preserve those settings.
- A known exported null means blank. Missing fields or `replyToMetadata.available=false` mean unknown, never blank. Do not infer Reply-To from `from`, a different locale, or account defaults. A private-only locale can have a metadata-only JSON artifact: require its real HTML/CSS before copying or localizing content.
- For an explicit change, call `update_email_metadata(message_id=<actual base or variant ID>, reply_to=<exact string>)`. Omit `reply_to` to preserve it; use `reply_to=""` only for an explicit clear. Never send null or put `reply_to` inside a payload object. No HTML/CSS upload or model write is needed. Require `persisted=true`, `replyTo` in `updatedFields`, and `verification.verified=true`, with no MCP `isError`; for a Reply-To-only write require its `writeOperation.evidence="readback_verified"` as well.
- Use `list_email_interfaces().replyToSelection` when the user needs available choices. Require `available=true`, then use an available option's exact `value`; `clearValue` is the explicit clear value. A stored Reply-To need not appear in the options. Unavailable choices are not an empty list of valid senders.
- A shared locale override may return `reply_to_shared_conflict`. Do not unshare the family or update its base unless the user's requested scope includes that change. Report the conflict with the affected locale. Keep subject and Reply-To writes separate so their verification results stay clear. Preheaders use the native model workflow above.

### Localization and recovery

Validate the actual finalizer receipt with `python3 <plugin-root>/scripts/receipts.py translation --response <receipt.json> --expected-id <base-id> --language <normalized-locale> --operation-id <stable-operation-id>`.

- For ordinary localization in the same message family, **omit `payload.replyTo`**. MCP preserves an existing locale's own stored/effective value, including an intentional blank, and inherits the base's effective value for a new locale. Pass an exact string or `""` only for a requested override, an authorized repair, or copying a source locale to a new destination as described below. Never send null.
- Before the first finalizer, choose one unique `payload.replyToOperationId` for that logical message/language edit (a UUID is suitable). Keep it separate from `uploadSessionId`. Reuse the same key and identical original HTML, CSS, and metadata on recovery; a new intentional edit gets a new key. MCP retains recovery intent independently of short-lived upload sessions and local working files.
- A translation succeeds only when the same response has `persisted=true`, `verification.verified=true`, `replyToVerification.verified=true`, and `senderVerification.verified=true`, with no MCP `isError`. Its receipt must identify the requested base ID and language. `writeOperation.status="succeeded"` alone is insufficient, including when propagation leaves `persisted=false`.
- For a transient, malformed, or unverified response, make at most one recovery attempt through `update_email_message_translation` for the same target and original input. Reuse its operation ID, including the returned `replyToOperationId` when MCP supplied one. Reuse the original session if usable; if a new language-bound upload session is needed, upload the identical original files and metadata and keep the operation ID unchanged. Do not take a fresh snapshot of possibly damaged metadata as the new intent, issue a raw content PUT, or create another variant to bypass recovery.
- Respect structured errors (`isError`, `error.code`, `contentMayHaveChanged`, `recoveryRetained`). A conflict, identity/sharing change, or changed completed replay needs resolution, not a new key or different payload to force the write through. If recovery remains unverified, report a failed/partial result with the target, exact error, and operation ID; state when content may already have changed. If original retry inputs were lost with a replaced runtime, do not reconstruct them from partially changed state or claim recovery from a local file.
- Only a later fully verified `update_email_message_translation` response resolves an unverified translation. A fresh export is still required for final content checks, but language presence or matching HTML/CSS cannot substitute for the Reply-To receipt.

## Translations

Treat multilingual messages as a first-class workflow. Each translation is a separate variant that must preserve its own exported HTML, CSS, and Unicode text exactly unless the user explicitly requests a change for that language.

### Batch scope and continuation

Keep the requested languages and their body, subject, and preheader requirements through
retries and compaction. A request to retry or continue resumes that scope unless the user
explicitly narrows it. Read current variants before writes, preserve already verified work,
and finish the remaining authorized targets after a successful first write; a control write
does not create a new approval requirement. Existing approval boundaries still apply.

Keep each target's saved, unverified, or blocked state tied to its write receipt and fresh
read-back. Prepared files and successful uploads are not saved translations. Carry the
remaining targets, exact callable names, and unresolved operation IDs into a handoff; resolve
current tool availability and account state again after resumption.

Do not defer a language merely because its word order or merge-token position differs.
Inspect the actual editable text and supported helper operations while preserving tokens and
markup. If the required edit exceeds that surface, assess the available native model workflow
under `email-model-editor` and its freshness checks. Report a concrete unsupported edit only
for the affected target; continue independent supported targets without weakening any guard.
The final reply must name saved languages and remaining work, including incomplete preheaders.

### Requested saved modules

Use `place_email_module` for a requested saved static footer, header, or other library module in
an existing email, including a language variant. This is an HTML/CSS operation owned here; do not
route it to the JSON editor or add it to native email creation. Translating module text alone
does not replace its library binding. The export's `.json` envelope is not a native editor model.

During full localization, inventory the existing static module bindings and look for their saved
target-language counterparts. Prefer a clearly matching localized module over translating its
text under the old binding. If no reliable counterpart exists, report the retained binding or
unresolved requested replacement; never silently substitute a different module family.

1. Discover the selected organization's modules with `list_custom_blocks(query=...)`. A visible
   library identifier supplied by the user is `uid`; the numeric `id` in the matching result is
   the value used for MCP calls. If a UID query returns nothing, broaden to relevant name words
   or omit `query`, then match the returned `uid` exactly. An empty UID query does not prove
   absence. If `total` exceeds the returned list, refine the search before concluding a module
   is missing. Match language, brand, module family and `blockType`; language alone is insufficient.
   Use the uniquely matched numeric `id` internally. For missing or ambiguous matches, offer
   actual returned module names and ask only for the unresolved choice, not a numeric ID.
   The listing omits HTML/CSS; MCP fetches it internally.
2. Complete and verify ordinary HTML translation writes first. A new locale must already exist
   before placement. Export the actual destination's current HTML/CSS and identify exactly one
   compatible complete builder `td` using an HTML selector, for example
   `[esd-custom-block-id="<current-library-id>"]`. Native JSON UUIDs are not HTML IDs.
3. Call `place_email_module(message_id=<base-id>, language=<locale>, module_id=<library-id>,
   target_selector=<HTML-selector>, position="replace")`. For a direct email, omit `language`.
   Use `before`/`after` only for requested insertion beside a compatible single-cell builder row.
   Static STRIPE, STRUCTURE and CONTAINER modules are supported; dynamic product configurations
   are not. Do not delete through JSON first, patch IDs manually, or assemble module HTML/CSS locally.
4. Accept placement only with no MCP `isError`, `persisted:true`, `verified:true`,
   `verificationScope:"saved_html_css"`, and a succeeded `writeOperation` with
   `evidence:"readback_verified"`. Confirm the requested module, base/locale and actual
   `targetMessageId`. A successful receipt verifies saved content, styles, module binding and
   metadata; it has no `modelHash` and reports `nativeModelVerification:"not_performed"`.
5. Re-export the exact target and verify the actual localized content, correct
   `esd-custom-block-id`, intended synchronization markers, and absence of the old module in that
   slot. For later HTML edits, use this fresh HTML AND CSS as the new baseline; never upload the
   pre-placement snapshot. The text-translation check's unchanged-CSS rule applies before
   placement, or against this new baseline afterward: MCP may append required module-local CSS.

An identical placement retry only verifies the previous attempt; it never repeats the content
write. On an uncertain response, retry the identical request once. If still unverified, or if
MCP rejects a selector, CSS, dynamic content or a conflict, report the exact target/error and
whether content may already have changed. Do not bypass the rejection with manual HTML, JSON,
a different selector to force a retry, or another copy. Complete independent supported work and
report any unresolved requested module; a translated body does not satisfy a failed replacement.

HTML success does not require populated or current native JSON. Translation and placement can
both leave an existing model stale. Before any subsequent JSON edit (including a native preheader),
the user must open the exact target in the browser editor; use placement's `nextAction` when
available. Then acquire `get_email_model` for that actual ID and verify the latest body, module
content and `moduleId` against the fresh HTML before using its model/hash. If the native model
already demonstrably matches, no additional refresh is needed. Do not claim that a browser visit,
a repeated placement receipt, or library `synchronizable:true` alone proves native synchronization.
Report verified HTML work as saved; report required native work separately as incomplete until
this check passes. Do not undo or repeat a verified HTML write to obtain fresh JSON.

When `get_email_message_export(message_id=<ID>)` returns per-translation artifacts:
- read and preserve each translation separately
- write a local `.html`, `.css`, and `.json` artifact for each language variant
- keep the base message and each translation variant distinct throughout the edit and upload flow

For multilingual `clone` and `update`:
- upload HTML for every requested language variant from that variant's local edited HTML artifact
- upload CSS for every requested language variant from that variant's dedicated exported `css` artifact unless the user explicitly provides replacement CSS for that same variant
- never reuse the base message CSS for a translation unless that translation export truly has no dedicated CSS and the user explicitly accepts the fallback
- before finalize, verify that every requested language variant has both uploaded HTML and uploaded CSS attached to the upload session

Unicode preservation is mandatory for translations:
- preserve all Unicode characters exactly, including emoji
- do not transliterate, normalize away, replace with ASCII, or drop unsupported-looking glyphs
- if the source translated HTML or JSON contains emoji, the output must contain the same emoji unless the user explicitly asks to remove or replace them

For requested translation/localization, run a translation self-check before finalize. Copying an existing language variant unchanged is not a request to translate it or apply localization edits:
- compare source versus output for each requested language variant
- confirm CSS is present for every variant
- confirm unchanged translated text preserved the same emoji content
- confirm visible text includes translated anchor text and translated product/tool labels unless the user explicitly requested English brand labels
- confirm visible text inside every `esd-block-menu` is localized
- confirm every natural-language image `alt` and `title` value is localized while empty, dynamic, technical, product, and brand values intentionally preserved by scope remain unchanged
- run `<skill-dir>/scripts/verify_reteno_email_translation.py <localized-html> --replacements <replacement-json> --source-html <source-html> --source-css <source-css> --localized-css <localized-css>` before upload/finalize when the task is full email translation/localization; this proves the old text is gone, the new text is present, the responsive visibility signature is unchanged, the Velocity/merge token multiset matches the source, and CSS is byte-identical
- create a fresh upload session for each language with `prepare_email_message_upload(operation="update", message_id=<ID>, language=<CODE>)`, upload that variant's HTML and CSS, then finalize it with `update_email_message_translation` using the same `uploadSessionId`
- follow "Localization and recovery" for Reply-To preservation, the four required receipt checks, and retry identity
- if the self-check fails, correct and rerun the local validation before any upload; do not finalize invalid content

Translation failure checklist:
- missing CSS in any requested translation is a hard blocker
- dropped or altered emoji in unchanged translated text is a hard blocker
- leftover English visible link labels or tool/product labels from the source language are a hard blocker unless explicitly preserved
- leftover source-language menu text or natural-language image `alt`/`title` values are a hard blocker unless explicitly preserved
- a malformed or unexpected `update_email_message_translation` response remains a hard blocker unless a later write for the same exact message and language succeeds
- a follow-up export that lists the language is verification evidence only; it never resolves a failed write because the language may have existed before the attempted update

## Subject adaptation

A full brandkit customization or rebrand adapts the message `subject`; a single targeted edit ("change the link color", "swap the header logo") leaves it alone. A rebrand that repaints the body and ships the source brand's subject — or the template's scaffolding subject — is the same defect as leftover source-brand body copy, one field further out. This section also governs the hand-off a model-editor rebrand makes when it reaches the message-level fields it cannot write itself.

Derive the new subject from three inputs and nothing else:
- The campaign type, inferred from the email's own content — the exported HTML's visible copy, blocks, and CTAs (an abandoned-cart reminder, a welcome, an order confirmation, a promotion, a newsletter). The message `name` and the current `subject` corroborate that inference; the brand's vertical, the org name, or the account's other messages never establish it on their own. State the inference and the evidence that carried it in the report. When the content genuinely does not say which campaign this is, write a subject that carries no campaign-specific claim rather than guessing one — and never leave a scaffolding subject standing because the type was unclear.
- The brandkit's voice and business context: `brand.brandVoice` (`toneOfVoice`, `styles`, `rulesToFollow.allowed`, `rulesToFollow.forbidden`) and `brand.businessContext` (`customerValue`, `revenueModel`). Derive only from the fields actually present — `brandVoice` licenses a tone/register rewrite, `businessContext` licenses the vertical and customer-value correction. With neither field present or non-empty you have no verified voice to write from: keep the existing subject and record that reason — unless it is scaffolding, which is always replaced, or source-brand residue, which is never "preserved" (both below).
- The language: write in the language of the email's existing copy. Rewriting a subject is not translating it, and it never changes the message's language. `brand.brandVoice.defaultLanguages` decides the language only when the email carries no readable copy language to follow.

Always replace, on a brandkit customization — a scaffolding subject is never kept and never blanked:
- an obviously scaffolding subject — `Test subject`, `test`, the template's own name, an empty or whitespace-only subject
- a placeholder-grammar token (`subject_placeholder`, a `..._or_blank` literal). The `_or_blank` suffix does not reach the subject: an empty subject is not a valid state for a sendable message, so the token is replaced with real copy like any other scaffolding, never blanked
- a subject that already reads as deliberate copy: on a full rebrand it is the source brand's copy, replaced under the same doctrine as source-brand body copy, with before → after recorded

**The no-voice case still replaces scaffolding.** With neither `brandVoice` nor `businessContext` the replacement simply derives from less — the campaign type plus the target brand's name, and nothing else, producing a plain subject that makes no claim it cannot support (the same shape as the ambiguous-campaign fallback above). A missing voice is a reason to write a plainer subject, never a reason to leave scaffolding in the message.

**A kept subject that names the source brand is residue, not a preserve.** When the existing subject survives (no voice fields, or a subject already on-voice) but still carries the SOURCE brand's name, phone, email, address, or support URL, dispose it exactly as source-brand body residue: replace the literal with the target brand's verified value when the brandkit supplies one, and otherwise record a blocking deferral and ask for that value. "Preserved" is not available to a subject that names the wrong brand.

Keep out of the new subject: any offer, discount, price, percentage, deadline, urgency claim, guarantee, or product fact the email does not already carry; any term in `rulesToFollow.forbidden`; any Velocity/merge token or personalization variable that was not copied byte-exact from the existing subject. Keep it to subject length — one line, not a sentence of body copy.

Mechanics — base subject is native message metadata:
- For a subject-only change, call `update_email_metadata(message_id=<ID>, subject=<value>)` with no upload session.
- A subject-only `update_email_metadata` must return `persisted:true`, `subject` in `updatedFields`, and `verification.verified:true` with fresh checks for `subjects`, `editableHtml`, `css`, `metadata`, and `otherLocales`. Its `writeOperation` must report `status:"succeeded"` and `evidence:"readback_verified"` for the requested message. A successful HTTP response or Reply-To check alone does not verify the subject. Preserve a failed or unavailable receipt as incomplete; a later read cannot turn it into a successful write.
- After a verified subject receipt, fetch a fresh export and compare the requested subject byte-for-byte, with unchanged HTML/CSS and unrelated metadata/locales. Cross-check `get_email_model(message_id=<ID>).messageMetadata` when a native model is available. A missing native model does not require an HTML rewrite; the subject-only tool's verified private read-back and fresh export are the relevant saved surfaces.
- A subject-only write cannot desynchronize a structured model because no HTML or model artifact is uploaded. If the task also changes a JSON model, finalize and verify the staged model first, then call `update_email_metadata` as a separate write. These writes are not atomic; report a subject failure as a partial result without retrying or undoing the already-verified body edit.
- Language variants carry their own subjects. Adapt the subject of each variant this customization actually rebranded, in that variant's own language, through that variant's language-bound session and `update_email_message_translation`. A variant the run did not touch keeps its subject — say so in the report instead of leaving it unmentioned.
- Verify base subject through `get_email_model.messageMetadata` and the fresh export.
- Report the subject as its own line item: before → after, plus the campaign-type inference and the voice/context facts that drove it. A subject write that fails is reported plainly as a partial result with the tool's verbatim error — never dropped in silence, never retried by hand-editing HTML, and never a reason to unsettle writes that already landed.

## Mode Details

### `read`

Call `get_email_message_export(message_id=<SOURCE_ID>)`, download the exported artifacts from the manifest links with `python3 <plugin-root>/scripts/transfer.py download`, then write the local files listed above.

For ordinary text workflows, edit this file:

- `output/reteno/email_<SOURCE_ID>.html`

For image replacement workflows, create and edit the fresh run-local file:

- `output/reteno/runs/email_<SOURCE_ID>_<UTC_TIMESTAMP>/email_<SOURCE_ID>.html`

Treat the current run's HTML file as the source of truth. Preserve its overall structure and use `<skill-dir>/scripts/edit_reteno_email_html.py` to edit only text nodes inside existing `esd-block-text`, `esd-block-button`, and `esd-block-menu` blocks, plus exact natural-language image `alt`/`title` values during full translation/localization.
For image tasks, inventory existing images with `<skill-dir>/scripts/edit_reteno_email_images.py` and replace only the selected existing image `src` after Reteno MCP returns a hosted asset URL.
Do not use `apply_patch` on `output/reteno/*.html`.
Treat base `subject` as a native metadata update outside the HTML edit path. Keep all hidden preheader HTML unchanged.

Do not treat `email_<SOURCE_ID>.html` as the CSS source. CSS comes from the separate Reteno `css` field only.
Do not expect Reteno storage field names in the exported JSON. Current `reteno-mcp` exposes the editable document as `html`.
When translation artifacts are present, read them into separate per-language local files and preserve each translation's dedicated CSS alongside its HTML.

### `clone`

#### Clone scope and completion

- **A duplicate includes the base email and all existing language variants.** Discover the languages from each source export; they are the requested variants even when the user says only "duplicate template". Use only the base when explicitly requested, or only the specified variants when the user supplies a language subset. Copy each variant's existing content, subject, sender, and dedicated CSS unchanged unless the user requests edits. Preserve preheaders during the HTML copy; requested changes use the Native preheaders workflow above.
- Reuse information already supplied in this request or conversation. Ask for missing information together: source IDs or name pattern; the email-number range when a series is ambiguous; and the destination naming pattern when renaming is requested but unspecified. Do not ask for a range when explicit IDs or an unambiguous request to copy all matching emails already resolves it. State "I'll include all existing language versions" instead of requiring an extra yes/no answer.
- Before any write, resolve the live source inventory into a source ID → destination name mapping with each source's language set. Preserve email numbers and zero padding when substituting a name pattern. An explicit range must match every requested number exactly once; ask about missing or ambiguous matches instead of copying a partial or broader series. Search regular emails as well as reusable templates when the user's word "template" does not match the stored classification, and preserve the source classification through the top-level `template` argument.
- Check for prior copies before creating: use destination IDs already returned in this conversation first, otherwise search exact destination names. A name alone does not authorize overwriting an existing email. Reuse a target only when the conversation and live content establish that it is this request's previous copy; ask if identity is ambiguous. Keep the source read-only. State the resolved count, range, naming change, and language scope briefly; this summary is not an additional approval gate.
- Complete one source at a time: create its base once with the procedure below, retain the returned destination ID, then prepare and finalize each included translation against **that new ID**, not the source ID. Each translation uses its own language-bound upload session. Finish verification for this copy before creating the next base.
- After all included languages are written, fetch a fresh destination export. Check its name and source classification, the exact expected language set, base and per-language subjects/senders, HTML content and dedicated CSS. Use normalized HTML hashes when available because Reteno can normalize markup; inspect exported content when hashes differ. Verify preserved text, links, images, and template tokens rather than accepting a list entry or a new ID as proof of a complete copy.
- A receipt with `verification.verified=false` remains unverified. For translations, use the bounded recovery in "Localization and recovery" and require all four receipt checks; a later export alone cannot complete it. Do not create another base just to get a fresh read.
- If permission is denied or expires, a write fails after its allowed retry, or verification remains unresolved, stop the batch and report an incomplete copy with the source → destination IDs, completed languages, unresolved languages, and unstarted emails. Preserve the existing permission boundary. On continuation, inspect those same destination IDs and finish only the missing or unverified work; already verified copies are not created again. Local files are disposable: recover unchanged source artifacts from live exports, but follow "Localization and recovery" for a pending finalizer's original inputs. Include the mapping in the user-visible result so the next execution can find the copies.

Use the fetched source message as defaults, load the edited local `html` file, call `prepare_email_message_upload(operation="create")`, upload the edited `html` and source `css` with `python3 <plugin-root>/scripts/transfer.py upload`, then create the message with Reteno MCP `create_email_message`.

Allowed changes for `clone` are limited to:
- text inside existing `esd-block-text` blocks
- text inside existing `esd-block-button` blocks
- text inside existing `esd-block-menu` blocks
- exact natural-language values in existing image `alt` and `title` attributes for full translation/localization
- one selected existing image `src`, only after uploading the replacement image through Reteno MCP image upload
- that selected image's `alt` attribute only when explicitly requested
- message `subject`
- message Reply-To through the metadata or copied-locale paths above

Everything else must stay byte-for-byte unchanged where practical, including layout markup, links, non-selected images, classes, attributes, CSS, and Reteno config blocks.

Build the payload with these defaults unless the user explicitly overrides them, or unless a brandkit customization adapts the `subject` per "Subject adaptation":

- `name`
- `from`
- `subject`
- `languageCode`
- `tags`
- `subscriptionsKeys`
- never flat `preheader` or `preHeader` fields; use the preheader workflow for the chosen native or HTML localization path

The uploaded `css` artifact is mandatory: always copy it from the source message's dedicated `css` field. Do not omit it, clear it, replace it with empty CSS, or derive it from HTML during clone.
For multilingual messages, the uploaded CSS artifact is mandatory for every requested translation variant as well. Use each translation's dedicated exported `css` artifact.

Send this write payload shape:

- `uploadSessionId` = returned by `prepare_email_message_upload`
- other copied metadata fields as listed above

Do not manually send `html` or `css` to `create_email_message`. Current `reteno-mcp` requires those files to be uploaded first and finalized by `uploadSessionId`.
For requested preheader changes after a clone, follow the Native preheaders workflow on the new copy's current model. If that model is unavailable or does not match the copied body, report the preheader as incomplete.

Reply-To preservation for localization does not copy metadata from a different source family. Before creating a copy, require available Reply-To metadata for its source base and every included locale. After creating the destination base, copy the source base's `replyToMetadata.effectiveReplyTo` with `update_email_metadata(message_id=<DESTINATION_ID>, reply_to=<source value>)`, converting a known null to `""`. Verify that write before adding languages. For each copied locale, explicitly set `payload.replyTo` to that source locale's effective value (known null becomes `""`); omitting it would inherit the destination base and lose distinct source values or intentional blanks. Preserve sharing settings; report an incompatible shared-value conflict instead of silently changing them. Verify source versus destination effective Reply-To for the base and every copied locale in the final export.

Because this skill preserves the original verbose Reteno HTML, the uploaded message should retain the builder-style markup rather than a stripped custom document.

After the base is created, finalize every included translation separately on the returned destination ID using `prepare_email_message_upload(operation="update", message_id=<DESTINATION_ID>, language=<CODE>)` and `update_email_message_translation`. Preserve its exported subject and sender in the translation payload. Each session must contain that language's HTML and CSS; preserve unchanged Unicode text exactly. The clone is complete only after the read-back checks above pass for the base and every included language.

If the user asks for the created message link or preview, call `get_email_message_view_link` for the new message ID.

### `update`

Use the same source-default behavior as `clone`, but call `prepare_email_message_upload(operation="update", message_id=<TARGET_ID>)`, upload the edited `html` and source `css` with `python3 <plugin-root>/scripts/transfer.py upload`, and then call Reteno MCP `update_email_message` for the target message ID instead of creating a new message.

Always include the original source message `css` field in the uploaded CSS artifact unless the user explicitly provides replacement CSS. Do not extract CSS from the HTML document.
Send `uploadSessionId`, not `html` or `css`, to `update_email_message`.
For multilingual updates, apply the same rule to every requested translation variant and preserve each translation's dedicated CSS artifact separately.

Allowed local HTML changes for `update` are the same as `clone`: edit only text in existing `esd-block-text`, `esd-block-button`, and `esd-block-menu` blocks plus exact natural-language image `alt`/`title` values for full translation/localization. Saved module placement uses `place_email_module` under "Requested saved modules" after these writes. Apply a requested base `subject` change separately through `update_email_metadata` after the HTML finalizer succeeds, then read it back. Explicit Reply-To changes use the metadata-only path above; do not re-upload content for them.
For image replacement, the same selected-image rule applies: replace exactly one existing image `src` with a Reteno-hosted asset URL, and change `alt` only when explicitly requested.

`update` needs two IDs:
- source ID: the message you read and use as the default field source
- target ID: the existing message to overwrite with the edited local HTML

Before finalizing a multilingual update:
- verify every requested translation variant has uploaded HTML and uploaded CSS
- verify unchanged translated text preserved emoji and other Unicode characters exactly
- resolve local content validation failures before upload; recover an unverified finalizer only through "Localization and recovery"

## Defaults and Notes

- Use Reteno MCP tools, not direct API calls or local HTTP scripts.
- Use the MCP tool `get_email_message_export(message_id)` for reads.
- Use `python3 <plugin-root>/scripts/transfer.py download` for every manifest artifact download.
- Use `python3 <plugin-root>/scripts/transfer.py upload` for every signed Reteno HTML and CSS upload URL.
- Use the transfer helper for signed Reteno tickets; never reuse a ticket across account or environment connections.
- Never route signed Reteno upload URLs through `/mcp`, and do not invent `?path=` wrappers for them.
- Keep text-only editing centered on `output/reteno/email_<SOURCE_ID>.html`; keep image replacement editing centered on a fresh `output/reteno/runs/email_<SOURCE_ID>_<UTC_TIMESTAMP>/email_<SOURCE_ID>.html`.
- Never use `apply_patch` on exported Reteno HTML artifacts under `output/reteno/`.
- Use `<skill-dir>/scripts/edit_reteno_email_html.py` for visible text, button/menu copy, and exact image `alt`/`title` localization inside exported Reteno HTML. It edits a recognized desktop/mobile responsive pair together while preserving its visibility classes; unrelated duplicate matches still fail closed.
- Use `<skill-dir>/scripts/verify_reteno_email_translation.py` to fail full translation/localization outputs that retain known English source phrases in visible text or image `alt`/`title`, omit replacement text, alter the source responsive visibility signature, change the source Velocity/merge token multiset, or change CSS. Pass `--source-html` for the token and visibility comparisons; without it neither runs.
- Treat the editor's skip set (`style`, `script`, `noscript`, `head`) and its merge-token fail-closed guard as hard scope limits, not helper quirks. Preserve merge/Velocity tokens byte-for-byte.
- The merge-token guard proves token presence, not token placement, and neither surface reads inside `<!--[if mso]>` for forbidden phrases. Both remain reader checks; do not report a translation as verified on gate output alone.
- Pin occurrence counts with `expected_matches` on short `old` phrases. `expected_blocks` alone cannot see two hits inside one block, and `auto` mode replaces both without reporting the difference.
- Run `edit_reteno_email_html.py --html <path> inventory` before writing replacements, and `inventory --replacements <json-path>` before applying them. The census names what block scoping can reach; the uncovered-run list names what it cannot; `document_sweep_matches` is the number `expected_matches` must carry.
- `block_type:"document"` plus `--allow-document-sweep` is the sanctioned path for email whose copy sits outside every `esd-block-*` td, and it is authorized ONLY for full translation/localization of a language variant. A bounded copy edit that cannot reach its target is a report, never a sweep.
- Every document replacement carries `expected_matches`, no document `old` may contain another, and hidden preheader spans stay outside the sweep. The Reteno write path never needed blocks — `prepare_email_message_upload(operation="update", language=<code>)` uploads the whole variant HTML — so the block requirement is an authoring guard, and the sweep is the explicitly-authorized second contract, not a loophole.
- Use `<skill-dir>/scripts/edit_reteno_email_images.py` for existing image inventory and image `src` replacement inside exported Reteno HTML.
- Follow [HOST.md](HOST.md) for generated image replacements; use the current authorized asset URL as the MCP input and preserve source dimensions, embedded text, and transparency by default.
- A completed MCP image job supplies the hosted URL and image metadata. Check the job result and visually inspect the asset; never substitute stale local artifacts or a guessed URL.
- If the user asks to replace an image but does not identify which current image to replace, inventory images and ask for the target image instead of guessing.
- Image replacement may only target an existing `<img>` tag. Do not add image blocks, remove image blocks, move blocks, or rewrite builder markup.
- Image `src` replacement must use a final hosted URL from a completed MCP image job or MCP `upload_image` for a user-supplied local file.
- Reteno image upload finalization must use the exact same `name` passed to `prepare_image_upload`; never finalize with a shortened or alternate filename.
- Treat base `subject` as a native metadata update through `update_email_metadata`, outside the HTML edit path.
- A full brandkit customization adapts the `subject` from the email's own campaign type plus the brandkit's `brandVoice`/`businessContext`, in the email's existing language; a single targeted edit leaves the subject alone. A scaffolding subject (`Test subject`, empty, a placeholder token) is always replaced during a brandkit customization. See "Subject adaptation".
- A base subject-only write has a metadata-only path: call `update_email_metadata` with a flat `subject` argument and no upload session. Never re-upload HTML/CSS for it, and never trust the acknowledgement without a fresh read-back.
- Preserve unrequested hidden preheaders; requested full HTML localization uses HTML localization preheaders above. Native edits use Native preheaders.
- Treat anchor text inside editable text/button/menu blocks as translatable content, and preserve `href` URLs unless URL localization is explicitly requested.
- During full translation/localization, translate meaningful natural-language `alt` and `title` values on every image with `block_type:"image"`; one replacement keeps matching `alt` and `title` values aligned. Preserve empty, dynamic, technical, product, and brand values unless explicitly requested.
- Translate product and tool labels during translation/localization unless the user explicitly asks to preserve English brand labels.
- If the helper reports a missing, ambiguous, or out-of-scope replacement, stop and report that validation failure instead of retrying with `apply_patch`.
- For every translation variant, call `prepare_email_message_upload(operation="update", message_id=<ID>, language=<CODE>)` to create a fresh session bound to that language. Upload only that variant's HTML and CSS, then finalize with `update_email_message_translation` using the same `uploadSessionId`.
- Treat malformed JSON and every other unexpected `update_email_message_translation` response as a failed write, not as confirmation that Reteno accepted it.
- Recover a failed translation only under "Localization and recovery": the same operation ID and original input, at most one recovery attempt, and all four receipt checks required for success.
- Use a fresh `get_email_message_export(message_id=<ID>)` after successful writes to verify final state, but never use export presence to turn a failed write into success. One export covers every language of that message, so perform final family verification **once per message after all of its languages are written**. Requested module placement also requires the fresh target baseline and read-back described above.
- Save that final successful verification export as `output/reteno/email_<ID>_verify.json`.
- Persist the original Reteno verbose HTML structure. Never simplify, re-template, prettify, or regenerate the document from scratch.
- Local text edits change only text inside existing `esd-block-text`, `esd-block-button`, and `esd-block-menu` blocks plus exact natural-language values in existing image `alt`/`title` attributes during full translation/localization. Whole saved modules use `place_email_module`, never local HTML surgery. Base `subject` changes use native message metadata, not HTML.
- During local text edits, do not add blocks, remove blocks, move blocks, rename classes, alter `href` URLs unless URL localization is requested, alter image sources, alter image `alt`/`title` outside an authorized localization replacement, alter `lang`, alter head contents, alter inline styles, or alter config/tracking sections.
- Unless the user requests overrides, or a brandkit customization adapts the subject, copy source values for `name`, `from`, `subject`, `languageCode`, `tags`, and `subscriptionsKeys`.
- For local edits and cloning, persist the current exported message `css`, including any styles saved by prior module placement. Missing or stale CSS can strip styling even if the HTML structure is preserved.
- Read CSS from the dedicated Reteno `css` field when fetching the message, persist that same field on writes, and never reconstruct CSS from the HTML.
- For multilingual messages, apply the same CSS preservation rule to every translation variant independently.
- Current `reteno-mcp` exports expose the editable document as `html`.
- Local HTML/CSS content writes require an upload session. Upload `html` and `css` first, then finalize with `uploadSessionId`; `place_email_module` composes and saves its content internally, while base subject-only and explicit Reply-To writes use native metadata without an upload.
- For Reteno email HTML and CSS session artifacts, default the upload helper to `PUT` and only override that method if the upload session explicitly says otherwise.
- `get_email_message_export` returns a manifest with signed download URLs for `json`, `html`, and `css` artifacts, plus per-translation artifacts when present.
- Per-translation exports must be preserved as separate artifacts. Do not collapse them into the base message or assume the base CSS covers translated variants.
- Preserve emoji and other Unicode characters exactly across translated variants unless the user explicitly asks for a language-specific change.
- Do not inject duplicate CSS into the HTML document, and do not remove trailing Reteno blocks such as `esd-config-block`.
- This skill supports reading, cloning, updating, and optionally retrieving a view link.
- Existing-image replacement supports completed MCP image jobs and manually uploaded user-supplied images.
- Do not use JWT/content upload endpoints, Slack-hosted URLs, local paths, OpenAI temporary URLs, or filename-based image URL rewriting in this skill.
- Run live regression checks only on dedicated test assets in the confirmed organization.
- If an uploaded message looks stripped, that means the local `email_<ID>.html` file was replaced with simplified markup before clone/update. Reteno stored exactly what was sent.

## Resources

Bundled helper scripts are part of the primary workflow in this revision:
- `python3 <plugin-root>/scripts/transfer.py download` for signed export artifacts
- `<skill-dir>/scripts/edit_reteno_email_html.py` for validated visible text, button/menu copy, exact image `alt`/`title` localization, complementary desktop/mobile responsive-pair edits, the `inventory` subcommand, and the `--allow-document-sweep` whole-body localization sweep inside exported Reteno HTML
- `<skill-dir>/scripts/verify_reteno_email_translation.py` for replacement completeness, image attribute and visible-source checks, responsive visibility preservation, and CSS byte equality
- `<skill-dir>/scripts/edit_reteno_email_images.py` for validated existing image inventory and replacement inside exported Reteno HTML
- `python3 <plugin-root>/scripts/transfer.py upload` for signed HTML and CSS upload-session artifacts
