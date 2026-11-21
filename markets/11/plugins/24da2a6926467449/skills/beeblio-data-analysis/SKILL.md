---
name: beeblio-data-analysis
description: Analyze or clean data in a connected Beeblio project with its MCP analysis jobs. Use for tabular cleaning, statistics, reproducible calculations, and research findings based on project files.
---

# Analyze Beeblio project data

Use Beeblio MCP to identify the project and input files, then run project analysis with `submit_analysis_job`. The job runs Python or shell commands in a disposable Beeblio compute workspace. It does not access unsaved editor content. Analysis uses account credits.

## Prepare project inputs

1. Resolve the project with `list_projects`; inspect candidate inputs with `list_files` and `stat_file`. Paths sent to MCP tools are project-relative.
2. Inspect the relevant source text with `read_text_file` or use a bounded format reader such as `read_office` or `read_matrix`. Record source paths and metadata. Avoid copying large datasets into the conversation.
3. Pass required project files in `inputPaths` as absolute `/workspace/` paths, for example `/workspace/2-Data/source.csv`. The compute job mounts those saved inputs. If a source is unavailable, explain the limit rather than claiming to have analyzed it.

## Compute and verify

- Keep raw input unchanged. Save substantial code under `3-Analysis/`, then run it with `submit_analysis_job` using a unique `idempotencyKey`, a suitable `timeoutSeconds` (at most 300), and explicit `inputPaths`. Poll `get_analysis_job` until it succeeds or fails; call `cancel_analysis_job` if the user asks to stop. Check the returned exit code, logs, and output paths. Verify libraries in the compute image before relying on them.
- For cleaning, inspect schema, units, missing-value markers, duplicates, ranges, and outliers before transforming. Choose and explain missing-data and outlier treatments. Write cleaned data to a new file, never over the raw source. Report input and output row counts and the material changes.
- For statistics, state the research question, unit of analysis, sample size, missing-data treatment, model or test, assumptions checked, effect size, and uncertainty. Validate key counts and at least one important result independently. Treat observational associations as associations unless the study design supports causal language. A nonsignificant result is not proof of no relationship.
- Do not paste a full source dataset into the conversation or generated code. Present a compact result table or narrative with the actual computed values and limitations.

## Save and report outputs

- Write job outputs to new paths under `/workspace/2-Data/derived/`, `/workspace/3-Analysis/`, or `/workspace/4-Reports/`. Confirm uploaded outputs with `stat_file` or `read_text_file`. Use `write_text_file` with `ifNotExists` for small scripts and reports; it does not write raw `2-Data/` files.
- Use `upload_artifact` when an external sandbox produced a file or when a user supplies one. Its 25 MB limit and create-only behavior still apply.
- Report actual input paths, code path, output paths, status, methods, and limitations. A queued job or saved script alone is not a completed analysis.
