# Search quality notes

- Separate *discovery* from *systematic retrieval*: `search` is relevance-oriented, returns up to 20 results per call, and does not expose database-native Boolean strategy execution, exhaustive pagination, or saved search audit logs. Do not claim PRISMA-S compliance from this tool alone.
- Search in distinct directions, e.g., target population and intervention, terminology variants, alternative outcomes, and seminal/earlier work when relevant; record what was actually executed.
- Do not quietly apply arbitrary publication-year, study-design, language, citation-count, or open-access restrictions.
- `journal_quartile` is index-derived and best-effort; publication status and study type require checking. Preprints are not automatically peer reviewed.
- DOI is the first deduplication key; if missing, compare title with year and authors. A shared keyword is not proof of identical studies.
- Suggested paper-list fields: Title | Year | Design/type (verified or uncertain) | DOI/link | Why included | Basis (metadata/abstract/full text).
- Report the number of unique results *you actually reviewed*, not a claim about the entire literature. Label coverage limits and incomplete metadata.
