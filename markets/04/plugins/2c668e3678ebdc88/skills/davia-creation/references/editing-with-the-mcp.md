# Editing with the MCP

The active Davia game appears as eight virtual files. Treat each read as the
latest snapshot and each edit as an exact textual patch against that snapshot.

## Workflow

1. `list_drafts` lists the creator's editable games.
2. `select_draft` stores the active game for the authenticated session.
3. `current_draft` confirms that selection when context may have changed.
4. `list_files` shows the virtual tree.
5. `read_file` returns a file with one-based line-number prefixes.
6. `grep` searches serialized file contents with a regular expression.
7. `edit_file` replaces exact unnumbered text.

Always read immediately before editing. Do not include the displayed line
number or tab in `old_string` or `new_string`. If an edit could match several
places, include enough surrounding JSON to make the target unique. Use
`replace_all=true` only when every matching occurrence is intentionally part
of the requested change.

To initialize an empty Markdown file, use `old_string=""` and put the complete
initial content in `new_string`. An empty search string is rejected for JSON and
for Markdown files that already contain text.

After an edit, reread the file and check related files when the change spans
more than one representation.

## File map

| File | Editable meaning |
| --- | --- |
| `story.json` | Name, subtitle, premise, visual style, and starting date |
| `world-description.md` | Institutions, material conditions, shared context, and opening pressures |
| `simulation-rules.md` | Game-specific causal constraints |
| `world-stats.json` | Starting values for stats that apply to the world |
| `stats.json` | Stat definitions, domains, subjects, defaults, colors, and instructions; append a complete object to create one |
| `cells.json` | Existing cell names, descriptions, and starting stat overrides |
| `entities.json` | Movable actors: create, edit, delete, describe, feature, place, and set stat overrides |
| `landmarks.json` | Fixed places: create, edit, delete, place, and set stat overrides |

## Read-only identities

The following fields identify existing records and must remain unchanged while
editing those records:

- `stats.json`: `stat_id`;
- `cells.json`: `cell_id`, `slug`, and `kind`;
- `entities.json`: the canonical `slug` returned after creation;
- `landmarks.json`: the canonical `slug` returned after creation.

An existing `stat_id` may contain spaces, capitals, or other legacy characters.
Copy it exactly. Formatting conventions for newly created ids do not apply to
these read-only identities.

Existing objects cannot be removed or reordered in `stats.json`; append a
complete definition to create a stat. The set of objects remains fixed in
`cells.json`. In `entities.json` and `landmarks.json`, append a complete object
to create it and remove its complete object to delete it. Before appending,
search the current definitions, entities, and landmarks by name and meaning so
a spelling or type difference does not create a duplicate.

For a new object, provide a kebab-case placeholder slug derived from its name.
The server derives the stored slug from the name and may add a collision suffix.
Reread the file after creation and use that canonical slug for later edits.
Changing the slug of an existing object is not a rename operation; edit its
`name` instead. Cell geometry is not part of the virtual filesystem.

## Values and legacy state

Only a value changed by the current edit must satisfy its stat's current
domain and subject. An unchanged legacy value may remain visible even when it
predates the current contract. Do not “clean up” unrelated legacy values.

Removing an explicit stat override generally restores its default. Confirm the
definition in `stats.json` before removing a key so the resulting state is
intentional.

## Large map edits

Use `grep` to learn the exact distribution before editing many cells. Prefer a
sequence of reviewable regional patches. A broad `replace_all` is safe only
when the same old value should change in every occurrence; otherwise target
complete cell objects or distinctive neighboring fields. Reread `cells.json`
afterward and use `grep` to count or inspect the final distribution.
