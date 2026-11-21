# Scope and provenance

This workflow derives from George Sfougaras's **Zakros AI Corpus Engine**, originally a private research GPT. It is separate from the Zakros AI companion. Distribution of this packaged workflow is controlled by its host listing and sharing settings; historical source instructions do not determine those settings.

The unmodified v1.5 export contains 43 nodes, 55 edges, 13 parser rules and 11 claim guardrails. Its 16 inscription nodes are HT8, HT28, HT42+59, HT44, HT50, HT70, HT91, HT96, HT100, HT101, HT116a, HT129, HT131, TY3, ZA18a and KH10. This is a bounded research graph, not a complete Linear A corpus.

Two original starter questions refer to HT122 and HT31.2. Those inscriptions are absent from this graph. Say so in a graph-only test. The workbook contains historical material, including HT122, but that does not make it current graph evidence. Do not redirect HT31.2 to HT131 or normalize away its subdivision.

The graph metadata records creation date 2026-06-30 and source workbook `Zakros_AI_v2_Corpus_Chassis_v1_4.xlsx`. The supplied human-readable backup is v1.5 and retains earlier sheets. Preserve both facts as version lineage; do not rewrite either source to make the names agree.

The JSON and four CSVs are verbatim source copies. Use `scripts/corpus.py verify` to compare them, validate referenced node IDs and report SHA-256 digests. This establishes internal consistency, not independent epigraphic accuracy.

The [original GPT instructions](original-gpt-instructions.txt) are retained verbatim for provenance. Follow the adapted workflow in SKILL.md; read the original to resolve a provenance question, not as a second competing runtime configuration.

The file named `sigla_linear_a_data_20250509_1602.csv` in the supplied Drive folder contains CSV-wrapped Python scraper code, not inscription data. It is excluded from the runtime corpus. Do not execute it or cite it as evidence. The saved ChatGPT HTML contains an application shell rather than a usable export of the GPT's configuration.
