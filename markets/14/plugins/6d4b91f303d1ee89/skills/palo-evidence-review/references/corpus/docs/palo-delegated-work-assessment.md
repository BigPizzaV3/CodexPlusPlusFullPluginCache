# Delegated-work assessment and comparative evidence

Experimental offline profile 0.1.0, 23 October 2026. This profile implements the assessment and evaluation recommendations from the GLM-5.3 and Gemini 4 Argon documentary review. It has no connection to those reviewers or to any commercial agent at runtime.

PALO provides a lifecycle method for assessing delegated AI work: who owns the responsibility, which authority applies, what happened, which effects can be evidenced, and when conclusions need review. This profile relates existing evidence across native control boundaries. Its added value must be measured against competently configured native controls and ordinary identity, workflow and assurance practices.

**Authorised does not mean executed. Executed does not mean the declared effect was verified. A verified declared effect does not establish that the business goal was achieved.**

## Assess, monitor and enforce

| Activity | Evidence needed | Current profile capability |
| --- | --- | --- |
| Assess documented controls | Named owner, identity model, approval scope, native controls and explicit coverage gaps | Validate a supplied local assessment and identify structural or freshness gaps. |
| Monitor exported evidence | Actual exports, correlation identifiers, coverage, timing and independent observations | Analyse an operator-prepared snapshot. No continuous collector or vendor adapter is included. |
| Enforce at an action boundary | A mediated path, action binding, bypass tests, revocation and recovery evidence | Record the declared test boundary. The report always leaves enforcement and production qualification false. |

Provider documentation, a successful tool receipt and a local reservation represent different kinds of evidence. None alone establishes business correctness, universal spending control or a non-bypassable deployment. Native controls remain part of the baseline, including their real approval and policy capabilities.

## Use the tool

From a repository clone with its pinned dependencies installed:

```sh
npm run delegated:check
npm run delegated:assess -- assess examples/delegated-work/synthetic-assessment.json
npm run delegated:assess -- assess examples/delegated-work/synthetic-assessment.json markdown
npm run delegated:assess -- schema
```

For machine-readable output or an explicit report file, invoke Node directly so npm's command banner is excluded:

```sh
node scripts/delegated-work.mjs assess my-assessment.json > my-report.json
node scripts/delegated-work.mjs assess my-assessment.json markdown > my-report.md
```

Start with the [empty assessment template](../templates/delegated-work-assessment.json), inspect the [synthetic example](../examples/delegated-work/synthetic-assessment.json), and use the [profile schema](../packages/palo-delegated-work/assessment.schema.json). Dates, four-pair minimums, thresholds and cost rates in the example/template are illustrative, not validated recommendations. Set the real protocol before collecting results. The empty template contains no observations or completed trials and produces inconclusive results.

The CLI reads one explicitly supplied regular JSON file of at most 5 MiB and writes to stdout. It does not fetch URLs, open artifact references, run tools from the input, change permissions, invoke agents or grant execution authority. Unknown fields, invalid dates, duplicate IDs, dangling dependencies and cycles fail validation.

## Reuse existing PALO objects

The lifecycle phases remain Frame, Classify, Assess, Control, Measure and Prove, with review as part of the lifecycle. The five PALO-AM objects remain Identity Profile, Authority Profile, Risk Matrix, Control Layer and Evidence Layer. This package adds an experimental assessment format, not a new canonical lifecycle or replacement runtime contract.

| Existing object or contract | How this profile uses it |
| --- | --- |
| Identity and Authority Profiles | Responsibility owner, surface identity, approval scope and native controls. |
| Action Claim | Reference the exact claim and its authority/delegation version; do not translate it into a new permission. |
| Policy decision and approval | Retain their own artifact references and commitment-time evidence coverage. |
| Effect Contract | Retain declared preconditions, effects, verification window and authorised recovery requirements. |
| Execution receipt and outcome attestation | Preserve execution state separately from observed-effect conclusions and observer provenance. |
| FinOps records | Reference financial evidence and distinguish known costs, unknown liabilities, acceptance and settlement. |
| Evidence Layer and business review | Preserve the independent review of whether the declared result served the business goal. |

Artifact `kind`, `ref` and `digest` are assertions supplied by the operator. The profile checks their structure and relationships, not the referenced file's contents, signature, schema or factual truth. Validate original contracts with their own tools before importing metadata. An input digest binds the complete supplied plan and data; it is not an external timestamp, proof of preregistration or independent attestation. Keep the original input alongside the report.

## Relationships and time

An artifact has effective time, recording time, optional expiry and dependencies. The dependencies form a bounded directed acyclic graph: parallel tasks and fan-in are allowed. Retries and recurring work use new event IDs, rather than cycles. The graph represents evidence dependencies; it does not infer causation, claim dependency completeness or assume a vendor exposes hidden memory.

The report is evaluated at explicit `assessmentAt`, never the machine's current clock. References recorded in the future are rejected. Evidence recorded after the claimed observation, or not yet effective then, reopens review. An effective revision, revocation or contradiction invalidates dependent conclusions for current review. An unrelated later event does not. Expiry is inclusive at the expiry instant. A future-effective change is recorded but not applied early.

Use a new ID for each immutable version. To use amended authority, point the new action and subsequent observations at the new mandate version. A change to an old mandate continues to flag evidence still depending on that old version. Historical reported states remain visible; a revocation does not erase a completed action. This is a conservative snapshot review, not a fresh authorisation decision or a claim that a historically observed effect ceased to exist.

The profile assumes the supplied UTC times are comparable. If clocks cannot establish ordering, collect or reconcile that evidence before making a conclusive comparison. Do not invent a serial order for parallel activity.

## Outcome and human judgement

Both a reported `verified` effect and a reported `mismatch` require an outcome-attestation reference, outcome coverage, a source reference and declared evidence for observer independence. Stale or unsupported conclusions become `inconclusive`. A missing business review changes a claimed achieved or not-achieved business goal to `not-assessed`, without erasing a separately supported effect observation.

Another collector identity alone does not establish independence. Document the authoritative source, lineage, freshness, shared failure modes and access boundaries in the observer basis records. A CRM flag written by the same agent is not automatically independent confirmation.

Similarly, retained information after disconnect does not automatically represent continuing authority, prohibited use or corrupted data. Record access revocation, use restrictions, fact expiry, retention/deletion and responsibility transfer separately. Compensation and remediation require their own authorised actions; this profile performs neither.

## Six experiments and a fair baseline

Use non-consequential fixtures or an authorised test environment. Both arms must receive matched tasks, the same evidence access and the same predeclared ground truth and acceptance rubric. Configure native permissions, workflow, audit, idempotency and reconciliation competently before adding PALO. Record exactly what PALO adds. Evaluate added instrumentation separately if it changes evidence access.

| Experiment ID | Task and evidence | Evidence against incremental value |
| --- | --- | --- |
| `mandate-change` | Revision, expiry or revocation while work is queued or delegated; bind grant versions to commitment and subsequent events. | Native controls and review reach equivalent decisions with equal or less effort. |
| `parallel-delegation` | Concurrent tasks, retry after lost receipt, duplicate effects and conflicts; collect task lineage and authoritative post-state. | Existing business keys, idempotency and workflow reconciliation provide the same result more cheaply. |
| `outcome-truth` | Delayed, partial, stale and self-reported effects; compare receipts with independent target-state observations. | Ordinary postcondition checks match accuracy, uncertainty and effort. |
| `offboarding` | Inventory connections, responsibilities, retained context, artifacts and delegated tasks after an access change. | Native administrator checklists provide equivalent closure and ownership evidence. |
| `attention-quality` | Controlled relevant facts, planted omissions/conflicts, briefing content and subsequent reviewer decisions. | Extra prompts add fatigue or fail to improve decisions at comparable review time. Sampling cannot establish exhaustive hidden-retrieval coverage. |
| `result-cost` | Matched task quality, background work, retries, failed attempts, verification, human work, integration allocation and settlement. | Native FinOps/accounting yields equivalent decisions at equal or lower total cost. |

In paired records, `allow` means the reviewer would accept the task-specific proposition, and `block` means it should be rejected or held under the rubric. They are experimental labels, never operational permission. `inconclusive` is counted separately from errors, with an explicit maximum rate to prevent an abstain-on-everything strategy from winning. Include both decision classes so false allows and false blocks can be measured. `accepted` refers to the separately defined outcome-acceptance rubric; it is not inferred from `allow` or from receipt success.

Preregister a positive minimum improvement in one primary metric: decision error rate, mean reviewer minutes, mean latency or mean known cost. Also set maximum regressions for decision errors, each error class, review time, latency, costs, evidence coverage and accepted-result rate. Comparisons require sufficient paired observations, complete decision evidence, matched access, declared full cost allocation and no known missing liabilities. Input dates and attestations remain declarations; independent reviewers should verify the protocol and data provenance.

## Reporting results and costs

The evaluator emits `supported_improvement`, `no_demonstrated_improvement` or `inconclusive` for the supplied sample. A gain in the primary metric cannot override a failed guardrail. Missing coverage, unknown liabilities, late protocol registration or an unfair baseline make the comparison inconclusive. Synthetic data always yields an inconclusive scoped result, while retaining a separate arithmetic `comparisonSignal` for testing the tool.

Metrics include incorrect allows/blocks, error and inconclusive rates, evidence coverage, accepted outcomes, reviewer minutes, latency and cost. Results are descriptive. They do not estimate field failure prevalence, provide statistical significance or demonstrate a competitive advantage. A negative result must remain visible. `incrementalValueEstablished` stays false because this tool cannot validate the experiment's authenticity or broader applicability.

Costs are non-negative integer millionths of the declared currency, with one shared allocation policy for both arms. Reconcile credit adjustments upstream. Raw token counts and credits are not comparable monetary units. Include shared monitoring costs and human/integration labour using a documented allocation rule, with marginal and allocated amounts preserved in the source evidence. The aggregate value supplied here is an experimental comparison input, not a replacement for the FinOps ledger.

Zero accepted outcomes retain all known cost and have an undefined cost-per-accepted-result ratio. Any unknown liability also leaves that ratio undefined. A justified no-action result may count only if the protocol explicitly defines and evaluates it. Local admission cannot establish a hard cap on a provider's hidden background work.

## Evidence required before broader claims

The implementation is tested on synthetic fixtures and malformed inputs. Commercial-agent exports, live observer independence, enforced mediation, measured reviewer behaviour and production integrations must be established separately. A useful next pilot is one bounded responsibility across two available surfaces, starting with the native administrator's decision and the same decision supported by PALO. A single-surface baseline is useful if cross-system access is unavailable. No vendor integration, source fetch, production control or live pilot is activated by this profile.
