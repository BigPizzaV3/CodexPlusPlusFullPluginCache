<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Master Lab: 08 | Title: AI RESEARCH ENGINEERING, AUTOMATION, EVALUATION, AND MODEL RISK -->

# MASTER LAB 08 - AI RESEARCH ENGINEERING, AUTOMATION, EVALUATION, AND MODEL RISK

> Purpose: design an AI-assisted public-equity research system that is faster than a manual workflow without weakening evidence quality, reproducibility, compliance, or human accountability. The system must preserve source provenance, use deterministic computation for math and state changes, test model outputs against known answers, and require human approval where judgment or external action matters.

## 1. Architecture: separate retrieval, transformation, calculation, decision, and action

Do not build one prompt that searches, interprets, calculates, writes the model, decides the investment view, and takes an action. Separate the system into layers with explicit permissions. This reduces error propagation and makes failures diagnosable.

| Layer | Function | Preferred control |
| --- | --- | --- |
| Source ingestion | Acquire filings, exhibits, transcripts, regulator data, market data, approved alternative data | Immutable raw store, timestamp, document hash, licensing and access controls |
| Parsing / extraction | Convert source documents into text, tables, structured fields | Schema validation, page/section spans, parser version, confidence |
| Retrieval | Select relevant approved source passages | Source whitelist, metadata filters, provenance, recency and version rules |
| Language-model transformation | Classify, summarize, compare, extract, generate hypotheses | Structured output, evidence requirement, no hidden arithmetic |
| Deterministic calculation | Reconcile statements, calculate ratios, build valuation, write files | Tested code or formulas, units and sign checks, reproducible inputs |
| Decision support | Compare evidence, scenarios, thesis, risk | Human-owned assumptions and sign-off |
| External action | Send email, update production model, publish research, trade or other action | Explicit authorization, scoped permissions, logging, approval gates |

## 2. Immutable source layer

The raw-source layer is the foundation. Store the exact document used, not only extracted text. Minimum metadata should include issuer/entity identifier, source type, accession or document identifier, URL or connector reference, publication time, period end, retrieval time, file hash, parser version, language, page count, and whether the source supersedes a prior version.

Never silently replace a filing with an amended filing in historical research. Preserve both and mark the amendment relationship. A model built on an earlier version must remain reproducible even after the source changes.

### Canonical source record

| Field | Example purpose |
| --- | --- |
| entity_id | Stable company mapping independent of ticker changes |
| document_id | Accession, regulator ID, or internal source identifier |
| source_type | 10-K, 10-Q, 8-K, proxy, debt agreement, transcript, regulator release |
| period_start / period_end | Financial-period alignment |
| published_at / retrieved_at | Point-in-time reproducibility and stale-data control |
| hash | Detect source or parsing changes |
| parser_version | Reproduce extraction behavior |
| raw_location | Immutable original file or approved repository reference |
| supersedes | Link amendments or corrected data |

## 3. Entity resolution and identifier discipline

Ticker is not a sufficient primary key. Tickers change, can be reused, and differ by exchange. Maintain stable entity identifiers plus CIK or relevant regulator identifier, LEI where useful, exchange/ticker history, legal name, former names, subsidiaries, brands, and major acquired or divested entities. Entity mapping errors can contaminate every downstream result.

1. Resolve issuer identity before retrieval.

1. Resolve period and fiscal calendar before comparing data.

1. Map segments and subsidiaries with effective dates.

1. Preserve historical tickers and names for alternative-data joins.

1. Flag ambiguous names for human review instead of fuzzy-matching silently.

## 4. Document parsing and table extraction

Prefer structured regulator data such as XBRL for machine-readable facts, but always reconcile material values to the human-readable filing because tags can be misapplied, dimensions can differ, and presentation context matters. For tables, retain row labels, column labels, units, scale, period, and footnotes. A number without those fields is unsafe.

When OCR is unavoidable, attach OCR confidence and route low-confidence fields to review. Never use OCR output as silently authoritative when a native text or structured source exists.

## 5. Structured extraction schema

Require model extraction to emit a schema that captures the semantics needed for audit. Free-form prose is insufficient for model writes.

| Field | Required behavior |
| --- | --- |
| entity | Stable entity identifier and displayed name |
| metric | Canonical metric plus source label |
| value | Raw numeric or categorical value |
| unit / scale | USD, shares, %, units, thousands, millions, etc. |
| period | Start/end date and fiscal label |
| segment / dimension | Segment, geography, product, customer class if applicable |
| source_id | Exact document version |
| source_span | Page, section, table, or exact text span |
| definition | Issuer definition when nonstandard |
| confidence | Extraction confidence separate from economic confidence |
| transformation | Any calculation or mapping applied after extraction |

Reject or quarantine records missing period, unit, or source span when those fields are necessary. Most catastrophic financial-data errors are mundane: wrong period, wrong scale, wrong sign, wrong segment, or wrong entity.

## 6. Retrieval-augmented generation that preserves provenance

Retrieval should prioritize approved primary sources and exact versions. Chunking should respect document structure such as sections, tables, footnotes, and exhibits. A chunk must retain document metadata and location. The answer layer should cite the exact retrieved evidence used for each factual claim.

- Filter by issuer and reporting period before semantic ranking when the question is period-specific.

- Prefer current filing plus directly comparable prior filing for definition-drift questions.

- Use debt agreements for covenant terms rather than summaries when available.

- Retrieve the footnote table and surrounding narrative together when definitions depend on context.

- Require the system to state when evidence is absent rather than infer a fact from nearby text.

## 7. Prompt injection and untrusted content

Treat instructions embedded inside retrieved webpages, documents, filings, emails, or datasets as untrusted data. The system prompt and authorization layer determine behavior, not text found in a source. Retrieval content should never be able to grant new tool permissions, override compliance rules, expose credentials, or trigger external actions.

1. Separate system instructions from retrieved content.

1. Escape or delimit source text clearly.

1. Disable or restrict action tools during untrusted-document analysis unless explicitly needed.

1. Allow only approved domains, connectors, or repositories for automated retrieval where appropriate.

1. Log tool calls and authorization decisions.

1. Test the system with adversarial source text that attempts to redirect behavior.

## 8. Deterministic math versus language-model judgment

Use code or spreadsheet formulas for arithmetic, reconciliations, statement roll-forwards, unit conversions, valuation, optimization, and file writes. A language model can propose the mapping or formula, but deterministic execution should calculate the result. This separates reasoning uncertainty from arithmetic correctness.

Example: the model may identify that a lease liability should be included in a debt-like claim bridge. Code should retrieve the balance and perform the enterprise-to-equity calculation. The language model then explains the result and its assumptions.

## 9. Numeric reconciliation engine

Create automatic checks before extracted data can enter the production model. Checks should operate at the statement, footnote, segment, and time-series levels.

- Assets = liabilities + equity within a defined tolerance.

- Segment revenue plus eliminations = consolidated revenue.

- Cash-flow change in cash = balance-sheet change in cash after FX/reclassification.

- Current period + prior comparable period agree with source table headings and fiscal calendar.

- Units and scale are consistent within a calculation.

- Sign conventions are normalized explicitly.

- Amended filings supersede but do not erase prior versions.

- XBRL value is cross-checked with presented filing for material facts.

- Share counts distinguish basic, diluted weighted average, and period-end shares.

- Debt balances reconcile with maturity and instrument tables.

## 10. Definition-drift detection

Automate comparison of KPI definitions, segment descriptions, non-GAAP reconciliations, risk factors, accounting policies, and guidance language across periods. Use text diff plus semantic classification. The output should show the exact old and new language and classify the change as formatting, clarification, scope change, methodology change, or potentially thesis-relevant removal/addition.

Do not let an AI system summarize a definition change without preserving the source text. Reviewers need the original wording to judge significance.

## 11. Filing-event pipeline

1. Detect new filing or approved source event.

1. Fetch and hash the source.

1. Classify form/event type and issuer.

1. Parse text, tables, XBRL, and exhibits.

1. Run materiality triage based on known thesis variables and event type.

1. Diff against the prior comparable filing.

1. Extract changed financial facts and definitions into a structured schema.

1. Run reconciliation and anomaly checks.

1. Generate a draft impact memo showing facts, calculations, open questions, and potential model lines affected.

1. Require human approval before writing material assumption changes to the production model.

1. Version the model change, memo, evidence, and reviewer decision.

## 12. Earnings-call and transcript workflow

Transcripts are management claims, not primary audited facts. Use AI to classify questions, guidance, KPI changes, contradictions, and new risk statements, then reconcile each material claim with the filing and earnings release. Track what management was asked, what was not answered, and whether the same issue recurs.

A useful transcript system creates a management-claim ledger with claim date, topic, metric, time horizon, confidence language, later outcome, and contradiction status. This supports management-quality analysis and reduces hindsight bias.

## 13. Spreadsheet and model-write controls

Automated model writes are high risk because one wrong cell can propagate through valuation. Use a staging layer. The system proposes changes with source, old value, new value, unit, period, cell/range, formula impact, and confidence. Human review approves or rejects material writes. After write, run the entire model check suite and record the diff.

- Never overwrite formulas with values unless the workflow explicitly expects an input cell.

- Reject writes to protected historical or formula ranges.

- Validate workbook version before applying a patch.

- Calculate before-and-after model outputs and flag large changes.

- Preserve a rollback copy and change log.

- Require deterministic address mapping rather than asking a model to guess cell locations from prose.

## 14. Model and prompt versioning

Record model provider/version, reasoning configuration where relevant, system prompt version, extraction schema version, retrieval configuration, code commit or script hash, source-set version, and evaluation-set version. An AI result that cannot be reproduced under the same versioned inputs is not audit-ready.

When an upstream model changes, run regression tests before promoting it to production. A newer model can improve prose while degrading table extraction or citation precision.

## 15. Evaluation framework

Build a golden set of representative tasks with known expected outputs. Include simple and adversarial cases, tables, footnotes, amendments, unusual fiscal years, segment recasts, negative values, parenthetical amounts, multi-currency disclosures, and documents containing misleading instructions.

| Metric | Definition |
| --- | --- |
| Extraction accuracy | Exact or tolerance-based correctness of values, units, period, and dimensions |
| Citation support | Percentage of factual outputs supported by the cited source span |
| Numeric reconciliation pass rate | Percentage of outputs that pass statement and roll-forward checks |
| Hallucination rate | Unsupported factual assertions per task or per 1,000 claims |
| Definition accuracy | Correct identification of issuer-defined KPI meaning and changes |
| False-positive anomaly rate | Benign items incorrectly escalated as red flags |
| False-negative rate | Known material issues missed by the workflow |
| Analyst correction rate | Share of outputs requiring substantive human correction |
| Net automation yield | Analyst time saved after review and correction cost |
| Regression stability | Change in task performance after model, prompt, parser, or retrieval update |

## 16. Evaluation-set construction

1. Select tasks from real historical workflows and anonymized or public sources.

1. Include multiple industries and filing structures.

1. Create ground truth from senior analyst review or deterministic calculations.

1. Freeze source versions and expected answers.

1. Split development and holdout sets.

1. Add adversarial and edge cases continuously from production failures.

1. Score factual fields separately from narrative quality.

1. Require minimum thresholds by task type before production deployment.

A single average score can hide a dangerous weakness. A system that is 99% accurate on narrative classification but 93% accurate on unit scale may still be unsafe for automated financial model writes. Set task-specific gates.

## 17. Confidence and abstention

Confidence should be calibrated to the task and evidence, not copied from the language model self-assessment. Use objective signals such as source agreement, parser confidence, schema completeness, reconciliation pass, ambiguity count, and historical error rate. When evidence conflicts or key fields are missing, the correct output is an escalation or abstention.

Example confidence components: source quality, extraction reliability, reconciliation status, definition match, and independent corroboration. Document the weighting rather than treating confidence as a magic probability.

## 18. Human approval gates

| Action | Default gate |
| --- | --- |
| Retrieve and summarize public filing | May be automated with provenance and logging |
| Extract values into staging table | May be automated with validation |
| Change a material forecast assumption | Human approval |
| Change production valuation model | Human approval plus model checks |
| Publish investment conclusion | Human accountable reviewer |
| Use expert/channel information with compliance implications | Compliance-approved process and human review |
| Send external communication or take market action | Explicit authorization under firm policy |

Human review should be targeted, not ceremonial. The reviewer should see the source span, proposed conclusion, calculation, uncertainty, and model impact. A checkbox without enough evidence to evaluate the change is not a meaningful control.

## 19. Private data, credentials, and access

Use least-privilege access. Keep secrets in an approved secret manager rather than prompts, notebooks, or documents. Separate public research data from confidential firm data and client information. Log access to sensitive sources. Respect retention, regional, and contractual requirements.

Do not send confidential or restricted material to an AI service unless the firm has approved the service, data handling, retention, and contractual terms. Model capability does not override data-governance policy.

## 20. Cost, latency, and model routing

Use the least expensive and fastest model that reliably passes the task evaluation. Simple classification or extraction may not require the most capable reasoning model. Complex contradiction analysis or ambiguous accounting may. Route by task difficulty, risk, and required latency.

Automation economics = Analyst time saved + error reduction value - model/API cost - infrastructure cost - review cost - expected error cost.

Cache immutable retrieval and deterministic calculations. Do not pay repeatedly to re-summarize an unchanged filing when the stored structured result is valid. Recompute only when source, prompt, model, schema, or analytical question changes.

## 21. Multi-agent or workflow orchestration

Multiple agents do not automatically improve quality. Use specialized stages only when separation creates a check or expertise benefit. One useful pattern is extractor, reconciler, skeptic, calculator, and reviewer. Each stage receives limited inputs and produces a structured output. The skeptic should search for contradictory evidence, not merely rephrase the first agent.

Avoid agent loops with no stop condition. Define a maximum number of retries, escalation criteria, and what constitutes resolved evidence. Store each stage output so the final answer can be audited.

## 22. Research memory and decision journal

Separate factual memory from thesis memory. Factual memory stores versioned source facts and definitions. Thesis memory stores analyst assumptions, probability judgments, scenario choices, and reasons for changes. Never allow a generated summary to overwrite the underlying source record.

When new evidence arrives, compare it with the prior thesis state. Record what changed, why it changed, whether the change was anticipated, and which forecast lines moved. This prevents the system from rewriting history after the fact.

## 23. Automated contradiction hunting

1. Extract management claims and guidance from prior periods.

1. Identify current reported outcomes for the same metric or promise.

1. Compare current narrative with prior wording.

1. Search competitor, customer, supplier, and regulator sources for evidence pointing the other direction.

1. Generate alternative explanations and list evidence needed to distinguish them.

1. Route material contradictions to the analyst with source spans and quantified model sensitivity.

The contradiction engine should not decide that management is wrong. It should make it hard for the analyst to miss evidence that challenges the current thesis.

## 24. AI-assisted valuation and scenario generation

AI can generate candidate scenario narratives, sensitivity dimensions, and missing-risk questions, but the operating model and valuation calculations should remain deterministic. Ask the system to explain the causal chain for each scenario and to identify internal inconsistencies such as growth without reinvestment, margin expansion despite falling utilization, or a debt path that violates liquidity constraints.

Use AI to search for hidden assumptions, not to manufacture precise target prices. The senior analyst owns the selected assumptions and probability weights.

## 25. Production incident response

Treat material AI errors like model incidents. Preserve the failed input and output, classify root cause, determine whether any published or model output was affected, correct the result, update the evaluation set, patch the workflow, and rerun regression tests. Do not quietly fix the one example without addressing the class of failure.

| Failure class | Example | System fix |
| --- | --- | --- |
| Retrieval | Wrong period filing retrieved | Metadata filter and period assertion |
| Extraction | $1.2 billion read as $1.2 million | Unit/scale schema plus reconciliation |
| Entity resolution | Subsidiary confused with parent | Stable entity IDs and ambiguity review |
| Reasoning | One-time gain treated as recurring | Accounting rules plus skeptic/reviewer stage |
| Calculation | DCF arithmetic error | Deterministic code and unit tests |
| Citation | Claim cites nearby but unsupported passage | Claim-level evidence validation |
| Action | Wrong model cell overwritten | Staging, protected ranges, explicit approval and rollback |

## 26. Worked AI workflow: 10-Q to model update

1. Watcher detects the new 10-Q and stores the exact file, accession, timestamp, and hash.

1. Parser extracts statements, footnotes, tables, XBRL facts, and exhibits.

1. Entity/period validator confirms issuer, fiscal quarter, currency, and scale.

1. Reconciliation engine ties statements and segments, flagging any discrepancy.

1. Definition-diff system compares KPIs, segments, and accounting policies with prior filing.

1. Language model extracts changed facts and produces source-linked structured records.

1. Deterministic code calculates growth, margins, working capital, cash flow, share count, and variance versus the existing model.

1. Skeptic stage searches for contrary footnote, cash, or competitor evidence.

1. System produces a proposed model-change package with old value, new value, source, reason, confidence, and sensitivity.

1. Analyst approves, rejects, or edits each material assumption change.

1. Model patch applies only approved inputs, recalculates, and runs all checks.

1. A draft earnings note is generated from the approved state and cited evidence.

1. Reviewer signs off and the system archives source, prompts, model versions, changes, and final output.

## 27. AI completion gate

- Every material factual output can be traced to an immutable source version and exact supporting span.

- Math, model writes, and reconciliations are deterministic and tested.

- Entity, period, unit, scale, and definition errors are actively checked.

- Retrieved content cannot change system permissions or execute instructions.

- The system has a representative golden evaluation set with task-specific thresholds.

- Model, prompt, parser, schema, source, and code versions are logged.

- Production failures become regression tests.

- Human approval is required for material assumptions, publication, compliance-sensitive evidence, and external actions.

- The workflow measures net analyst time saved after correction cost, not just raw automation volume.

- The analyst remains accountable for the conclusion and can reconstruct exactly why the system produced it.
