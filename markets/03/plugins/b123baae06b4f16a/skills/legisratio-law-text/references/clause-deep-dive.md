# Clause / Compliance Deep-Dive — ready-to-use prompt

Source: migrated from root `prompts.md` Prompt 2. Targets the `legisratio-law-text` skill.

## Notes

- Always pass `dateInForce` = today for current text; a historical date returns the version in force that day (verified: art. 18 L.300/1970 differs between 2010 and today).
- Codes and the Constitution have NO retrievable full law text by YEAR|NUM id (e.g. `1942|262` -> "No text found"). Read them at article level via the special IDs: `codice_civile#NNNN`, `codice_penale#NNNN`, `costituzione#NN`.
- secondary-act-search `entity` is case-sensitive: `Consob` (not `CONSOB`), plus `Bankitalia`, `IVASS`, `CCNL`, `EDPB`, `ConsiglioNotarile`.

## Prompt

"Analyze this [contract clause / compliance obligation] against the governing Italian law using the LegisRatio MCP. CLAUSE/OBLIGATION: [PASTE TEXT]

1. Identify the controlling legal provision — search to find the law and the exact article(s) (give IDs in YEAR|NUM#ART form; for Constitution or codes use the special names: costituzione, codice_civile, codice_penale, codice_procedura_civile).
2. Retrieve the article text AS IN FORCE TODAY using get-article-text-by-id (pass dateInForce = today), and the full law text with get-law-text. For codes/Constitution, get-law-text returns no text (e.g. 1942|262) — get the article via `codice_civile#NNNN` instead. Quote the operative language verbatim with citation.
3. Pull the jurisprudence interpreting that article (judgment-related-to-article) — list the leading judgments with court, date, number.
4. Check for applicable secondary acts (secondary-act-search) from the relevant authorities and retrieve their full text (get-secondary-act).
Output: whether the clause/obligation is valid, what it must be amended to comply, with cited authority for each conclusion."
