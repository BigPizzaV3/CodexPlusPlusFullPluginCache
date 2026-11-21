---
name: jexpress-normalization
description: Choose and apply data-type-aware J-Express normalization, transformation or scaling when asked to preprocess matrices, RNA counts, microarrays or embeddings.
---

# jexpress-normalization

**Status: preview.** This procedure is still being validated against the J-Express tools and has not been scientifically validated.

## Shared tool procedure
1. Call `list_datasets`; select an explicit dataset ID, never assume the active dataset.
2. Call `list_scientific_capabilities` and `read_dataset_details`. Check the registry version, actual method status and connected tool schemas. A code-audited MCP path is not evidence of successful execution.
3. Call `inspect_dataset_quality` with `offset:0, limit:20`; follow `samples.nextOffset` for sample/cell summaries. A scan over 5 million values is explicitly incomplete. Metadata presence does not prove valid experimental design.
4. Call `propose_analysis_workflow` with the goal below. Supply optional `objective` as scientific context; the assistant chooses the controlled goal. This is a read-only proposal, not an LLM or an executor.
5. Explain prerequisites, blockers, parameter choices and human review gates. Never execute a blocked step or silently reinterpret a UI-only operation as an MCP method.
6. After user-authorized analysis, call `run_analysis` separately, poll `get_analysis_job`, require `status:completed` and an `analysisId`, then use `get_analysis_summary` and bounded `query_analysis_result` pages (`limit` ≤100). Record failed jobs as failed. Prefer saved results over `query_pca`, which recomputes on current values.
7. For a derived dataset, resolve its actual returned ID, inspect its new scale and QC, and re-plan. Dependencies do not pipe PCA scores or transformed values automatically into another tool. Report source ID, derived/analysis IDs, versions, parameters, validation, rationale and limits.

Do not use proposal text as an unlock or execution command. Matrix writes remain locked by default. `normalize_dataset` creates a child and requires a separately explicit `unlock_dataset`, `confirm:true`, then `lock_dataset` after the operation. Preserve source values and check the child's recipe. Existing authorization still applies; do not unlock without user authorization.

## Decision procedure
Use goal `normalization`. Distinguish technical normalization, distribution transformation, variable scaling and batch correction; none is interchangeable.

| Input | Defensible route | Executable boundary |
|---|---|---|
| Raw RNA counts, genes in rows | Inspect count validity/library totals; exploratory `rna-logcpm` | `normalize_dataset`, after explicit unlock and confirmation; creates child |
| Normalized counts/CPM/TPM | Establish upstream method and intended model; decide transformation explicitly | No automatic RNA renormalization; raw-count model still requires original counts |
| Log expression or VST/rlog | Avoid double logging; inspect units and variance | No automatic RNA transform offered |
| Microarray | Establish platform and upstream background/normalization; quantile only if comparable distributions are justified | `quantile` available for explicitly classified microarray, complete matrix only; not full RMA |
| General continuous data | Decide centering vs z-scoring from units/noise and analysis target | `row-center`, `column-center`, `row-zscore`, `column-zscore` |
| Positive linear data | Justify logarithm and offset from measurement process | `log2` requires declared linear scale; every finite value + offset must be >0 |
| Original embeddings | Preserve model geometry; assess cosine/Euclidean and any L2 normalization | Generic expression transforms rejected by MCP; no L2 normalization MCP tool |
| Batch effects | Establish biological design/confounding first | Validated batch correction missing; no substitute implemented |

Rows and columns are physical axes in transform names; confirm roles before choosing. `rna-logcpm` requires raw nonnegative integer counts, complete values, positive sample libraries, linear/undeclared count scale and genes in rows. It computes `log2(1 + 1e6 * count / sampleTotal)`. This is exploratory library-size normalization, not TMM, DESeq2 size factors, VST or dispersion modeling. Filtered gene subsets change totals; retain raw parent and record the exact matrix used.

For quantile normalization, review whether equalizing distributions could erase real biology; complete values are required and ties use average ranks. Centering/z-scoring retain nulls, use available values, and map constant profiles to zero for z-scores. Do not hide missingness or confuse standardized deviations with detection.

## Controlled execution
After explicit user authorization: `unlock_dataset`, `normalize_dataset({datasetId,method,confirm:true})`, then `lock_dataset`. Record returned child ID and recipe, inspect finite results and scale, and re-plan on that child. Never send an entire matrix through ChatGPT to reproduce a transform. The source is preserved; the child is locked by default. For raw-count filtering, first call `preview_dataset_filter`; only then execute `filter_dataset` with reviewed thresholds, source unlock and confirmation. Cell filtering shares its recipe with the UI; feature/cell IDs and parent lineage are preserved.

## Validation and evidence
Compare library totals, zeros, missingness and selected exact transformed values; check parent IDs, methodVersion, parameters and source immutability. Tests cover formulas, lock enforcement, malformed requests, transposed genes and inappropriate modalities.

## References
- Bolstad et al. (2003), A comparison of normalization methods for high density oligonucleotide array data, https://doi.org/10.1093/bioinformatics/19.2.185
- Robinson & Oshlack (2010), A scaling normalization method for differential expression analysis of RNA-seq data, https://doi.org/10.1186/gb-2010-11-3-r25
- Love et al. (2014), DESeq2, https://doi.org/10.1186/s13059-014-0550-8


Call `list_scientific_capabilities` for the current supported versus blocked methods.
