# Compute Lifecycle Transitions

Use this reference before starting, stopping, or suspending a Compute.

## Transition Gate

- Resolve and read the exact Compute immediately before each requested
  transition. Use either a sufficiently detailed unique list result or describe
  of a supplied immutable ID; do not duplicate reads without an evidence gap.
- Use live state, mutation schema, and tool response evidence to determine
  whether the transition is accepted. Do not invent a state matrix.
- Treat start, stop, and suspend as separate operations. A sequence requires a
  fresh read, impact statement, and confirmation before every operation.
- If the requested terminal state is already observed, report it and do not
  call the mutation tool.
- Do not switch to another lifecycle operation after a state conflict unless
  the user approves a newly proposed transition.

## Terminal Verification

After the single mutation call, observe the exact ID with list or describe
until a terminal state, explicit failure, or the tool timeout. Do not claim
success from an accepted or transitional response. Report the last observed
state and correlation evidence when the terminal result remains unknown.
