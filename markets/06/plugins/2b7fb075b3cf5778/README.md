# Whitespace Reentry

Whitespace Reentry restores the thread of paused work from bounded evidence and surfaces one clear next move. Version 0.2.3 packages the established `whitespace-reentry` skill from AxonDynamic for portable distribution.

The skill supports five read-oriented modes:

- Resume: recover the intended outcome, stopping point, current state, open loops, and one reversible next action.
- Decision trace: reconstruct a decision, its alternatives, evidence, uncertainty, and whether it still holds.
- Handoff: give another person or agent the smallest operational context needed to continue.
- Drift check: compare a prior plan or claim with current evidence and separate matches, drift, and unresolved items.
- Possibility compression: reduce many open loops to at most three explainable, reversible paths.

Invoke it with prompts such as:

```text
Use $whitespace-reentry to show what changed, why it matters, and the smallest useful next move.
I have not touched this project in weeks. Catch me up from the evidence I provide.
Why did we make this decision, and does it still hold?
```

The package is a skills-only workflow. It does not connect to Whitespace Live, a Context Graph, an account, or external connectors. It has no daemon, scheduler, telemetry, MCP server, or background monitor. Orientation does not authorize edits or external effects; saving a Reentry Capsule happens only when requested.

## Package layout

The installable plugin is in `plugins/whitespace-reentry/`. Its manifest, skill, agent metadata, references, and image assets are copied from the established local source. `tests/evals.json` contains synthetic workflow cases, and `tools/check_package.py` performs release consistency and publication-safety checks.

## Validation

From this release directory:

```sh
python3 <plugin-creator>/scripts/validate_plugin.py plugins/whitespace-reentry
python3 <skill-creator>/scripts/quick_validate.py plugins/whitespace-reentry/skills/whitespace-reentry
python3 tools/check_package.py
```

The public repository is `https://github.com/FibonacciAi/whitespace-reentry`. Its support channel is the repository issue tracker at `https://github.com/FibonacciAi/whitespace-reentry/issues`. The packaged privacy and release-terms documents are in `docs/`; the source-available license is in `LICENSE`. See `docs/distribution.md` for the release boundary.
