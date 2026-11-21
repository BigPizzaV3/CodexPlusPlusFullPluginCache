---
name: jexpress-single-cell-rnaseq
description: Plan single-cell RNA-seq quality control, normalization, features, PCA, neighborhoods, clusters, markers and annotation in J-Express; use for PBMC and donor-aware inference.
---

# jexpress-single-cell-rnaseq

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
Use goal `single-cell`. The returned plan deliberately contains blocked UI-only/missing prerequisites; partial exploration is not a completed single-cell pipeline.

1. Confirm genes/cells orientation, raw UMI counts, organism/gene IDs, feature subset, donor/sample IDs, condition and batch. Confirm that cells are nested within biological samples; cell count is not donor replication.
2. Use `import_demo_dataset({demo:"pbmc3k",confirm:true})` if an authorized appended demo is needed; retain existing project data. Inspect per-cell library sizes and detected features on raw counts, following pages. Review mitochondrial gene annotation, doublets, ambient RNA and batch distribution. MCP QC does not calculate mitochondrial percentages; doublet detection and ambient correction are missing. Do not invent these metrics or automatically apply universal cutoffs.
3. Call `preview_dataset_filter` with `method:"cell-qc"`, `minimumGenes`, `minimumCounts` and optional `maximumCounts`; review retention, then use source unlock and confirmed `filter_dataset` to create a child. This shares the raw-count selection recipe with the UI. Retain parent lineage. Thresholds must reflect the assay and gene panel. The PBMC 3k demo is reduced to 800 genes × 2,700 cells; its totals and detected genes do not represent the full transcriptome. A 200-gene rule for a full assay is not transferable unchanged.
4. On reviewed raw counts with genes in rows, call `run_scientific_analysis({datasetId,operation:"variable-features",nTopGenes:400,nBins:20,targetSum:10000})`; choose the requested feature count for the actual panel rather than copying 400 universally. Poll the job, require its saved analysis ID and inspect paginated scores/selected flags. This is single-batch Seurat mean.var.plot dispersion selection, not Seurat v3 or batch-aware HVG. Threshold ties may retain more than requested; default 2000 can retain all eligible genes in the reduced demo. After source unlock and confirmation, call `create_variable_feature_dataset({datasetId,analysisId,confirm:true})`, then lock the source. Resolve the child ID and re-inspect. Its log2 normalization uses full supplied-panel cell totals BEFORE gene selection; it preserves all cells and original raw counts. Run sample PCA on that transformed child. Batch integration and donor inference remain missing; do not claim a complete inferential single-cell pipeline.
5. Run a current sample PCA on the transformed HVG child with reviewed PC count. Call `run_scientific_analysis({datasetId,operation:"neighbor-graph",sourceAnalysisId:"<saved PCA ID>",k:15,pcaComponents:8})`; choose k below cell count and available PCs (at least 2). Resolve its completed graph analysis ID, then call `run_scientific_analysis({datasetId,operation:"leiden",sourceAnalysisId:"<saved graph ID>",resolution:1,seed:42,iterations:10,starts:3})`. Read paginated per-cell assignments. This exact binary union-kNN graph is not Scanpy's standard UMAP fuzzy graph. Evaluate PC/k/seed/resolution sensitivity; labels are arbitrary and clusters are not cell types. Optionally call confirmed `create_group_from_leiden` for a specific saved cluster; the exact cell IDs/axis are used, with no matrix mutation or unlock.
6. UI `SingleCellClusters` optionally runs PCA then K-means and ranks genes by mean transformed-expression difference; it is exploratory and **not statistical marker discovery**. `run_analysis` K-means on a dataset does not automatically consume previous PCA scores. Positive centered values are not gene detection.
7. `run_scientific_analysis({operation:"umap",datasetId:...})` runs UMAP on reviewed transformed expression, with explicit PCA preprocessing parameters and saved coordinates. Poll its job, then page results. Original-embedding `projection-quality` uses cosine geometry and is restricted to original embedding datasets, not gene expression. Assess neighborhood fidelity/hyperparameter sensitivity with appropriate expression-space methods; do not claim that the embedding-specific diagnostic validates a single-cell result. Clusters and 2D boundaries do not establish cell types. Annotate only with credible multiple markers, known biology, contradictory markers and uncertainty; annotation is human/AI interpretation, not an implemented classifier.
8. For condition DE, request donor-level pseudobulk or a validated hierarchical model respecting sample/donor independence. That path is missing. One donor cannot support between-condition biological inference, regardless of number of cells. Do not substitute cell-level independent tests or exploratory marker rankings.

## Validation and evidence
Check raw-count validity and scale, subset-aware totals, filtered IDs, preserved lineage and outputs after each manually executed step. Compare normalization against exact values, evaluate clustering/marker stability and report limitations. Automated tests use the bundled PBMC counts when present and verify blocked graph/marker/donor inference paths; HVG statistics and exact selected genes agree with Scanpy 1.11.5 on the reduced PBMC 800-gene × 2,700-cell panel; normalized-child values agree at 1e-12. Do not generalize that fixture to full-transcriptome or batch-aware validity. The actual PBMC graph/Leiden pipeline has exact neighbor/edge agreement and independently checked modularity; partition ARI versus Python leidenalg is 0.8624 on that graph. This does not validate full-transcriptome or donor inference. Full donor-aware inference and automatic cell typing have not run.

## References
- Luecken & Theis (2019), Current best practices in single-cell RNA-seq analysis, https://doi.org/10.15252/msb.20188746
- Heumos et al. (2023), Best practices for single-cell analysis across modalities, https://doi.org/10.1038/s41576-023-00586-w
- Squair et al. (2021), Confronting false discoveries in single-cell differential expression, https://doi.org/10.1038/s41467-021-25960-2


Call `list_scientific_capabilities` for the current supported versus blocked methods.
