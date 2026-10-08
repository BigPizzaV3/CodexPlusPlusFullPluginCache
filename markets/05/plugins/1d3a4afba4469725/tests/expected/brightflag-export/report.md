# Q3 Outside Counsel Panel Review -- Brightflag Line Item Export (Internal)

**Audience:** Internal legal ops review
**Fixture status:** Entirely synthetic test data; no real client, matter, firm, timekeeper, or invoice data is included.
**Source file:** `sample_brightflag_line_item_export.csv` -- a Brightflag "Line Item Report" export (28 line items, 3 invoices, 3 matters, 3 outside counsel firms, all for a single synthetic client entity, Acme Industries, Inc.). This is a clean, well-formed e-billing export, not a LEDES file and not a messy/malformed one -- no parsing or reconstruction was needed, only column normalization.

## Executive Summary

Across the three matters in this export, staffing mix -- not hourly rate -- is the story. Whitfield Bosch billed 100% of its document-review work on M-1005 (67.3 hours, \$65,617.50 in fees) at partner rates with zero associate or paralegal involvement, and Harmon & Slate billed 92% of its motion-drafting work on M-1001 (71.1 of 77.5 fee hours) at two-partner rates with only 6.4 associate hours of legal research. Reyes Chen Kaplan's M-1003 provides a positive example of associate-led drafting with partner review, but the matters are different work categories and should not be treated as a like-for-like rate benchmark. This export has no budget or estimate field, so no budget-variance conclusion is offered anywhere in this report; the findings below are staffing-mix and allocation findings only, and several of the flagged task types (document review, legal research, routine drafting) are also strong candidates for AI-assisted first-pass work, addressed in its own section below.

## Recommended Actions

| Priority | Action | Why It Matters | Timeframe |
|---|---|---|---|
| 1 | Require associate- or paralegal-level staffing for first-pass document review (task L320) in the next engagement letter or billing guidelines with Whitfield Bosch, reserving partner time for privilege calls and QC. | This single pattern is the largest cost-mix issue in the dataset: 67.3 hours of document review, all billed at the \$975/hr partner rate, on a matter where the client's own panel (Reyes Chen Kaplan, M-1003) shows the same client using associate-led staffing successfully. | Immediately -- M-1005 is still in the discovery phase, so this affects invoices still to come. |
| 2 | Ask Harmon & Slate directly why two partners (Whitcombe and Reyes) are both billing full days of motion drafting and co-counsel strategy calls on M-1001, and request that routine drafting shift to an associate with partner-level revision only. | 92% of the fee hours on this litigation matter are partner-billed; the two-partner drafting pattern is the second-largest staffing-mix concern and is happening on an open matter. | Immediately -- M-1001 appears to be an active, ongoing litigation. |
| 3 | Adopt a panel-wide staffing expectation tied to task and phase, such as associate- or paralegal-led first-pass document review unless complexity is documented. | The three matters are not like-for-like rate comparisons, but each shows whether senior time is aligned with the described work. A shared task-level guideline makes future comparisons more defensible. | Before next engagement letter / panel renewal with each firm. |
| 4 | Add a budget or estimate field to matter setup in Brightflag (or require it from firms at matter intake) going forward. | This export has no budget/estimate column at all, so this quarter's review cannot say whether any matter ran over or under plan -- that is a real analytical gap, not a clean bill of health. | Ongoing practice change -- implement before next quarter's data pull. |
| 5 | Before assigning the next document-review-heavy or research-heavy matter, evaluate AI-assisted first-pass review/drafting tools (subject to the firm's or department's confidentiality and AI-use policy) as a way to reduce the volume of hours billed for this kind of work in the first place. | Document review, legal research, and template-style drafting collectively account for a large share of the hours in this dataset and are exactly the categories of work AI-assisted tools are best suited to accelerate as a first pass. | Ongoing practice change -- evaluate ahead of the next discovery-heavy or drafting-heavy matter. |

## Staffing Mix Findings

**Whitfield Bosch -- M-1005, Document Review / Discovery Phase (task L320 / activity A104) -- High severity**
All 10 fee line items on this matter (67.3 hours, \$65,617.50) were billed by two partner-level timekeepers -- Elizabeth R. Harmon (22 years) and Marcus D. Castillo (17 years) -- both at \$975/hour, for "review of produced documents for responsiveness and privilege." No associate or paralegal time appears anywhere on this matter, including on the accompanying e-discovery hosting expense line. Document review is typically the most delegable task type on a litigation matter, so an all-partner pattern here is a real outlier, not a hunch -- especially set against M-1003 in this same export, where a comparable review/drafting task was staffed at the associate level.
*Driver:* Likely overstaffing rather than case complexity -- nothing in the line descriptions suggests this document review required partner-level judgment throughout, and the firm shows no associate/paralegal bench being used on this matter at all.
*Recommendation:* Require associate- or paralegal-level (or contract-reviewer) staffing for first-pass document review going forward; reserve partner time for privilege-call escalations and QC sampling. Raise this specific invoice with Whitfield Bosch and ask them to justify the all-partner staffing.

**Harmon & Slate LLP -- M-1001, Vendor Contract Dispute (task L220/A103 drafting, task L210/A102 research) -- Medium-High severity**
Two partners -- James A. Whitcombe (25 years) and Priya N. Reyes (14 years) -- billed 71.1 of the matter's 77.5 fee hours (92%) drafting and revising motion papers and holding strategy calls with co-counsel, each logging near-full days across ten separate dates through the month. The only non-partner time on the matter is 6.4 hours of legal research from an associate, Sarah K. Delgado, billed at the very end of the period. Two partners carrying nearly all of the drafting workload on the same motion, with associate involvement limited to a small research slice, suggests the firm isn't delegating first-draft work even though the matter has an associate available.
*Driver:* Staffing mix / possible redundant senior coverage -- both partners appear to be doing overlapping drafting and call work rather than one partner directing and an associate drafting.
*Recommendation:* Ask Harmon & Slate to clarify why two partners are needed on the same motion, and request an associate-first drafting workflow with partner-level review only -- using Reyes Chen Kaplan's M-1003 staffing (below) as the internal benchmark for what "normal" leverage looks like on this panel.

**Reyes Chen Kaplan -- M-1003, IP Licensing Agreement Renewal (task L190, activity A103 drafting / A104 review) -- No flag (benchmark)**
An associate, Daniel O. Reyes (6 years), billed 16.5 of the matter's 18.5 fee hours (89%) drafting license agreement amendments; a partner, Cheryl A. Kaplan (19 years), billed 2.0 hours for final review of the license terms before it went out. This is an efficient, well-leveraged staffing model -- associate does the drafting, partner does the final sign-off -- and is the pattern the other two matters in this dataset should be compared against.
*Driver:* Normal, appropriately leveraged staffing. No action needed on this matter itself.
*Recommendation:* Use this matter as the internal reference point when raising the M-1005 and M-1001 staffing patterns with Whitfield Bosch and Harmon & Slate.

## Budget Variance Findings

**No budget variance analysis is possible from this data.** The Brightflag export provided contains no budget, estimate, or fee-cap field of any kind -- only Line Quantity, Line Unit Cost, Line Amount, their "Adjusted" counterparts, and each Invoice Gross Total. (In this export, the adjusted quantities/rates/amounts are identical to the unadjusted ones on every line, meaning nothing was reduced or rejected on review, but that is a billing-adjustment observation, not a budget comparison.) No overrun or underrun finding is offered for M-1005, M-1001, or M-1003, in either direction, because doing so would mean inventing a number the data does not support. If matter budgets exist elsewhere (a matter-management system, the engagement letter, or a legal ops tracker), pull them in and re-run this analysis with that field populated -- until then, this section should be read as "not assessed," not as "on budget."

## Allocation Findings

**Cross-firm staffing observations for the same client -- Medium severity**
All three matters bill the same client entity, but they cover different work categories: document review, motion practice, and license-amendment drafting. Their blended effective rates therefore are not a like-for-like performance comparison. The useful cross-firm observation is narrower: the descriptions allow the client to ask whether each task used an appropriate senior/junior mix, and M-1005 remains a clear within-matter leverage concern.
*Driver:* The available sample mixes task types and contains only one matter per firm, so it cannot distinguish firm habit from matter complexity at a panel-wide level.
*Recommendation:* Adopt a task- and phase-specific staffing guideline, then use additional matters of the same type before drawing comparative firm-performance conclusions.

**Whitfield Bosch -- single-tier staffing model -- Medium severity**
Across all 11 line items on this invoice (10 fee lines plus the e-discovery hosting expense), no junior timekeeper appears anywhere -- this looks like a firm-level resourcing choice (a lean or partner-heavy team with limited bench) rather than a one-off decision on this matter.
*Driver:* Could be a genuine bench limitation at this firm, or simply a lack of a staffing plan in the engagement letter -- the data can't distinguish between the two.
*Recommendation:* Confirm the firm's available associate/paralegal bench at the next renewal conversation. If the firm genuinely lacks junior capacity, consider routing high-volume, lower-complexity work like document review to a different panel firm or a review vendor instead.

**Sample size caveat -- Low severity**
This export covers one invoice per matter, one matter per firm, for a single month. That's enough to spot a stark within-matter staffing pattern (as above) but not enough to declare a firm-wide habit confirmed across every matter type each firm handles.
*Driver:* Data availability, not a finding about spend itself.
*Recommendation:* Treat the cross-firm comparison above as a flag to watch and confirm with additional invoices/matters from these firms before it hardens into a formal panel policy position.

## AI Leverage Opportunities

E-billing data alone can't tell you exactly how many hours AI would save -- that would be a fabricated number dressed up as analysis. What it can tell you is which categories of billed work, based on the task codes, activity codes, and line descriptions in this export, are a good structural fit for AI-assisted first-pass work versus which ones aren't. Any use noted here still requires attorney review of AI output before reliance, and has to go through the firm's or department's confidentiality, privilege, and AI-use policy first -- that's a genuine professional-responsibility question, not a formality.

**Document review / responsiveness & privilege triage -- Whitfield Bosch, M-1005 (task L320/A104) -- High opportunity**
67.3 hours of "review of produced documents for responsiveness and privilege" is exactly the high-volume, pattern-based task type where AI-assisted first-pass document review tools do meaningful work today (responsiveness triage, privilege-term flagging, near-duplicate/thread clustering). This is also the matter flagged above as all-partner staffed -- an AI-assisted first pass wouldn't just save associate hours, it changes the staffing conversation with the firm entirely, since much of this volume shouldn't need partner-level eyes at all in a first pass.
*Caveat:* Privilege calls specifically carry real risk if relied on without attorney review; any AI-assisted review workflow here needs to run through Whitfield Bosch's (or the client's) confidentiality/AI-use policy before this document set touches a tool, and every privilege determination still needs attorney sign-off.

**Legal research -- Harmon & Slate, M-1001 (task L210/A102) -- High opportunity**
The 6.4 hours of "legal research re: breach of contract remedies" billed by an associate is a discrete, well-scoped research question -- a strong candidate for an AI-assisted first-pass research memo or issue summary that the associate then verifies and refines, rather than starting the research from a blank page.
*Caveat:* Case-law citations and holdings from AI research tools still need independent verification (citation accuracy and currency in particular) before they go into any filing.

**Motion drafting -- Harmon & Slate, M-1001 (task L220/A103) -- Medium opportunity, mixed**
The 71.1 hours billed here bundle two different things: drafting/revising motion papers (template-like sections -- procedural history, standard recitations, boilerplate -- are a reasonable AI-assisted-first-draft candidate) and "strategy calls with co-counsel" (case-specific judgment, not an AI target at all). Only the drafting portion is a fit; the strategy component should stay exactly as-is.
*Caveat:* Even for the drafting portion, motion strategy and argument framing are substantive attorney work -- AI's role here is a first-draft shell for routine sections, not the persuasive argument itself, and every draft needs full attorney revision before filing.

**Contract/license amendment drafting -- Reyes Chen Kaplan, M-1003 (task L190/A103) -- Medium-High opportunity**
16.5 hours drafting license agreement amendments against an existing agreement is playbook-style work -- a good fit for AI-assisted drafting or redlining against a standard license template or clause library. Notably, this matter already has an efficient human staffing model (associate drafts, partner reviews); AI assistance here would compress the associate's first-draft time further rather than fix a staffing problem, since the staffing is already sound.
*Caveat:* License terms have deal-specific and client-specific nuance; any AI-assisted draft still needs the same partner-level final review this matter already has built in -- AI should shorten the first draft, not replace the review step.

**Final license review and privilege/strategy judgment calls -- all matters -- Low opportunity**
Cheryl Kaplan's final review of license terms (M-1003), the privilege-call component of document review (M-1005), and the strategy-call component of motion practice (M-1001) are not AI targets. These are exactly the moments where case-specific judgment and client relationship management are the value being delivered, not hours to be reduced.

## Spreadsheet Export

A companion Excel workbook (`brightflag_review.xlsx`, with Summary / Action Plan / Findings / AI Leverage / Normalized Data tabs, including severity, priority, and opportunity-level color-coding) and a flat findings CSV (`brightflag_review_findings.csv`) have been produced alongside this report for sorting, filtering, or sharing the underlying numbers.
