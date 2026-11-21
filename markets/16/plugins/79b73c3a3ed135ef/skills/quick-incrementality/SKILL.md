---
name: quick-incrementality
description: Get a directional, low-effort read on incrementality without a formal experiment. Compares a period before and after a change (pause, budget cut, new campaign) against several baselines and their normal noise, or analyzes an on/off switchback in a single market. Use when a team paused or changed ads and wants to know if it mattered, cannot split by region, or wants a quick check before investing in a proper test.
---

# Quick incrementality

Directional methods for teams that cannot run a geo experiment or need a fast read. The output is always labeled directional and states what it cannot rule out.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Choose

| Situation | Method |
|---|---|
| A change already happened, one date | `prepost` |
| The team can alternate on and off for 4+ blocks | `switchback` (plan it, then analyze it) |
| No data yet, need to know if a test is feasible | `quick` sizing |
| Brand search pause | See the brand section in `references/directional-methods.md`, prefer switchback |

## Steps for prepost

1. Ask for a daily CSV of the business KPI (not platform conversions), at least 8 weeks before the change, ideally over a year. Ask for spend, and for a control series if one exists: another country, organic-only, a product without ads.
2. Run `python scripts/geolift.py prepost --data <file> --start <change date> [--end <date>] [--control-col <col>] [--exclude-windows a:b] --out prepost`.
3. Report each comparator: change, its normal range, and how often past windows moved more. Then the verdict.
4. If the verdict is "directional signal", give the size as a range across comparators, never as one number.
5. Say what else changed in the window, if the user knows, and how it could explain the result.
6. Recommend the test that would confirm it (`references/method-ladder.md`), with a rough sizing via `quick` if useful.

## Steps for switchback

1. Plan: block length 1 to 2 weeks, at least 6 blocks, washout 2 to 3 days, schedule fixed before starting. Use only for channels without long carryover.
2. Analyze: `python scripts/geolift.py switchback --data <file> --off-periods a:b c:d ... --start <first block> --end <last block> --out switchback`.
3. Report the effect when off, the permutation p and the minimum attainable p.

## Rules

- Label every result "directional". Never call it causal.
- Never give one number without the noise band next to it.
- If the change is inside the normal band, say the data cannot tell it apart from a normal period. Do not say the channel has no effect.
- Do not mix platform-attributed conversions with the business KPI.

## Scripts and references

- `scripts/geolift.py`, documented in `references/script-reference.md`.
- `references/directional-methods.md` for the comparators and their failure modes.
- If code execution is not available, give the user the exact command to run locally.
