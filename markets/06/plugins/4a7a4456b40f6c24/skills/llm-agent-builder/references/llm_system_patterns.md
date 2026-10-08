# LLM System Patterns

## Purpose

Use this file to choose the simplest LLM architecture that solves the product requirement.

Do not start with an agent. Start with the product decision and increase autonomy only when needed.

# Pattern 0 — Deterministic software

Use when ordinary code can solve the task reliably.

Examples:
- validation;
- fixed calculations;
- exact routing rules;
- database lookup;
- deterministic transformations.

Avoid an LLM when variability adds no value.

# Pattern 1 — Single LLM call

Use for bounded tasks such as:
- rewriting;
- classification;
- extraction;
- summarization;
- structured generation.

Prefer structured output when downstream code depends on the result.

Define:
- input contract;
- output schema;
- refusal/error behavior;
- eval examples.

# Pattern 2 — LLM + bounded tools

Use when the model needs fresh/private data or must perform a limited action.

Flow:

`user → model → tool call → validated tool result → model → response`

Define:
- allowed tools;
- when each should be used;
- authorization;
- timeout/retry;
- tool errors;
- side-effect approval.

The model should not receive tools it cannot safely use.

# Pattern 3 — Explicit workflow

Use when the task is multi-step but the path is mostly known.

Examples:
- classify → retrieve → draft → validate;
- extract → normalize → enrich → generate;
- research → compare → produce artifact.

Advantages:
- predictable;
- testable;
- easier to observe;
- easier to recover.

Use code for control flow and models only where judgment is useful.

# Pattern 4 — Autonomous agent

Use when:
- the number/order of steps cannot be known in advance;
- the model must inspect environment feedback and adapt;
- tool selection must remain dynamic;
- a fixed workflow would be brittle.

Define:
- goal;
- tools;
- state;
- max turns/budget;
- stopping conditions;
- approvals;
- failure recovery;
- eval trajectory.

Autonomy increases latency, cost, and compounding-error risk.

# Pattern 5 — Multi-agent

Use only when specialization or isolation creates a real benefit.

Possible reasons:
- independent expertise;
- distinct permissions;
- isolated contexts;
- parallelizable research;
- separate ownership boundaries.

Do not split one coherent task into many agents merely to make the diagram look modular.

# Selection checklist

Choose the lowest complexity level that answers “yes” to the requirement.

Ask:
1. Can deterministic code solve it?
2. Can one model call solve it?
3. Does the model need tools?
4. Are the steps predictable?
5. Must the model dynamically plan?
6. Is more than one agent actually beneficial?

State what evidence would justify moving to the next level.

# Output contracts

When machine consumption matters, prefer:
- JSON schema;
- typed objects;
- enums;
- explicit nullability;
- bounded strings/numbers;
- versioned contracts.

Validate outputs before using them in side effects.

# Model selection

Select models based on the task:
- reasoning difficulty;
- structured-output reliability;
- tool-use reliability;
- latency;
- context size;
- multimodality;
- cost.

Do not use the largest model by habit.

Verify current capabilities/pricing when they affect the decision.
