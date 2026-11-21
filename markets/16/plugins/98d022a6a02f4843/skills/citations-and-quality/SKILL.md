---
name: citations-and-quality
description: Extract and verify bibliographic identifiers, source locations, author-reported conclusions/limitations, conflicts, and bias-related evidence from research documents. Use for provenance, citation checks, or cautious appraisal support.
---

# Citations, provenance, and quality support

Use source text first. Apply `../research-data-extraction/references/citation-rules.md` and `risk-of-bias-rules.md`. Never fabricate an identifier or turn a reporting omission into a definitive flaw.

## Citation extraction

Extract author(s), title, journal, year, volume, issue, pages, DOI, PMID, PMCID, URL, and trial registration when present. Preserve exact identifier text. Flag missing values `NR` and inconsistent values with source locations. External verification is performed only when requested or needed to answer a current-metadata question; use authoritative publisher, PubMed, Crossref/DOI, ClinicalTrials.gov, repository, or official preprint records, and label these as external.

## Author statements vs. assistant notes

Keep author-reported study conclusion, interpretation, limitations, and future research separate from assistant observations such as inconsistent counts, unclear definitions, missing reporting, or possible sources of bias. Attribute every author claim to its location. Do not rewrite a qualified author statement as a stronger conclusion.

## Bias-related evidence

Extract evidence for assessment before offering any judgment. Record domain/question, source evidence, source location, missing information, confidence, and reason. Use `UNCLEAR` when the source does not permit a defensible judgment. RCT risk-of-bias is result-specific in RoB 2; observational intervention/exposure and diagnostic/qualitative/laboratory designs require appropriate design-specific instruments. Ask which instrument and version the user's protocol selected before applying formal ratings. Do not default to an overall low/high label.

## Quality flags

Possible flags include missing registration/protocol; sample-size inconsistencies; outcome switching; attrition/missing data; unclear randomization/masking; missing comparator; short follow-up; unclear outcome definition; multiple testing without stated adjustment; selective subgroup reporting; funding/conflict disclosure; and abstract/full-text mismatch. Report only if supported, say what the source does and does not establish, and invite human review.

## Final citation pass

Ensure external citations support the exact claim; ensure extracted claims point to the supplied document's page/section/table/figure; do not cite a search-result page; and distinguish article bibliography from web-confirmed metadata.
