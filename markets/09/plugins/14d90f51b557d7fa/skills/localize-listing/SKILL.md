---
name: localize-listing
description: >-
  Translate or rewrite an App Store listing in one or many languages through
  MetaRun: name, subtitle, description, keywords, What's New and promotional
  text. You write the copy; MetaRun checks limits, shows one change card for
  every language, and applies it when the person presses Apply. Use for
  "translate my listing", "add German", "localize my App Store page", "rewrite
  my subtitle", "update What's New in every language".
---

# Localize the listing: you write it, MetaRun ships it

## 1. Read before writing

- `apple_list_apps` to resolve the app (use the bundle id after that).
- `apple_list_app_metadata` for the current copy in every language.
- `apple_get_listing_coverage` to see which languages and fields are missing.
- New language? `apple_list_supported_locales` gives the exact App Store codes
  (for example `de-DE`, `ja`, `pt-BR`, `zh-Hans`).
- A field reported as locked: `apple_get_listing_editability` explains why
  (name, subtitle and description change only while a version is being
  prepared; promotional text can change any time).

## 2. Write the copy yourself

- Translate from the primary language with the app's tone; keep brand names.
- Apple's limits are hard: name 30 characters, subtitle 30, keywords 100,
  promotional text 170, description 4000. Count before staging.
- Keywords are comma-separated without spaces and should not repeat words
  already in the name or subtitle. `aso_lint_metadata` checks a draft.
- What's New only exists on updates; skip it for a first release.

## 3. One card for everything

Call `apple_preview_import_fastlane_metadata` ONCE with every language:

    { "bundleId": "com.example.app",
      "metadata": {
        "de-DE": { "subtitle": "...", "keywords": "...", "description": "..." },
        "ja":    { "subtitle": "...", "keywords": "..." } } }

Field keys: `name`, `subtitle`, `description`, `keywords`, `whatsNew`,
`promotionalText`, `supportUrl`, `marketingUrl`, `privacyPolicyUrl`.
Unchanged fields are skipped, over-limit or locked ones come back as
warnings, and nothing is ever cleared.

For a single field in one language, `apple_preview_set_version_localization`
(description, keywords, What's New), `apple_preview_set_app_info_localization`
(name, subtitle) or `apple_preview_set_promotional_text` also work.

## 4. Let the person apply, then verify

Tell them to review the card and press Apply. Promotional text on a live app
goes public the moment it applies; say so. After they apply, check
`apple_get_listing_coverage` again before saying every language is done.
