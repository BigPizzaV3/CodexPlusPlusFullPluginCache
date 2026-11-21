---
name: inspect-herb
description: Read current TTMNG scientific identity, material, clinical, constituent and registered analytical research across the full current herbal registry, preserving exact preparation and evidence limits through the authenticated project service.
---

Use `ttmng_reference_catalog` kind=herb, with pagination, to select the exact current scientific identity/rank and reference_id. Names follow dated foreign taxonomy evidence. Thai, mixed, transliterated, fuzzy and historical names cannot select a taxon. Ask only for the indispensable scientific identity when it is missing; an unplaced identity remains held. Never transfer evidence to another species, rank, plant part, preparation or source sample.

Read `ttmng_reference_answer` for the chosen reference. Use section=clinical, materials, constituents or research for focused pages; section=profile exposes paginated profile fields. Follow next_offset and read exact record_ids through `ttmng_evidence_record`; independent reads may use `ttmng_evidence_batch`. Use `ttmng_evidence_question` for a scoped question and inspect its existing facts and research history before a new search.

Answer from the actual source scope. Separate current taxonomy from the source-reported historical taxon; material documentation from project authentication; human component/formulation trials from whole-herb evidence; constituent occurrence/quality markers from experimental mechanisms or clinical activity. Preserve solvent/extraction, route, population, reported quantities, units, denominator, assay/calibration, analytical n/precision, source versions/locators, negative results and table/text conflicts. Unknown calibration or denominators remain unknown. Oil peak area, solution concentration, extract mass and plant mass are not interchangeable. Voucher/botanical identification reports are source observations, not a project-authenticated consumed material.

All existing current records and registered research are available through this reader; the corpus remains partial where the evidence is partial. A missing clinical record or incomplete chemical profile is not worldwide absence or safety. Do not infer complete chemistry, pharmacobotany/dossiers, treatment dose, co-use safety or substitution. Do not request another clinical answer for unchanged already-reviewed content.

Reuse a sufficiently answering source/history without research repetition. Research a real gap only with actual available host primary-source tools and preserve the exact scope and access limits. The backend performs no new web searches and cannot register canonical findings. Do not claim saved results or a received clinical review from retrieval.

All data calls require approved access; provisioned OpenAI reviewer entitlement is permanent. Client flags cannot grant access. Do not invoke legacy 1.2 tools or expose source files, owner replies or credentials. Read actual counts and snapshot date from `ttmng_reference_status`.
