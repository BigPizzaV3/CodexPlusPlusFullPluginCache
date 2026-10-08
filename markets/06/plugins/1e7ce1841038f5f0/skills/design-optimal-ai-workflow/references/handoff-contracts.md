# Handoff Contracts

Use a contract for every material stage transition.

When the workflow produces implementation documentation, each stage contract must carry artifact identity, version, lifecycle status, source IDs, usage, precedence, acceptance evidence, retry owner, and stop condition. A conversational summary is not a sufficient handoff contract for a controlled specification suite.

## Contract template

| Field | Definition |
|---|---|
| Handoff ID | Stable identifier such as `H03-research-to-script` |
| Sender | Tool, agent, automation, or person producing the artifact |
| Receiver | Tool, agent, automation, or person consuming it |
| Artifact | Exact output and purpose |
| Format | File type, schema, headings, dimensions, codec, or other constraints |
| Required fields | Content that must exist before acceptance |
| Context package | Applicable fields of the shared [Context Package](../../../shared/expert-system/context-package.md), or an accessible reference to the current task contract |
| Provenance | Sources, generation tool/model, prompt/version, date, owner |
| Validation | Automated and human checks before the next stage |
| Failure behavior | Retry, repair, fallback, quarantine, or escalation |
| Version/status | Draft, reviewed, approved, released, superseded |

## Minimum acceptance gate

Before a receiver uses an artifact, verify:

- format opens and conforms;
- required fields are complete;
- sources and rights information remain attached;
- factual claims are distinguishable from creative or inferred content;
- sensitive data is allowed in the receiving system;
- version is current and approval state is clear;
- output meets the stage's acceptance criteria.

## Context preservation

Use the shared Context Package as a derived, task-sized source slice. Do not create a separate canonical project brief that competes with approved project sources. Receiver access, changed sources and invalidated evidence must be checked before reuse.

## High-risk handoffs

Require explicit human approval before:

- publishing or sending externally;
- financial, legal, medical, employment, or safety-impacting outputs;
- irreversible changes;
- use of confidential or personal data in a new provider;
- final factual claims whose errors would materially harm users or the business.
