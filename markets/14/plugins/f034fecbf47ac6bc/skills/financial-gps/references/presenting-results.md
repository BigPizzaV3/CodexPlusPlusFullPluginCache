# Presenting results

## The shape of an answer

1. **The answer first.** Quote the tool's headline line, or say it in one sentence that keeps its numbers and tier.
2. **Why, in two or three numbers:** what they'd owe when repayment starts, the 10-year payment, the share with its tier, and money left each month.
3. **What would change it:** borrowing less (the ceiling line says by how much), a different field or school, more grant aid, a downside scenario.
4. **One next step:** a follow-up question, a comparison, or the site's tool link.

Keep the first answer short. Leave the rest of the result for follow-up questions.

## Numbers

- Use the figures as the tools give them. Dollars in whole dollars, shares to one decimal ("7.2%"), the tier next to the share ("7.2%, Excellent").
- Money left each month is **before tax**; say so the first time it appears.
- Name the earnings basis once: "typical pay four years after graduating", "the downside case", or "your own figure" when `earnings_annual` was used.
- Name the allowance and its year once per answer.
- Don't round tool figures further, add them together, or derive new ones (break-even years, totals across scenarios). If a number isn't in a result, it doesn't go in the answer.

## Parent results

Show three things:
1. The 10-year payment with its share and tier, on the parent scale.
2. The billed standard plan: the monthly bill, how many years, and the ages it runs. Say so when it runs past 67.
3. Anything above the caps, as a gap to fill some other way, not as borrowing.

Keep the student's and the parents' results separate. Never combine them into one tier.

## Comparisons

A table works when there are two to four schools:

| | School A | School B |
|---|---|---|
| Field used | | |
| Typical pay, four years out | | |
| Owed when repayment starts | | |
| 10-year payment | | |
| Share of pay above basic expenses | | |
| Money left each month (before tax) | | |
| Most you can owe and stay in Good | | |
| Six-year graduation rate | | |

Fill it only from `compare_schools`. Keep the columns in the order the user named the schools. Follow the table with the conditional framing in `comparisons.md`, not a verdict.

## Links

- Each check returns a `site_tool_url` (collegeazimuth.com's Financial GPS tool for that school). Offer it when the user wants to try different amounts or scenarios: the site has the sliders, and it runs the same rules.
- `find_school` returns each school's page URL. Use it when the user wants more about the school.
- Link to no other site for figures.

## Visual displays

Plain text and tables are the default. Where the surface supports artifacts and a picture helps (a comparison chart, a bar of money left by scenario), a static display of tool results is fine. It must:
- show only figures from tool results, labeled with the earnings basis, the allowance and its year;
- not compute anything: no sliders or calculators that recalculate payments, which would be a second copy of the math;
- use the exact tier labels;
- point to the site's tool for interactive changes.

## Formats

The checks take `format: "compact"` by default, which returns the numbers and the headline. Ask for `format: "full"` when the user wants the whole picture: the detail line, limits, owe and ceiling lines, the rules text and the source note. Use full when presenting a final summary for a decision; keep compact for quick back-and-forth.

## Source line

When a summary will be saved or shared, end it with a short source line built from the result: "Federal rates for [academic year]; earnings and debt from College Scorecard via College Azimuth; basic expenses at 150% of the [year] federal poverty guideline. A planning estimate, not financial advice."
