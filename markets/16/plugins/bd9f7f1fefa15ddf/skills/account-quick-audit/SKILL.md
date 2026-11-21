---
name: account-quick-audit
description: Run a quick, prioritized audit of a Google Ads account from screenshots and report exports the user shares. Checks measurement, bidding, structure, queries, ads and spend efficiency in order of money at stake, and returns the top findings with evidence and one action each. Use when the user asks to audit, review or health-check a Google Ads account.
---

# Account quick audit

A senior's first look at an account: what is costing money now, in order, with evidence.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Steps

1. Ask what the account sells, the main conversion, the target CPA or ROAS, and monthly spend. One message.
2. Ask for the minimum evidence, in this order (accept what the user can share):
   - Campaign report, last 90 days, by campaign: type, bid strategy, budget, Impr., Clicks, Cost, Conversions, Conv. value, Search impr. share, lost IS (rank) and (budget).
   - Conversion actions page: which are primary, counting, values.
   - Search terms report, last 30 days.
   - Settings of the top 3 campaigns by spend (locations and location options, networks, brand exclusions for PMax).
   - Recommendations, auto-apply settings.
3. Go through `references/audit-checklist.md` in order. Use `scripts/ppc.py inspect` on exports, and `ngrams` on the search terms report.
4. Rank findings by money at stake. Quantify each one from the data shared.

## Output

- **Top 3 findings**: what, the number, the action. Most money first.
- **Checklist**: pass, fail or unknown for each item in `references/audit-checklist.md`, with the evidence or what is needed.
- **What not to change yet**: items that look odd but should wait (learning periods, thin data).

## Rules

- No finding without evidence from what the user shared. Mark the rest "unknown" and say what would answer it.
- Do not pad the audit with generic best practices that do not apply to this account.
- Measurement problems come first: a broken goal makes every other finding unreliable.
- Platform facts only from `references/platform-facts.md`.
- Do not change anything in the account. The user decides and applies.

## Scripts and references

- `scripts/ppc.py` for exports; `references/` for the rules.
- If code execution is not available, give the user the commands to run locally.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
