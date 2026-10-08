# The Business Engineer plugin

A Codex plugin that combines The Business Engineer's analytical method, complete mental-models library, and interactive 3D Atlas.

## What it does

| Capability | Use it for |
| --- | --- |
| Business analysis | Apply selected models to a company, strategy, market, operating model, or concrete decision; test the thesis and derive a faithful visual brief. |
| Mental models | Retrieve exact definitions, applications, source context, instruments, typed connections, and guided decision paths. |
| Visual Atlas | Open or export the full 3D explorer; switch between 3D and List with the same selection and filters. |

Try these prompts after installation:

- “Use The Business Engineer to analyze where this business captures value and what could erode its moat.”
- “Find the models for evaluating cost per accepted outcome, then show their assumptions and connections.”
- “Open the complete Business Engineer 3D Atlas.”
- “Compare core:137 with concept:137 and preserve their different meanings.”

## Included knowledge

The consolidated catalog contains **1,052 entries**, including **261 core models** across 25 categories and 791 entries across thirteen disciplines. The source index distinguishes 811 model entries from 241 apparatus items. The package also contains 15 complete practice instruments, 12 guided paths, the analytical engine, quality checklist, shared-spine references, 258 overlapping earlier concepts, and 50 preserved canonical redirects.

The earlier JSON-LD and Turtle files describe the 258-concept ontology. Their scope is labeled explicitly. They are not presented as a separate expansion of the 1,052-entry catalog.

The plugin retrieves a few relevant records at a time. It does not put the full library into every prompt. Its local search is lexical; the assistant uses the retrieved definitions and case evidence for judgment.

## Installation and availability

The plugin manifest is `.codex-plugin/plugin.json`. The three bundled skills are in `skills/`. It is packaged for Codex plugin loading, not as a Replit application plugin or browser extension.

The creator has registered the plugin in the local personal marketplace. In a Codex environment using that marketplace, open the plugin's card and install it. If using the Codex CLI, the corresponding command is:

```sh
codex plugin add the-business-engineer@personal
```

For another machine, copy the complete `the-business-engineer` folder into that machine's plugin workflow and register it in its personal marketplace. The package intentionally contains no absolute machine path or replacement marketplace file. It does not replace another machine's existing plugins. Use that environment's Plugin Creator workflow to register the folder and then install it.

The creation environment did not expose a Codex CLI or a native custom-plugin installation operation, so package validation and local marketplace registration do not establish installation in the current chat. Plugin skills are picked up in a new conversation after installation.

## Local commands

Python 3 runs the retrieval helper using only the standard library:

```sh
python3 scripts/library.py search "bottleneck" --collection core --limit 6
python3 scripts/library.py get core:137 instrument:J
python3 scripts/library.py links BE-00-137
python3 scripts/library.py routes
python3 scripts/library.py export atlas /absolute/output/Business-Engineer-Atlas.html
```

All commands except `export` are read-only. The package makes no external calls and requires no API keys. Current company or market research is performed by the assistant through the host's available research tools. User accounts, email, private conversations, external data sources, and live Atlas updates are not connected by this package.

## Verification and maintenance

`python3 scripts/verify_content.py` checks source fidelity, exact IDs and redirects, retrieval pagination, all guided paths, typed connections, CLI errors, and an exact self-contained Atlas export. Plugin and skill manifests are validated with the creator's bundled validators.

The knowledge and Atlas are snapshots of the completed library and Atlas edition. Future source changes require updating the package data and asset together; they do not synchronize automatically. Browser-stored investigations remain on the browser and origin where they were created.

Source text and methodology: **The Business Engineer · Gennaro Cuofano**. Packaging does not grant a new license to redistribute the source library.
