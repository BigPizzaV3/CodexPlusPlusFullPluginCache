# Agent State and Memory Patterns

## Purpose

Use this file to decide what an LLM/agent should remember, where it should live, and how it should be controlled.

Do not call all persisted information “memory.”

# 1. Current-turn context

Information needed only for the active request.

Examples:
- current question;
- tool results;
- temporary calculations.

Usually discard after completion.

# 2. Conversation/session history

Prior turns needed for conversational continuity.

Questions:
- How long should history persist?
- Can it be compacted/summarized?
- Can the user reset it?
- Does it contain sensitive data?

Avoid replaying unlimited history forever.

# 3. Workflow state

State required to resume a multi-step process.

Examples:
- current step;
- completed tools;
- pending approval;
- partial outputs;
- retry count.

Workflow state should be structured and recoverable.

Do not infer critical workflow state from free-form chat history when explicit state is available.

# 4. Durable user preferences

Examples:
- preferred format;
- saved settings;
- recurring configuration.

Store only information that has a clear future purpose.

Provide edit/delete/reset behavior appropriate to the product.

# 5. Long-term application memory

Information derived from prior usage that improves future behavior.

Define:
- write criteria;
- provenance;
- confidence;
- update/merge rules;
- expiration;
- deletion;
- privacy.

Do not automatically embed/store every conversation.

# 6. External system state

Authoritative business state lives in the source system.

Examples:
- order status;
- bank balance;
- repository state;
- calendar event;
- deployment state.

Fetch it from the source of truth when current accuracy matters.

Memory should not silently override authoritative state.

# 7. Vector stores

Use vector retrieval when semantic lookup across stored content is useful.

Do not use a vector database merely because the system has “memory.”

Consider:
- relational/key-value state;
- event logs;
- document stores;
- search indexes;
- summaries;
- semantic retrieval.

Choose based on access pattern.

# 8. Consistency

For consequential workflows define:
- source of truth;
- version;
- concurrency behavior;
- stale-read handling;
- write conflict policy.

# 9. Privacy and retention

For persisted state define:
- what is stored;
- why;
- retention;
- access;
- deletion;
- encryption/security boundary;
- whether it is used in model prompts.

Minimize sensitive state.

# 10. State review questions

Before adding memory ask:
1. What decision needs this information later?
2. Who owns the source of truth?
3. How stale can it be?
4. How is it updated?
5. How can the user correct/delete it?
6. What happens if storage is unavailable?
