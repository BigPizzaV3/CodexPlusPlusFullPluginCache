# ChatGPT and Codex execution

This plugin provides a skill with all upstream recipes, API references, and YAML examples. It does not supply an MCP server or an authenticated Frigade connection. Load `SKILL.md` through the installed plugin; its YAML frontmatter provides skill discovery metadata for ChatGPT/Codex. No project-level `AGENTS.md` installation is required.

## Project and capabilities

Resolve `recipes/`, `reference/`, and `examples/` relative to this skill directory. Resolve `.env.local`, `.frigade/`, source files, and package-manager commands against the user's selected application project, never the plugin directory. Select the project before running setup.

In Codex, use the available filesystem and command tools. In ChatGPT, execute API calls and edits only when an available tool environment can access the intended project, securely use its credentials, and reach the API. If any required capability is absent, explain what is missing and provide the relevant YAML, code, or commands as a draft for the user to run in a capable environment. Do not claim that a draft changed Frigade or project files. A chat-only content draft does not require credentials; run first-run setup before executing any recipe against a workspace.

## Recipe terminology and tool mapping

“The agent” means the current ChatGPT or Codex assistant. Upstream action labels describe capabilities, not tool names to invent.

| Recipe label | Action | Codex implementation when available |
|---|---|---|
| `Read` | Read a file | `exec_command` with `cat` or `sed` |
| `Write` | Create or overwrite a file | `apply_patch` or a filesystem tool |
| `Edit` | Modify a file | `apply_patch` |
| `Glob` | Find paths | `exec_command` with `rg --files` |
| `Grep` | Search contents | `exec_command` with `rg` |
| `Bash` | Execute a shell command | `exec_command` using the configured shell |
| Background command / monitor | Start and inspect a process | `exec_command`, then `write_stdin` with its returned session ID |

In other hosts use equivalent tools that are actually exposed. Await successful package installation before wiring or testing. Report a dev server as started only after inspecting startup output. If process support is unavailable, give the command for the user to run and explain that verification is pending.

## Credentials and authorization

Prefer keys already configured securely in the project. When a recipe asks for private keys, have the user enter them directly into a gitignored `.env.local` or a supported secret-input surface; do not ask them to paste secrets into ordinary chat. Preserve other environment entries. Load keys within the execution environment without printing them or placing literal values in tool arguments. Parse `/v1/apiKeys` responses inside that environment and return only the binding result and non-secret workspace identifiers; never print the raw response.

Follow the upstream dev/prod, promotion, destructive-operation, logging, and partial-failure rules in `SKILL.md` and `reference/operations.md`, subject to host instructions and existing user authorization. Host permission boundaries still apply. Never infer successful execution from a proposed command, unavailable capability, or failed API call.

## Preserved procedures

The API contracts, payloads, examples, dispatch tables, framework rules, and recovery steps are preserved from the baseline. Some upstream recipes are explicitly abbreviated; their existing caveats remain. Consult the closest fully authored recipe as instructed by `SKILL.md` and disclose extrapolation.
