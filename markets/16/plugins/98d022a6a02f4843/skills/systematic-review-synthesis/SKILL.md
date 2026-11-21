---
name: systematic-review-synthesis
description: Extract consistent fields across several research papers, construct evidence tables, compare studies, identify discrepancies, and flag possible duplicate reports/cohorts. Use for systematic/scoping reviews or multi-paper synthesis preparation.
---

# Multi-paper extraction and evidence tables

This skill supports structured data extraction, not automatic meta-analysis or a completed review. Follow `research-data-extraction` invariants. PRISMA is a reporting guideline; do not conflate reporting completeness with study validity or risk of bias.

## Workflow

1. Determine the review question and requested fields; ask only if the question/schema is materially ambiguous.
2. Define the normalized schema once before extracting. If user supplied one, use it exactly.
3. Assign a stable unique Study ID to every paper/report. Where sources may be companion reports, record separate Report IDs and only a tentative shared-cohort ID.
4. Process each source independently. Never fill one study's missing field from another study or from generic knowledge.
5. Preserve each value's source location and missingness code.
6. Build rows with identical columns, then run consistency checks across sample sizes, groups, timepoints, units, outcome definitions, and estimates.
7. Flag possible duplicate underlying studies for human review. Do not merge reports or counts automatically.
8. Return the evidence table plus unresolved discrepancies, extraction uncertainties, and any scope not completed.

## Suggested columns

Study ID; report/citation; country; design; population; eligibility; total/enrolled/analyzed sample sizes; intervention/exposure; comparator; primary outcome; follow-up; main result; effect estimate; CI; p-value; adverse events; author conclusion; author limitations; funding/conflict; bias-related evidence; locations; uncertainty.

## Duplicate-study signals

Possible overlap indicators include the same registration number, authors, recruitment dates, institution, sample size, intervention groups, or baseline characteristics. Report signal(s), confidence (`HIGH`/`MEDIUM`/`LOW`) and reason. A match on one attribute is not proof. Keep records separate unless the user confirms linkage or the reports clearly identify a single study.

## Synthesis boundary

Describe patterns without implying pooled effects. Do not calculate a meta-analysis, GRADE certainty, or causal conclusion unless asked and sufficient methodological inputs and an appropriate protocol are supplied. Keep risk-of-bias evidence separate from formal judgments.
