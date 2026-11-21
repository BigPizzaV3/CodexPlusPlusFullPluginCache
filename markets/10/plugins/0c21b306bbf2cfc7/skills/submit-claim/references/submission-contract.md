# Existing submission field mapping

This is a reference for the unchanged payloads, not a replacement for the exposed
host tool schema. Advertise only the available product routes in the generated
product source: four single-payment services and portfolio sale/collections.
Permissive legacy enums do not add portfolio products or enable paused liens.
Use payer/planned payment for Payment Protection, invoice recipient for Factoring,
and debtor for Claim Sale/Collections in customer-facing questions. The backend
continues to use the existing debtor and original_claim_balance fields.

All four tools take `payload` and `confirmed`. Only the two `_with_documents` tools also take the required `documents` file input; the no-document tools do not expose that field. Collect these common payload fields first:

| Field | Requirement |
| --- | --- |
| `review_purpose` | Exactly one of `claim_purchase`, `collections`, `factoring`, or `payment_protection`. Choose from the user's stated intent and the available product route; ask when unclear. If several services are requested with no primary purpose, ask which should be the primary review purpose and retain all requested interests below. |
| `description` | A nonempty description of the claim or portfolio and relevant circumstances. |
| `creditor.name` | Creditor's name. |
| `creditor.address.country` | Full country name as stated by the user, such as `United States`, `United Kingdom`, or `Poland`. Never convert it to a two-letter or three-letter code. |
| `creditor.address.state` | Required when the country is `United States`; optional elsewhere. |
| `creditor.contact_person` | `first_name`, `last_name`, `email`, and `phone` are required. `role` is optional. |
| `creditor.type_of_service_interested_in` | A nonempty array of free-text interests reflecting the user's request, such as `Claim purchase` or `Collections`; there is no fixed label list. |

Then collect only the fields for the selected branch. Do not make a portfolio submitter answer individual-debtor questions.

### Single claim

| Field | Requirement |
| --- | --- |
| `debtor.entity_type` | `business` or `individual`. |
| Debtor's name | For a business, use only `debtor.legal_name`. For an individual, use only `debtor.first_name` and `debtor.last_name`. |
| `debtor.address.country` | Full country name as stated by the user. Never convert it to a country code. |
| `debtor.address.state` | Required when the country is `United States`; optional elsewhere. |
| `financials.currency` | `USD`, `EUR`, `GBP`, `PLN`, or `CAD`. |
| `financials.original_claim_balance` | Original claim amount as a finite, nonnegative number in the selected currency. |

### Portfolio

| Field | Requirement |
| --- | --- |
| `portfolio.name` | A nonempty portfolio name. |
| `portfolio.portfolio_financials.case_count` | An integer of at least 1 describing the number of receivables. |
| `portfolio.portfolio_financials.principal` | Total principal as a finite, nonnegative number. |
| `portfolio.portfolio_financials.currency` | `USD`, `EUR`, `GBP`, `PLN`, or `CAD`. |

Read [optional portfolio financial details](portfolio-financials.md) only when the user supplies or asks to include fees, interest, repayments, or balances beyond principal. Those details are optional; do not turn them into additional required questions.

For portfolios, do not include `debtor`, top-level `financials`, `invoice`, `case_ids`, organization/user/creditor IDs, or an `auth0_id`. Do not split a portfolio into multiple claim submissions.

Preserve the user's full country name after trimming surrounding whitespace. If only a country code is supplied, ask for the country name before submission. Do not translate, abbreviate, or infer it. Either supported address may also include `address_line_1`, `address_line_2`, `city`, `county`, and `zip` when supplied. Do not require optional fields or send unsupported fields, including `creditor.how_heard_of_delos`. A selectable review purpose does not establish service eligibility or approval.

