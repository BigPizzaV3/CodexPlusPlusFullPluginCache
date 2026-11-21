---
name: narrative-search
description: Search site diary narratives for keywords or themes — find evidence for
  claims across all shift records, mentions of events, issues, instructions, or conditions.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Narrative Search — Find Evidence in Site Diary Narratives

Search across all shift diary narratives for specific keywords, phrases, or themes. Replaces the manual process of reading hundreds of diary entries — a QS can find every relevant mention in seconds.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Search Terms

Parse `the user’s request` for:

1. **Project name** — resolve using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
2. **Search terms** — everything remaining in `the user’s request` after the project name is resolved. These are the keywords or phrases the user wants to find in narratives.
3. **Date range** — if the user specifies a date range, parse using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`. If no date range is specified, default to the **last 4 weeks** and state this plainly, with how to widen it: "Searched the last 4 weeks — say a date range (or 'all history') to widen." A full-history search is a valid explicit choice; use a wide fixed window (e.g. 5 years back to today) and note that cached-report retention may limit how far back results actually reach.

If no search terms are provided, ask the user:
> "What would you like to search for? You can provide:
> - **Exact phrases** — e.g. `"stop notice"` (in quotes for exact match)
> - **Keywords** — e.g. `drainage access delay` (finds narratives containing any of these)
> - **Themes** — e.g. `access problems` (I'll expand this to related terms)"

Per **Pattern 2**, confirm the interpreted parameters with the user **only when the interpretation was non-trivial** (e.g. an ambiguous theme, a relative date phrase with multiple readings, or uncertainty over which token was the project vs the search term). When the project and terms are unambiguous, proceed without confirmation. When confirmation is warranted:
> "I'll search narratives for **[project name]** looking for: **[search terms]**[, from **[start date]** to **[end date]**]. Does that look right?"

---

## Step 2: Retrieve Narrative Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardNarrative`
- **Project:** the resolved project UUID
- **Date range:** the parsed from/to dates (or full project range if no dates specified)

If no data is returned, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. Specifically suggest:
- Narratives may not be recorded for this project — check whether supervisors are writing shift narratives
- If a date range was specified, try expanding it or removing the date filter
- Check the project name is correct

---

## Step 3: Search and Match

Apply the search terms against every narrative entry. Support three search modes:

### Mode 1: Exact Phrase Search
If the user provided terms in quotes (e.g. `"stop notice"`), search for that exact phrase (case-insensitive).

### Mode 2: Keyword Search (OR)
If the user provided multiple unquoted words (e.g. `drainage access delay`), search for narratives containing **any** of the specified words. Rank results by number of keywords matched (narratives matching multiple terms appear first).

### Mode 3: Thematic Search
If the user provided a theme or concept rather than specific keywords, expand the search to include related terms. Use the following expansions:

| Theme | Search Terms |
|---|---|
| access problems | access, possession, couldn't get on site, could not access, no access, denied access, restricted access, blocked, site closed, late access, late possession |
| weather issues | rain, heavy rain, wind, high wind, storm, snow, ice, frost, frozen, flooding, flooded, waterlogged, weather, inclement, adverse weather |
| delays | delay, delayed, disruption, disrupted, standing time, stood down, waiting, idle, hold, hold-up, holdup, stoppage, suspended, lost time |
| safety | safety, incident, accident, near miss, near-miss, unsafe, hazard, RIDDOR, injury, first aid, stop work, safety stand-down, toolbox talk |
| design issues | design, drawing, RFI, request for information, awaiting information, awaiting design, design change, revised drawing, discrepancy, clash, coordination |
| instructions | instruction, instructed, directed, PM instruction, client instruction, variation, variation order, compensation event, CE, early warning |
| plant / equipment | plant, machine, excavator, dumper, crane, roller, piling rig, breakdown, broken down, defect, LOLER, inspection, maintenance |
| material issues | material, delivery, no materials, shortage, awaiting delivery, wrong material, damaged, rejected, concrete, steel, aggregate, sub-base |
| quality | quality, inspection, rejected, failed, non-conformance, NCR, defect, snag, rework, re-work, specification |
| subcontractor | subcontractor, sub-contractor, subbies, specialist, nominated, domestic sub |

If the user's theme does not match any of the above, perform a best-effort keyword search and inform the user which terms were used.

### For Each Match

Extract and store:
- **Date** of the shift
- **Supervisor** who wrote the narrative
- **Shift reference** (ID or reference number)
- **Matching excerpt** — the sentence(s) containing the match, plus one sentence of context before and after
- **Match term** — which search term triggered the match

---

## Step 4: Follow Up on Key Matches (If Requested)

If the user asks for more detail on a specific match, or if a match appears particularly significant (e.g. a stop notice, a formal instruction, or a safety incident), follow **Pattern 20 (Evidence Retrieval)** in `../../shared/patterns/20-evidence-retrieval.md` to fetch the full `getShiftRecord`, including its record-lookup fallback when the `dashboardNarrative` row carries no shift-record ID, and its pagination/quoting/citation rules.

---

## Step 5: Present Search Results

### Narrative Search Results — [Project Name]
**Search terms:** [terms used, including any thematic expansions]
**Period searched:** [start date] to [end date]
**Total narratives scanned:** [count]
**Matches found:** [count]

### Chronological Results

Present matches in date order, with the search term highlighted in the excerpt:

---

**[Date]** — Supervisor: [name] — Ref: [shift reference]

> "...[preceding context]. **[matching text with search term]**. [following context]..."

Match: `[term that matched]`

---

**[Date]** — Supervisor: [name] — Ref: [shift reference]

> "...[preceding context]. **[matching text with search term]**. [following context]..."

Match: `[term that matched]`

---

If there are more than 15 matches, show the first 15 and summarise the remainder:
> "Showing 15 of [total] matches. [Remaining count] additional matches found between [date] and [date]. Would you like to see the next batch, or narrow the search?"

### Frequency Analysis

Show how often the search terms appear over time:

| Month | Matches |
|---|---|
| January 2026 | 8 |
| February 2026 | 12 |
| March 2026 | 3 |

Or if the period is shorter than 3 months, show weekly:

| Week Commencing | Matches |
|---|---|
| 2026-01-06 | 3 |
| 2026-01-13 | 5 |
| 2026-01-20 | 2 |

### Related Terms Found

List other notable terms or phrases found alongside the search terms in matching narratives. This helps the user discover related issues they may not have searched for:
> "In narratives mentioning **[search term]**, the following related terms also appeared frequently: [term 1] ([count] times), [term 2] ([count] times), [term 3] ([count] times)."

### Summary

Provide a brief summary of the findings:
- Total matches and date range of matches
- Peak periods (when mentions were most frequent)
- Key supervisors (who reported the most matches — they may have the most knowledge of the issue)
- Whether the issue appears ongoing, resolved, or escalating based on the frequency trend

---

## Step 6: No Results Handling

If the search returns no matches, provide helpful guidance:

> "No narratives matching **[search terms]** were found for **[project name]**[ between **[dates]**]."
>
> **Suggestions:**
> - Try alternative terms — for example, instead of "delay" try "waiting", "standing time", "held up"
> - Broaden the date range if one was specified
> - Check spelling of specific terms
> - Try a thematic search — e.g. "access problems" instead of a single keyword
>
> **Available themes for expanded search:** access problems, weather issues, delays, safety, design issues, instructions, plant/equipment, material issues, quality, subcontractor

---

## Related Skills

After presenting results, suggest these related skills for deeper analysis:

- `$record` — View the full detail of specific shift records identified in the search
- `$delay-analysis` — Build a complete delay register from narratives, access records, and shift data
- `$diary` — Browse shift diary entries chronologically rather than by keyword
- `$weather-impact` — If weather-related terms were prominent in results, quantify the weather impact specifically
