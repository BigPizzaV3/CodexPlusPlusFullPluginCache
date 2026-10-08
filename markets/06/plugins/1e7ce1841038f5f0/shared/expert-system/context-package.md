# Minimum sufficient context / Context Package

Canonical provider-neutral contract. Read when selecting sources for a material task, a source conflict, or a handoff; not as mandatory overhead for every answer. AVAILABLE CONTEXT is everything discoverable; REQUIRED CONTEXT is the smallest set needed for the next authorized outcome, its constraints and acceptance. Availability is neither relevance nor permission.

## Select before loading

1. Identify the next outcome and risk. Inspect the source index/metadata before bulk content where possible.
2. Select governing instructions, protected invariants, current authoritative source sections, relevant resources, observed baseline and acceptance evidence. Retain exceptions, negative evidence and dependencies that could change the answer; brevity must not cherry-pick truth.
3. For material sources record identity/location, version or observed date, authority class, provenance, relevant section, freshness and recipient access. A file's modification date alone proves neither approval nor factual freshness.
4. Exclude unrelated firms, memories, duplicate copies, abandoned proposals and superseded instructions. Consult history only for an active dependency, conflict, omission or requested history. Retain pointers; do not delete originals.
5. Expand only when a named question or dependency requires it. Missing required context blocks the dependent action; noncritical unknowns may remain explicit. Never invent the missing value.

Read [decision authority](decision-authority-model.md) for source classes and conflict handling. A package is a derived view, never a second source of product truth. It records authority; it does not grant or override it. Respect higher-priority runtime instructions and access boundaries.

## One contract, task-sized views

```text
OBJECTIVE
SCOPE
CURRENT VERIFIED STATE
AUTHORITY
METHOD_LOCK: when an applicable method governs execution
RELEVANT SOURCES
RELEVANT RESOURCES
CAPABILITY_CONTEXT: when technical execution depends on environment prerequisites
CONSTRAINTS
KNOWN UNKNOWNS
OPEN DECISIONS
ACCEPTANCE
EVIDENCE REQUIRED
STOP CONDITIONS
```

For a trivial self-contained task, a short objective, supplied input, relevant bounds and success criterion suffice; omit irrelevant headings. For material tasks include every applicable field and explicitly identify critical unknowns. An existing approved task contract may supply fields by exact accessible reference instead of copying them.

Mappings to [task execution contract](task-execution-contract.md): RELEVANT SOURCES→SOURCES; CONSTRAINTS→FIXED/BOUNDS/PROHIBITED; ACCEPTANCE→PASS_CONDITION; EVIDENCE REQUIRED→EVIDENCE; STOP CONDITIONS→STOP_CONDITION. SCOPE and AUTHORITY come from the authorized task boundary and source/decision record; CURRENT VERIFIED STATE comes from the observed baseline. Resources identify tools, files or assets, not presumed connections. Add no duplicate fields when aliases already carry the meaning. Conflicting aliases require a conflict report.

Keep canonical source identity and update trigger with the view. After relevant source, permission, environment or decision changes, invalidate affected derived claims, refresh the slice and recheck dependent acceptance. Unaffected evidence need not be repeated. A compact summary is not a substitute for evidence needed by the receiver.

For an applicable closed method include the compact `METHOD_LOCK` view defined in [decision authority](decision-authority-model.md), or an exact accessible record resolved before execution. Context reduction and fresh sessions must preserve its scope, essential mechanisms, substitution prohibitions, calibration bounds and reopen conditions; they do not restart method selection.

For technical handoff, CAPABILITY_CONTEXT maps to the same field in the [task contract](task-execution-contract.md), using the [provider gate](provider-capability-routing.md). Include only required toolchain, observed relevant versions/environment, status, gaps, access, evidence/date and recheck triggers. Retain the method/guidance freshness outcome with METHOD_LOCK. No machine-wide inventory; no recipient READY from sender-only observations. Existing fields may supply these meanings without duplication.

## Context-efficient backpressure

On success return outcome, counts, relevant warnings, evidence location and scoped verification status. On failure return the failed check, expected versus observed result, environment identity and enough diagnostic output for the next decision. Keep raw logs in authorized artifacts when useful; disclose omitted or truncated portions. Do not suppress errors or redact away required evidence. Inspect detailed logs incrementally; no hundreds of successful lines in the main context. If logs cannot be retained, disclose that limitation. Never log secrets.

## Handoff and related contracts

Use the existing [handoff schema](../../skills/handoff-work-between-chats/references/handoff-schema.md) for sender/receiver, next action and resume state; this package supplies its context, not another mandatory document. Existing task/report templates own execution and evidence reports. [Decision authority](decision-authority-model.md) owns CONFLICT REPORT and OWNER DECISION PACK. [Representation strategy](representation-strategy-contract.md) owns asset lineage; attach that only when asset handoff is material. No seven-form paperwork bundle.
