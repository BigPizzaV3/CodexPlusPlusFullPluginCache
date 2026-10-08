# Litigation / Caselaw Package — ready-to-use prompt

Source: migrated from root `prompts.md` Prompt 3. Targets the `legisratio-caselaw` skill.

## Notes

- get-judgment-text already returns the official shareable PDF link inline — get-judgment-url is only needed when you didn't fetch the text.

## Prompt

"Build a case-law package for an Italian legal filing on this dispute theme. THEME: [DESCRIBE DISPUTE / LEGAL POINT]

1. Judgment search — run judgment-search across the relevant courts (e.g. CASSAZIONE_CIVILE, CASSAZIONE_UNITE, TAR_LAZIO, CORTE_GIUSTIZIA_UE) with a start date if useful; k high. Educated this on the strengths: find the leading and most recent on-point rulings.
2. For the top 10-20 judgments: retrieve full text (get-judgment-text) — it returns the official shareable PDF URL inline, so only call get-judgment-url when you skipped the text — and give the OFFICIAL PDF link for each.
3. Map the jurisprudence to specific statutory articles — for each article that anchors the dispute, run judgment-related-to-article to catch rulings the keyword search missed.
Output: a citation-ready table — ruling, court, date, number, official PDF URL, and the article(s) it interprets — deduplicated and organized by legal point."
