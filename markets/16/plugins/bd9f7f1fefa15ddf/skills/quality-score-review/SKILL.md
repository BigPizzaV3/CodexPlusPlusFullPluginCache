---
name: quality-score-review
description: Analyze Google Ads Quality Score from a keyword export, weighted by spend, and find which component (expected CTR, ad relevance, landing page experience) costs the most and where to fix it. Use when the user asks about low Quality Score, high CPCs from poor quality, or how to improve Quality Score.
---

# Quality Score review

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

Keywords report, last 30 to 90 days: Keyword, Campaign, Ad group, Quality Score, Exp. CTR, Ad relevance, Landing page exp., Impr., Clicks, Cost, Conversions. Exclude brand campaigns unless the question is about brand.

## Steps

1. Run `python scripts/ppc.py qs --data <file> [--low 5] --out qs`.
2. Report the spend-weighted Quality Score and the component most often below average, weighted by cost.
3. Map the component to the fix:
   - Expected CTR below average: ads do not match the query, or match types pull queries the ads do not answer. Check search terms and write ads for the main queries.
   - Ad relevance below average: the ad group mixes themes. Split it, or align ad text with the keywords.
   - Landing page experience below average: the page does not answer the query, loads slowly or is hard to use on mobile. It is judged per keyword, so a good page can still score low for keywords it does not cover.
4. List the low-score keywords with the most spend, with their conversions. A low score with a good CPA is not a priority.

## Rules

- Quality Score is a diagnostic. Decide on cost and conversions, not on the score.
- Do not promise a CPC reduction from a score change; give the direction, not a number.

## Scripts and references

- `scripts/ppc.py qs`; `references/ad-copy.md`, `references/search-terms-negatives.md`.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
