# Codex-Hermes Skill Bridge

## Identity and paths

The installed Windows command is Nous Research Hermes Agent, not the JavaScript engine with the same name.

Resolve the executable with `Get-Command hermes -ErrorAction Stop`. Confirm that the selected binary belongs to the expected Hermes installation before changing configuration.

Resolve Hermes home in this order:

1. active `HERMES_HOME`;
2. `%LOCALAPPDATA%\hermes` on this Windows setup;
3. the path reported by Hermes configuration commands.

Never edit the `hermes-agent` git checkout to install personal skills.

## Preferred sharing

Keep one canonical skill package. Expose a dedicated directory containing only approved personal skills through `skills.external_dirs`, or create narrowly scoped directory links to those skills. Do not point Hermes at the whole `.codex\skills` tree because it also contains system skills.

Before writing configuration:

- inspect the current value;
- preserve unrelated entries;
- resolve every directory to an absolute path;
- confirm that every target contains an intended `SKILL.md`.

After writing:

- run the Hermes configuration check;
- list installed/local skills;
- confirm every intended skill appears once;
- confirm no system or unrelated skill leaked into discovery.

## Bundles

Create a bundle only when several focused skills are regularly loaded together. Use a stable slash-command name, list the included skill names explicitly, and inspect the resulting bundle before reporting success.

## Execution safety

Do not invoke Hermes one-shot or YOLO modes from automation. Do not auto-accept hooks. Prefer interactive use with normal approvals when the user later configures a model.

If no model/provider is configured, registration and local validation can still finish. Report that the skill files are available but Hermes inference is not yet authenticated.
