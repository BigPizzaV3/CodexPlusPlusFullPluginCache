# Contract details

Use the connected tools' current schemas and responses as authority. This
reference explains the observed contract, not a fixed catalogue inventory.

## Inputs and identity

`search_voices` accepts query, provider, voice_locale, interface_locale, family,
gender, tier, model, primary_only, page_size and cursor. Page size is 1 to 24,
default 6. Genders are female, male, neutral and unknown; tiers are premium and
ultra. Standard can be a family; it is not a tier. The query limit is 120
characters. There is no voice_id, style, accent or arbitrary sorting filter in
this search tool. A name search uses `query`, then resolves exact returned IDs.

`providerOptions` supplies provider keys. `filterOptions.families` supplies
provider-scoped family keys/labels. `filterOptions.languages` supplies exact
voice-locale codes. Interface locales come from the tool's supported enum and
the effective `interfaceLocale`, not the voice-language list. Ask which region
or script is intended when that distinction matters; do not map a broad language
name silently to one regional voice locale. An all-locale browse may leave the
voice locale omitted when that matches the user's intent.

## Dependent options and eligibility

Family options are scoped by provider, not query, voice locale, gender or tier.
Language options consider provider, family and model. Model options consider
provider, voice locale and family, not query, gender or tier. Thus a listed
choice does not promise a match under every active filter. A selected model or
locale may be echoed with `available:false`, including an invalid string. Its
presence alone proves neither validity nor compatibility.

Validate using usable options in the relevant scope. To distinguish a valid
but incompatible model from an invalid one, a clearly labeled diagnostic can
inspect options without the conflicting locale or model, without replacing the
requested result. If no usable option establishes validity, say it is unverified
or not exposed rather than claiming an unsupported identifier is valid.

Each row's `models` is an eligible list bounded to eight entries, not a promise
of an exhaustive global inventory. Filter-level model options are broader and
cannot establish eligibility for a chosen voice/locale on their own. If a
requested model is absent from a bounded row list but usable in filter options,
search with that exact model and the relevant constraints, then verify the exact
voice ID in returned rows before using it. Do not equate an empty models array
on a non-model-selectable family with an empty voice result or invent selectors.

An omitted model allows inference only when the server can resolve supported
intent conservatively. Explicit concrete model overrides query model intent;
empty model disables inference. Inspect what the server actually applied. Keep
the original request separately from effective filters for follow-ups and paging.
Sample omission resolves a row-eligible default; a provider-wide preference is
not proof that a restricted row admits that model.

## Sample states

`get_voice_sample` accepts voice_id, optional nonempty model, formats,
refresh_after_media_error and interface_locale. Formats are opus, aac and wav,
with one to three entries. There is no custom-text field or MP3 option.

| Status | Response |
| --- | --- |
| ready | Use returned audio URL and reuse deadline. Do not claim playback or listening without evidence. |
| generating | Explain that preparation is pending; honor retryAfter if a further authorized lookup is needed. |
| busy / rate_limited | Explain the delay and honor retryAfter; no tight retry loop. |
| expired | Explain expiry; a further authorized lookup may obtain a new URL. |
| unavailable | Say this selected sample is unavailable; do not change voice/model silently. |
| configuration / failed | Report the returned failure without promising a successful retry. |
| invalid_request | Recheck exact selected voice/model eligibility. Do not retry an unchanged invalid choice. |

An autoplay restriction is not a media URL failure: suggest a user tap rather
than requesting refresh. Keep catalog eligibility, sample availability, media
progress and perceived sound quality as separate evidence.
