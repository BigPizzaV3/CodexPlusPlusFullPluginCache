# Troubleshooting

## `camber` not found

Install:

```bash
$ curl -sL https://cli.dev.cambercloud.com/install-v2.sh | bash
```

Then restart the shell and run:

```bash
$ camber version
```

## Not logged in

```bash
$ camber login
$ camber me
```

## Agent alias already exists

List agents:

```bash
$ camber agent list --output json
```

Update the existing agent instead of creating a duplicate:

```bash
$ camber agent update @owner.alias --instructions-file instruction.md --output json
```

## Skill compile failed: Validation failed

Check `SKILL.md` frontmatter. Valid fields:

```yaml
name: my-skill
description: what this skill does
camber-entrypoint: scripts/main.py
```

Remove fields such as `allowed_tools`, `tags`, or other unrecognized keys. Valid fields are `name`, `description`, and optional `camber-entrypoint`.

## Push failed: `.camber/sync.yaml` not found

Push must run from a directory that already has `.camber/sync.yaml`.

For a fresh mirror from the project root:

```bash
$ camber agent context init
```

Then fill placeholders and run `$ camber agent push`.

For an existing pulled mirror:

```bash
$ camber agent pull @owner.alias
```

Then run push from that pulled mirror folder.

Using `$ camber agent context init` to create `.camber/sync.yaml` so that do not hand-write it. Do not copy `.camber/sync.yaml` into an unrelated folder just to make push work.

## Placeholders still present in `.camber/sync.yaml`

Before `$ camber agent push`, replace every `{{...}}` placeholder with concrete values for the local workspace (owner, alias, name, instruction path, knowledge-base paths, etc.).

**First-time push:** leave `agent:` blank — do **not** call `agents_create` or `$ camber agent create` first to obtain a uuid. The first push creates the remote agent and may write the id back into `sync.yaml`.

**Refresh:** set `agent:` to the known remote id from a prior push or `$ camber agent list`.

## Push failed: sync path must be relative

`$ camber agent push` requires relative paths. Save staging files under `.camber/` (for example `.camber/instruction.md`, `.camber/chats/`) — do not point `sync.yaml` at absolute temp directories.
