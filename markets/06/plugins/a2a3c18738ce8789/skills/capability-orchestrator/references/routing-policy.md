# Routing Policy

## Priority

Evaluate candidates in this order unless user constraints, safety, or host
rules require otherwise:

1. Explicit user request for a valid available capability.
2. Specialist domain capability.
3. Specialist workflow or process skill.
4. Connected app or connector.
5. MCP tool.
6. Native tool.
7. Generic router.
8. Direct model reasoning.

A lower-priority option may win only when the higher-priority option is
unavailable, incompatible, disconnected, unnecessarily expensive in
context, or unable to complete the requested action.

## Minimum effective set

Use one capability when one capability can complete the task correctly.
Use multiple capabilities only when their responsibilities are genuinely
complementary or sequential.

## Candidate evaluation

Compare:
- direct relevance to the requested outcome;
- specialization;
- current availability and connection state;
- required permissions;
- surface compatibility;
- expected result quality;
- context cost;
- redundancy;
- execution risk;
- explicit user preference.

Do not invent numeric precision. The comparison is ordinal in v1.

## Conflict resolution

When two specialists appear equally suitable:
1. choose the more domain-specific one;
2. choose an already installed and connected one;
3. choose lower context and permission cost;
4. use a known relevant user preference;
5. ask the user only when the choice materially changes the result.

## Loop prevention

Before delegating:
- exclude capability-orchestrator itself from candidates;
- reject a route that returns only to a generic router that points back here;
- increment conceptual routing depth for each delegation layer.

Stop routing when:
- the task is complete;
- no further capability materially improves the result;
- routing depth reaches 4;
- a required user connection or permission blocks the remaining action;
- a higher-priority platform or safety rule requires termination.

## Decomposition

Use Direct when one specialist is sufficient.
Use Complementary when independent capabilities contribute separate results.
Use Sequential when one capability must produce input for another.
Use Discovery when no suitable current capability exists.
Use Native fallback when no specialist materially improves the task.
