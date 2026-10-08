# Universal Plugin Installer

Universal Plugin Installer is a Codex plugin that adapts a selected
local folder of skill or plugin sources into importable Codex plugin folders.

It is designed for people who collect skills from different sources and need a
repeatable way to inspect each folder, scaffold the Codex plugin structure, and
generate a manifest of valid and invalid candidates.

## What It Does

- Prompts for, or accepts, a source directory.
- Treats each immediate subfolder as one candidate plugin source.
- Adapts folders with a root `SKILL.md` into Codex plugin structure.
- Inspects existing Codex plugin folders with `.codex-plugin/plugin.json`.
- Writes a stable `<source-root>/manifest.json`.
- Tracks generated files in `.codex-adaptor/state.json`.
- Creates backups before replacing generated files that were edited manually.
- Supports dry runs, strict validation, and JSON output.

## Why This Exists

Many reusable agent skills are shared as plain folders rather than complete
Codex plugins. This plugin adds the missing Codex structure while preserving the
original source content wherever possible.

## Quick Start

From this plugin directory:

```bash
python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root --dry-run
python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root
```

The selected source root should contain one immediate subfolder per candidate:

```text
source-root/
├── first-skill/
│   └── SKILL.md
├── second-skill/
│   └── SKILL.md
└── existing-plugin/
    ├── .codex-plugin/
    │   └── plugin.json
    └── skills/
```

## Directory Selection

Pass the directory explicitly:

```bash
python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root
```

Use an environment variable:

```bash
UNIVERSAL_PLUGIN_INSTALLER_SOURCE_ROOT=/path/to/source-root python3 scripts/adapt_agent_skills_plugins.py
```

Use the prompt in an interactive terminal:

```bash
python3 scripts/adapt_agent_skills_plugins.py
```

In non-interactive mode, the script exits clearly if no source directory is
selected.

## Commands

Preview changes without writing files:

```bash
python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root --dry-run
```

Apply changes:

```bash
python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root
```

Fail when any candidate is invalid:

```bash
python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root --strict
```

Print machine-readable output:

```bash
python3 scripts/adapt_agent_skills_plugins.py --root /path/to/source-root --json
```

## Candidate Requirements

A valid candidate folder must be one of:

- a skill source with a root `SKILL.md` containing YAML frontmatter with
  non-empty `name` and `description` fields;
- an existing Codex plugin with `.codex-plugin/plugin.json`.

Folder names must be valid Codex plugin identifiers. Use ASCII letters, digits,
hyphens, underscores, and dots.

## Generated Files

For each valid skill source, the adaptor creates or updates:

```text
<candidate>/
├── .codex-plugin/
│   └── plugin.json
├── .codex-adaptor/
│   └── state.json
└── skills/
    └── <skill-name>/
        └── ...
```

At the source root, it writes:

```text
<source-root>/manifest.json
```

The manifest contains:

- `plugins[]`: marketplace-style entries for valid plugin folders;
- `validPlugins[]`: adapted plugin details;
- `invalidCandidates[]`: folders that could not be adapted and why;
- `security`: untrusted-source handling metadata.

## Prompt-Injection Safety

Candidate folders are treated as untrusted input during adaptation.

The adaptor does not execute candidate scripts, import candidate code, run
commands found in source text, or obey instructions inside candidate `SKILL.md`,
README, metadata, scripts, or manifests.

The workflow protects this boundary by:

- parsing only the frontmatter fields needed to assess structure;
- copying source files as bytes;
- ignoring symlinks and generated/cache folders while copying;
- using neutral generated plugin descriptions instead of copying untrusted
  source prose into generated metadata;
- marking generated manifests with `sourceTrust: "untrusted"`.

Important: copied skill files can become instructions after a user intentionally
installs the adapted plugin. Review adapted plugin contents before installing
plugins from unknown sources.

## Local Validation

Run the regression tests:

```bash
python3 scripts/test_adapt_agent_skills_plugins.py
```

Validate the plugin with the Codex plugin validator:

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py /path/to/universal-plugin-installer
```

## Project Structure

```text
universal-plugin-installer/
├── .codex-plugin/
│   └── plugin.json
├── assets/
│   ├── composer-icon.png
│   └── logo.png
├── docs/
│   ├── architecture.md
│   ├── publishing.md
│   └── usage.md
├── scripts/
│   ├── adapt_agent_skills_plugins.py
│   └── test_adapt_agent_skills_plugins.py
└── skills/
    └── universal-plugin-installer/
        └── SKILL.md
```

## Publishing

This is a skills-only Codex plugin. It does not require an MCP server, OAuth,
hosted UI, API key, or remote backend.

For public OpenAI submission, use the OpenAI Platform plugin submission flow and
choose `Skills only`. See [docs/publishing.md](docs/publishing.md) for the
submission checklist.

For usage and architecture details, see:

- [docs/usage.md](docs/usage.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/publishing.md](docs/publishing.md)

## Configuration, Secrets, And Auth

No secrets, API keys, or authentication are required. The plugin operates on a
user-selected local directory.

## Limitations

- Only immediate subfolders of the selected source root are treated as
  candidates.
- Invalid or incomplete candidates are reported, not repaired automatically.
- The adaptor prepares plugins for review and import; it does not certify that
  third-party skill instructions are safe to install.

## License

No license file is included yet. Add a license before publishing the repository
as open source.
