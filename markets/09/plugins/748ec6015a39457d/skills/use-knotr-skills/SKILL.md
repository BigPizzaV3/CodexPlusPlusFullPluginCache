---
name: use-knotr-skills
description: >-
  Discover and run Knotr profile skills over MCP (list_skills, get_skill), and
  know when to write them back with create_or_update_skill. Use when the user
  wants profile skills, commands, or subagents without syncing a full IDE skill
  bundle. Prefer knotr-save-skill when the user explicitly wants to persist.
---

# Use Knotr skills (MCP)

Profile skills live on knotr.ai. Discover and fetch them over the connected
profile MCP server—do **not** call `get_ide_plugin_install` for skill bodies.

## Read path

1. Call `list_skills` (optional `query`) or read `knotr-ai://manifests/skills`
   (active only).
2. Pick by name, description, and `intended_use` (`skill` | `command` |
   `subagent`).
3. Call `get_skill` with `skill_id`, or `resources/read` on `resource_uri`
   (`knotr-ai://skills|commands|agents/<uuid>`).
4. Follow the returned markdown. Use `referenced_documents` from `get_skill`
   when present.
5. Content is live—no `knotr-sync` / reload required to pick up remote edits.

## Write path

Prefer the **knotr-save-skill** command when the user should explicitly persist.
Otherwise use `create_or_update_skill` (`mcp_write`) when:

**Write when**

- User asks to save, create, update, or publish a skill on Knotr.
- A reusable workflow should travel across tools/machines with this profile.
- Refining an existing Knotr skill (`skill_id` from list/get).
- Persona/team procedures belong on the profile (not only in a repo’s
  `.cursor/skills/`).

**Do not write when**

- One-off chat instructions.
- Facts/docs → knowledgebase / `create_or_update_document`; finished shareable
  outputs → Artifact.
- Secrets, tokens, or machine-only absolute paths.
- A matching skill already exists and the user only wanted to run it.
- Soft-off (`inactive`) or overwrite of an active skill without confirmation.
- Inventing skills nobody asked to persist.

**Checklist**

1. `list_skills` — avoid duplicates; prefer update with `skill_id`.
2. Confirm with the user if create vs update is unclear.
3. Set `intended_use`; prefer `status: draft` on create unless they want
   `active`.
4. Store clean markdown; attach `reference_document_ids` only for owned docs.
5. Report UUID—live on MCP immediately (no full skill sync).

## Repo-local vs Knotr

- Project `.cursor/skills/` — git, this codebase only.
- Knotr profile skill — durable across MCP clients. Default for “save as a
  skill” in a connected session: Knotr via `create_or_update_skill`.
