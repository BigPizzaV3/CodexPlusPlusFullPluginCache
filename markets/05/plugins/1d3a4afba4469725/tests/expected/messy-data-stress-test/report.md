# Outside Counsel Billing Review — Red Flags

**Data source:** `sample_messy_incomplete.csv` (6 line-items, 3 matters, 2 firms)
**Data type:** In-house / legal ops export — money paid to outside firms (columns present: Firm, Matter, Category, Timekeeper, Hrs, Rate, Total). No budget/estimate column is present anywhere in the file.
**Fixture status:** Synthetic test data only; no real client, matter, firm, timekeeper, or invoice data is included.
**Audience:** Internal legal operations, selected after the audience clarification step in the test scenario.

## A note on data quality before the findings

This file has several gaps that limit what can be said with confidence. Rather than filling them in, each is called out so nothing below rests on an invented number:

- **R. Diaz (Associate), ACME – Supply Contract**: Rate and Total are both blank. 18 hours were logged with no billed amount attached.
- **Beta Corp – Trademark Filing, row 4**: Timekeeper name *and* role are both blank. 12 hours were billed at $470/hr ($5,640 total), but there is no way to confirm whether this was associate, paralegal, or another timekeeper — the analysis below treats this row's role as unknown rather than guessing "associate" just because the rate looks lower than partner rate.
- **T. Wynn (Partner), ACME – Labor Grievance**: Hours and Total are both blank. Only the rate ($940) is known, so this line's contribution to total spend or staffing mix cannot be computed.
- **No budget or estimate column exists anywhere in this file.** Budget-variance analysis is not possible on this data — see that section below rather than a fabricated overrun/underrun figure.

Known, fully-populated billed amounts sum to **$60,240** (29,700 + 4,500 + 5,640 + 20,400). The true total is higher once the two incomplete lines are resolved, but by how much cannot be said from this data.

## Executive Summary

This is a small, 3-matter dataset split across two firms, and it's too thin to show a systemic pattern with confidence — but one line item stands out: Nolan Prescott Group billed 33 partner hours against only 18 associate hours (with the associate's rate/total unrecorded) on a commercial supply contract, a heavier partner load than the firm's own trademark matter in the same file. There is no budget data at all in this export, so no overrun/underrun conclusions can be drawn — that gap should be treated as a process fix in itself. Before drawing firm-level conclusions, the missing hours, rates, and one missing timekeeper role should be resolved with the firm.

## Staffing Mix Findings

- **ACME – Supply Contract (Nolan Prescott Group, Commercial): partner-heavy split worth a closer look.** J. Nolan (Partner) logged 33 hours at $900/hr ($29,700); R. Diaz (Associate) logged 18 hours with no rate/total recorded. Even taking the hours alone, that's roughly 65% partner time on a commercial contract matter — a category that typically leans on associate time for drafting and redlining, with partner time reserved for negotiation strategy and review. On the same firm's IP matter in this dataset (Beta Corp Trademark Filing), the partner-to-other ratio is closer to 5:12, i.e., associate/other-heavy. That contrast is suggestive of overstaffing on the Commercial matter, but with only one matter of each type in the file, this isn't yet a confirmed pattern — it's a single outlier, not a trend. **Recommendation:** ask Nolan Prescott Group for the task-level breakdown of J. Nolan's 33 hours on this matter, and get R. Diaz's missing rate/total filled in before deciding whether this is legitimate (e.g., complex negotiation) or a staffing mismatch worth addressing in the next engagement letter.

- **Beta Corp – Trademark Filing (Nolan Prescott Group, IP): role of the second timekeeper is unrecorded, which blocks a real staffing-mix read.** 12 hours were billed at $470/hr by an unnamed, unrecorded-role timekeeper alongside J. Nolan's 5 partner hours. $470/hr is well below the $900 partner rate, consistent with an associate or senior paralegal rate, but the file doesn't say so, and guessing would misstate the finding. **Recommendation:** get the firm to fill in the timekeeper name and role for this line before including it in any staffing-ratio conclusion — right now it can only be described as "5 partner hours + 12 hours at a non-partner rate," not confirmed as a specific staffing mix.

- **ACME – Labor Grievance (Kessler Wynn LLP, Employment): cannot be assessed for staffing mix.** T. Wynn (Partner)'s hours are missing entirely, so the partner/associate hour ratio for this matter cannot be calculated — only P. Ahn (Associate)'s 40 hours at $510/hr ($20,400) is usable. **Recommendation:** this is a data-completeness gap, not a staffing red flag by itself; request T. Wynn's hours from Kessler Wynn LLP before drawing any conclusion about this matter's staffing.

## Budget Variance Findings

**No budget or estimate column exists in this file, for any matter.** Per the instruction not to invent numbers where data is missing, no overrun, underrun, or variance figures are reported here. This is worth flagging as a process gap in its own right: without an estimate captured at matter intake, there is no way to know later whether $29,700 on a supply contract or $20,400 on a labor grievance was in line with expectations or a surprise. **Recommendation:** if this export is representative of what's tracked today, add a budget/estimate field at matter opening so future spend reviews can actually assess variance rather than staffing mix alone.

## Allocation Findings

- **Work is currently split cleanly by matter type across the two firms** — Nolan Prescott Group handles the Commercial and IP matters, Kessler Wynn LLP handles the Employment matter. On the data available, this looks purposeful (each firm working in a distinct area) rather than overlapping or duplicative, so there's no allocation red flag to raise here.
- **One rate-consistency note, not necessarily a problem:** J. Nolan (Partner) billed $900/hr on both the Commercial matter and the IP matter — the same rate regardless of matter type or complexity. A flat partner rate across practice areas is common and not inherently an issue, but it's worth confirming that's the negotiated rate card rather than a coincidence, especially if future data shows the same rate applied to markedly different complexity levels.
- With only 3 matters and 2 firms in this file, there isn't enough breadth to assess whether either firm is handling a mismatched share of routine vs. complex work — that assessment needs a larger sample than this export provides.

## AI Leverage Opportunities

**Not assessed from this fixture.** The incomplete export contains no task/activity codes or narrative work descriptions. Matter labels, rates, and role guesses are not sufficient evidence for an AI-opportunity finding; obtain task-level detail and resolve the missing fields first.

## Bottom line / next steps

1. Go back to both firms for the missing fields: R. Diaz's rate/total, T. Wynn's hours, and the name/role of the unrecorded Beta Corp timekeeper. None of the findings above can be finalized without these.
2. Treat the ACME Supply Contract's partner-heavy hours as a question to ask, not a conclusion — worth a task-level breakdown request.
3. Add a budget/estimate field to future exports; its absence here blocks the single most useful spend-management check (variance against plan).
