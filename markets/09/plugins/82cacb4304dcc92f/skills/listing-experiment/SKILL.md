---
name: listing-experiment
description: Improve store listing copy by preparing a localized Stora draft or experiment from relevant search evidence, preserving existing draft fields.
---

Read `get_listing`, relevant `get_keywords_table` rows and `list_experiments` for the chosen app, platform and market. Ground copy in verified product features and localized intent. Do not claim unverified functionality, guaranteed ranking gains or invented search volume.

Prepare the requested draft or hypothesis with the proposed change, evidence, baseline, observation period and success measure. Do not save it just because the user requested analysis. If saving is requested, inspect the current draft first: `save_listing_draft` replaces the draft. Send all six fields (`title`, `subtitle`, `keyword_field`, `google_title`, `google_short`, `google_long`) plus `app_id` and `store`, and preserve every field outside the requested change. Omitted fields can be cleared. Read the draft back to verify it.

Use `create_experiment` or `update_experiment` to record the agreed hypothesis and observation plan, preserving existing entries. Use `log_listing_change` only to record a change the user confirms actually happened. `mark_draft_published` changes Stora's ledger; it does not publish to a store and must not be called for a prepared draft.

Stora cannot execute App Store Connect or Google Play Console changes. Keep the result reviewable and make the publication step clear to the user. Separate measured observations from proposed actions and avoid attributing causation to a single coincident rank movement.
