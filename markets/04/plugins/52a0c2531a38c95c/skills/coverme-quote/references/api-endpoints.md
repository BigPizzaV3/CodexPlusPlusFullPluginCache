# CoverMe quote MCP server

Quotes are obtained by calling tools on the **CoverMe quote MCP server** (streamable HTTP transport), not by making raw REST calls. The workflow lives in [../SKILL.md](../SKILL.md); this file is a reference for tool payloads and the handoff-URL template.

## Endpoint

| Environment | URL |
| --- | --- |
| PROD | `https://cdt-mcp.manulife.com/mcp` |
| Non-prod (UAT) | `https://aff-mcp-uat.manulife.ca/mcp` |

Transport: `streamable_http`. The agent connects via the `covermeQuoteMcpProd` dependency declared in [../agents/openai.yaml](../agents/openai.yaml).

## Tools

Three tools per happy-path conversation. `getRecommendations` and `saveQuotes` are called once each; `getQuotes` is called once per returned plan code (typically 4–6 calls):

1. `getRecommendations` — Stage 2a, once. Returns eligible `plans[].code`.
2. `getQuotes` — Stage 2b, once per returned code. Returns the price for the plan code and `tripPreference` values sent in `paxes[0].plans[]`.
3. `saveQuotes` — Stage 3. Persists an issued quote and returns `paxes[0].policyNumber` (`QTE...`).

### MCP annotations

| Tool | Read Only | Open World | Destructive |
| --- | --- | --- | --- |
| `getRecommendations` | true | false | false |
| `getQuotes` | true | false | false |
| `saveQuotes` | false | false | false |

## `getRecommendations` payload

Same top-level shape as `getQuotes`, but the pax omits `contact` and `plans`. See [../assets/sample-quote-request.json](../assets/sample-quote-request.json) for the shape (drop `paxes[0].contact` and `paxes[0].plans` for `getRecommendations`).

Key required fields:

| Field | Value |
| --- | --- |
| `travellerType` | `"SINGLE"` |
| `travellerCategory` | `"TRAVELLING_CANADIANS"` |
| `language` | `"EN"` or `"FR"` |
| `applicationDate` | ISO 8601 datetime with `Z` |
| `tripInformation.startDate`, `endDate` | `YYYY-MM-DD` |
| `tripInformation.tripType` | `"SINGLE"` |
| `tripInformation.provinceOfResidence` | 2-letter code |
| `tripInformation.countryOfResidence` | `"CANADA"` |
| `tripInformation.travellingWithinCanada` | `true` iff destination is Canada |
| `tripInformation.destinationCountry` | ISO alpha-2 |
| `tripInformation.tripCost` | Integer, CAD |
| `tripInformation.tripBookingDate` | ISO 8601 datetime with `Z` |
| `paxes[0].referenceNumber` | `"1"` |
| `paxes[0].age` | Integer, computed from DOB |
| `paxes[0].dateOfBirth` | Real DOB, `YYYY-MM-DD` |
| `paxes[0].tripBookingDate` | Same datetime as `applicationDate` |

Response returns eligible plans at `paxes[0].plans[]` with a `code` field each.

## `getQuotes` payload — one call per plan code

`paxes[0].plans[]` is an array, but populate it with a **single entry** per call. A multi-entry array is unreliable: at best only the first entry is returned, and if any entry is invalid for the trip cost the ENTIRE call fails with `No Rates Error`. Call `getQuotes` once per plan code instead.

Per-entry shape:

```json
{
  "code": "<plan code from getRecommendations>",
  "tripPreference": {
    "tripCost": <integer>,
    "deductible": <number — always 0; send for SEMH and STCIH only>,
    "coverageAmount": <number — always 30000; send for STCIH only>
  },
  "adjustments": []
}
```

Call sequence (also in SKILL.md Stage 2b and Stage 3a):

- **Stage 2** — one call per code returned by `getRecommendations`, base variants only:
  - Non-variant plans (SAIH, SNMIH, SYDELH, SYAIH, any other): `tripPreference: { tripCost }`.
  - SEMH: `tripPreference: { tripCost, deductible: 0 }`.
  - STCIH: `tripPreference: { tripCost, coverageAmount: 30000, deductible: 0 }` — the literal `30000` (Unlimited), always, for every trip cost. `coverageAmount` is mandatory; without it the call returns `No Rates Error`. Only if `tripCost > 30000` do not call `getQuotes` for STCIH; drop it from Stage 2.
- **Stage 3** — **no `getQuotes` call is ever made in Stage 3, for any plan.** Every plan is fully priced in Stage 2, so Stage 3 goes straight from the user naming a plan to `saveQuotes`. There is no follow-up question and no second pricing round.
  - SEMH picked → SEMH has exactly one variant, `deductible: 0`, already priced in Stage 2. Never call `getQuotes` for any other SEMH deductible, in any stage, and never render more than one SEMH row.
  - STCIH picked → STCIH is always `coverageAmount: 30000`, already priced in Stage 2. Never call `getQuotes` for any other STCIH coverage tier, in any stage, and never render more than one STCIH row.
  - Non-variant plan picked → `saveQuotes` directly with `tripPreference: { tripCost }`.

See [../assets/sample-quote-request.json](../assets/sample-quote-request.json) for a single-entry example.

### Response fields (per `paxes[0].plans[]` entry)

| Field | Meaning |
| --- | --- |
| `code` | Echoes the plan code from the request |
| `basePremium` | Base premium in CAD, before tax |
| `baseTaxTotal` | Tax in CAD |
| `basePremiumTotal` | **Total premium in CAD, tax-in — use this for display** |
| `adjustments`, `adjustmentTotal` | Applied rate adjustments |
| `optionalBenefits` | Priced add-ons (empty when none requested) |
| `rateCategory` | Underwriting rate category |

When a plan returns null/missing pricing, drop that row from the Stage 2 table. If every row is null, refuse (`HANDOFF-DEFAULT`).

## `saveQuotes` payload — different shape

`saveQuotes` uses the legacy CoverMe REST-API structure, **not** the `plans[]` array shape used by `getQuotes`. Key differences:

- `paxes[0].plan` is a **singular object**, not `paxes[0].plans` array.
- `paxes[0].plan.optionalBenefits: []` and `paxes[0].plan.adjustments: []` required as empty arrays.
- `paxes[0].questionnaires: []` required as an empty array at the pax level. Missing → backend 500.
- **Do NOT send `paxes[0].plan.questionnaires`.** The ChatGPT connector schema rejects it (`additionalProperties` — `"Removed additional property 'questionnaires'"`) and the auto-retry does not fire reliably in production. Include it only at pax level.
- `paxes[0].firstName: "notyetprovided"`, `lastName: "notyetprovided"` (const).
- `paxes[0].contact.email: "notyetprovided@manulife.ca"` (const).
- `paxes[0].contact.address.addressLine1: ""`, `addressLine2: ""`, `city: ""`, `postalCode: "I0I 0I0"` (const).
- `paxes[0].contact.address.province` — real 2-letter province code (required).
- `paxes[0].contact.address.country: "Canada"`.
- `paxes[0].contact.phone` — **required by the deployed server** as a string of length 1–20. Use the sentinel `"0000000000"`. Never omit and never send `null`; the schema you may see published elsewhere lists it as optional, but the running server rejects with `VAL_LENGTH` / `VAL_TYPE` errors when the field is missing or non-string.
- `paxes[0].countryOfResidence: "Canada"` — required at pax level (in addition to `tripInformation.countryOfResidence`).
- `paxes[0].bill96Consent` — strict boolean. `true` ONLY when province is `QC` AND `lang` is `"EN"`; `false` in every other case, Quebec-in-French included. QC+EN with `false` or missing → 422 `REG_BILL96_CONSENT_REQUIRED`. `true` sent for QC+FR, or for any non-QC province, → 400 `REG_BILL96_NOT_NEEDED`. (Bill 96 consent covers receiving the confirmation in both languages; a French-language customer is already served in French, so no consent is required.)

**Staged validation — an error reports only the FIRST fault.** `saveQuotes` validates in a fixed order, so a failing payload surfaces one gate at a time:

| Gate | Missing field | Response |
|---|---|---|
| 1 | `firstName` / `lastName` | 400 `VAL_REQUIRED` |
| 2 | `bill96Consent` | 422 `REG_BILL96_CONSENT_REQUIRED` — **QC + EN only** |
| 3 | `contact` | 500 `Cannot read properties of undefined (reading 'email')` |

QC in English passes through all three gates; French Quebec and every other province skip gate 2. A payload missing both `bill96Consent` and `contact` therefore needs TWO corrections in QC+EN but only ONE elsewhere — which is why field-by-field patching fails in Quebec within a single retry. Always recover by rebuilding from `assets/save-quotes-template.json`, which clears all three gates at once. Note the gate-3 message names `email` but the fix is the entire `contact` object.
- `paxes[0].plan.eligibilityConsent: true` — user consents by clicking the Stage 3 handoff link after seeing Important Eligibility Information.
- `paxes[0].lang: "EN" | "FR"` — sticky locale.
- `tripInformation.destinationCountry` — ISO alpha-3 (e.g. `USA`, `ESP`, `FRA`), converted from the alpha-2 used in `getRecommendations` / `getQuotes`.
- `tripInformation.tripCost` — same integer as `getQuotes`.
- `tripInformation.countryOfResidence: "Canada"`.
- `organizationCode: "CM"` at top level (const).
- `referenceId: ""` and `referredBy: ""` at top level — required at runtime as empty strings.
- `createdAt` at top level — same ISO 8601 timestamp as `applicationDate`. Missing → backend rejects.

See [../assets/save-quotes-template.json](../assets/save-quotes-template.json) for the canonical payload with placeholder markers, and [../assets/sample-save-request.json](../assets/sample-save-request.json) for a populated example.

### Response

Success returns `paxes[0].policyNumber` in the `QTE...` format. **No URL field is returned** — construct the handoff URL locally per the template below.

## Handoff URL (Stage 3 success only)

After `saveQuotes` returns a `QTE...` value, build **exactly one** clickable link.

### Templates

**EN:**

```
https://www.coverme.com/travel-insurance/get-a-quote?quoteNum=<QTE...>&cid=CA-EN_ML_IS_CAI_CGPT_CGPTTravelPlugin_COVERMETRAVEL_IM_-_-_Quote_B2C_AQCTR_-_-
```

**FR:**

```
https://www.pourmeproteger.com/assurance-voyage/obtenir-une-soumission/apercu-soumission?quoteNum=<QTE...>&cid=CA-FR_ML_IS_CAI_CGPT_CGPTTravelPlugin_COVERMETRAVEL_IM_-_-_Quote_B2C_AQCTR_-_-
```

### Parameters

| Parameter | Source |
| --- | --- |
| `quoteNum` | The exact `QTE...` value from `paxes[0].policyNumber` returned this turn. Never display to the user. |
| `cid` | Constant ChatGPT campaign ID above (contains `_Quote_B2C_AQCTR_`). |

Refusal URLs use a different path (`/travel-insurance.html` / `/assurance-voyage.html`) and a different `cid` fragment (`_NoQuote_B2C_AQCTR_`). They live in `references/verbatim-messages.md § Refusal variants` and must never be emitted on a Stage 3 success handoff.
