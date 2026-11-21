# Research Data Extraction Assistant

Public-facing display name: **Research Extractor**. This is a skills-only plugin: it has no MCP server, OAuth, API key, external backend, or database. It works from files and text the user supplies in the conversation and uses optional web research only when the user asks for external verification or related sources.

## Skills and routing

| Skill | Use it for |
|---|---|
| `research-data-extraction` | Request triage, schema selection, source-grounding rules, output mode, and quality control |
| `study-design-and-methods` | Study-type classification and methods extraction |
| `population-and-pico` | Participants, eligibility, baseline data, intervention/comparator, and PICO/PICOS/PECO |
| `results-and-statistics` | Outcome records, effect estimates, statistical methods, and requested calculations |
| `tables-figures-and-supplements` | Table transcription, figure/caption reading, appendices, and supplementary material |
| `systematic-review-synthesis` | Consistent extraction across papers, evidence tables, duplicate-study flags, and cross-paper checks |
| `citations-and-quality` | Bibliographic metadata, source citations, author limitations, and bias-related evidence |

## Core promise and limits

Every extracted claim must be traceable to the supplied source. Missing information is marked `NR`, truly inapplicable fields `NA`, uninterpretable evidence `UNCLEAR`, and deliberately unrequested fields `NOT_EXTRACTED`. The assistant does not fabricate, silently reconcile conflicts, or present calculations as author-reported data. It extracts evidence relevant to critical appraisal; it does not replace a protocol-specific risk-of-bias assessment or professional judgment.

## Sources and usage

The detailed behavior is based on the creator-supplied specification. Current methodological reference links are inventoried in `skills/research-data-extraction/references/source-notes.md`. Optional web lookups are limited to requests that require verification, current citation metadata, registration status, or related sources; the supplied paper remains the source for extraction.
