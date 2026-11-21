---
name: search-terms-cleanup
description: Find wasted spend in a Google Ads search terms report and propose negative keywords safely. Runs an n-gram analysis of cost and conversions, flags candidates that would block converting traffic, and classifies terms by intent before suggesting the level (ad group, campaign, list). Use when the user shares a search terms report or asks which negatives to add.
---

# Search terms cleanup

Finds the patterns that waste money in search terms, and turns them into negatives that do not cut converting traffic.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

- Search terms report export: Search term, Match type, Campaign, Ad group, Impr., Clicks, Cost, Conversions (and Conv. value if relevant). Last 30 to 90 days. Include Performance Max search terms if available.
- Target CPA, or let the script use the account CPA of the file.
- What the business sells and to whom, in one line. Needed to judge intent.

## Steps

1. Run `python scripts/ppc.py inspect --data <file>`.
2. Run `python scripts/ppc.py ngrams --data <file> [--target-cpa X] --out ngrams`. Brand campaigns are excluded by default.
3. Classify every candidate before proposing it, with `references/search-terms-negatives.md`:
   - Wrong intent: negative.
   - Wrong product or audience: negative only in the campaigns of the wrong side.
   - Competitor, geo modifier, brand navigational: routing decision, not a negative. Say where the traffic should go.
   - Mixed intent (free, cheap, jobs in some verticals): segment first; do not negate blindly.
4. Drop or narrow any candidate with `conflicts_with_converting = true`. Propose an exact negative or a longer phrase instead.
5. Measure the proposal before giving it: rerun with `--negatives "term one" "term two" ...`. Report the share of zero-conversion spend it covers and any converting terms it would block (`negatives_coverage`). Remove or narrow negatives that block converting terms.
6. For each proposed negative give: text, match type, level, the spend it would have saved in the period, and why. Use `intent_hint` as a starting point for the classification, not as the answer.
7. Point out high-CPA n-grams that still convert. They are bid or structure questions, not negatives.

## Output

- First line: share of spend on zero-conversion terms, and how much of it the proposed negatives cover.
- Table of proposed negatives: n-gram, match type, level, cost in period, reason.
- Table of routing decisions (competitors, geos, brand) with the suggested destination.
- Terms to protect.
- Next step: when to review again (weekly for large accounts with broad match, monthly otherwise).

## Rules

- A zero-conversion n-gram with less cost than one target CPA is not evidence. Do not propose it.
- Never propose a phrase or broad negative that a converting term contains.
- Check the level: a negative that is wrong in one product can be right in another.
- Do not add negatives for misspellings: Google's negatives already block misspellings (see `references/platform-facts.md`). Add plurals and synonyms where needed.
- Do not apply anything. The user reviews and applies.

## Scripts and references

- `scripts/ppc.py`. Exports in English and Spanish; other languages via `--map`.
- If code execution is not available, give the user the command to run locally.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
