# Genomic interpretation: educational rigor

## Distinct questions; do not collapse
1. **Gene–disease validity:** is the gene convincingly linked to this phenotype and mode of inheritance? Check ClinGen curation framework and current SOP (the source may classify as definitive, strong, moderate, limited, disputed, refuted; classifications apply to gene–disease pairs, not isolated variants).
2. **Variant identity:** gene symbol (HGNC), canonical transcript/accession+version, HGVS c./p./g. string, GRCh build, zygosity, phase, test technology and variant class (SNV, indel, CNV, repeat, mtDNA). If details absent, do not create them.
3. **Variant classification:** ACMG/AMP (or relevant validated disease/variant-type-specific updates) uses pathogenic, likely pathogenic, uncertain significance, likely benign, benign; use ClinGen SVI expert specifications where available. Do not pretend every ACMG criterion is independently satisfied from a narrative.
4. **Evidence check:** segregation/de novo evidence, functional evidence, inheritance, disease-specific mechanism, allele frequency, penetrance, technical quality, phenotype specificity and computational support with appropriate weight.
5. **ClinVar:** evaluate germline vs somatic type, aggregate vs individual submission, date, review status, assertion criteria and conflicts. ClinVar is an archive of submissions, not an infallible expert verdict; do not translate star ratings into clinical accuracy percentages.
6. **Phenotype match:** use specific clinical features, age of onset, syndromic pattern and competing explanations; consider whether the molecular mechanism fits.

## VUS and uncertainty
- A VUS is NOT a definitive molecular diagnosis. Do not recommend irreversible clinical or family decisions based on a VUS alone. Discussion of segregation or reanalysis is educational, not a stand-alone order.
- Inconsistency across laboratories or database records should be described, not silently resolved by choosing the most pathogenic label.
- Distinguish low allele frequency from pathogenicity; rare is not the same as causal.
- 'Compound heterozygote' requires attention to cis/trans phase; two variants in one gene are not necessarily on opposite alleles.
- Do not infer a pathogenic variant simply from gene loss-of-function constraint (e.g. LOEUF), protein prediction scores or a case report.

## Verify identifiers only if actually retrieved
Reference anchors:
- ClinGen: https://clinicalgenome.org/curation-activities/gene-disease-validity/
- ClinGen SOP: https://clinicalgenome.org/docs/gene-disease-validity-standard-operating-procedure/
- ClinVar review status: https://www.ncbi.nlm.nih.gov/clinvar/docs/review_status/
- HGVS recommendations: https://hgvs-nomenclature.org/stable/recommendations/general/
- gnomAD: https://gnomad.broadinstitute.org/
