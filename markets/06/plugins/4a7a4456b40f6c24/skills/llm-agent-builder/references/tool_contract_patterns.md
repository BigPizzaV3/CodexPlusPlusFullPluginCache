# Tool Contract Patterns

## Purpose

Use this file to design tools that models can call reliably and safely.

A tool is an interface between a nondeterministic model and deterministic software. Design it for agent usability, not just human developers.

# Tool definition

For each tool define:

## Name
Short, specific, action-oriented.

Prefer:
`get_order_status`

Avoid:
`do_stuff`

## Purpose
Describe when the model should use it and when it should not.

## Inputs
Use explicit schemas:
- required fields;
- enums;
- formats;
- bounds;
- descriptions;
- defaults only when safe.

Avoid ambiguous “options” blobs.

## Output
Return only information useful for the next decision.

Prefer structured results with:
- status;
- data;
- error category;
- recoverability when useful.

# Tool granularity

A tool should correspond to a meaningful action or information need.

Avoid:
- one giant universal tool;
- dozens of microscopic tools that require unnecessary planning.

Design for composability.

# Authorization

Authorization belongs at the tool/resource boundary.

Validate:
- user identity;
- tenant/resource ownership;
- scope/role;
- action permission.

The model deciding to call a tool is not authorization.

# Side effects

Classify tools:

## Read-only
Search, lookup, fetch.

## Reversible write
Draft, stage, update with rollback.

## Consequential/irreversible
Send, publish, purchase, delete, deploy, transfer, permission change.

For consequential tools, require approval or an equivalent trusted control when appropriate.

# Idempotency

For retriable writes define:
- idempotency key;
- operation identity;
- duplicate behavior;
- safe retry semantics.

Do not rely on the model to remember whether an external side effect already occurred.

# Errors

Return errors the agent can act on.

Useful categories:
- invalid input;
- unauthorized;
- not found;
- conflict;
- rate limited;
- transient dependency failure;
- permanent failure.

Distinguish retryable from non-retryable errors.

Do not leak internal stack traces or secrets.

# Timeouts and retries

Define:
- timeout;
- retry count;
- backoff;
- rate-limit handling;
- cancellation.

Retry only operations that are safe to retry.

# Tool descriptions

Tool descriptions should help the model choose correctly.

Include:
- what it does;
- required preconditions;
- meaningful limitations;
- side effects.

Do not stuff the whole application manual into tool descriptions.

# Sensitive data

Minimize:
- secrets;
- tokens;
- credentials;
- raw PII;
- internal IDs not needed by the model.

Redact logs and traces.

# Validation checklist

Before shipping a tool test:
- correct selection;
- incorrect selection;
- missing inputs;
- malformed inputs;
- unauthorized access;
- dependency failure;
- timeout;
- repeated call;
- partial failure;
- user cancellation.

Evaluate tool selection and argument correctness separately.
