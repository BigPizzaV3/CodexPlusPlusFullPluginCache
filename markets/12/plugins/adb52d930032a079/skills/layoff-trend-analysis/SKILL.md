---
name: layoff-trend-analysis
description: "Use for U.S. layoff trend research, comparisons, rankings and statistics from WARN Act notices: whether layoffs are rising or falling, which states, industries or companies filed the most notices, and how time periods, states, census regions, industries or companies compare by notices or affected workers. Use the DataCEVA US Layoff Notices connector to retrieve comparable data and check state coverage before drawing conclusions."
---

# Layoff trend analysis

Answer trend and ranking questions with WARN layoff notices, using the DataCEVA US Layoff Notices connector,
and make every comparison fair. Before answering for the first time in a conversation, read
`references/warn-data-notes.md` for what the data covers and how to cite it.

## Steps

1. **Define the comparison.** Decide what is compared (periods, states, regions, industries or companies), the
   measure (notices, workers, or both) and the period. With no period, use the last two full years by month,
   or the last five full years by year for long-run questions.
2. **Check coverage first.** Call `get_data_coverage` (for the states involved, or all states for national
   questions). For each state, note `first_filed`, `last_filed`, `last_refreshed` and `status`. Only compare
   periods that every included state covers. Leave out, or list separately, states whose history starts later,
   ends earlier, or is unavailable.
3. **Get the numbers.** Call `summarize_layoffs` with the matching `group_by` (`month`, `quarter`, `year`,
   `state`, `census_region`, `industry` or `company`) and filters.
   - If GA, NJ, PA or MI matter to the question, run it a second time with `include_scheduled_only: true` and
     explain that those states publish only planned layoff dates.
   - For industry questions, say that industry is reported by some states only (the tool's caveats name them).
4. **Make it fair.**
   - Treat the current period as incomplete: label it, or compare like with like (for example January to
     September of each year).
   - Show changes as numbers and percentages, and don't call small differences a trend.
   - Rankings: give both notices and workers; one very large notice can dominate workers.
5. **Write the analysis** in the format below.

## Format

**Answer** (two or three sentences) that directly answers the question with the key numbers.

**Table** of the series or ranking (period or group, notices, workers, change).

**How this was measured** (two to four bullets): the period, the states included and left out, filed date or
planned layoff date, and that update notices are not counted twice.

**Limits** (bullets that apply): WARN covers larger layoffs only, so it is a floor rather than a count of all job
losses; industry coverage; partial or missing states; the as-of date.

## Rules

- Use only what the tools return; don't mix in other statistics (such as BLS figures) unless the user provides
  them, and label any outside figure as not from WARN data.
- Don't forecast future layoffs; describe past and current filings only.
- Never describe or look for individual employees.
