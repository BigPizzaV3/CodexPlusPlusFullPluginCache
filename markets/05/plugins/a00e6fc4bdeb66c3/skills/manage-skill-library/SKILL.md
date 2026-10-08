---
name: manage-skill-library
description: Inventory, catalog, compare, version, back up, synchronize, package, and maintain a personal or organizational agent-skill library. Use when a user asks how many skills exist, where they are stored, what each skill does, whether copies differ, which skills overlap, whether a catalog is current, how to organize skills across Codex and desktop folders, or to prepare safe backups, manifests, checksums, archives, portability maps, and controlled updates.
---

# Manage Skill Library

Maintain one declared source of truth and make every other copy traceable.

## Workflow

1. Confirm library roots, installed root, backup/export roots, runtime, and whether the request is read-only or authorizes changes.
2. Run `scripts/inventory-skills.py ROOT --json OUTPUT.json --markdown OUTPUT.md` for each root.
3. Compare normalized skill names, descriptions, file lists, hashes, UI metadata, and modified content. Do not assume same folder name means same version.
4. Classify entries as `identical`, `changed`, `installed-only`, `backup-only`, `conflicting`, `invalid`, or `unknown`.
5. Detect overlaps by intended trigger and outcome, not merely keywords. Recommend keep, route, merge, split, archive, or retire.
6. Propose a sync plan naming source, destination, overwrite behavior, recovery copy, and expected changes.
7. Obtain explicit approval before overwriting, deleting, replacing, symlinking, installing, or activating anything.
8. After approved changes, rebuild inventories and verify hashes.

## Rules

- Never designate a source of truth silently.
- Preserve user changes and unrelated files.
- Prefer recoverable archives and dated versions.
- Do not auto-update third-party skills without provenance, security review, diff review, and approval.
- Keep the human catalog derived from the installed inventory so counts cannot drift.
- For project/documentation skills, maintain the ownership and lifecycle routing matrix in `references/project-documentation-routing.md`; test positive triggers and near-neighbor exclusions before changing descriptions.

## Output

Return authoritative count by root, status table, duplicates/conflicts, coverage map, proposed actions, and verification result. State whether counts include system/plugin skills or only personal skills.
