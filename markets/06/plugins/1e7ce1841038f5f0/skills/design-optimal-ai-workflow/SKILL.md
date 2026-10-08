---
name: design-optimal-ai-workflow
description: Design, compare, optimize, or audit the best current combination of AI tools, models, workers, capabilities, execution surfaces, automations, and human review for any project. Use when the user asks which AI or environment should perform each project step, how Chat, Work, Cowork, coding agents, local tools, browsers or connectors should work together, how outputs should be handed off, which primary and fallback tools to use, how to balance quality, cost, speed, privacy, reliability, or automation, or how to replace a fragmented AI stack with an end-to-end workflow.
---

# Optimal AI Workflow Designer

Design the smallest effective AI toolchain for the actual project. Optimize the complete system, not individual tools in isolation.

## Protect truth and currentness

- Treat model availability, features, prices, limits, integrations, licenses, privacy terms, and regional access as time-sensitive.
- Research current official product documentation before recommending named tools when these details affect the decision. Record the review date and cite material claims.
- Distinguish verified capability from vendor claim, third-party observation, inference, and unknown.
- Never invent access, subscriptions, API availability, connectors, benchmarks, prices, or enterprise controls.
- Do not claim that a workflow is automated until the required integrations exist and have been tested.
- Never expose or place secrets, API keys, personal data, confidential documents, or credentials in prompts or workflow diagrams.

## Frame the project

Infer what is safe and ask only for missing constraints that materially alter tool selection. Establish:

- desired final result and acceptance criteria;
- recurring or one-time workflow;
- input types, output types, volume, languages, and deadlines;
- available tools, subscriptions, devices, skills, budget, and team;
- quality, speed, cost, privacy, control, and automation priorities;
- sensitive data, copyright, regulatory, brand, or approval constraints;
- required publishing or external actions.

Mark each item as confirmed, assumed, unknown, or proposed. Offer a useful provisional design when noncritical information is missing.

## Decompose before selecting tools

Split the project into outcome-oriented stages such as discovery, research, reasoning, writing, coding, asset generation, transformation, verification, approval, publishing, measurement, and iteration. Do not force stages that do not apply.

For each stage define:

- objective;
- required inputs;
- expected output artifact and format;
- objective acceptance test;
- sensitivity and failure impact;
- whether AI, deterministic software, a human, or a hybrid should own it.

Do not use AI where a deterministic method is safer, cheaper, or more reproducible.

For visual, 3D, or otherwise medium-constrained outcomes, do not jump from concept to detailed pipeline specification. Use the shared [representation strategy contract](../../shared/expert-system/representation-strategy-contract.md) and sequence `concept → representation/tool feasibility → proof of quality → approved production strategy → detailed specification`. Select a tool because evidence shows it can carry the required outcome, not because it is fashionable or convenient.

## Select the toolchain

Read [selection-framework.md](references/selection-framework.md) and the shared [provider capability routing](../../shared/expert-system/provider-capability-routing.md) before comparing named tools. Use [provider candidates](references/provider-candidates.md) only for the named surfaces relevant to this task. Read [handoff-contracts.md](references/handoff-contracts.md) when two or more stages exchange artifacts. Read [report-template.md](references/report-template.md) for final delivery.

First inspect any applicable method decision under the shared [decision-authority and method-closure model](../../shared/expert-system/decision-authority-model.md). If it is `METHOD_CLOSED`, still recheck time-sensitive provider capability when reliance requires it, but do not rerank tools, representations or workflows unless a canonical reopen trigger is evidenced. Calibration, provider availability checks and bounded implementation choices inside the closed method are not renewed technique shopping.

For relevant start/re-entry follow the shared [session decision](../../shared/expert-system/session-lifecycle.md). Derive task prerequisites, inspect the actual environment and assess scoped freshness through provider capability routing. Its controlled repair/update policy owns installation and version-change decisions; use the existing CAPABILITY_CONTEXT view, not another tool register. Missing tools do not authorize fallback or reopening.

Choose a primary tool and at most two meaningful alternatives per stage. Evaluate fit using evidence rather than popularity. Prefer fewer tools when quality remains acceptable; every additional tool creates cost, context loss, privacy exposure, integration work, and failure modes.

Route the worker, capability and execution surface as separate decisions under the shared contracts. A worker may use several surfaces, and file access, browser access, computer use and shell execution must not be inferred from one another. Permit a hybrid route when, for example, a local shell supplies deterministic technical evidence and a visual surface supplies perceptual acceptance. Temporary availability or quota may break an otherwise equal tie but never lowers required quality or becomes durable workflow truth.

Consider the user's existing tools first, but do not preserve them when they fail essential requirements. Explain every replacement.

## Design reliable handoffs

For every connection between stages, define:

- sending and receiving owner/tool;
- exact file or data format;
- required fields and naming conventions;
- prompt/context package;
- provenance and source links;
- version and status;
- validation before acceptance;
- retry, fallback, and escalation behavior.

Avoid copy-paste chains of uncontrolled prose. Prefer structured artifacts such as Markdown with fixed headings, JSON schemas, tables, CSV, subtitle formats, image specifications, shot lists, or source manifests as appropriate.

## Separate design from activation

Planning a workflow does not authorize purchases, account creation, subscriptions, API activation, uploads, publishing, messaging, or changes to external systems. Prepare those actions and identify approvals; execute only when separately authorized.

For automation, design observability, idempotency, rate-limit handling, error queues, retries, manual checkpoints, logs, and rollback. Use `$automate-any-workflow` when implementation-level automation design is required. Use `$design-ai-agents` for autonomous or multi-agent systems. Use `$design-ai-production` for detailed media-production pipelines. Use `$orchestrate-projects` when the workflow is part of a larger execution program.

## Provide implementation assets

When useful, include:

- stage-specific prompts or prompt skeletons;
- schemas and file naming;
- folder structure;
- tool configuration checklist;
- test dataset or pilot task;
- acceptance checklist;
- cost and run-time model with disclosed assumptions;
- migration plan from the current workflow;
- fallback workflow when a provider fails.

Do not bury the user in prompts before the architecture is stable.

## Validate and red-team

Before delivery, test the proposed chain conceptually against:

- tool unavailable or feature removed;
- output quality below threshold;
- context lost during handoff;
- source or rights information missing;
- sensitive data reaching an unsuitable provider;
- costs or runtime exceeding assumptions;
- automation repeats or publishes the wrong output;
- vendor lock-in;
- human approval omitted at a high-impact step.

Repair the design and state residual risks. If the project is recurring or material, recommend a small pilot and measurable comparison rather than a full immediate migration.

## Deliver

Lead with the recommended stack and why it wins. Then show the complete stage-by-stage workflow, alternatives, handoff contracts, controls, costs, implementation order, and open decisions using [report-template.md](references/report-template.md). Make clear what is verified, provisional, and not yet testable.

## Controlled implementation-documentation workflow

Use an adaptive lifecycle, not mandatory ceremony. Select scale from dependencies, risk and approval needs: small `brief → task spec → implementation → verify`; medium `planning → spec → implementation → QA`; complex `planning → suite → readiness → coding-agent execution → gates → release`. A small security-critical task still needs its required review; fewer documents never waive authority or evidence.

For complex builds, model the chain `planning → documentation blueprint → specialist specifications → read-only readiness audit → gap closure → re-audit → coding-agent first-read → implementation → QA`. At each transition define artifact version/status/source, precedence, input acceptance, output acceptance, authority, completion evidence, retry owner, and stop condition.

This is an artifact lifecycle, not a chat-summary sequence. Route the multi-document package to `$architect-implementation-documentation`; retain responsibility here for selecting and connecting the AI/tool workflow.

When an external coding agent is the ongoing execution environment under a project/controller layer, route session/context, task prompts and the report-feedback loop to `$orchestrate-coding-agent-execution` and read the shared [coding-agent execution model](../../shared/expert-system/coding-agent-execution-model.md). When the reusable project harness itself must be architected, route to `$architect-coding-agent-harness` and the shared harness model; do not duplicate harness design or the execution controller here, and do not imply an unconnected toolchain is automated.

Use the shared [expert routing model](../../shared/expert-system/expert-routing-model.md) for discipline ownership inside the toolchain, and issue the shared [task execution contract](../../shared/expert-system/task-execution-contract.md) at implementation boundaries. Test technical ambition against available tools and stop when the medium cannot support the target.
