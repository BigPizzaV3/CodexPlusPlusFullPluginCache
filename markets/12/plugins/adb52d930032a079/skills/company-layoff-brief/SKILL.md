---
name: company-layoff-brief
description: "Use for questions about a specific company's U.S. layoffs, WARN Act notices, workforce reductions, plant closures or layoff history: whether a company is laying people off, an employer's layoff or WARN history, or its job cuts, closures or downsizing. Writes a sourced company layoff briefing. Use the DataCEVA US Layoff Notices connector to find and verify notices, counts, dates and state coverage."
---

# Company layoff brief

Write a short, sourced briefing on one employer's WARN layoff notices, using the DataCEVA US Layoff Notices
connector. Before answering for the first time in a conversation, read `references/warn-data-notes.md` for what
the data covers and how to cite it.

## Steps

1. **Find the company.** Call `get_company_layoff_history` with the company name the user gave. Add `states` or
   `since` only if the user asked for them.
   - If it returns no notices but offers `suggestions`, list them and ask which one the user means. Don't
     guess.
   - If `matched_companies` contains names that look like different businesses (for example a franchise or a
     company with a similar name), say which ones you included, and leave out the ones that are clearly
     different.
2. **Read the latest notices.** Call `get_layoff_notice` for the one to three most recent notices in
   `latest_notices`, to get the site, dates, worker count as published, layoff type and reason.
3. **Check coverage.** Call `get_data_coverage` for each state in the history (at most five), so you can say
   whether a state's list is current, partial or missing.
4. **Write the brief** in the format below.

## Format

**Headline** (two or three sentences): number of notices and workers, the period they span, the states, and
whether the most recent notice is recent (within about 90 days) or old. Give the data's as-of date.

**By year** (table: year, notices, workers) and **by state** (table: state, notices, workers), from the tool's
`by_year` and `by_state`.

**Latest notices** (table, newest first): filed date, layoff date, site (city, state), workers, type, source
(link to `notice_url`, or the agency's `state_warn_page` when there is no notice link).

**What this does and doesn't show** (three to five bullets), chosen from the notes that apply:
- WARN covers larger layoffs (generally 50 or more workers at one site), so smaller cuts won't appear.
- Totals leave out update and correction notices for an earlier notice; say how many were left out if the tool
  reports it.
- Any state in this history whose list is partial, saved-history-only or unavailable.
- Counts are as filed and can change in later updates.

## Rules

- Use only what the tools return. Don't add numbers, reasons or dates from memory, and don't predict future
  layoffs.
- Keep filed date and layoff date distinct, and label which one a date is.
- Never describe or look for individual employees.
- If the company has no notices, say that no WARN notices were found in the covered states, not that it has
  had no layoffs.
- Keep the brief under about 400 words plus tables unless the user asks for more.
