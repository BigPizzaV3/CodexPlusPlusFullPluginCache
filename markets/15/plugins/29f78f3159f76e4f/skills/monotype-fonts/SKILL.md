---
name: monotype-fonts
description: Process uploaded brand guidelines or typed font specifications with the Monotype Fonts connector, extract font names only from document text or reliable metadata, match fonts in Monotype inventory, show production status, and then guide the user to either reuse an existing library asset or create a new Web Project, Digital Ad, or FontSet. Use when a user uploads a brand guideline/style guide/brand book/type spec or asks to apply its fonts to Monotype library assets. Also use when the user asks for a site, page, ad, or other web output for a named brand or project without supplying a guideline or font names - look up an existing Web Project or Digital Ad by that name and use its fonts and CSS. Always require explicit user consent immediately before creating any new asset.
---

# Monotype Fonts

## Core rule

Use only the **Monotype Fonts** connector for font matching, production status, existing-asset lookup, asset creation, and any CDN/CSS output.

Support exactly these user-facing asset types:

- **Web Project** (`WebProject`)
- **Digital Ad** (`DigitalAd`)
- **FontSet** (`FontSet`; aliases: font list, fontlist, font set, fontset, list, font collection)

Never create a new asset without explicit user consent in the immediately preceding user turn.

Font identity must come from written font names or reliable file metadata, never from visual similarity.

## Brand-guideline entry flow

When a user uploads a supported brand guideline, style guide, brand book, or type specification, first extract and resolve the fonts as described below. Then present the asset action choice before any asset operation unless the user's prompt already unambiguously chooses both the action and asset type.

When action or type is not explicit, present these two paths compactly:

1. **Use an existing asset** — choose **Web Project**, **Digital Ad**, or **FontSet**, then provide the existing asset name.
2. **Create a new asset** — choose **Web Project**, **Digital Ad**, or **FontSet**. Collect or suggest the asset name, check for duplicates, show the creation summary, and ask for explicit consent before creation.

If the user's prompt already says, for example, “use existing Web Project Acme Site” or “create a new FontSet called Acme Brand Fonts,” do not ask them to choose again. Continue with the selected path while still enforcing every required approval below.

Do not infer **Digital Ad** unless the user explicitly selects or requests it. If the user chooses an action but not an asset type, ask them to select one of the three types rather than silently defaulting.

## Project-name fallback flow

Use this flow when the request needs brand fonts (for example a website, landing page, HTML ad, or other web output) but **no brand guideline is uploaded and no font names are written in the prompt**. Check the conversation's uploads first; an upload that is not a guideline for this brand does not count.

1. **Derive the lookup name.** Take the project, brand, campaign, or site name from the user's prompt (for example `VEXTOR` from "a launch page for VEXTOR"). If the prompt contains no usable name, ask for the guideline, the font names, or the existing project name in one question and stop.
2. **Look up existing assets.** Call `get_web_projects_by_name` with that name and `assetTypes` set to `["WebProject", "DigitalAd"]`, leaving `accessTypes` unset so owner and shared assets are both covered. Do not search FontSets in this flow: a FontSet has no CSS and cannot serve web output.
3. **Resolve the match.**
   - **One exact match** (ignoring case and punctuation) -> use it without asking.
   - **Several plausible matches** -> list only names, asset type, and created date (newest first), and ask the user to choose one. Never pick among them silently, and never merge fonts from several projects.
   - **No match** -> say no Web Project or Digital Ad with that name was found, show any close names the connector returned, and ask for the guideline, the font names, or the correct project name. Do not create an asset, and do not guess fonts.
4. **Read the chosen asset.** Call `get_asset_details` (or the connector-equivalent detail operation) for the chosen asset to get its fonts and `publishedCSSPath` / `cdnUrl`. Asset names are never a source of font identity; only the fonts the connector returns for the asset are.
5. **Check production status.** Make one `get_production_fonts_with_filters` call with `fontIds` set to all of the asset's fonts and show the status table, using `Project font` as the first column heading and `(in project)` as the match note. Production status stays informational.
6. **Use the asset.** Build the requested output with the connector-provided CSS/CDN link only, keeping all text live. Do not add, remove, or create anything on this path; it is read-only. If the user wants different fonts, switch to the existing-asset or new-asset path and follow its approvals.
7. **Be transparent about design tokens.** A project carries fonts, not colors or layout rules. When no guideline was supplied, say in one line that colors and layout are an original design choice rather than guideline-aligned, and offer to align them once a guideline is shared.

If a guideline or font names arrive later in the conversation, switch to the brand-guideline entry flow; written names and guideline text take precedence over the project's contents, and any mismatch is reported.

## Supported input gate

Accept font names only when they come from **text or reliable file metadata**.

Supported font-identity sources include:

- Font names written in the user's prompt.
- Text-extractable brand guidelines, style guides, brand books, or type specs such as PDF or DOCX.
- Embedded font metadata exposed by supported documents.
- Structured PDF text objects that expose font names.

Do not identify fonts from screenshots, JPG/PNG brand boards, flattened PDFs, scanned PDFs, or any other source whose typography exists only as pixels.

When the user supplies only image-based typography and no reliable text/font metadata, say:

> I can't identify fonts from an image — reading them off the artwork would be a guess, and the wrong family would get licensed. Send the guideline as a PDF or DOCX, or just tell me the font names.

Colors and patterns may still be read from image-based inputs as unlicensed design tokens. Only font identity is gated.

## Supported output gate

Do not render, export, or return raster artwork containing licensed type. Do not convert licensed type to outlines or paths.

For Web Project or Digital Ad, return only connector-provided CDN/CSS output. For FontSet, return no CSS/CDN output.

If the user asks for image artwork, offer code that keeps text live and loads the connector-provided webfont CSS instead of generating raster or outlined type.

## Connector requirements

Before resolving fonts or assets, confirm the Monotype Fonts connector is available. Every match, production status, existing asset result, asset creation, and CDN link must come from successful connector calls made in the current turn.

If the connector is unavailable, stop and say:

> I can't match these fonts without the Monotype Fonts connector - it's the only licensed source for this. Once it's connected I'll pick up from the font list.

Use the available Monotype Fonts connector operations, including when present:

- `font_search_by_name(name, userQuery, ...)`
- `get_production_fonts_with_filters(userQuery, fontIds, ...)`
- `get_web_projects_by_name(name, assetTypes, ...)` for existing-asset lookup and duplicate checks
- `get_asset_details(assetType, assetId, ...)` for an existing asset's fonts and published CSS/CDN path
- `create_web_project(name, fontIds, userQuery, assetType?, description?)` for Web Project / Digital Ad creation
- `create_font_list(name, fontIds, userQuery, description?)` for FontSet creation
- `font_search(fontId, userQuery)` only as an MD5 font-id fallback, never with a name

Pass the user's verbatim message as `userQuery` whenever the connector exposes that parameter.

## Font extraction pipeline

For every uploaded document, use this strict order:

1. **Read document text first.** Extract every explicitly written font family, weight, and style.
2. **Read embedded metadata second.** Inspect embedded font metadata/resources after text extraction.
3. **Merge with precedence.** Preserve every text-derived face and add metadata-only faces. If text and metadata conflict, keep the written document name and report the mismatch.
4. **Include prompt-specified font names.** Treat typed font names as explicit requested faces without skipping the document passes.
5. **Never identify by appearance.** Reject pixel-only typography for font identity.

Treat each weight/style as a separate requested face. Strip PDF subset prefixes such as `ABCDEF+` before searching while preserving the recognizable source name in the response.

## Match fonts in Monotype inventory

Call `font_search_by_name` once per distinct requested face and cache the result. Keep each result's `fontId`; it is needed for the production check and asset creation.

Normalize requested and candidate names by lowercasing and removing spaces, hyphens, underscores, and periods.

### Search ladder for generic or partial names

Many requested names are generic family names (for example `Helvetica`, `Futura`, `Gill Sans`, `Frutiger`) that exist in the inventory only under a fuller name such as `Neue Helvetica`, `Helvetica Now Text`, `Futura PT` or `Gill Sans Nova`. An empty first search is therefore not proof that nothing exists. Before marking a face as not found, work down this ladder and stop at the first step that returns results:

1. **Full face name as written** (for example `Helvetica Bold`).
2. **Family name only**, with the weight/style words removed (`Helvetica`).
3. **Common Monotype family variants** of that family name, one search each until results appear: `Neue <Family>`, `<Family> Neue`, `<Family> Now`, `<Family> Nova`, `<Family> LT`, `<Family> Std`, `<Family> Pro`, `<Family> PT`.
4. **Core family token alone** when the family name has several words (`Gill` for `Gill Sans`), accepting only candidates whose name still contains the full requested family name or a recognised variant of it.

A result counts as a candidate only when its name contains the requested family name (or one of the variants above). Never offer an unrelated family just because the connector returned it.

### Classify each face

- **Exact normalized match** -> accept silently.
- **No exact match but candidates exist** -> pick up to three candidates per face, ranked by: same family name first, then closest weight/style to the one requested (Regular/Roman when none was requested), then the most current family version (for example `Now` or `Nova` over older cuts). Ask **one combined substitution-approval question** covering every such face, with the top candidate marked as recommended. In the table, show the recommended candidate as `<name> (closest - awaiting approval)` until the user answers.
- **Nothing found after the full ladder** -> keep the requested face in the table with `Not found` in both the match and production columns. Do not auto-substitute another family.

Only exact matches and explicitly approved substitutions may be included in an asset.

## Check production status

Collect the `fontId` of every accepted face (exact matches and approved substitutions) and make one `get_production_fonts_with_filters` call with `fontIds` set to the complete list. Do not pass style IDs or the old `pimStyleIds` parameter.

Read `inProduction` fresh in the current turn. A matched font whose `fontId` has no returned production row is treated as not in production (❌).

Production status is informational only. It must not add, remove, or block a matched font.

## Required status table

Show the table before existing-asset use or new-asset creation.

Use exactly:

| Guideline font | Match in Monotype inventory | In Production |
| --- | --- | --- |
| Sohne Buch | Sohne Buch (exact) | ✅ |
| Gill Sans Regular | Gill Sans Nova Regular (closest - approved) | ❌ |
| Helvetica Bold | Neue Helvetica 75 Bold (closest - awaiting approval) | ❌ |
| Foundry Gridnik | Not found | Not found |

Keep one row per requested face. Do not expose font IDs, style IDs, hashes, or asset IDs.

## Existing asset path

When the user selects **Use an existing asset**:

1. Require an explicit asset type: Web Project, Digital Ad, or FontSet.
2. Require the existing asset name. If the prompt already contains it, use it directly.
3. Look up the exact name in the selected asset type with the Monotype Fonts connector.
4. If there is one exact match ignoring case and punctuation, use that asset.
5. If there are multiple plausible matches, show only the minimal distinguishing names/details and ask the user to choose.
6. If there is no exact match, report that and offer the closest matching asset names returned by the connector, if any. Do not create a replacement automatically.
7. Do not call any creation operation on this path unless the user explicitly switches to the **Create a new asset** path.

When reusing an existing Web Project or Digital Ad, return the connector-provided CDN/CSS path if the connector exposes it. When reusing a FontSet, return the list name and concise membership summary only; never imply CSS/CDN delivery.

## New asset path

When the user selects **Create a new asset**:

1. Require an explicit asset type: Web Project, Digital Ad, or FontSet.
2. Use the user-supplied asset name if present. Otherwise, suggest a sensible name derived from the brand/site/domain and ask for the name once.
3. Check the proposed name for duplicates within the single selected asset type before asking for creation consent.
4. If an exact-name asset already exists, do not create a duplicate. Offer to use the existing asset or ask for a different name. Only create a duplicate if the user explicitly requests a duplicate and then gives creation consent.
5. Show a concise creation summary containing:
   - asset type
   - proposed asset name
   - accepted font faces to be included
   - production warnings, if any
6. **Ask for explicit creation consent.** Use a direct question such as: `Create this Web Project now?` or `Create this FontSet now?`
7. Wait for an affirmative user reply such as `yes`, `create it`, `proceed`, `go ahead`, or equivalent.
8. Only after that affirmative reply, call the route-specific create operation.

### Consent invariant

The create operation must never run based solely on:

- the original request to create a skill or asset,
- an asset name supplied earlier,
- approval of font substitutions,
- approval of a duplicate name,
- or any inferred intent.

Consent must be explicit and specifically authorize the pending creation after the creation summary is shown. If the asset type, name, or font manifest changes after consent, show the revised summary and ask for consent again.

### Route-specific creation

After explicit consent:

- **Web Project** -> call `create_web_project` with `assetType=WebProject` or the connector-equivalent value.
- **Digital Ad** -> call `create_web_project` with `assetType=DigitalAd` or the connector-equivalent value.
- **FontSet** -> call `create_font_list`.

For FontSet, do not add WOFF/WOFF2 web-delivery containers when an eligible desktop font file is required. Use an eligible desktop match when available.

Never claim creation succeeded without a successful connector response in the current turn.

## Return results

For a successfully created or selected Web Project / Digital Ad, return the connector's exact `cdnUrl` / `publishedCSSPath` when available.

For a successfully created or selected FontSet, return the list name and concise membership summary only. Do not return or fabricate CSS, CDN URLs, `publishedCSSPath`, `@font-face`, or web-usage code.

Do not expose internal IDs, hashes, `fontId`, `styleId`, or `assetId`.

## User-question policy

Ask only questions required to move the selected flow forward:

- asset action/type choice when not explicit
- existing asset name when missing
- combined substitution approval for non-exact font matches
- new asset name when missing
- ambiguous existing-asset selection when lookup returns multiple plausible matches
- project-name fallback: which project to use when several match, or the guideline/font names/project name when nothing matches
- **mandatory explicit creation consent immediately before every creation call**

Do not ask for confirmation of facts already supplied by the user.

## Invariants

- Use only the Monotype Fonts connector for Monotype inventory, production status, asset lookup, creation, and CDN/CSS output.
- Source font identity from written names or reliable metadata, never appearance.
- Read document text before embedded metadata.
- Keep one row per requested face in the status table.
- Require explicit approval for every non-exact font substitution.
- Run the full search ladder before reporting a face as `Not found`; never show `—` in the status table.
- Check production status with `fontIds`, never style IDs.
- Treat production status as informational only.
- After a supported guideline upload, route to either existing asset or new asset and one of Web Project, Digital Ad, or FontSet.
- With no guideline and no font names, look up a Web Project or Digital Ad by the project/brand name before asking; that path is read-only, never picks silently among several matches, and never treats an asset's name as font identity.
- Never silently choose Digital Ad.
- Never create an asset when the user selected the existing-asset path.
- Never create an asset without explicit, current consent after showing the creation summary.
- If any creation-critical detail changes after consent, obtain fresh consent.
- Return only connector-provided CSS/CDN data for Web Project / Digital Ad.
- Never return CSS/CDN data for FontSet.
- Never rasterize or outline licensed type.
