# Vantage Health Systems — Q2 Outside Counsel Spend Review
**Audience:** Internal review (your own review, legal ops)
**Data:** Q2 outside counsel invoices, 3 firms, 8 matters, 17 line items — Merrow Kline LLP, Osei Bramwell Fitch, Corrigan Vance LLP
**Fixture status:** Synthetic test data only; no real client, matter, firm, timekeeper, or invoice data is included.

*Note on data completeness: this file is a clean tabular export (not a raw LEDES file), and it does include a budget/estimate column, so budget-variance analysis is fully supported. It does not include task/activity codes or narrative line-item descriptions, so AI-leverage opportunities are not assessed from this fixture.*

---

## 1. Executive summary

Q2 outside counsel spend came in at **$196,410 against a combined budget of $145,000 — 35.5% over ($51,410)**, but that overrun is not evenly spread: it's concentrated almost entirely in two matters. One Data Privacy matter (VH-401) was staffed entirely by a partner with no associate support and ran 122% over its estimate, and one Litigation matter (VH-404) ran partner-heavy and 40% over. By contrast, Commercial Contracts work — handled consistently at the associate/paralegal level — came in *under* budget on both matters. The headline story is a staffing-mix problem on two specific matters, not a firm-wide rate or scoping issue.

## 2. Recommended actions

**1. Follow up now on VH-401 (Patient Data Breach Notification Review, Merrow Kline LLP) if it's still open.**
- *Why it matters:* This is the single largest overrun in the dataset — $34,300 over a $28,000 estimate (+122%) — driven by 70 hours billed entirely at partner rate with zero associate or paralegal involvement.
- *Timeframe:* Immediately.

**2. Require a minimum associate-hour allocation on breach-response engagements in the next Merrow Kline engagement letter.**
- *Why it matters:* Notification-tracking and correspondence logistics on a breach-response matter don't typically require partner-level work throughout; without a staffing floor/ceiling this recurs on the next incident.
- *Timeframe:* Before next engagement letter / renewal.

**3. Get an itemized breakdown of the two partner time blocks (30h + 18h) on VH-404 (Wrongful Termination Defense, Osei Bramwell Fitch) before the matter closes.**
- *Why it matters:* Second-largest overrun in the dataset (+40%, $18,150), driven by partner hours (48) nearly matching associate hours (45) — a heavier senior/junior ratio than document-intensive defense work typically needs.
- *Timeframe:* Before the matter closes.

**4. Set a shared staffing benchmark for Regulatory Compliance work regardless of which firm handles it.**
- *Why it matters:* Two Regulatory Compliance matters with similar total hours (28 vs. 30) were staffed in opposite ways — partner-heavy at Corrigan Vance (VH-407, +17% over budget) vs. associate-heavy at Merrow Kline (VH-408, +7.6% over budget). The associate-heavy model cost less on comparable hours; formalizing that expectation across firms would likely have avoided VH-407's overrun.
- *Timeframe:* Ongoing practice change / next intake instructions.

**5. Revisit intake estimates specifically for Data Privacy and Litigation matter types.**
- *Why it matters:* Those two matter types drove essentially the entire overrun (+86% and +40% respectively), while Commercial Contracts landed 9–12% *under* estimate on both of its matters and Employment landed 21% under. This isn't a firm-billing problem across the board — it looks like intake estimates for privacy/litigation work aren't accounting for realistic staffing, while other matter types are reasonably well-calibrated.
- *Timeframe:* Next budgeting cycle.

## 3. Staffing mix findings

**Merrow Kline LLP — VH-401 Patient Data Breach Notification Review — High severity**
*Driver:* All 70 hours were billed by a partner at $890/hr, with no associate or paralegal support at all — unlike VH-402, the firm's other Data Privacy matter, which used only associate/paralegal time. Partner-only staffing on a matter that likely includes notification-list tracking, correspondence logistics, and vendor coordination looks like overstaffing rather than a matter that genuinely required senior judgment for all 70 hours.
*Recommendation:* Request a role breakdown of the 70 partner hours; require a minimum associate-hour allocation on future breach-response engagements with this firm.

**Osei Bramwell Fitch — VH-404 Wrongful Termination Defense — Medium severity**
*Driver:* Partner hours (48, billed across two separate entries) slightly exceed associate hours (45) on this litigation defense matter — a near 1:1 senior-to-junior ratio, heavier than typical for document-intensive defense work where associate-led discovery review usually dominates.
*Recommendation:* Request an itemized description of the two partner blocks (30h, 18h) to confirm how much was strategy/negotiation versus work an associate could have absorbed; set staffing-ratio expectations for discovery-heavy phases in the next engagement letter.

**Corrigan Vance LLP (VH-407) vs. Merrow Kline LLP (VH-408) — Regulatory Compliance — Medium severity**
*Driver:* Two Regulatory Compliance matters with comparable total hours (28 vs. 30) were staffed in opposite ways: VH-407 (State Licensing Compliance Review) used partner-heavy staffing (20 partner / 8 associate hours), while VH-408 (HIPAA Risk Assessment) used associate-heavy staffing (24 associate / 6 partner hours). The partner-heavy approach cost more ($21,120) than the associate-heavy approach ($17,220) on fewer total hours, and drove a larger budget overrun.
*Recommendation:* Set a shared staffing benchmark for regulatory/compliance review (e.g., associate-led with partner review of findings) and apply it regardless of which firm is doing the work.

**Corrigan Vance LLP — VH-405 and VH-406 (Commercial Contracts) — Low severity / no outlier**
*Driver:* Both matters used a consistent associate + paralegal staffing model with no partner time, and both landed modestly under budget. This is a clean staffing pattern, not a flag.
*Recommendation:* No change needed — worth using as the reference model when setting staffing expectations for other matter types.

## 4. Budget variance findings

| Matter | Firm | Billed | Budget | Variance | Severity |
|---|---|---|---|---|---|
| VH-401 Patient Data Breach Notification Review | Merrow Kline LLP | $62,300 | $28,000 | **+122% (+$34,300)** | High |
| VH-404 Wrongful Termination Defense | Osei Bramwell Fitch | $63,150 | $45,000 | **+40% (+$18,150)** | High |
| VH-407 State Licensing Compliance Review | Corrigan Vance LLP | $21,120 | $18,000 | +17% (+$3,120) | Medium |
| VH-408 HIPAA Risk Assessment | Merrow Kline LLP | $17,220 | $16,000 | +7.6% (+$1,220) | Low |
| VH-403 Employment Handbook Update | Osei Bramwell Fitch | $5,520 | $7,000 | −21% (−$1,480) | Low (underrun) |
| VH-402 Vendor Data Processing Agreement | Merrow Kline LLP | $8,400 | $10,000 | −16% (−$1,600) | Low (underrun) |
| VH-405 MSA – Supplier Renewal | Corrigan Vance LLP | $10,560 | $12,000 | −12% (−$1,440) | Low (underrun) |
| VH-406 SaaS Vendor Contract Review | Corrigan Vance LLP | $8,140 | $9,000 | −9.6% (−$860) | Low (underrun) |

**VH-401 (High):** *Driver* — partner-only staffing (see Staffing Mix). *Recommendation* — escalate now if open; use as the concrete example in a staffing-terms conversation with Merrow Kline.

**VH-404 (High):** *Driver* — partner-heavy staffing on defense work. *Recommendation* — confirm remaining scope and request a revised estimate plus staffing plan for any phases left.

**VH-407 (Medium):** *Driver* — partner-heavy staffing relative to its Regulatory Compliance peer (VH-408). *Recommendation* — discuss whether future licensing-review matters can run associate-led.

**VH-408 (Low):** *Driver* — modest overrun, consistent with efficient associate-led staffing. *Recommendation* — no action needed beyond routine monitoring.

**Underruns — VH-403, VH-402, VH-405, VH-406 (Low, as a group):** *Driver* — four matters across three matter types landed 9.6–21% under estimate. This is a *consistent, modest* pattern rather than a dramatic one-off, which more plausibly reflects reasonably (or slightly conservatively) set estimates than a scoping problem. *Recommendation* — no action now; if underruns of this size persist next quarter, consider tightening these matter types' estimates.

## 5. Allocation findings

**Firm-to-matter-type assignment overall — Low severity / no outlier**
*Driver:* Each firm handles a coherent bucket of work — Merrow Kline: Data Privacy + HIPAA-adjacent Regulatory Compliance; Osei Bramwell Fitch: Employment + Litigation; Corrigan Vance: Commercial Contracts + (licensing) Regulatory Compliance — and partner/associate/paralegal rates step down appropriately within each firm (partner rates cluster $875–$890, associate $440–$495, paralegal $220–$245). This doesn't look like historical inertia; it looks like intentional specialization.
*Recommendation:* No change needed.

**Regulatory Compliance split across two firms with no shared staffing approach — Medium severity**
*Driver:* Regulatory Compliance matters go to two different firms (Corrigan Vance for licensing, Merrow Kline for HIPAA) with no apparent coordination on how the work should be staffed — which is likely *why* VH-407 and VH-408 ended up staffed so differently (see Section 3). This looks like an intake/process gap, not either firm doing something wrong.
*Recommendation:* When routing a new Regulatory Compliance matter, specify the expected staffing model in the intake instructions regardless of which firm receives it.

## 6. AI leverage opportunities

**Not assessed from this fixture.** Matter names, roles, rates, and hours do not establish what work was actually performed. Because the export has no task/activity codes or narrative line-item descriptions, it does not support a defensible AI-opportunity finding. Obtain task-level billing narratives or equivalent work descriptions before evaluating AI leverage, then apply attorney-review, confidentiality, privilege, privacy, and client-policy safeguards.

---

## Spreadsheet export

A companion workbook (`vantage_review.xlsx`) and a flat findings CSV (`vantage_review_findings.csv`) are included alongside this report — Summary, Action Plan, Findings, AI Leverage, and Normalized Data tabs, so you can sort, filter, or hand specific rows to someone else without re-reading the prose above.
