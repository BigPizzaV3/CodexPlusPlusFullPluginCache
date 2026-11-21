# Real multi-agent workflow contract

**No fictional subagents.** A skill package contains role instructions, not executable parallel agents. Use actual host subagent/agent SDK tools only when present. Otherwise do one-agent, serial work.

| Role | Input | Output | Tool rights |
|---|---|---|---|
| Lead | user goal, repository state | task graph, final evidence | integrates changes; seeks approvals |
| Architect | feature requirements, constraints | protocol/transport, tool contracts, data boundaries | read-only planning |
| UI/UX | host requirements, references | UI layout/states, design tokens | bounded UI files if assigned |
| Implementer | frozen contracts | code and commands | assigned files/worktree only |
| Security | source, permissions | vulnerabilities, regression expectations | read-only review |
| QA | source + built artifacts | observed tests and failures | read-only with test execution |

1. Lead inspects real environment and chooses minimum specialists (usually 1–3 for modest tasks).
2. Architecture and UI research may run in parallel. Freeze tool contract before implementation.
3. Split file ownership or independent worktrees. Reviewers must not silently edit production code.
4. Integrator reconciles findings, fixes critical defects and reruns tests. Review comments alone don't prove bugs fixed.
5. Each worker handoff includes artifacts, commands actually run, observed output, blocker list and unresolved risks.
6. Enforce budgets and host permission boundaries; no unattended deployment, secret use or unexpected paid runs.
