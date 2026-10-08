<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Module: 070 | Title: Research System Automation and AI Assistance -->

## PART XIV - RESEARCH COMMUNICATION AND MASTERY | MODULE 070

# Research System Automation and AI Assistance

> Mission. Use automation and AI for retrieval, extraction, QA, and scenario generation while keeping human verification and accountability.

## Decision output

Objective: Use automation and AI for retrieval, extraction, QA, and scenario generation while keeping human verification and accountability. The completed work product must be reproducible from evidence, show the downstream financial or decision effect when material, state the strongest contrary case, and define a dated update rule.

## Explicit operating procedure

1. Build an immutable source-ingestion layer with document identifier, URL/accession, timestamp, version/hash, parsed text/tables, and exact source spans.

1. Use structured extraction schemas carrying entity, metric, value, unit, period, definition, source location, and confidence; route discrepancies and low-confidence fields to review.

1. Use retrieval that prioritizes approved primary sources and preserves provenance. Retrieved document instructions are untrusted data, not executable commands.

1. Use deterministic code or spreadsheet logic for arithmetic, reconciliations, valuation, and file writes whenever possible; use language models for classification, contradiction search, extraction assistance, hypothesis generation, and drafting under checks.

1. Run automated numeric and definition QA: statement totals, XBRL versus filing tables, segment reconciliation, signs/units, current versus prior definitions, stale-source detection, and citation support.

1. Maintain a golden evaluation set and track extraction accuracy, citation accuracy, numeric reconciliation, hallucination rate, false-positive red flags, regression stability, analyst correction rate, and net automation yield.

1. Require human approval before material assumption changes, published conclusions, compliance-sensitive use of channel data, or external actions; version prompts, models, schemas, code, and reviewer decisions so prior outputs are reproducible.

## Required evidence and model bridge

- Primary-source set: investment memo, evidence pack, model outputs, monitoring dashboard, review and automation logs. Preserve exact document/version, date, period, and source location for every material factual input used in research system automation and ai assistance.

- For each key concept - source ingestion, immutable raw store, structured extraction, RAG, provenance, deterministic math - state whether it is a reported fact, analyst calculation, management claim, external estimate, or judgment. Quantitative concepts must retain raw components and units; qualitative concepts must retain the specific evidence and counterevidence.

- Map only economically relevant findings into the model or decision record. Process-control modules such as research system automation and ai assistance may have no direct valuation line; in that case document the downstream error or governance risk the control prevents.

## Metrics and calculation controls

| Metric / concept | Construction | Required validation |
| --- | --- | --- |
| citation accuracy | % of sampled citations that directly support the adjacent factual claim with the correct document, date, page/section, and interpretation. | citation accuracy: Recalculate independently from cited source data; verify definition, period, units, scope, signs, and any reconciliation to reported financial or operating totals. |
| numeric reconciliation | % of sampled extracted or modeled figures that reproduce the primary-source value after unit, sign, scale, and period normalization. | numeric reconciliation: Recalculate independently from cited source data; verify definition, period, units, scope, signs, and any reconciliation to reported financial or operating totals. |
| hallucination rate | Unsupported or materially incorrect AI-generated factual claims divided by all sampled factual claims before human correction. | hallucination rate: Recalculate from same-scope numerator and denominator; confirm period, units, cohort/geography, and issuer definition; reconcile material differences to filings or operating data. |
| automation yield | automation yield = annualized economic output / current market value or invested base; match numerator and denominator. | automation yield: Recalculate automation yield from cited inputs; reconcile definition, period, units, signs, and source version; investigate and document any variance before use. |



## AI research system architecture

- Create an immutable raw-source layer. Store filing accession/URL, publication timestamp, document hash/version, extracted text, tables, and source spans before any LLM transformation.

- Use structured schemas for extraction. Each extracted value should carry company, period, metric, value, unit, source document, page/section, exact supporting span, and confidence.

- Use deterministic code for arithmetic, reconciliations, valuation, and spreadsheet writes whenever possible. The LLM can propose mappings or explanations, but calculations should be reproducible.

- Build retrieval with source whitelists and provenance. Primary-source passages should outrank summaries. The answer layer must cite the exact evidence used, not a nearby document.

- Run automated checks: totals versus components, XBRL versus filing table, current versus prior filing definition, sign/unit consistency, and balance-sheet/segment reconciliation. Route failures to human review.

- Maintain an evaluation set containing known filings and expected outputs. Track extraction accuracy, citation support, numeric reconciliation pass rate, hallucination rate, false-positive red flags, and analyst correction rate over time.

- Defend against prompt injection and untrusted content. Treat instructions inside retrieved documents/web pages as data, not executable instructions. Separate retrieval, transformation, and action permissions.

- Human approval gates are mandatory before changing valuation assumptions, publishing a research conclusion, using channel evidence with compliance implications, or taking any external action.

- Version prompts, models, schemas, source sets, and outputs. A research result is not auditable if a reviewer cannot reconstruct which model and evidence produced it.

## Worked application

> Case: LLM extracts 10-Q numbers that are checked against XBRL and source spans before model write.

- Reconstruct the relevant reported fact from primary evidence before interpreting the case. For research system automation and ai assistance, show the raw components rather than only the resulting ratio or narrative.

- Build the causal chain through source ingestion, immutable raw store, structured extraction, RAG, then identify which link is directly observed and which link remains an assumption.

- Calculate citation accuracy, numeric reconciliation, hallucination rate, automation yield from sourced components under the reported/base interpretation and at least one skeptical alternative interpretation.

- Translate the difference between cases into the variable that matters for research system automation and ai assistance: evidence quality, revenue, operating profit/NOPAT, free cash flow, invested capital, financing/dilution, risk, or valuation. Mark non-applicable links instead of inventing them.

- Expert consistency test: use AI for retrieval, extraction, contradiction hunting, and drafting while humans retain factual and decision accountability.

- Precommit the specific future filing, KPI, customer/supplier observation, regulator action, or market input that would materially invalidate the research system automation and ai assistance conclusion.

## Failure tests

- FAIL if source ingestion cannot be defined and reproduced from the source pack.

- FAIL if an AI-produced material fact, calculation, model change, or conclusion cannot be traced to versioned sources, deterministic checks, evaluated workflows, and an accountable human approval.

- FAIL if the research system automation and ai assistance conclusion depends on an unstated assumption, unreconciled definition, or evidence that cannot be traced to its source/version.

- FAIL if evidence materially inconsistent with the research system automation and ai assistance conclusion is omitted, reclassified, or dismissed without a documented definition, materiality, causal, timing, and source-quality analysis.

## Completion test

A senior reviewer must be able to reproduce the research system automation and ai assistance conclusion, vary the most sensitive assumption independently, trace the change through the model, understand the strongest opposing case, and identify the next evidence that would force an update. If any link is missing, the module remains open.
