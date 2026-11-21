## weather-threshold-check

**Cadence:** Monthly, the 1st, 08:00 (covering the prior calendar month)
**Surface:** Desktop
**Prerequisites:** `contract-profile.md` (Contract Data weather measurements — required, not optional, here); `{{FOLDER}}/routine-state/weather-threshold-check/last-run.md`
**Priority:** Recommended starter — clause 60.1(13) is tested per calendar month, the 1st is exactly when a weather CE becomes knowable

**Instructions:**
```
Month = the full prior calendar month relative to this scheduled 1st-of-month run (explicit
month, e.g. "June 2026" — a late catch-up still covers that same month, never the month the
run happens to fire in).

Run $weather-impact for {{PROJECT}} over that month, using the Contract Data weather
measurements in the contract profile in this folder as the baseline (do not substitute a
generic Met Office average if the profile states project-specific measurements). If a 1-in-10-
year value was exceeded, say so plainly and state the clause 60.1(13) 61.3 notification clock
this starts, with the exact deadline date.
Read and update {{FOLDER}}/routine-state/weather-threshold-check/last-run.md.
End with ACTION AVAILABLE NOW if a threshold was exceeded: the specific CE notification due and
its deadline. If no threshold was exceeded, reply in three lines and stop.
```
