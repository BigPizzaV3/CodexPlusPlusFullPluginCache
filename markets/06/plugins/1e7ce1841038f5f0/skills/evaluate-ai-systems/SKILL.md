---
name: evaluate-ai-systems
description: Independently evaluate an AI feature, model workflow, RAG system, tool-using agent, prompt, or model/prompt revision with realistic behavioral tasks, grounding, hallucination, unknown/refusal behavior, tool trajectories, adversarial safety cases, latency/cost where material, and regression evidence. Use when AI behavior and quality are the primary object of evaluation. Do not use to design the agent architecture, build broad test infrastructure, choose a provider, or implement repairs.
---

# Evaluate AI Systems

Own behavioral AI evaluation, not agent architecture or general test-platform engineering. Evaluate the real candidate against an approved task and safety contract; do not improve prompts or code inside the independent gate.

## Evaluation contract

Define before execution:

- `TASK SET`: representative normal, edge, ambiguous, unknown, conflicting and high-impact tasks with provenance and version;
- `EXPECTED OUTCOME`: observable success criteria, allowed variation, required evidence and prohibited outcomes;
- `EVALUATOR`: deterministic oracle, rubric, qualified human, independent model judge or combination, including limitations and conflict handling;
- `FAILURE CLASS`: taxonomy such as grounding, retrieval, factuality, hallucination, instruction following, refusal, fallback, tool selection, argument, order, side effect, privacy or safety;
- `SAFETY SET`: use-case-specific harmful, adversarial, injection, exfiltration, permission and consequential-action cases;
- `REGRESSION SET`: protected cases, prompt/model/tool/retrieval versions and prior accepted baseline;
- `PASS / FAIL`: per-criterion threshold and overall gate logic;
- `STOP CRITERIA`: failure, uncertainty, unsafe behavior, budget exhaustion, insufficient evidence or required owner/specialist escalation.

Apply the shared [Product Quality Principles](../../shared/expert-system/product-quality-principles.md), [risk-adaptive assurance](../../shared/expert-system/risk-adaptive-assurance-model.md) and [decision authority](../../shared/expert-system/decision-authority-model.md). The evaluator must not silently change the candidate, expected truth or acceptance threshold.

## Execute proportionately

Test as applicable:

- prompt/model behavior across realistic and held-out scenarios;
- grounding, source attribution, retrieval relevance/coverage and behavior when evidence is absent or conflicting;
- factuality, hallucination, calibrated `UNKNOWN`, refusal and safe fallback;
- tool choice, arguments, ordering, retries, duplicate calls, permission boundaries and consequential actions using safe stubs or isolated environments where possible;
- indirect/direct prompt injection, untrusted context, data exfiltration, cross-user leakage and instruction-priority conflicts;
- human control, confirmation, cancellation, recovery and observable failure;
- response quality, consistency and bias/harm criteria appropriate to audience and use case;
- latency, cost and resource use only where approved thresholds make them material;
- prompt, model, retrieval, tool and policy version regression.

Keep evaluation data separate from candidate-authored expected truth. Protect secrets and personal data. Do not execute real purchases, publications, messages, deletions or other consequential side effects merely to test a trajectory.

## Routing boundary

- Agent objectives, tools, permissions, memory, state and architecture → `$design-ai-agents`.
- Durable CI, fixtures, runners and broad cross-system regression infrastructure → `$engineer-test-and-regression-systems`.
- Provider/tool selection → `$design-optimal-ai-workflow`.
- Defect diagnosis or repair → `$diagnose-and-fix-software-defects` or the responsible implementation skill.

## Output

Return candidate identity and environment, versioned task/safety/regression sets, evaluator design and limitations, raw-result pointers, aggregate and per-class results, failures with reproducible evidence, latency/cost evidence where applicable, regression comparison, verdict `PASS`, `PASS WITH RISKS`, `FAIL`, or `NOT VERIFIABLE`, stop/escalation conditions and exact re-evaluation scope. Never claim universal safety, absence of hallucination or production readiness from a bounded evaluation.

