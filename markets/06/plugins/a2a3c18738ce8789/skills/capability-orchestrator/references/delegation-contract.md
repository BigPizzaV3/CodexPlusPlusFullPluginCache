# Delegation Contract

Each delegated unit has one clear objective.

Use this conceptual contract:

```yaml
subtask:
  objective: <single clear objective>
  relevant_context: <only information required for this objective>
  constraints:
    - <relevant user or platform constraint>
  expected_output: <result required by the next step or final answer>
  depends_on: <prior result, or null>
```

## Context rule

Never pass unrelated conversation history.
Never include the full capability catalog.
Never pass source material that the specialist does not need.

## Sequential work

When a subtask depends on an earlier result, pass the result itself or a
minimal structured summary, not the entire earlier interaction.

## Complementary work

Give independent specialists separate contexts. Synthesize only after both
results are available.

## Mutation boundary

When a downstream capability can mutate external state, preserve the host's
normal confirmation and permission requirements. The orchestrator cannot
expand the downstream capability's authority.

## Completion

Return control when the delegated objective is satisfied. Do not ask a
specialist to solve unrelated subtasks merely because it is already loaded.
