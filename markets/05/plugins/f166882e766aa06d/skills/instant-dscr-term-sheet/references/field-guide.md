# Field guide — plain-English intake for request_instant_term_sheet

Use this to turn what the investor says into the tool's values, and to word the one-round intake message. `instant_term_sheet_requirements` is the source of truth; if it disagrees with this file, follow the tool.

## One-round intake template

Adapt to what's already known — only ask for what's missing.

> To get your term sheet I need a few things:
>
> **The property** — full address (street, city, state, ZIP); property type (single-family, townhouse, condo, 2–4 unit, etc.); number of units; any ADUs on the lot?
> **The loan** — purchase or refinance (and if refi, cash-out or rate-and-term)? Loan amount you want; purchase price (if buying) or estimated value; if refinancing, current payoff, how long you've owned it, and whether it's rented or vacant.
> **The rent and costs** — monthly rent (lease, or market rent if vacant; 12-month average if it's a short-term rental), annual property taxes, annual hazard insurance, monthly HOA if any, flood insurance if any.
> **You** — credit score; citizenship/residency; any bankruptcy, foreclosure, short sale or deed-in-lieu (and how many months ago); any late mortgage payments in the last 12 months; will title be in your name, an existing LLC, or an LLC you'll form before closing?
> **Where to send it** — your full name and email. (Phone is optional.)
> **Three confirmations** — Is this loan for a business purpose? Is the property an investment property that you won't live in? Will title vest the way you described?

## Value mapping

| Investor says | Field | Value |
|---|---|---|
| Single-family house | property.propertyType | `sfr` |
| Townhouse, row house | property.propertyType | `sfr_attached` |
| House in an HOA planned community | property.propertyType | `pud` |
| Condo | property.propertyType | `condo` (use `condo_non_warrantable` only if they say it's non-warrantable) |
| Duplex / triplex / fourplex | property.propertyType + units | `multifamily`, units 2 / 3 / 4 |
| Buying | loan.purpose | `purchase` (purchasePrice required) |
| Refi to lower rate / change terms, no cash out | loan.purpose | `rate_term` |
| Refi and take cash out | loan.purpose | `cash_out` |
| 30-year fixed (default) / 40-year / 5-, 7-, 10-year ARM | loan.requestedProduct | `fixed_30` / `fixed_40` / `arm_5_6` / `arm_7_6` / `arm_10_6` |
| No prepayment penalty | loan.prepayTermMonths | `0` |
| "3-year prepay" | loan.prepayTermMonths | `36` (ask structure only if they have a preference) |
| US citizen / green card / visa holder / foreign national / ITIN | borrower.citizenship | `us_citizen` / `permanent_resident` / `non_permanent_resident` / `foreign_national` / `itin` |
| In my name / my existing LLC / LLC I'll form | borrower.vesting | `individual` / `entity` / `entity_to_be_formed` |
| Owned rentals before / first rental | borrower.experience | `experienced` / `first_time_investor` |
| No lates in 12 months | borrower.housingHistory | `clean` (others: `1x30x12`, `0x60x12`, `0x90x12`) |
| Airbnb / VRBO / nightly | property.rentalType | `short_term` |

## Credit events

- None of any kind, no pending foreclosure on this property → `{ "none": true }` and nothing else.
- Otherwise → `mostRecentMonths` (any event), plus `bankruptcyMonths` / `foreclosureMonths` where there's been one (`null` for none), plus `foreclosureOnSubject` / `foreclosureBailout` if the event involves this property.
- Convert years to months ("about 3 years ago" → 36) and say you did.

## Watch-outs

- Leverage is measured on the lower of estimated value and purchase price — don't promise LTV off value alone on a purchase.
- `purchasePrice` is only for purchases; `existingLienPayoff`, `ownershipMonths`, `vacant`, and `subjectHousingHistoryDaysLate` are only for refinances.
- `fico` and `noScore` are never sent together.
- `phone` is never sent without `phoneConsent: true`.
