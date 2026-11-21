---
name: ololand-dd-real-estate-diligence
description: Use when the OloLand deal target is a commercial real estate asset, portfolio,
  or operating company (CRE, multifamily, industrial RE, retail, office, hospitality,
  healthcare RE). Loads NOI / cap rate / DSCR / debt yield / rent-roll discipline
  and the verifier checklist for property-level diligence.
---

# Real estate diligence

CRE deals are valued off NOI and cap rate, not EBITDA and multiples. The KPI discipline, verifier checklist, and red flags differ from operating-company DD.

## Canonical KPIs

| KPI | Definition | Mistake to avoid |
|---|---|---|
| **NOI** | Effective gross revenue − operating expenses, **before** debt service, depreciation, capex | Including capex or debt service |
| **Cap rate** | NOI ÷ Property value | Using trailing NOI when projections are stronger |
| **DSCR** | NOI ÷ Annual debt service | Using EBITDA instead of NOI |
| **Debt yield** | NOI ÷ Loan amount | Confused with cap rate |
| **Occupancy** | Occupied units ÷ total OR occupied SF ÷ rentable SF | Mixing physical and economic |
| **Economic occupancy** | Effective gross revenue ÷ gross potential rent | Reporting physical when economic is lower |
| **T-12 NOI** | Trailing-12-month actual NOI from operating statements | Using underwriting NOI as "trailing" |

## Verifier checklist

- [ ] Rent roll × 12 reconciles to T-12 revenue
- [ ] T-12 from GL or tax return, not sponsor pro-forma
- [ ] OpEx normalized (taxes, insurance current quotes, mgmt fee 3-5% market not affiliated rate)
- [ ] CapEx reserve included in underwriting NOI
- [ ] Top-10 lease abstracts reviewed (term, escalations, options, exclusives, kick-out, co-tenancy)
- [ ] WALT by SF and by revenue
- [ ] Title commitment exceptions reviewed; survey + ALTA current
- [ ] Phase I (and Phase II if recommended); PCA immediate repairs
- [ ] Zoning compliance; tax history + appeal/reassessment exposure
- [ ] Insurance loss runs 5-year; service contract cancellability at close

## Debt + capital stack

Senior loan terms (fixed/floating, IO, prepayment via yield maintenance / defeasance / open), mezz/pref equity intercreditor, refinance scenario at exit, DSCR + debt-yield headroom on 10% NOI drop.

## Common red flags

- Rent roll × 12 ≠ T-12 revenue → unstated concessions
- "Pro forma NOI" used as cap-rate denominator
- Replacement reserves excluded
- Tenant concentration > 25% without IG credit
- Mgmt fee 1-2% (affiliated subsidy) vs market 3-5%
- Floating-rate bridge loan near cap with extension caveats

Every NOI cited MUST disclose basis (T-12 actual / T-3 annualized / underwriting) and cite source with `[N]`. Every cap rate MUST state the NOI basis.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
