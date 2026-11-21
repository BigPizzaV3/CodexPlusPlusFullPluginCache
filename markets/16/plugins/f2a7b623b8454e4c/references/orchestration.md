# Specialist-agent orchestration policy

**Reality:** text prompts and role files do not create actual workers. Invoke real subagents only through supported host tools or authenticated agent runtime; otherwise sequentially apply specialist checklists and say so when material.

## Roles
- Lead: scope, architecture decisions, agent selection, integration and evidence.
- Product analyst: user journeys, acceptance criteria, data/permission boundaries.
- Design director: source-grounded art direction, system tokens, state inventory.
- Platform architect: stack, navigation, data model, module boundaries.
- Builders: platform-specific source work with non-overlapping file ownership.
- Security reviewer: read-only threat model, auth and dependency checks.
- QA/visual reviewer: reproducible tests, screenshots, defect ledger.

## Orchestration sequence
1. Lead forms minimal vertical slice and acceptance criteria. Check execution environment, user authorization and budget.
2. Parallelize independent research and brief work only when supported and valuable.
3. Freeze interfaces/acceptance criteria. Assign isolated modules/worktrees to implementation agents and avoid overlapping edits.
4. Integrate centrally. Run builds/tests, review actual code. Reviewers must not silently modify source.
5. Send bounded findings to implementers, fix, rerun and produce a single report with explicit statuses.
6. Disclose actual number of independently executing agents when relevant; do not report fictional agent runs, consensus or trace IDs.

Use `../templates/agent-handoff.md`. No unauthorized background work, deployment, paid services or project data transfer.
