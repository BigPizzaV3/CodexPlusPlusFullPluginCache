# Structured data: inspection, validation, and recommendations

Apply this procedure whenever the workflow is given a relevant URL, including supplied competitor URLs. Apply it to other pages actually analyzed when technically feasible. This is a page-scoped check, not a site-wide crawl. Read this reference before checking or recommending markup.

## Evidence and access

1. Reuse the page retrieval. Obtain raw HTML and, when an available tool permits it, rendered DOM to inspect markup injected by JavaScript. Record the URL, redirects, retrieval date, method, and completeness. Do not bypass authentication, robots restrictions, or access controls.
2. Inspect every accessible JSON-LD block, including arrays, nested objects and @graph nodes, plus all accessible Microdata and RDFa. Inventory every discovered type and entity, not just the recommended types below. Retain a block number, @id, or HTML location for evidence.
3. Text-only search extracts, screenshots, and readable article text are not evidence that markup is missing. If HTML or rendered markup is unavailable, report "Not verifiable with available access", continue the content workflow, and offer to inspect supplied HTML, JSON-LD, or a validator export. Raw HTML alone cannot rule out JavaScript-injected markup. Never describe blocked or partial extraction as a complete crawl.
4. If no markup is found, say "No structured data found in the inspected source" and identify that source and its limits. Do not infer that no structured data exists anywhere on the page or site.

## Validation layers

Check each accessible block/entity at the following distinct levels:
- Syntax: parse JSON-LD with a parser when available; report parse errors and duplicate JSON keys. A syntactic parse alone is not schema validation. For Microdata/RDFa, use supported extraction/validation tooling; otherwise label the review as partial.
- Vocabulary and graph: verify @context, actual schema.org types/properties, expected value types, nested relationships, @id links, duplicate/conflicting descriptions of the same entity, and references that cannot be resolved in the inspected evidence. Inspect unfamiliar types using current primary documentation instead of ignoring them.
- Content consistency: compare markup against the visible page, its main entity, authors, dates, media, organization details, products and offers. Distinguish an unsupported claim from an unverified value. Do not invent authors, reviews, ratings, prices, business addresses, or missing facts.
- Search eligibility: separately check current platform-specific required and recommended fields and content policies for supported features. Distinguish schema.org validity, search-feature eligibility, actual indexing, and appearance in results. A valid schema.org type need not have a supported rich-result feature.

Use https://validator.schema.org/ for vocabulary checks and https://search.google.com/test/rich-results for current Google feature checks when tools can actually run them. Prefer current official schema.org and Search Central documentation for interpretation. Report the exact tool, scope and returned result only after execution; a link to a validator is not an executed test. If services cannot be run, perform only supported local parsing and documented manual checks, mark external validation as not run, and provide those links for follow-up. Do not send private URLs, credentials, or unpublished content to external validators without appropriate user authorization.

Give each entity/block an evidence-backed status: "Errors found", "No errors found in the checks performed", "Partial review", or "Not verifiable". Report warnings and missing recommended fields separately from errors; never claim blanket validity from partial access. Link to the relevant current primary guidance for consequential findings.

## Select markup from actual page content

Recommend the most relevant of the following only when supported by visible content; do not prescribe all types on every page.

| Page or entity | Appropriate markup and checks |
| --- | --- |
| Publisher-authored FAQs with a defined answer per question | FAQPage with Question and acceptedAnswer/Answer reflecting the visible questions and answers. |
| A page focused on one question with user-submitted alternative answers | QAPage with Question and the applicable acceptedAnswer/suggestedAnswer and answerCount. Do not use it as a synonym for an editorial FAQ or for several unrelated questions. Check current platform eligibility separately. |
| Editorial article or post | Article or an appropriate subtype such as BlogPosting, with real author identification (Person or Organization as applicable), name and profile URL, headline, image and accurate dates where supported by evidence and current guidance. Recommend a visible author box and useful author profile consistent with the markup. |
| A video present on the page | VideoObject describing the actual video, verified title/description, thumbnail, upload date and playback/content URL as applicable; check current required fields. |
| A real organization | Organization with consistent identity and verified properties, linked through stable @id references where useful. |
| A real local business/location | The most specific suitable LocalBusiness subtype with accurate location and contact information; do not infer a local storefront from an online business. |
| Software or a software offering | SoftwareApplication, WebApplication or MobileApplication as appropriate; Product and Offer may also apply to an actual product/offer. Verify types against the current vocabulary. Do not emit SoftwareProduct as an assumed schema.org type simply because it is used as a business label. |
| A real page hierarchy | BreadcrumbList with correct ordered ListItem entries and corresponding names/URLs. |

Recommend other types only when the page warrants them and current primary documentation supports them. Schema.org and search support change: verify current guidance when discussing eligibility. FAQPage remains usable for semantic description, but Google retired FAQ rich results in 2026; never promise their display or claim FAQ markup is a proven GEO ranking factor. Valid markup does not guarantee rankings, traffic, rich results or AI citations.

## Report and proposed fixes

Provide a concise table in the result language: URL/source | Type and entity/block | Checks performed and status | Evidence/problem | Recommended fix or next check. Group genuinely identical findings without concealing unchecked blocks. Keep observed markup findings separate from proposed additional types.
Prioritize concrete errors, inconsistent authorship/entities and content mismatch before optional enhancements. Explain why each suggested type fits this page. With text-only or topic-only input, recommendations are provisional; no deployed markup can be validated.
Offer corrected JSON-LD when useful or requested, based only on verified facts. Label unknown fields explicitly outside deployable code; do not present placeholders as production-ready markup. Parse proposed code and apply the same scoped checks before calling it validated. Recommend a final check against the deployed URL after implementation; never claim edits were deployed.
