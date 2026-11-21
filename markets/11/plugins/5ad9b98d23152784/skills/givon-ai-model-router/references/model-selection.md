# Model Selection Checklist

Use live model data as the source of truth.

## Catalog Fields

- `id`: pass as `model`.
- `kind`: `image`, `video`, `music` or `voiceover`; must match generation `type`.
- `status`: prefer `active`.
- `tags`: use only as hints, not guarantees.
- `cost`: present token pricing metadata; do not invent missing totals.
- `schemaUrl`: equivalent to `givon_get_model_schema`.

## Schema Fields

Inspect:

- `required`: ask only for required fields that cannot be inferred.
- `properties`: allowed input keys.
- `default`: omit fields when the default is acceptable.
- `enum`: allowed values only.
- `minimum`, `maximum`, `multipleOf`: numeric limits.
- `additionalProperties`: if false, remove unsupported keys.
- `x-assetSlots`, `x-supportsReferences`, `x-inputModes`, `x-variants`: media
  and variant behavior.

## Recommendation

Rank compatible active models using the user's requested result and priorities
plus each model's current guidance, supported inputs, choices and cost. Recommend
one practical path and name a material tradeoff only when it helps the decision.

## Guardrails

- If the user names a specific model, verify it against the live catalog before
  accepting or rejecting it.
- If a filtered search misses a model the user expects, inspect the unfiltered
  catalog before concluding it is unavailable.
- Treat `x-assetSlots` as capability discovery and verify the matching input
  fields before passing any media.
- If a model schema has no reference/media field, it is prompt-only for the
  public surface. Do not attach reference media, local files, URLs, data URIs,
  or `asset://...` handles to it.
- Local files should use the host-native `givon_upload_file_asset` route when
  available; otherwise upload first with `givon asset upload`. HTTPS/data media
  can be imported with `givon_import_asset` or `givon asset import`.
