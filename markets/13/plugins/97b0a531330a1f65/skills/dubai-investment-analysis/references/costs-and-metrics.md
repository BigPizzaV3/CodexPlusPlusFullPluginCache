# Dubai cost stack and metric definitions

Reference figures for turning a headline price into a real return. Ranges are
market norms, not quotes - verify anything a buyer will act on.

## One-off purchase costs

| Item | Typical | Notes |
|---|---|---|
| DLD transfer fee | 4% of price | + ~AED 580 admin |
| Agency commission | 2% + VAT | Standard for resale |
| Title deed issuance | ~AED 580 | |
| Trustee / registration office | AED 2,000-4,000 + VAT | Tiered by price |
| Mortgage registration | 0.25% of loan | + ~AED 290, if financing |
| Valuation | AED 2,500-3,500 | Lender-required |
| NOC from developer | AED 500-5,000 | Resale only, varies by developer |

Rule of thumb: **budget 6-7% on top of the price** for a cash resale purchase,
7-8% with a mortgage. Off-plan direct from developer skips agency commission but
still carries the 4% DLD.

## Recurring costs (the ones that eat yield)

| Item | Typical | Notes |
|---|---|---|
| Service charge | AED 10-30 per sqft per year | The dominant variable. Prime towers and serviced buildings run far higher than mid-market communities; villas are usually lower per sqft. |
| Property management | 5-8% of annual rent | If not self-managing |
| Vacancy allowance | 4-8% of annual rent | ~2-4 weeks between tenancies |
| Maintenance / reserve | 0.5-1% of value | |
| Chiller / district cooling | Varies | Sometimes landlord-paid, sometimes tenant - check before modelling |

There is no annual property tax and no rental income tax in Dubai. A 5% VAT
applies to commercial, not residential, rent.

## Metric definitions

**Gross yield** = annual rent ÷ purchase price. The number quoted in most
marketing. Ignores every cost above.

**Net yield** = (annual rent − service charge − management − vacancy −
maintenance) ÷ (purchase price + purchase costs). Typically **1.5-2.5 points
below gross** in Dubai. This is the number a buyer actually lives with.

**Payback period** = purchase price ÷ annual rent. Gross payback; the net figure
is meaningfully longer.

**Cash-on-cash return** (with a mortgage) = (annual rent − all costs − mortgage
payments) ÷ cash actually invested (down payment + purchase costs). Leverage can
lift this well above the net yield, or turn it negative when the mortgage rate
exceeds the net yield.

**Price per sqft** is the only fair way to compare across unit sizes. Compare
like for like: the same bedroom count, the same ready/off-plan status, the same
building tier.

**CAGR** = compound annual growth rate. Use it over 3+ years; over shorter
windows it exaggerates.

## Rental market rules that affect returns

- **RERA rental index** caps how much a landlord can raise rent on renewal, on a
  sliding scale tied to how far below market the current rent sits. A unit let
  well below market cannot simply be repriced at renewal - it steps up over
  years. This matters when buying a tenanted unit.
- **Notice**: 12 months' written notice to a tenant for owner use or sale.
- **Short-term / holiday lets** need a DET permit and carry far higher gross
  yields with far higher costs and vacancy. Do not compare a short-let gross
  yield to a long-let one without saying so.

## Sanity bands

Rough long-let gross yields by segment, as a smell test - if a computed number
falls far outside, re-check the inputs before presenting it.

- Prime waterfront / branded: 4-6%
- Established mid-market apartments: 6-8%
- Affordable / emerging apartment communities: 7-9%
- Villas and townhouses: 4-6%

A gross yield above 10% on a long let usually means a data problem: a mismatched
bedroom count, a distressed or off-plan price against a ready rent, or a
short-let contract in the sample.
