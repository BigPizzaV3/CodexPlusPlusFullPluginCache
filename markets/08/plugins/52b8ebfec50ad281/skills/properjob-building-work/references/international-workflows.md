# Country and language rules for cost workflows

Use these rules across quote comparison, missing-cost reviews, combined jobs,
budget options, small jobs, drawing schedules, project budgets and variations.
They coordinate conversation and supplied evidence; they do not add local rates.

## Keep the project and the conversation distinct

- Respond in the requested language, otherwise the conversation language, where
  the host can do so. Language does not select a country, currency, tax regime,
  construction method, measurement unit or contractor location.
- Keep the actual project country, relevant region, source currency, measurement
  units, reply language and document language as separate facts. A Spanish reply
  about Texas still uses US scope and USD; French about Quebec still uses Canada
  and CAD. Changing explanation language alone does not require recalculation.
- Use a supported card locale when available, including a regional language tag
  where accepted. If the card falls back to another language, explain it briefly
  when material. Do not claim all card text, listings or documents are translated
  just because the host can answer in the user's language.
- Country is needed for local engine pricing and jurisdictional checks. A
  supplied-quote comparison or draft scope can proceed with known evidence while
  country remains unknown. Ask one useful clarification when the missing country,
  region or currency materially affects the requested conclusion.
- A currency symbol is not a location. Clarify ambiguous dollar currencies, and
  ambiguous places or abbreviations. Use the existing market catalog's codes;
  do not silently interpret an ambiguous “SA” as either ZA or Saudi Arabia.

## Preserve sources while translating the explanation

Translate headings, descriptions and questions for the user. Preserve original
amounts, currency codes, units, document tags, item IDs, page/detail references,
revision identifiers, product specifications and source labels. A short original
term alongside its explanation is useful when trade or tax terminology differs.
Do not silently replace a local product, material or work method with a British
equivalent or assume familiar words describe equivalent installation scope.

Read documents in their supplied language only as far as the host can actually
interpret them. Mark uncertain translations, unreadable text and conflicting
revisions; ask for the relevant excerpt or clarification when material. Translation
is not certification of a contract or proof of the original author's intent.

Keep statutory and contractual terms attached to their actual jurisdiction.
Possible approvals, professional services, warranties, retention and payment
terms are questions unless established. Do not import UK planning/Building
Control/party-wall requirements into another country's job. Verify current
official sources when asked for jurisdiction-specific legal or tax guidance;
do not infer applicability from the conversation language or property age.

## Numbers, dates and money

- Preserve the source notation and parse before doing arithmetic. Decimal commas,
  decimal points, spaces and nonbreaking spaces may have different roles. If a
  material amount such as “1,500” is ambiguous in context, clarify rather than
  silently choosing 1.5 or 1500. The same applies to ambiguous dates/revisions.
- Respect explicit numerical multipliers such as lakh/crore and 万/万円. Keep a
  room area expressed in 畳/帖 distinct from a count of replacement tatami mats.
  Do not reinterpret a bare number or an unfamiliar local area unit by guessing.
- Format the explanation for the user's locale without changing the numeric
  amount. Retain sufficient precision during arithmetic and round at presentation.
  Keep source amounts visible if the display notation changes. For right-to-left
  responses, keep amount/currency/unit associations unambiguous; ISO currency
  codes are useful when symbols are shared.
- Keep currencies separate unless the user explicitly requests a conversion.
  Such a conversion needs a supplied or verified rate and date, preserves the
  original totals, and is labelled separate host arithmetic. It never supplies
  destination-country construction rates or makes different scopes comparable.
  No exchange-rate fallback is passed into the building-cost engine.

## Tax and budget basis

Read the document's stated tax basis. Terms such as HT/TTC, netto/brutto,
tax-exclusive/inclusive, VAT, GST, IVA or consumption tax must not cause an
unstated rate, exemption or eligibility to be inferred. Preserve whether tax is
included, excluded, mixed or unconfirmed. Tax can differ by item and jurisdiction.
Do not add tax a second time to a supplied or returned inclusive amount.

Compare or sum amounts only when currency, scope, tax basis and included
allowances are compatible. Unknown tax or scope remains visible and can prevent
a tax-inclusive or all-in conclusion. User-supplied tax arithmetic is labelled
as supplied facts, not an independently verified tax assessment. Keep recurring
rent/service costs and their periods separate from upfront construction costs.

## Measurements and pricing coverage

Preserve the source unit and measurement basis: floor area, living area, footprint,
wall area, roof area, length, volume and item counts are distinct. Explicitly pass
supported units to the engine and let its checked conversion path handle them.
For supplied quantity × rate arithmetic, align the rate's unit first and show
any justified conversion. A US project measured in m² still uses US prices; a
UK project measured in ft² still uses UK prices. Geometry alone does not establish
a jurisdiction-specific living-area definition or an approved measurement.

Read the current `properjob://building-work/market-coverage` and actual tool schema
before pricing a task. Supported country does not mean every trade is supported.
The current pricing countries are GB, US, AU, NZ, IE, DE, FR, ES, CA, JP and IN,
each with its own work limits. Do not substitute one country's rates for another,
turn an allocation of a whole-project guide into trade rates, or rename unsupported
work to force a result. Do not describe broad regional guides as local bids.

Supplied-quote arithmetic, omissions reviews and draft work schedules can help
in any country the host can discuss, including countries without engine pricing.
Keep unsupported prices unavailable while still reviewing the supplied work.
Detailed measured trade costing remains GB-only. Foreign drawing facts may
refine supported guides or form an unpriced review; they do not gain UK rates.
