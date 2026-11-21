# Render: Chat / Mermaid (asbuilt-programme Step 7)

## Step 7: Present the As-Built Programme

Use this **exact structure**. Fill every placeholder `[…]` with data. Do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** from `../../../shared/patterns/08-report-numbering.md` for the `Ref: AB-[NNN]` line.

---

```
AS-BUILT PROGRAMME — [Project Name]
Ref: AB-[NNN]
Method: [as-built reconstruction from site records (timing evidence only) / As-Planned vs As-Built comparison (SCL Protocol family, simplified — single whole-period comparison, not windowed; criticality as stored in the imported programme)]
Period: [Start Date] to [End Date]
Generated: [Today's Date]
Data Granularity: [Per-date progress records / Narrative-based reconstruction (LOW confidence — see caveats)]
```

---

### 1. SUMMARY

Write exactly 2 sentences:

> The as-built programme for [Project Name] covers [X] activities across [Start Date] to [End Date] — [X] complete, [X] ongoing at the data cut-off. [X] total dormant days were recorded across [X] dormant windows, the largest being [activity] at [X] working days [coinciding with [category] / with no recorded explanation].

---

### 2. AS-BUILT ACTIVITY TABLE

| Activity | Unit | Cum. Actual | Cum. Planned | As-Built Start | As-Built Finish / Status | Active Days | Elapsed (Working) | Dormant Days | # Dormant Windows |
|---|---|---|---|---|---|---|---|---|---|
| [activity] | [unit] | [X] | [X or "n/a"] | [date] | [date / "Ongoing at data cut-off"] | [X] | [X] | [X] | [X] |

Sort by As-Built Start (earliest first).

---

### 3. AS-BUILT TIMELINE

A compact, per-activity card view, designed to stay readable at normal chat width — not a wide week-by-week grid that wraps or scrolls off screen. (The fully rendered Mermaid Gantt chart appears at the end of this report; the Dormancy Register in section 4 below is the formal, sortable record of every dormant window — these cards are the scannable view.)

**Construction rules:**

- **One legend/scale line at the top of the section**, computed from the report's period bounds: fix the bar width at **~25 characters** and set `days per character = (period end − period start, in days) / 25`. Every activity's bar uses this same scale, so bars line up vertically across activities.
- **One card per activity**, in the same order as the activity table (as-built start ascending):
  - Bold activity name — `cum actual / cum planned unit` (add the percent in parentheses if status is Ongoing) `·` status with an icon (✅ COMPLETE or ⏳ ONGOING) and the as-built start/finish dates, or "at cut-off" if ongoing.
  - The mini-bar on its own backticked line directly below the name — built from the same scale as the legend, using `█` for active, `░` for dormant, `·` for outside the activity's own start/finish range.
  - Each dormant window (from Step 4/5) as an indented `⚠` line **directly under its activity**: the window's dates and length in working days, then the coincides-with list with each item's date and confidence letter (H/M/L), or "no recorded explanation" if none was found.
- No week-by-week grids, no per-activity date-scale headers, no stacked blocks — nothing that wraps at normal chat width.

Example:

```
Timeline scale: 01 Jan ——— 31 Jan (each ▪ ≈ 1.3 days) · █ active · ░ dormant · · outside range

**Pier Construction (Piers 3–5)** — 210.6 / 210.0 m³ · ✅ COMPLETE (05→30 Jan)
`···█████████████████████·`

**Deck Steel Fixing** — 36.4 / 40.0 t (91%) · ⏳ ONGOING at cut-off (from 05 Jan)
`···████░░░░░░░░░░░██████·`
   ⚠ Dormant 10–25 Jan (10 working days) — coincides with: standing time
     awaiting design answer (12 Jan, M) · heavy rain (15 Jan, M) · late
     possession handover (20 Jan, M)
```

---

### 4. DORMANCY REGISTER

| Activity | Window | Working Days | Coincides With | Confidence |
|---|---|---|---|---|
| [activity] | [start date] to [end date] | [X] | [category / "no recorded explanation"] | [HIGH/MEDIUM/LOW / —] |

Sort by working days descending (longest gaps first).

---

### 5. AS-PLANNED VS AS-BUILT COMPARISON

**Conditional on Step 6.** If planned dates were available:

| Activity | Planned Start | As-Built Start | Planned Finish | As-Built Finish / Status | Variance (Working Days) |
|---|---|---|---|---|---|
| [activity] | [date] | [date] | [date] | [date / Ongoing] | [+/−X] |

If planned dates were not available, replace this section with the single sentence from Step 6 explaining why it is omitted.

---

### Caveats

Always include — do not modify this text:

> **Notes:**
> - Recorded output is not the same as all work done. Mobilisation, setup, and snagging are rarely captured as measured output, so as-built starts may in reality be earlier and finishes later than the reconstructed dates suggest.
> - Accuracy is bounded by the recording interval — if progress is recorded weekly rather than daily, start/finish dates are accurate only to within that interval.
> - Intermittent recording inflates apparent dormancy — a gap in the data is not the same as a gap on site. If coverage looks poor, cross-check with `$data-quality` before relying on the dormancy figures.
> - This is a reconstruction from progress records, not a contemporaneous planner's programme. It shows actual timing only — there are no logic links and no critical path in this analysis.
> - For formal delay analysis, this supports an as-planned vs as-built method but should be reviewed by a planner before submission.
> - Per Pattern 11, this is timing evidence, not a lost-time register. Cross-reference DA-[NNN] delay registers by ref where relevant — never sum dormant days here with DA/AC/WI totals from other skills, as they use different units and scopes.
> - Ref: AB-[NNN] is a session-local sequence number for cross-referencing.

---

### RENDERED CHART

Close the report with a fully rendered Mermaid Gantt chart, built from the same as-built dates as the cards and register above.

**Construction rules:**

- One `section` per activity.
- Each continuous work period is its own task, tagged `:done` if the activity had completed by the data cut-off, or `:active` if it was still ongoing at the cut-off.
- Each dormant window (from Step 4/5) is its own task tagged `:crit` (renders red) with a **short** label: `Dormant — coincides with [cause]` or `Dormant — no recorded explanation`.
- Use the real ISO (`YYYY-MM-DD`) as-built dates from the reconstruction — never invented or rounded dates.
- Keep task labels under ~40 characters; long labels break the Mermaid layout.
- Never use `:`, `#`, or `,` inside task names — these collide with Mermaid Gantt syntax. Replace with dashes.
- If Step 2's degraded narrative-based path was used, still emit the chart, but suffix the chart's `title` with ` (LOW confidence — narrative-based)`.

Print this line immediately before the chart:

```
Rendered chart (paste into GitHub, or view on ChatGPT / VS Code markdown preview):
```

```mermaid
gantt
    title As-Built Programme — [Project] ([period]) — Ref AB-[NNN]
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    section [Activity 1 name]
    Work                      :done, a1, [as-built start], [end of work period]
    section [Activity 2 name]
    Work                      :done, b1, [start], [last day before gap]
    Dormant — coincides with [short cause] :crit, b2, [gap start], [gap end]
    Work                      :active, b3, [resume date], [cut-off or finish]
```

