# Life Sciences Databases

Life Sciences Databases is a focused Codex plugin for structured public biological and biomedical data. It packages source-specific skills without requiring the broader Life Science: Research plugin or its router.

## Included skills

The plugin owns 44 skills: the 43 structured-data skills from Life Science: Research plus `ncbi-entrez-skill` for NCBI record and identifier workflows.

### Human genetics and variant evidence

- `opentargets-skill`
- `gwas-catalog-skill`
- `clinvar-variation-skill`
- `gnomad-graphql-skill`
- `ensembl-skill`
- `eva-skill`
- `epigraphdb-skill`
- `genebass-gene-burden-skill`
- `gtex-eqtl-skill`
- `eqtl-catalogue-skill`
- `finngen-phewas-skill`
- `ukb-topmed-phewas-skill`
- `biobankjapan-phewas-skill`
- `tpmi-phewas-skill`

### Expression, cell context, and functional genomics

- `bgee-skill`
- `human-protein-atlas-skill`
- `cellxgene-skill`
- `encode-skill`
- `rnacentral-skill`

### Proteins, structures, pathways, and functional biology

- `alphafold-skill`
- `rcsb-pdb-skill`
- `uniprot-skill`
- `string-skill`
- `quickgo-skill`
- `reactome-skill`
- `rhea-skill`

### Chemistry, metabolites, and pharmacology

- `bindingdb-skill`
- `chembl-skill`
- `pubchem-pug-skill`
- `chebi-skill`
- `pharmgkb-skill`

### Clinical, translational, and disease evidence

- `clinicaltrials-skill`
- `cbioportal-skill`
- `civic-skill`
- `ipd-skill`

### Public records and study data

- `biostudies-arrayexpress-skill`
- `ncbi-datasets-skill`
- `ncbi-clinicaltables-skill`
- `ncbi-entrez-skill`

### Multi-omics and specialized data sources

- `pride-skill`
- `proteomexchange-skill`
- `metabolights-skill`
- `mgnify-skill`
- `efo-ontology-skill`

The plugin intentionally excludes literature-only `biorxiv-skill` and `ncbi-pmc-skill`, service-oriented `ncbi-blast-skill`, workflow-oriented `locus-to-gene-mapper-skill`, and orchestration-oriented `research-router-skill`.

## Standalone ownership

All 44 skills, their runtime files, and their shared REST, variant-resolution, and source-contract utilities are owned under `chatgpt/oai-maintained-plugins/plugins/life-sciences-databases/`. Skill-local entrypoints preserve the original invocation paths while delegating repeated behavior to the plugin-owned helpers. The plugin has no runtime, build, or distribution dependency on Life Science: Research or Life Sciences Literature and remains usable if either plugin is removed.

The initial copies preserve the implementations present on `origin/master` at `c1cb315bdb09128189f7d40f5034c7cc00645a1d`. From this point forward, this plugin owns its copies independently; changes in the original plugin do not propagate automatically.

## Evidence and source citations

Each skill follows the plugin-local source-presentation contract in `references/source-presentation.md` and the authoritative per-skill URL registry in `references/source-links.json`. Retrieval clients emit sanitized structured provenance and deterministic `canonical_url` values when a supported record mapping exists. Claim-adjacent links are reserved for evidence that the returned record actually supports; empty results, failures, connectivity checks, and source metadata are never promoted to evidence. Raw JSON, XML, FASTA, and text responses remain unchanged when requested.

## Example prompts

- Summarize public genetics and expression evidence linking IL6R to asthma.
- Interpret a variant using ClinVar, gnomAD, Ensembl, and cohort evidence.
- Find structure, pathway, ligand, and pharmacology records for EGFR.
