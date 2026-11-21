# Output Template: Programme Import Report (programme-import Step 7)

## Step 7: Report

```
PROGRAMME IMPORT
Ref: PI-[NNN]
Source: [filename] | Format: [MSPDI/P6 XER] | Data date: [date] | Revision: [stated]
Accepted Programme: [yes, as at DATE / no / not confirmed]
Self-check: [match_pct]% — [verdict]

1. PARSE SUMMARY (verbatim from the parser)
   Tasks: [n] | Milestones: [n] | Links: [n] | Baseline present: [yes/no] | Encoding: [enc]
   Warnings:
   - [each parser warning, verbatim — NO BASELINE / calendar / constraint / manual-schedule etc.]

2. ACTIVITY MAPPING
   | Gather activity | Programme task | Match basis |
   Unmapped (Gather): [...] | Unmapped (programme): [...]

3. REVISION HISTORY
   [current] programme-baseline.json — [revision], [data date]
   [prior]   programme-baseline-<revision>.json — [revision], [data date]
   Diff any two with $programme-compare.

4. WHAT THIS UNLOCKS
   - $asbuilt-programme — planned-vs-actual comparison against this baseline
   - $delay-analysis — critical-path flags on delay register entries
   - $ce-quotation — the two-programme method for a compensation event quotation
   - $programme — milestone comparison against the imported baseline
   - $programme-compare — diff this revision against a prior one

5. CAVEAT
   Float and criticality above are STORED — read from the export at its data date, never
   recomputed here. The [match_pct]% self-check is a trust calibrator for the engine
   (scripts/cpm.py), not a schedule; any later INDICATIVE recalculation carries its own banner
   and is never presented as, or blended with, the Accepted Programme.

Ref: PI-[NNN] is a session-local sequence number for cross-referencing (Pattern 8).
```
