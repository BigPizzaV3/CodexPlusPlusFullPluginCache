# Research Brief — ready-to-use prompt

Source: migrated from root `prompts.md` Prompt 1. Targets the `legisratio-research` skill.

## Query style (applies to all searches)

- Use 2-4 concrete fact terms (the object, sector, or transaction), never a generic legal phrase or a full sentence. "non concorrenza lavoratore" nails art. 2125 c.c.; "adempimento obbligazioni" returns off-topic laws. Re-search with the fact-words if the first pass drifts.

## Prompt

"Using the LegisRatio MCP, research the following question as you would for a first-pass memo for an Italian law firm. QUESTION: [PASTE FACT PATTERN / LEGAL QUESTION]

Produce a structured research brief:
1. Relevant legislation — run a broad hybrid search (k≈80, EU + National, add regional levels only if the question is region-specific). For each law give its ID (YEAR|NUM) and the specific article numbers that matter.
2. Relevant case law — run a judgment search; for the most on-point judgments give court, date, number and their SENTENZA-... IDs.
3. Relevant secondary regulation — run a secondary-act search across the applicable authorities (Consob, Bankitalia, IVASS, CCNL, EDPB, Consiglio Notarile) and list the issuing entity + act ID. NOTE: entity values are case-sensitive (e.g. `Consob`, not `CONSOB`).
Group by legal issue, cite stable IDs for every source, and flag what is missing so the brief can be completed."
