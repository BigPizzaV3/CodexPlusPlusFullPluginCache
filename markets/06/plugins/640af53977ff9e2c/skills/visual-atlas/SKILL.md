---
name: visual-atlas
description: Open or export The Business Engineer complete interactive 3D Atlas, or take the user to a model, discipline, instrument, or guided path in it. Use for the existing visual library rather than creating a new strategic diagram.
---

# The visual Business Engineer Atlas

The plugin bundles `assets/Business-Engineer-Atlas.html`, the complete self-contained Atlas. The default Model library opens 3D; its 3D/List toggle shares the selected entry and filters. It contains the full 1,052-entry catalog, plus separate practice instruments and the earlier ontology.

The plugin root is two directories above this skill directory. Export with:

```sh
python3 <plugin-root>/scripts/library.py export atlas /absolute/output/Business-Engineer-Atlas.html
```

Use an actual writable artifact location selected by the host environment. The script refuses an existing output unless `--force` is supplied for an intended replacement. Follow the host's artifact-saving and delivery workflow. Do not link a cached skill directory as the user's output.

When requested, open the exported file using a supported user-facing artifact-opening capability. If that capability is absent, provide the file link without claiming it opened. No server, API key, or network request is required to run the exported Atlas.

For a particular model, resolve its exact ID with the library script, then use the returned `atlas_fragment`. Useful routes:

| Fragment | View |
| --- | --- |
| `#atlas` | Full 3D library |
| `#atlas?entry=BE-00-137` | Core model 137 in 3D |
| `#atlas?collection=core&part=II` | Core era models |
| `#atlas?collection=practice` | Practice instrument collection |
| `#atlas/library` | List view |
| `#atlas/map` | Discipline map |
| `#atlas/practice` | Operating instruments and engine |
| `#atlas/investigation?route=geopolitics` | Guided investigation |

If the artifact viewer cannot preserve fragments, provide the full Atlas and tell the user which model name to search. The lookup command uses `instruments`; the Atlas URL uses `practice`.

The package is a snapshot, not a live content-sync service. Saved investigations remain in the browser and origin that created them. The Atlas's Download investigation action preserves a portable analysis. Changes to the separate live site require an explicit site-editing task through the environment's site workflow.
