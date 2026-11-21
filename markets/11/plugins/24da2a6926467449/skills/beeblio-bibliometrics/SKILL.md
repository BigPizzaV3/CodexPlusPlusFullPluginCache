---
name: beeblio-bibliometrics
description: Build a reproducible bibliometric or science-mapping study for a Beeblio project using MCP collection and analysis tools. Use for publication trends, citation and keyword patterns, co-citation, collaboration networks, or quantitative maps.
---

# Bibliometric study in Beeblio

Bibliometric maps depend on a defined corpus. Start a new run under `3-Analysis/bibliometric/<run-name>/` and record a study design: question, field-specific synonyms, databases, queries, retrieval date, years, document types, language rules, screening criteria, and planned metrics. Do not reuse a fixed topic vocabulary across fields. Preserve the raw metadata and collection script or query log so another researcher can reconstruct the corpus.

## Collect and screen

Use `search_literature` for focused discovery and `get_paper` for individual metadata. For a larger OpenAlex corpus, use `fetch_openalex_works` with queries or work IDs, year filters, page limits, and a new destination under `3-Analysis/` or `2-Data/derived/`. Choose `full` records when reference and affiliation detail matters; `labels` is a smaller representation. Record each returned page and count, and check `partial` and `failedRequests` before treating the corpus as complete. For other sources, collect through a documented provider only when access permits, respecting its terms and rate limits.

Deduplicate records by stable work identifiers. Screen titles and abstracts against the design, record inclusion and exclusion counts, and keep the selected corpus as a coding sheet. Avoid selecting solely the most cited works: older papers have had more time to accumulate citations. If limiting corpus size, use a defensible year-aware or otherwise documented strategy and report the resulting bias. Do not interpret missing affiliation, references, or keywords as zeros.

## Compute and interpret

Use saved scripts and `submit_analysis_job` to calculate publication and citation trends, sources, authors, countries, keywords, and themes when the metadata supports them. Pass collected JSON pages as `/workspace/` input paths and poll `get_analysis_job` to completion. For co-citation, bibliographic coupling, or collaboration networks, state the edge definition, counting method, thresholds, and missing-reference coverage. Distinguish diagnostic plots from findings worth discussing. Check plotted counts against the coding sheet and label each figure with its sample size and filters.

Use `beeblio-data-visualization` for chart design. Write a synthesis that explains patterns, competing interpretations, retrieval bias, database coverage, and research gaps. Avoid claiming that citation counts measure study quality or that a keyword cluster proves a theoretical relationship.

Save the study design, source manifest, coding sheet, scripts, chart data, figures, and a Markdown report in Beeblio. Use `write_text_file` for small text artifacts; write generated files from the analysis job under `/workspace/3-Analysis/`, `/workspace/4-Reports/`, or `/workspace/2-Data/derived/`. Use `upload_artifact` for files created outside Beeblio. Verify required files with `stat_file` before reporting completion.
