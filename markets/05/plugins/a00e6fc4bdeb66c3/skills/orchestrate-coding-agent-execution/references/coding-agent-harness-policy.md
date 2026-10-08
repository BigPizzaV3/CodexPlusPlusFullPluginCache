# Coding-agent harness readiness boundary

Use the shared [coding-agent harness model](../../../shared/expert-system/coding-agent-harness-model.md) and [harness complexity policy](../../../shared/expert-system/harness-complexity-policy.md). This controller checks only whether the declared harness version, applicable instructions, permissions, commands, source access and review topology are compatible with the current task.

If the harness is absent, fundamentally new, contradictory, overloaded, stale, unsafe or requires durable project instructions, project skills, agents, hooks or permission architecture, route to `$architect-coding-agent-harness`. If complexity is itself the failure mode, record `HARNESS_OVERENGINEERING_RISK` and route to simplification rather than another layer. Do not design the full harness inside the live execution loop.

Minor task-local configuration explicitly allowed by an approved harness may remain in the current task contract. No inspection, blueprint or task-local proposal grants authority to install files, activate tools, widen permissions, change global/provider settings or execute repository hooks.
