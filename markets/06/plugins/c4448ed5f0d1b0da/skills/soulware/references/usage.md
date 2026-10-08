# Local Soul Kit setup

Use these operations when shell and local filesystem tools are available. `SCRIPT` below means the absolute path to this skill's `scripts/soulkit.py`; substitute it and the actual input paths safely. The runtime uses Python 3.10+'s standard library and does not connect to a server.

## Validate and export

```text
python3 SCRIPT validate /path/to/moss.soulkit.json
python3 SCRIPT export /path/to/moss.soulkit.json --output /path/to/new-skill-directory
```

Export creates a native voice skill in a new directory for inspection or manual distribution. It does not register it or set a default.

For a revised downloadable `.soulkit.json`, use `revise`, not `export`:

```text
python3 SCRIPT revise /path/to/moss.soulkit.json --changes /path/to/changes.json --output /path/to/moss-revised.soulkit.json
```

See [conversation controls](conversation-controls.md#save-a-revised-portable-kit) for authoring changes and reviewing their meaning. `revise` merges allowed communication fields, validates, increments the version, and writes a new file without changing the source or an installation. For successive saves from the same original, add `--after-version X.Y.Z` with the latest known saved version of that kit ID. A supplied array replaces that whole array. The output directory must already exist. The changes file is a local authoring input, not a Soul Kit to import.

## Install or update

```text
python3 SCRIPT install /path/to/moss.soulkit.json --scope user
python3 SCRIPT install /path/to/moss.soulkit.json --scope project --project /path/to/project
```

User scope installs to `~/.agents/skills/soulware-<id>`. Project scope installs under the selected project's `.agents/skills/`. Project files may be shared with collaborators or committed, so explain the destination.

Use the same install command for a newer version of the same kit. Generated files must match their recorded hashes. A modified installation or unmanaged destination is preserved and reported as a conflict. Identical installs are idempotent; a changed kit needs a higher version. Keep the kit ID stable when updating.

## Set a default

Add `--set-default` to the installation command only when the user requested that choice. This installs the skill and manages one Soulware preference block in global or project `AGENTS.md`. User scope respects `CODEX_HOME` when set. Other instructions are preserved.

Only one Soulware default is selected per scope. A project default can coexist with a user default; the project's more specific instruction controls that project. Project defaults reference the skill relative to their `AGENTS.md` so they remain usable when the project moves. An `AGENTS.override.md` can shadow `AGENTS.md`; the installer refuses default setup there so the user can resolve the existing configuration. If a user edits the managed default block, preserve it and report the conflict before an update, replacement, or removal.

A new Codex task may be needed to pick up instruction changes. Describe default setup as a saved preference, not an unconditional guarantee over every task or every ChatGPT surface.

## Inspect and remove

```text
python3 SCRIPT status --scope user
python3 SCRIPT status --scope project --project /path/to/project
python3 SCRIPT remove moss --scope user
python3 SCRIPT remove moss --scope project --project /path/to/project
```

Status reports known installations and the selected default at that scope. It does not prove what a different task has already loaded. Removal deletes only an unmodified managed installation and removes its default block if selected; unrelated files and instructions are preserved.

Return success details from the tool result. On a conflict, explain what needs attention instead of deleting or rewriting user edits. Do not add a forced-overwrite workaround.

## Isolated checks

The runtime's `--home DIR` option redirects user-scope locations into an isolated directory and ignores the real `CODEX_HOME`. It is for development or explicitly requested alternative roots; omit it for ordinary setup.
