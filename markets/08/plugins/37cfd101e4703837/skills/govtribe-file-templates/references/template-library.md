# Template library

This guide ships only on hosts that install the GovTribe template files. Its presence means `assets/` holds the catalog, blank masters, examples and previews, and `scripts/` holds the helpers below.

## Select a template

Required buyer forms take precedence. For a new library file, match the requested name, ID or deliverable in `assets/catalog.json`, then run `python3 scripts/resolve_template.py TEMPLATE_ID` from this skill's root. Verify the selected revision and copy its blank master; examples are illustrative. The catalog's `domain_skill` names the workflow for needed research.

When the handoff supplies expected hashes, use `python3 scripts/resolve_template.py TEMPLATE_ID --expected-catalog-sha256 HASH --expected-master-sha256 HASH`. Resolve missing or mismatched selected bytes before adapting. Without Python, verify catalog identity, contained paths, byte counts and SHA-256 values with native file/checksum tools. `--verify-all` checks the whole library.

## Proposal Compliance & Control helpers

For an optional structure check, run from the installed `govtribe-proposal-workflows` root (Python and `openpyxl` required):

```bash
python3 scripts/validate_proposal_workbook.py working.xlsx
```

This checks the eleven-sheet template's structure, selected formula bindings and print setup. Use native spreadsheet checks for custom layouts; source coverage, calculations and visual quality still need inspection.

For a selected workbook revision, grow changed wrapped rows inside its retained
print panels without replacing widths, print settings, formulas or embedded
objects. From the installed `govtribe-proposal-workflows` root:

```bash
python3 scripts/prepare_proposal_workbook_render.py revised.xlsx --previous-workbook selected-original.xlsx --output revised-readable.xlsx
```

Keep the selected original unchanged. This mode sizes only changed wrapped text
in visible working sheets' existing print areas; unchanged text, hidden content
and cells outside those panels are left alone. Its sizes are estimates: inspect
the saved output's affected normal-print panels at readable scale and confirm
the final lines fit. A separately prepared fit-to-width preview does not verify
the retained layout. For custom layouts or unsupported rotated/vertically merged
text, use native row sizing and inspect the result. Reconcile calculations after
content edits; row sizing itself preserves existing formula caches.

## Annotated outline helper

For an optional machine-readable outline, `govtribe-proposal-workflows` retains `assets/annotated-proposal-outline-schema.json` and `scripts/validate_annotated_outline.py` at its installed root. That helper checks supplied JSON structure and mappings; use native document checks for the delivered file.
