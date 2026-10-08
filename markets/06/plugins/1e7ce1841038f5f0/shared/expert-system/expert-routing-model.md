# Expert routing model

Skills define the working method. Roles define the discipline that leads, supports, or independently reviews it.

## Worker, capability and execution surface

Keep three routing dimensions separate:

- **WORKER:** the person, chat, agent or execution product responsible for a step, such as normal chat, ChatGPT Work, Claude Cowork, Claude Code or another authorized worker.
- **CAPABILITY:** what the step needs, such as reasoning, file access, coding, shell execution, browser navigation, computer use, connector access or visual inspection.
- **EXECUTION SURFACE:** where the capability actually operates, such as a local host, local project environment, sandbox, VM, container, browser, computer-use session, remote host or connector.

A worker may expose several capabilities and environments; the same capability may be available through several workers. A product name, visible tool or technical ability proves neither access to a particular surface nor authority to act. Temporary availability, quota or outage information may break a tie for the current route but is not durable system truth.

## Routing sequence

1. Classify the project, phase, task, risk, and observable outcome.
2. Select the narrowest active skill that owns the method.
   When the outcome depends materially on external factual research, current/disputed claims, or web/database search, `$control-deep-research` owns evidence admission and claim verification while the domain skill retains domain decisions.
3. Identify required capabilities and suitable workers.
4. Verify available execution surfaces, environment match, authority/permissions, required context/data access and acceptance evidence through the provider-capability contract.
5. Prefer the smallest reliable route. Use a hybrid route when different acceptance dimensions require different surfaces; availability/capacity and cost/latency may break ties only after required quality, authority and verification are preserved.
6. Assign one `LEAD`, only necessary `SUPPORT`, and an independent `REVIEWER` when failure impact or perceptual judgment warrants it.
7. Instantiate role contracts from the registry. Do not activate every plausible role.
8. Record material routing in the existing project, phase, or task record; a simple task needs no new matrix.
9. Re-route when scope, evidence, medium, capability, environment or risk materially changes.

## Selection tests

- The lead owns the primary artifact or decision class.
- Support roles have named contributions that the lead cannot safely absorb.
- The reviewer did not implement or approve the same critical decision it reviews.
- No title exists only for prestige or repeated commentary.
- Regulated or high-stakes work still requires qualified human review where applicable.

Use `$compose-role-teams` when the requested deliverable is a reusable role blueprint or role prompt. Use `$orchestrate-projects` when roles must be routed dynamically across a real project.

Select context through [Context Package](context-package.md) only when source selection is material. For cross-provider stages use [provider capability routing](provider-capability-routing.md), owned by `$design-optimal-ai-workflow`; role assignment alone proves neither tool access nor agent invocation.

For external coding-agent work, keep responsibilities distinct: `$architect-implementation-documentation` owns controlled source suites, `$architect-coding-agent-harness` owns the reusable repository harness blueprint, `$orchestrate-coding-agent-execution` owns the live task/report loop, domain skills own implementation, `$verify-implementation-checkpoint` owns read-only intermediate ratification, and `$verify-production-implementation` owns final release verification. Project orchestration retains project outcomes and dependencies.
