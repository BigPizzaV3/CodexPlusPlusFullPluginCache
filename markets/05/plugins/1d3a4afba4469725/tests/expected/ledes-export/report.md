# E-Billing Extract Review (Internal)

**Audience:** Internal review
**Source file:** `sample_ledes_1998b_export.txt` -- a raw **LEDES 1998B** e-billing export (pipe-delimited, 24-field standard format), not a hand-formatted CSV. It was parsed with `parse_ledes.py` before analysis; see the Data Limitations section below for what that format does and does not carry.
**Fixture status:** Synthetic test data only; no real client, matter, firm, timekeeper, or invoice data is included.

## Executive Summary

This extract contains two invoices covering two matters from two different outside firms. The standout finding is on matter M-1005 (document review / discovery phase): all 57.4 hours of that work were billed by two partner-level timekeepers at $975/hour, with zero associate or paralegal time anywhere on the matter -- an unusual staffing pattern for what is typically the most delegable task type. The other matter, M-1001 (a vendor contract dispute), shows a more typical mix: partners handled motion drafting and strategy, while an associate handled legal research. Because LEDES 1998B carries no budget/estimate field, this review cannot and does not assess budget overrun or underrun for either matter.

## Recommended Actions

| Priority | Action | Why It Matters | Timeframe |
|---|---|---|---|
| 1 | Require associate- or paralegal-level staffing for document review/discovery tasks (UTBMS L300 series) in the next engagement letter or billing guidelines for firm 58-1129034 (matter M-1005), rather than allowing partner-level timekeepers to bill this work. | 57.4 hours of document review were billed entirely at the $975/hr partner rate ($55,965); shifting this to an associate rate in the $400-500/hr range would plausibly have saved roughly $25,000-30,000 on this invoice alone. | Before next invoice cycle / next engagement letter with this firm |
| 2 | Ask firm 58-1129034 directly why two partners (Castillo and Harmon) split document review on M-1005 with no associate or paralegal involvement, and whether that reflects genuine case complexity or default staffing habit. | Without an explanation, this pattern reads as overstaffing rather than a complexity-driven choice, and it is the single largest cost driver identified in this extract. | Immediately -- M-1005 appears to still be in the discovery phase |
| 3 | Obtain a firm-name mapping for LAW_FIRM_ID values `58-1129034` and `13-4477216` (e.g., from the firm's W-9 or the e-billing platform's vendor table) so future reviews can reference firms by name instead of tax ID. | LEDES 1998B carries no firm-name field; without this mapping, every future review of this data source has the same identification gap. | Ongoing practice change -- do alongside the next data pull |
| 4 | If budget or estimate figures exist for M-1005 or M-1001 in another system (a matter budget tracker or the engagement letter), pull them in manually before drawing any budget-variance conclusion. Do not treat the absence of a finding here as evidence spend is on track. | LEDES 1998B has no budget/estimate field at all, so this extract cannot support a budget-variance finding in either direction -- confirming actual budgets before acting is the responsible next step. | Before this data is used to state a budget position to any stakeholder |

## Staffing Mix Findings

**Firm 58-1129034 -- Matter M-1005 (Document Review, Discovery Phase, task code L320) -- High severity**
All 10 fee line items on this matter (57.4 hours, $55,965) were billed by two PARTNR-classified timekeepers -- Castillo, Marcus D. and Harmon, Elizabeth R. -- at $975/hour. No associate or paralegal time appears anywhere on this matter. Document review is typically the archetypal task delegated to lower-cost timekeepers, so an all-partner staffing pattern here is a real outlier rather than a hunch.
*Driver:* Likely overstaffing rather than case complexity, though the file doesn't tell us why.
*Recommendation:* Push back on staffing for this matter's discovery phase specifically; require associate/paralegal staffing going forward and ask the firm to justify partner-level review on this invoice.

**Firm 13-4477216 -- Matter M-1001 (Vendor Contract Dispute, task codes L220/L210) -- Low severity**
Motion drafting and strategy conferences (67.3 hours, $63,935) were staffed by two partners -- Whitcombe, James A. and Reyes, Priya N. -- at $950/hour, which is reasonable for pre-trial motion work. Separately, 8.5 hours of legal research were delegated to an associate, Delgado, Sarah K., at $525/hour.
*Driver:* Normal, appropriately leveraged staffing.
*Recommendation:* No change needed. This matter is a useful internal benchmark of appropriate leverage when raising the M-1005 pattern with that firm.

## Budget Variance Findings

**No budget variance analysis is possible from this data.** LEDES 1998B does not carry a budget or estimate field, and none was supplied separately with this extract. We are not reporting an overrun or underrun finding for either matter because the data cannot support one -- doing so would mean inventing a number. If a budget-variance view is needed, obtain matter budgets from the source system (e.g., the matter management platform or the engagement letter) and re-run this analysis with that field populated.

## Allocation Findings

**Firm 58-1129034 vs. Firm 13-4477216 -- rate and leverage comparison -- Medium severity**
Partner billing rates between the two firms are broadly comparable ($975/hr vs. $950/hr), so this isn't primarily a rate-mismatch story. The meaningful difference is leverage: firm 58-1129034 shows zero associate/paralegal hours on the one matter in this extract, while firm 13-4477216 shows some (11% of hours). With only one invoice per firm here, this is a single data point, not a proven cross-matter pattern.
*Driver:* Possibly a firm-level staffing default rather than a one-off; can't confirm without more invoices from firm 58-1129034.
*Recommendation:* Track staffing mix on firm 58-1129034's future invoices before treating this as a firm-wide pattern. If the next 1-2 invoices repeat all-partner staffing on routine tasks, raise it as a billing-guideline issue rather than a one-off.

**Sample size / scope of this extract -- Low severity**
This extract contains only two matters, one invoice each, from two firms -- too small a sample to establish firm-wide or matter-type-wide patterns with confidence.
*Driver:* Data availability, not a finding about spend itself.
*Recommendation:* Treat the findings above as flags to watch, not confirmed patterns. Re-run this analysis once more invoices from these firms are available.

## AI Leverage Opportunities

The LEDES task codes and line-item descriptions support two scoped opportunities for follow-up. Matter M-1005 includes document-review activity (L320), which may be suitable for AI-assisted first-pass classification or prioritization. Matter M-1001 includes legal research and motion-drafting activity (L210/L220), where AI may assist with research organization or initial drafting support. These are workflow candidates, not promised savings: attorney review remains required, and any use must comply with confidentiality, privilege, client, firm, court, and applicable professional-responsibility requirements. Strategy, negotiation, and final legal judgment are not presented as automation targets.

## Data Limitations (LEDES 1998B format)

This extract is a genuine LEDES 1998B file -- identified by the `LEDES1998B[]` marker on line 1 and the pipe-delimited, bracket-terminated (`[]`) record structure that follows -- not a malformed or broken CSV. It was converted with `scripts/parse_ledes.py` into a normalized table before any analysis was run. That conversion has real, structural limitations inherent to the LEDES 1998B standard itself, not to this particular file, and they are stated here explicitly rather than being silently absorbed into the findings above:

- **No firm name field.** LEDES 98B carries only `LAW_FIRM_ID` (a tax ID / EIN, e.g. `58-1129034`, `13-4477216`). This report refers to firms by that ID throughout because no name is available in the data and none should be guessed. If you know which ID maps to which firm, substitute the name in before circulating this further.
- **No native matter-type field.** Matter type was approximated from each line item's UTBMS task code family (e.g., task code `L320` was mapped to "L300 series (Discovery)"). This is a reasonable proxy but is not the same as a true practice-area or matter-type classification, and some task codes fell outside the mapped ranges (labeled "Not specified in LEDES data").
- **No budget/estimate field.** LEDES 98B carries only actual billed amounts. Budget-variance analysis is not possible on this file alone, as reflected above -- no overrun/underrun figures have been invented to fill that gap.
- **Expense lines carry no timekeeper or hours.** The single expense line item ($412.00, expense code E106, matter M-1005) is included in total billed amounts but was excluded from all staffing-mix ratio calculations, consistent with how LEDES separates fee (F) and expense (E) line types.

## Spreadsheet Export

A companion Excel workbook (`ledes_review.xlsx`, with Summary / Action Plan / Findings / AI Leverage / Normalized Data tabs, including severity and priority color-coding) and a flat findings CSV (`ledes_review_findings.csv`) have been produced alongside this report for sorting, filtering, or sharing the underlying numbers.
