---
name: orchestrate-game-agents
description: Coordinate real specialist agents for a complex game project while maintaining single-agent fallback and independent verification.
---

# Orchestrate Game Agents


1. Read `../../references/orchestration.md`. A role description is not an independent agent; check whether real subagent tools or an authorized backend are available.
2. Lead Game Director owns project scope, game-design brief, engine choice, task graph, user approvals and integration.
3. Delegate independent subproblems only when helpful: Game Designer, Engine Architect, Art Director, Gameplay Developer, Level Designer, Audio, QA/Playtester and Release. Use few agents for small games.
4. Freeze interfaces and shared asset naming before parallel implementation. Give separate non-overlapping files/branches/worktrees and concrete acceptance checks.
5. Keep security and QA review read-only and independent of implementers. Reconcile cross-agent decisions centrally; never claim '8 agents completed' based on simulated personas.
6. Limit token/time/cost budgets and external side effects. Report actual subagent tasks, commands, artifacts and failures, with sequential fallback identified when used.

## Execution truth and safeguards
- A skill is an instruction workflow, not a remotely running game engine or a separately running AI agent. Inspect tools and repo state before claiming execution.
- Preserve existing projects, names, dependencies, save formats, and user work unless a change is explicitly requested. Obtain approval for deployment, payments, destructive edits, publication, and major third-party connections.
- Avoid reproducing protected commercial characters, levels, dialogue, soundtracks, logos, or copyrighted assets unless authorized. For assets, record origin and license. Read `../../references/security-and-rights.md`.
- Report what was implemented, what was actually run, what failed, and what remains unverified; never describe proposed tests as passed.
