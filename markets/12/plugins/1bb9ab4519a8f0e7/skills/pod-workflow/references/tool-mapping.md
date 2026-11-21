# Listing check and export tools

## Questions about the rules

Call `get_listing_rules` with `{}` when the user asks which formats or checks are supported, or asks about limits. Its returned `version`, `originType`, `note`, counting definitions, `resourceLimits`, and `platforms` describe the actual current profiles. No platform is needed for this general question. Explain that these are the publisher’s workflow rules rather than a live marketplace-policy or legal check. Do not force a creative listing for a rules question.

## Purpose and limits

`validate_listing_batch` checks structured listing drafts against this plugin’s versioned drafting profiles. It is ordinary server-side validation, not an AI model, a marketplace connection, legal advice, trademark clearance, or a guarantee of platform approval. The ChatGPT workflow performs the limited screening and writes the creative text. Do not claim the server screened the idea for IP rights or checked live marketplace policy.

`export_listing_batch` creates CSV text from supported listing fields. It does not publish listings, log in to a marketplace, or guarantee that a marketplace can import the CSV. The server does not create persistent projects. Use only the actual result and any download interface the host displays; never invent a file URL.

## Inputs

Each tool accepts one selected `platform` and an ordered `listings` array. Use these canonical values:

| User intent | `platform` |
| --- | --- |
| Etsy PNG | `etsy_png` |
| Etsy Shirt | `etsy_shirt` |
| Merch by Amazon / MBA | `merch_by_amazon` |
| TeePublic | `teepublic` |
| Redbubble | `redbubble` |

For a creative idea or a check/export requiring a selected platform, the workflow asks the user to disambiguate Etsy and to choose a supported platform if none is provided. Do not silently choose a subtype. Do not split one idea into different platforms without a user request.

Send only generated draft fields needed for the requested check/export. Do not send the conversation, uploads, reference images, marketplace credentials, buyer details, or unrelated personal information. A design phrase may be included in its generated title or design prompt; avoid adding personal data that is not needed for the listing.

Per-item field mapping:

| Platform | Required listing fields |
| --- | --- |
| `etsy_png`, `etsy_shirt` | `title`: string; `tags`: array of 13 tag strings; `description`: string |
| `merch_by_amazon` | `title`: string; `bullet1`: string; `bullet2`: string |
| `teepublic` | `title`: string; `mainTag`: string; `supportingTags`: array of 15 tag strings |
| `redbubble` | `title`: string; `tags`: array of 15 tag strings |

An optional `id` preserves association with the input item. Use stable simple IDs such as `trend-1`, `trend-3`; never renumber an output trend merely because a stopped item was skipped. `designPrompt` is an optional string when exporting an accompanying artwork prompt. Do not include tool-only validation notes inside a product description. Omit irrelevant platform fields rather than filling them with empty strings.

Example validation call for an already drafted Merch by Amazon batch:

```json
{
  "platform": "merch_by_amazon",
  "listings": [
    {
      "id": "trend-1",
      "title": "Garden Bird Watcher Nature Lover",
      "bullet1": "A cheerful garden bird concept for people who enjoy observing backyard wildlife.",
      "bullet2": "An illustration idea celebrating bird watching, gardens, and quiet weekends outdoors."
    }
  ]
}
```

## Reading validation results

Inspect the response `ok`, normalized `platform`, `ruleProfileVersion`, `ruleOrigin`, `counts` (`total`, `valid`, `invalid`, `warnings`), and ordered `results`. Each result has `index`, `id`, `valid`, `errors`, `warnings`, and `metrics`; each finding has `field`, `code`, and `message`. Read the actual errors and warnings instead of guessing that HTTP success means the listing passed. Preserve each result’s input ID/index. Character limits count Unicode code points including spaces; word counts use whitespace-separated tokens, with hyphenated text counted as one token. Duplicate tags are compared after Unicode normalization, case folding, and whitespace normalization. The submitted spelling is preserved.

For newly generated copy, revise only the affected draft fields while preserving the user’s concept and platform, with at most two repair attempts. Revalidate every affected chunk and preserve the same complete draft batch across the ordered calls. For existing user-supplied drafts, preserve the copy and report the actual findings; revise only if the user asks for repairs. Titles, tags, descriptions, or bullets displayed to the user must match the final tool-checked values. Keep analysis and repair details internal unless the user asks about them.

A title target warning on TeePublic or Redbubble is this workflow’s readability preference. Do not tell the user it is an official hard maximum. The tool’s known drafting rules have a version; they are not automatically current official marketplace policy.

Do not treat a passed response as evidence of original artwork, ownership, demand, sales, source-association safety, accuracy of product claims, or acceptance by any marketplace.

## Export

Only after an explicit request for CSV/export, call `export_listing_batch` with the same `platform` and requested `listings`. Omit `include_invalid` or set it to `false` for normal exports. Never set it to `true` to silently bypass errors in the normal creative workflow. If the user explicitly asks to export existing invalid drafts with findings marked, preserve the supplied copy, set `include_invalid: true`, and state that the CSV contains invalid drafts. Report the actual findings and never call them passed. Export only the items requested, and include `designPrompt` only when it belongs to those items and is wanted in the export.

Inspect `ok`, `filename`, `mimeType`, `csv`, `rowCount`, `includesInvalidRows`, `preview`, `formulaProtection`, `warning`, and the nested `validation`. A successful normal export has `includesInvalidRows: false`; an explicitly requested marked invalid-draft export may have `includesInvalidRows: true` and must be described accordingly. `preview` contains `headers`, `rows`, and `truncated`; its cells match the exported CSV. Formula-like spreadsheet cells are prefixed with an apostrophe for safer CSV viewing; source draft text remains unchanged. Tell the user about that transformation if it affects their requested content. A returned CSV is the export; an optional host-provided download view may make it downloadable. If a real download is absent, show the returned CSV in a fenced `csv` block with the returned filename, without claiming to have created a hosted download link or saved a file to the user’s device. Do not invent a persistent export or an external marketplace import result.

For a requested export exceeding the per-call limits, export every ordered chunk separately. Label each returned result by chunk number and original item range; make clear that these are multiple CSV exports. The server may return the same filename for each chunk, so keep each actual view/result separate and suggest distinct local names when saving. Never invent a combined file or claim that the first CSV contains the complete batch. Do not silently omit any requested items.

## Errors and recovery

If the tool returns invalid inputs, an unsupported platform, or a size-limit error, explain the actual error, correct the input if possible, and retry only the affected operation. Never silently discard batch items. The server accepts at most 25 listings in one call, at most 128 KiB of UTF-8 JSON tool-argument data, at most 4,000 Unicode characters per string, at most 50 tags per array, and at most 10 fields in a row (the platform-specific required counts still apply). If a supported batch is too large, split it into ordered chunks within these limits and preserve every item’s ID and output order; do not change the platform between chunks.

If validation is unavailable, malformed, or still reports errors after two repairs, do not claim success. For a creative draft, keep the normal output sections and include a brief note inside Listing such as “Format check unavailable; this draft is unverified.” If errors remain, identify the actual unresolved field issue. Never display tool failure as IP risk, never fabricate a passed result, and never export an invalid batch as validated.

If export fails, state that export was not created and give the returned reason. Preserve the completed creative output and do not promise a download that does not exist. If the tools are unavailable in the host, name that limitation without claiming that the MCP functionality ran.
