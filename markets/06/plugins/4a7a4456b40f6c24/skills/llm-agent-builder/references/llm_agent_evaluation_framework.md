# LLM and Agent Evaluation Framework

## Purpose

Use this file to create evaluations that support real product decisions.

An eval is useful only when it helps decide whether a system, prompt, model, tool, or architecture change is better or safe to ship.

# 1. Start with the decision

Examples:
- Should we switch models?
- Did the new tool schema improve success?
- Is the agent safe enough to enable write actions?
- Did routing reduce cost without hurting quality?
- Does the workflow recover from tool failures?

Write the decision before choosing metrics.

# 2. Task taxonomy

Split the product into meaningful task classes.

Examples:
- information lookup;
- extraction;
- planning;
- tool execution;
- multi-step task;
- destructive/consequential action;
- ambiguous request;
- unsupported request.

Do not rely on one aggregate score.

# 3. Dataset

Build examples from:
- real user tasks;
- historical failures;
- edge cases;
- adversarial cases;
- important business flows;
- synthetic cases for rare failures.

Track provenance and expected behavior.

# 4. Evaluation layers

## Model/output
- correctness;
- completeness;
- style;
- schema validity.

## Tool use
- correct tool selected;
- unnecessary tool avoided;
- arguments correct;
- authorization respected;
- tool error handled.

## Trajectory
- reasonable sequence of actions;
- no loops;
- recoverable failures;
- approvals requested correctly;
- stopping condition respected.

## Outcome
- task completed;
- external state correct;
- no duplicate/destructive side effect;
- user goal satisfied.

# 5. Metrics

Possible metrics:
- task success rate;
- exact/semantic correctness;
- structured output validity;
- tool selection precision/recall;
- tool argument accuracy;
- side-effect success;
- approval compliance;
- policy violation rate;
- retry/recovery success;
- human override rate;
- p50/p95 latency;
- tokens/cost per success.

Tie each metric to a failure mode.

# 6. Graders

Use deterministic graders where possible:
- exact match;
- schema validation;
- executable assertions;
- database/state checks;
- tool-call checks.

Use model-based judges for qualitative criteria when needed.

For LLM-as-judge:
- use a clear rubric;
- calibrate against human labels;
- blind comparisons where practical;
- check consistency;
- do not treat it as ground truth.

# 7. Agent evals

For agents, inspect the whole run.

Capture:
- decisions;
- tools;
- arguments;
- tool results;
- retries;
- approvals;
- handoffs;
- final output;
- final external state;
- latency/cost.

A good final answer does not excuse unsafe or wasteful intermediate actions.

# 8. Regression gates

Define thresholds before launch.

Examples:
- no regression in critical task success;
- zero unauthorized side effects in test set;
- schema validity above target;
- latency/cost within budget;
- improvement in known failure slice.

Do not move thresholds after seeing results without documenting why.

# 9. Online validation

Use:
- shadow traffic;
- canary;
- limited beta;
- feature flag;
- human review;
- rollback trigger.

Offline eval success is not proof of production success.

# 10. Continuous improvement

Add new production failures to the eval set.

Track results by:
- model version;
- prompt/version;
- tool version;
- workflow version;
- user/task slice.

Evals should become more representative over time, not merely larger.
