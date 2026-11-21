---
name: catalogue-discovery
description: Discover, browse and compare the current SpeakShelf text-to-speech catalogue by provider, family, model, voice name or locale, and handle a requested catalogue sample for a selected voice.
---

# SpeakShelf catalogue discovery

Draft workflow. Follow the user's explicit constraints over these guidelines.
Use SpeakShelf's existing `search_voices` and, only for an authorized sample
request, `get_voice_sample`. There is no separate options, details or comparison
tool. Do not substitute another TTS service. If the tools are unavailable,
explain the missing connection instead of inventing catalogue results.

## Find the requested voices

1. Separate provider, family, concrete model, voice name, voice locale and
   interface locale. A family is not a model ID; a voice name is not a unique
   voice ID. Family identity is the pair of provider and exact family key.
   Voice locale selects spoken-language catalogue rows. Interface locale only
   changes labels and links; changing it must not change voice locale.
2. Search directly when the intended filters and their exact values are known
   from current tools or earlier usable results. Otherwise make the smallest
   useful `search_voices` discovery request, retaining known user constraints.
   Read `providerOptions` and `filterOptions` from that response. Do not run an
   unfiltered discovery call before every search or repeat a call to open the
   same widget. Reuse current results when they answer the request.
3. Use returned provider/family `key`, model `id` and language `code` values,
   never translated labels or guessed spellings. An echoed option with
   `available:false` is not validation. Discover outside a conflicting scope
   only as an explicitly described diagnostic, keeping it separate from the
   user's requested result. Read [contract details](references/contract.md)
   when validating dependent options, handling ambiguity or selecting a model.
4. Put exact constraints in structured fields. Use `query` for concise residual
   name or trait terms: its tokens are matched together, not as semantic prose.
   Do not paste the whole request into it. Split comparison alternatives into
   structured searches; prose such as "A or B" is not Boolean OR. Use only schema-supported filters.
   A request for a style or trait can use catalogue search terms, but returned
   metadata is descriptive, not a synthesis control or sound-quality proof.
5. Preserve model intent: omit `model` to allow conservative inference, pass a
   usable concrete model ID for an explicit selection, or send `model: ""` for
   deliberate All models in search. Never replace All with an inferred model.
   An ambiguous or unsupported model qualifier is not permission to select a
   nearby model. Clarify material ambiguity or show the available choices.
6. Read `appliedFilters`, `modelSelection`, `voices`, `total` and pagination
   fields. Explain unexpected applied filters or an empty result. Distinguish
   invalid identifiers, valid but incompatible filters and a genuine no-match
   result using usable discovered options and the selected rows. The server may
   return `total:0` for all three. If evidence cannot distinguish them, say so.
   Never silently drop a requested constraint to manufacture results.

## Browse and compare

For catalogue-wide discovery, obtain current provider options, then each
provider's family options as needed. Cover every currently exposed family,
including unfamiliar future additions. Do not use a static family list or
source registry as live inventory. A page is not the whole catalogue. When the
user requests all rows, continue through returned cursors within a stated scope
and report any incomplete traversal or catalogue refresh.

Compare returned rows in a compact table when helpful: name, exact voice ID,
provider, family key/label, voice locale, eligible returned models, tier and
relevant traits. Keep unknown metadata unknown. Compare multiple providers
using separate scoped searches only when one search cannot answer the request.
Report partial or empty sides honestly; do not invent rankings, accents,
prices, quality claims or synthesis support. Counts describe catalogue rows,
not necessarily unique personas or spoken languages. Use returned `siteUrl`
or `referralUrl` as related provider/language pages, not voice-selection links.

For next/previous pages, send the returned `nextCursor`/`previousCursor`
unchanged with the ORIGINAL request's query, provider, voice_locale,
interface_locale, family, gender, tier, page_size, primary_only and model
presence/value. In particular, do not copy an inferred `appliedFilters.model`
into an originally omitted `model`: auto, explicit and All have distinct cursor
scopes. Keep the effective interface locale stable across paging. If original
intent cannot be recovered, restart transparently rather than guess. A changed
filter starts a new search without the old cursor. Missing cursors mean a page
boundary. If a stale cursor resets or fails, explain and restart the same scope;
do not claim uninterrupted traversal or fabricate a cursor.

Use `primary_only:true` only for an Azure Primary request, with `provider:azure`
and the intended voice locale. Primary means exact Azure-declared locale
metadata after BCP-47 canonicalization. It guarantees neither accent nor audio
quality and is not a cross-provider rule. Do not derive it from a name or ID.

## Handle a requested sample

Browsing and comparison do not authorize audio preparation. A sample lookup
can prepare owner-cost audio even though visitors are not charged. Respect the
user's sample permission and any no-audio constraint. Resolve the selected row
from the current result; clarify ambiguous names or ordinals before calling.

Preserve its exact `id` as `voice_id`, locale identity and eligible model. A
user's explicit eligible sample override wins; otherwise retain the concrete
applied search model when eligible for that row. If no concrete model was
selected, omit sample `model` to use the server's row-eligible default. Never
send `model:""` to `get_voice_sample`; All is a search state. Do not infer a
model selector from a family name or from `models:[]`. `sampleAvailable:false`
means unavailable; an absent flag does not prove readiness. Do not substitute
another voice or model for an incompatible selection.

Read [sample states](references/contract.md#sample-states) before handling a
pending or failed lookup. Explain the returned state, respect `retryAfter`,
and avoid uncontrolled retries. Only use `refresh_after_media_error` after an
actual failure of the returned media URL. A ready URL is not audible playback
proof. Never substitute custom text generation, cloning, uploads, purchases or
private-library actions; these are outside the exposed tools.

## Present the result

Give a short answer focused on the user's criteria, meaningful differences,
constraints and next page or sample choice. Avoid duplicating the widget's
entire contents. Do not claim it rendered from metadata alone or claim it is
unavailable without a host signal. When unavailable, use structured results,
text and returned catalogue links. Preserve exact identifiers even when prose
or interface labels are localized. Read [examples](references/examples.md)
for representative edge cases; examples are not a frozen catalogue inventory.
