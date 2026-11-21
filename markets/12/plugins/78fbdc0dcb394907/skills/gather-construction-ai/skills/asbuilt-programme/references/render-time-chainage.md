# Render: Time-Chainage (asbuilt-programme Step 9)

## Step 9: Time-Chainage Output (Offered for Linear Works)

For linear work — rail, pipeline, tunnel, road, or viaduct/bridge deck runs, or any activity set with a natural chainage/distance dimension — offer the time-chainage (distance-time) chart in addition to (not instead of) the Gantt outputs above. This is the primary visual for linear rail/civils work: chainage on one axis, time on the other, each activity a sloped band tracking progress along the alignment over time.

**When to offer it:**

- Offer it when the project or activity names suggest linear/chainage-based work (e.g. "track renewal", "pipeline", "viaduct", "tunnel drive", chainage-looking task names), or when the user asks for it directly.
- Do not generate it unasked for projects with no linear/chainage character — offering an irrelevant chart every run is noise.

**Step 9a: Establish chainage per activity — in this order, never guessed:**

1. **Imported programme baseline** (Pattern 15) — if `programme/programme-baseline.md`/`.json` exists, its project matches, and the import captured a chainage field as an optional per-task attribute, use it. Cite as "per the imported programme ([revision], exported [date])" — this is a STORED value.
2. **A task-name/WBS pattern the user confirms** — if activity names or WBS codes embed a chainage-like pattern (e.g. "Ch 1200–1400", "1200-1400m", a WBS segment coding a distance range), propose the parsed reading and get explicit user confirmation before applying it to any activity. Never assume the pattern is consistent across all activities — confirm per activity or per stated naming convention.
3. **A user-pasted chainage map** — ask the user to paste a simple activity → chainage-range mapping (e.g. a table or list) and use it as given.
4. If none of (a)-(c) resolves an activity's chainage, **do not guess** a range from the activity's description, sequence, or any other inference. List it under the chart in an "Activities Without Mapped Chainage" section instead — it is never dropped from the response silently.

State which of the three sources was used for each mapped activity in the output; never blend a guessed value into a chart cell.

**Step 9b: Planned vs as-built bands — same gating as Sections 5/6:**

- A **planned band** is drawn only where a mapped baseline start/finish date exists per Step 6/Pattern 15 (i.e. the same conditions that gate Section 5 of the chat report). If no baseline is mapped for an activity, its chart row shows the as-built band only, with "no baseline mapped" noted in the activity table row — never fabricate a planned date to complete the pair.
- The **as-built band** comes from the Step 4 reconstruction (start/finish, work/dormant segments) exactly as used in the Gantt outputs — the same segments, the same dormancy findings, the same "coincides with" (never "caused by") language.
- **Possessions**: if `dashboardAccessPossession` data covers the period, render matching windows as possession bands; if none exist for the period, state that plainly ("no possessions recorded for this period") rather than omitting the section.

**Procedure:**

1. Confirm chainage per Step 9a for every activity in scope; build the "Activities Without Mapped Chainage" list for the remainder.
2. Read the template at `references/time-chainage-template.html` (inside this skill's folder, alongside `gantt-template.html`).
3. Build the run's data as a single JSON object matching this schema:

```json
{
  "project": str, "ref": "TC-001", "periodStart": "YYYY-MM-DD", "periodEnd": "YYYY-MM-DD",
  "generated": "YYYY-MM-DD", "dataCutoff": "YYYY-MM-DD", "chainageUnit": "m" | "km",
  "summary": str, "confidenceNote": str | null, "caveats": [str],
  "possessions": [{ "label": str, "start": "YYYY-MM-DD", "end": "YYYY-MM-DD", "note": str | null }],
  "activities": [{ "name": str, "unit": str, "chainageFrom": num, "chainageTo": num,
    "chainageSource": "imported programme baseline (Pattern 15)" | "task-name/WBS pattern (user-confirmed)" | "user-supplied chainage map",
    "planned": { "start": "YYYY-MM-DD", "finish": "YYYY-MM-DD" } | null,
    "asBuilt": { "status": "complete" | "ongoing", "start": "YYYY-MM-DD", "finish": "YYYY-MM-DD" | null,
      "segments": [ {"type": "work", "start": "...", "end": "..."},
        {"type": "dormant", "start": "...", "end": "...", "workingDays": num, "flag": int,
         "coincidesWith": [{"date": "...", "evidence": str, "confidence": "H"|"M"|"L"}]} ] } | null }],
  "unmapped": [{ "name": str, "reason": str }]
}
```

4. Replace everything between the markers `/*__TIMECHAINAGE_DATA__*/` and `/*__END_TIMECHAINAGE_DATA__*/` in the template with the JSON object built above — keep both markers in place, immediately surrounding the data.
5. Write the result to `time-chainage-[project-slug]-[YYYYMMDD].html` in the working directory using the Write tool.
6. Present it the same way as Step 8's Gantt file: preview or send the file directly in ChatGPT Work; give the file path in the CLI and say it opens in any browser and prints to A4 landscape.

**What the file contains** (state this to the user): a chainage(x)-vs-time(y) chart with dashed PLANNED bands and solid/hatched AS-BUILT bands clearly legended, possession time-bands, numbered dormancy flags with hover tooltips, an activities table (with chainage source per row), a possessions table, an "Activities Without Mapped Chainage" table, a dormancy findings table, the caveats block, and a permanent "INDICATIVE-free zone" banner stating the chart renders STORED and RECORDED values only — no INDICATIVE recalculation is performed or plotted.

**Fallback:** if `references/time-chainage-template.html` cannot be read, say so plainly and offer the Mermaid/HTML Gantt outputs from Steps 7-8 instead — do not hand-draw an SVG time-chainage chart as a substitute.
