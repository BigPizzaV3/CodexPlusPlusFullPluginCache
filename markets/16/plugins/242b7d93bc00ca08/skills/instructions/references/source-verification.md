# Evidence policy, anti-hallucination and 'Update by Bing'

## Source hierarchy (adapt to question)
1. **Disease overview:** disease-specific GeneReviews chapter (check revision date), Orphanet disease entry/coding hierarchy, NIH GARD for lay summaries, relevant specialist-society guidelines. Database home pages give source locations, not proof of a disease-specific claim.
2. **Gene / variant:** ClinGen gene–disease validity and SVI, HGVS nomenclature, ClinVar submissions and review status, gnomAD population context, original molecular / functional papers.
3. **Treatments:** regulatory agency label (FDA/EMA or relevant country) for authorization/indication, clinical practice guideline, original RCT or systematic review, trial registry status. Trial registration DOES NOT establish efficacy or approval.
4. **Epidemiology:** population-based registry or reproducible observational evidence rather than a single case report; explicitly report country, sample, diagnostic criteria, calendar period and whether incidence/prevalence is estimated.
5. **Research:** PubMed/PMC and publisher site for DOI, PMID, publication date, abstract/full text, retractions and corrected versions. A PubMed hit does not mean article full text was read.

## Mandatory update behavior
- On requests containing 'Update by Bing', 'latest', 'mới nhất', current guideline/treatment or approval: seek live information using tools actually available in the runtime. The phrase **Update by Bing** is the user's shorthand for verifiable live search, not a claim of integration with Bing.
- Report query focus, actual source accessed, access/check date, publication/revision date, source level and limitations. Use primary documents when possible, cross-check critical treatment/genetic claims, prefer explicitly dated revisions.
- If search tools are unavailable/inaccessible or a site blocks access: say `Chưa thể cập nhật trực tuyến trong phiên này`, give cautiously labeled background and source landing pages (do not misrepresent them as read).
- Separate `newly published`, `recently updated` and `current consensus`; check full publication dates rather than ranking order in search results.

## Citation integrity checks
- Each precise numerical, gene, variant, treatment, eligibility or regulatory claim must map to supporting source, NOT mere association in one results page.
- Copy DOI, PMID, ORPHAcode, OMIM identifier and variant HGVS exactly from verified source; if none, leave absent and say not verified.
- Source label: `Verified from full text`, `Verified from abstract/landing page`, `Reported by user-supplied document`, or `Not verified`. Do not use first two labels when no live/document read occurred.
- Do not quote long paywalled text or claim to have inspected it.
- DOI links should resolve to the intended article; if unsure, provide journal/title/date without DOI.
- Explain source disagreement. Record database update/review status and any competing assertions, not just one record.

## Authoritative entry points (not substitutes for disease-specific citations)
- GeneReviews: https://www.ncbi.nlm.nih.gov/books/NBK1116/
- Orphanet: https://www.orpha.net/en/disease/list
- NIH GARD: https://rarediseases.info.nih.gov/
- ClinGen: https://clinicalgenome.org/
- ClinVar: https://www.ncbi.nlm.nih.gov/clinvar/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/
- ClinicalTrials.gov: https://clinicaltrials.gov/
- US FDA: https://www.fda.gov/drugs
- European Medicines Agency: https://www.ema.europa.eu/
