# Mode 1 — Portfolio Review: output format and template

## Output Format Contract
- **Primary format:** Markdown with numbered sections and tables exactly as defined below.
- **Data placeholders:** replace with values, `Not available`, or `User input required`.
- **Metric formatting:** dates `YYYY-MM-DD`; percentages `X%`; durations `X days`/`X hours`;
  currency (user-supplied only) `£X,XXX.XX`.
- **Status tokens:** only defined labels (Green/Amber/Red, High/Medium/Low).
- **Machine-readable appendix (optional):** a final fenced `json` block named `report_meta`
  with `ref`, `project`, `period`, `confidence`, `missing_inputs`.

## Template
```
PORTFOLIO COMMERCIAL REVIEW
Ref: CD-[NNN]
Period: [Start Date] to [End Date]
Projects Analysed: [X]
```

1. **EXECUTIVE SUMMARY** (2–5 sentences: period, portfolio size, RAG split, top risk, systemic vs isolated)
2. **PROJECT RAG STATUS** — table: # | Project | Programme | Resources | Productivity | Overall | Key Issue. Sort Red→Amber→Green. RAG: 🟢 within ±10% of plan · 🟡 10–20% off or declining · 🔴 >20% off or multiple Amber indicators.
3. **PERFORMANCE RANKING** — best performer / requires attention / most improved, each with a supporting metric.
4. **COMMERCIAL PERFORMANCE (user-supplied only)** — Gather exposes no financial data. Ask at Step 1 whether the user wants to paste contract value/forecast final account/CVR/margin/certification per project. If supplied: table labelled "Source: user-supplied figures, not Gather data." If not: one line — "Commercial performance metrics are not available from Gather and were not supplied; this review covers operational performance only." Never a table of empty cells.
5. **RESOURCE OVERVIEW** — table: # | Project | Avg Headcount | Trend | Assessment, plus one summary sentence.
6. **PROGRAMME OVERVIEW** — table: # | Project | Health | Activities Behind | Worst Activity | Days Behind, plus one summary sentence.
7. **RECOMMENDED ACTIONS** — one per Red/Amber project: issue + data, then intervention. If all Green: "No interventions required — continue monitoring at the next reporting cycle."
8. **PORTFOLIO TRENDS** (2–5 sentences: direction, key metric movement, systemic vs isolated; state any time-bar/compliance risk explicitly).
9. **CONFIDENCE & DATA QUALITY** — table: Data Completeness (%) | Evidence Quality (High/Medium/Low) | Key Missing Inputs | Decision-Use Guidance. Bands: ≥85% High, 60–84% Medium, <60% Low.

**Caveats (verbatim, always included):**
> - This review is based on data recorded in Gather. Projects with incomplete data recording may appear better or worse than actual performance.
> - RAG ratings are data-driven but indicative — validate with project teams before acting.
> - Financial performance is not included — the Gather MCP does not expose contract sums or cost data.
> - Ref: CD-[NNN] is a session-local sequence number for cross-referencing.
