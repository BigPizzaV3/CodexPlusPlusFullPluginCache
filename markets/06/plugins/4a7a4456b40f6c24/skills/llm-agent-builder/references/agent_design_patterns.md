# Agent Design Patterns

## Purpose

Use this file when the problem requires orchestration beyond a single LLM call.

Prefer explicit workflows when the control flow is known.

# 1. Prompt chaining

Flow:

`Step A → check → Step B → check → Step C`

Use when subtasks are predictable and sequential.

Good for:
- transform then validate;
- outline then draft;
- extract then synthesize.

Add deterministic gates where possible.

# 2. Routing

Flow:

`input → classifier/router → specialist path`

Use when inputs fall into distinct categories that benefit from different instructions, tools, or models.

The router should have:
- clear categories;
- fallback/unknown path;
- confidence or deterministic guard where useful.

# 3. Parallel workers

Flow:

`input → worker A`
`      → worker B`
`      → worker C`
`          ↓`
`       aggregate`

Use when subtasks are independent.

Examples:
- research sources;
- analyze multiple documents;
- independent review perspectives.

Define aggregation and conflict resolution.

# 4. Orchestrator-worker

A central model dynamically creates subtasks, delegates them, and synthesizes results.

Use when the number/nature of subtasks depends on the input.

Useful for:
- complex coding changes;
- broad research;
- large document analysis.

Limit worker scope and total budget.

# 5. Evaluator-optimizer

Flow:

`generator → evaluator → improve → stop`

Use when:
- output quality has clear criteria;
- iterative feedback demonstrably improves results.

Define a hard stop:
- max iterations;
- quality threshold;
- budget.

Avoid endless self-critique loops.

# 6. Manager with specialists

Manager retains conversation/control and invokes specialists as tools.

Use when:
- one surface should enforce global policy;
- specialists provide bounded capabilities;
- central synthesis is valuable.

Benefits:
- centralized guardrails;
- consistent final response;
- easier user experience.

# 7. Handoffs

One agent transfers control to another specialist.

Use when the specialist should own the remainder of the interaction.

Define:
- handoff conditions;
- context passed;
- authorization at destination;
- return/escalation behavior.

Do not assume handoff authorization is automatically equivalent to tool authorization.

# 8. Autonomous loop

Generic loop:

`goal → decide → tool/action → observe → update state → done?`

Required controls:
- max turns;
- cost/time budget;
- termination condition;
- tool allowlist;
- retry limits;
- approval gates;
- state checkpointing;
- failure/escalation path.

The agent should ground progress in actual tool/environment results.

# 9. Multi-agent boundary test

Before adding another agent ask:

- Does it need different tools?
- Does it need different permissions?
- Does it need isolated context?
- Can it run independently/in parallel?
- Does it have a distinct evaluation target?

If not, prefer one agent with clearer tools or explicit code.

# 10. Production review

For any agentic design check:
- duplicate side effects;
- tool retry safety;
- stale state;
- context growth;
- prompt injection;
- approval bypass;
- unbounded loops;
- hidden cost multiplication;
- traceability;
- replay/recovery.

The design is incomplete until the failure path is defined.
