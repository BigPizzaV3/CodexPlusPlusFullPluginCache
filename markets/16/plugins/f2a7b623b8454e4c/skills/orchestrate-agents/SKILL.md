---
name: orchestrate-agents
description: Coordinate real specialist agents for complex web or mobile app builds, with task boundaries, independent review and transparent single-agent fallback when subagents are unavailable.
---

# Orchestrate Agents

1. Read `../../references/orchestration.md` and `../../references/execution-model.md`. A skill instruction is not an executable agent: verify actual host subagent support before delegating.
2. Lead decides smallest set of specialists: product analyst, design director, platform architect, implementer(s), security reviewer, visual/functional verifier. Avoid all agents for a simple bug fix.
3. Parallelize nonconflicting research/analysis. Freeze shared interfaces before parallel implementation. Assign separate modules/worktrees to writers and independent read-only review to reviewers.
4. Define for each specialist objective, allowed tools, files to touch, inputs, deliverable, deadlines/budget and approval boundaries. Use `../../templates/agent-handoff.md`.
5. Gather actual outputs, compare against source/test evidence, integrate and rerun. Do not invent 'agent consensus' or independent reviews when only one agent ran.
6. If subagents unavailable, execute roles sequentially with the same checklists and disclose that orchestration was simulated as a workflow, not parallel runtime.
7. Do not launch unapproved background jobs or use paid third-party services without authorization.
