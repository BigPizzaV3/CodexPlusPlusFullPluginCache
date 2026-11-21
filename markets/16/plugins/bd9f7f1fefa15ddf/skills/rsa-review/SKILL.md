---
name: rsa-review
description: Write or review Google Ads responsive search ads (headlines, descriptions, paths). Checks character limits, editorial rules that cause disapprovals, duplicates, competitor mentions and insertion syntax with a bundled script, then improves the copy using the landing page. Use when the user asks to write, rewrite, check or improve Google Ads ads or RSA headlines.
---

# RSA review

Writes and checks responsive search ads so they pass review and give Google real variety to test.

The user's explicit instructions take priority over this guidance. Reply in the user's language and write ads in the language of the market.

## Inputs

- The landing page (URL or pasted text) and the ad group's main keywords. Every claim in an ad must exist on the page. If the keywords are missing, infer the main ones from the page and the user's request, list them, and ask the user to confirm.
- Existing headlines and descriptions, if reviewing.
- Competitor names, to keep them out of the copy.

## Steps

1. If writing: read the landing page and list what can be claimed verbatim (prices, numbers, guarantees, proof, features). Do not invent claims.
2. Draft at least 8 headlines with distinct angles (keyword, benefit, proof, offer, call to action), up to 15 only if each one adds a new angle, and 4 descriptions. Fill both paths with the keyword theme.
3. Save the page text to a file and run `python scripts/ppc.py rsa --data assets.csv --landing page.txt --competitors name1 name2 --out rsa`, with assets.csv holding columns type,text[,pin]. Use `--allow-caps` for brand names or acronyms written in capitals.
4. Fix every error and warning. Rerun until `ok` is true.
5. Return the final assets as a table with their lengths, ready to paste.

## Rules

- Follow `references/ad-copy.md`: full use of the character budget, no pinning except legal text, consistent capitalization, money figures with their qualifier, no competitor names.
- Every headline must make sense in any position and next to any other headline.
- Ad Strength is a hint about variety, not a goal. Do not add weak assets to raise it.
- Never claim what the landing page does not say.

## Scripts and references

- `scripts/ppc.py rsa`: lengths (insertion counted as its default text, double-width characters as 2), repeated punctuation, emoji, distorted text, capitals, phone numbers, competitor names, duplicates and near-duplicates, counts.
- `references/ad-copy.md`.
- If code execution is not available, count characters carefully and say so.

## Running the script

- Run it with the Python that has pandas installed (`python` in ChatGPT's code environment). Write outputs to the working folder (for example `--out /mnt/data/result`) and share the files with the user.
- Put ad text and any value with `$` in single quotes, or pass a CSV with `--data`: the shell expands `"$12"`.
