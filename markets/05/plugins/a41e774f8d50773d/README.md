# Biohub ESM plugin

This plugin turns natural protein questions into the scientifically appropriate ESM workflow:

- Biohub managed API for public ESMC inference, including bounded concurrent calls, and interactive ESMFold2 inference
- the public Biohub MCP for ESM Atlas discovery and structure views, with the plugin script and anonymous S3 for the feature catalog, batch jobs, and bulk data
- Modal for bulk or long-running folds
- pinned Hugging Face weights on user-owned compute for private, offline, data-resident, customized, fine-tuned, or sustained workloads

The plugin declares the public Biohub MCP server in `.mcp.json`.
The `esm-atlas` skill uses it for Atlas discovery, and every skill can use its `ui_show_protein_structure` tool to show a protein's 3D structure.
The small standard-library client under `scripts/` handles deterministic routing, validation, readiness checks, the remaining Atlas HTTP routes, durable Modal job state, result presentation, and provenance.
Managed HTTP stays lightweight; managed ESMC mutation scoring, `esmc-landscape`, and `managed-post --output-dir` serialization of a real ESMFold2 response lazily require and verify the exact pinned `esm==3.4.1.post1` wheel.

- A supported unmodified protein sequence is shown first with the Biohub MCP's `ui_show_protein_structure`, labeled as the server's coordinates rather than the exact prediction.
- Complexes, modified residues, ligands, DNA/RNA, structures outside the MCP input limits, and requests for the exact prediction file use the separately installed OpenAI Molecular Structure Viewer.
- A missing MCP connection, error, or unavailable preview is reported without switching viewers.
- Successful folds emit `presentation-request.json`, which binds the verified artifact and retained `openIntentId` for the OpenAI Molecular Structure Viewer.
- When that viewer is unavailable for an unsupported structure or exact prediction file, the agent may generate and display a rendering image of the verified coordinates as a last resort.
- Supported sequence requests and MCP operational failures continue using the MCP app without a custom replacement viewer.
- See the [handoff reference](references/structure-viewer-handoff.md) for the full contract.

## Marketplace starter experiences

The plugin page highlights one visual, outcome-rich workflow from each official Biohub tutorial:

- `Map the mutational landscape of PETase and show me where it is most constrained or tolerant.`
- `Show me what ESMC has learned about ATP synthase and map the strongest features onto its structure.`
- `Model how a modified GLP-1 peptide with a lipid linker might engage GLP-1R, then show me the complex.`

The machine-readable [`examples/tutorial-use-cases.json`](examples/tutorial-use-cases.json) is the source of truth for those visible defaults and the broader prompt gallery. It binds each natural question to the pinned official [mutation-scoring](https://github.com/Biohub/esm/blob/main/cookbook/tutorials/esmc_mutation_scoring.ipynb), [SAE interpretation](https://github.com/Biohub/esm/blob/main/cookbook/tutorials/esmc_sae_feature_interpretation.ipynb), or [ESMFold2](https://github.com/Biohub/esm/blob/main/cookbook/tutorials/esmfold2.ipynb) workflow, plus exact hidden inputs, scientific invariants, and automatic presentation.

The PETase card invokes the shipped `esmc-landscape --tutorial petase` command. That command validates the pinned sequence, makes all 259 managed logits calls through a bounded 16-worker pool, and writes raw-response, JSON, CSV, and provenance artifacts before returning the constrained and tolerant positions.

## Reproducible GB1 regression experiences

The original focused-skill starters remain available as compact, exactly executable regression workflows:

- `What might W43F do to GB1?`
- `Show me what GB1 looks like.`
- `Find proteins similar to GB1.`

The packaged [`examples/starter-examples.json`](examples/starter-examples.json) contract resolves `GB1` to the pinned RCSB 1PGA chain-A sequence and owns the exact input, route, request, output, and presentation details. Users do not need to paste an amino-acid sequence or specify internal artifact names to get a traceable result. The fold request is separately materialized at [`examples/gb1-esmfold2-fast-fold-request.json`](examples/gb1-esmfold2-fast-fold-request.json). Validate the contract and every prompt surface with:

Selecting a starter runs it. Status-only preflight goes first, and when managed access is missing the plugin hands back the API-key page rather than a plan. Managed Biohub inference at tutorial scale, including every ESMFold2 tutorial fold, then runs without a separate confirmation. Managed requests may incur cost. Report provider-returned credit or token usage when available; otherwise state that the API did not report usage or cost, and never invent an estimate. Modal, self-hosted GPU campaigns, and bulk transfers still show the exact route, request scope, artifact plan, and cost ceiling and ask a plain yes/no question first. Small public Atlas API reads need no confirmation either, but every route still respects an explicit planning-only or no-network request. Before a bulk anonymous-S3 transfer, freeze the exact source prefix, destination, estimated bytes, storage and egress impact, and cost ceiling, then obtain separate explicit current-turn confirmation. Automatic SVG or Structure Viewer presentation happens only after successful checksummed artifact creation.

The script's Atlas protein-record lookup is non-folding by default. On-demand folding requires an explicit opt-in and a guarded preliminary lookup that returns the actual stored sequence, verifies its MD5 binding and supported alphabet, and proves it is no longer than 699 residues. Missing sequence evidence, length-only metadata, a hash mismatch, an unsupported residue, or an over-limit sequence stops before a fold request.

```bash
python3 plugins/biohub-esm/scripts/validate_starter_examples.py
```

## Additional tutorial-informed use cases

The official Biohub notebooks also inform a broader prompt gallery. The three exact marketplace prompts above are curated tutorial launchers: the plugin discloses the pinned tutorial target or construct, route, and request count, then runs the managed workflow and leads with the result. Other prompts that use a bundled tutorial literal say so explicitly; prompts that say “my” retain the user's supplied input and never substitute tutorial data:

- `Reproduce the official Biohub PETase ESMC mutation-landscape tutorial example.`
- `Reproduce the official Biohub ATP synthase SAE feature-interpretation tutorial example.`
- `Reproduce the official Biohub RNase H1 RNA-DNA hybrid ESMFold2 tutorial example.`
- `Using my supplied ubiquitin A3M, follow the official Biohub ESMFold2 tutorial example and show the structure and confidence.`
- `Reproduce the official Biohub modified GLP-1 peptide with lipid linker ESMFold2 tutorial example.`
- `Using my supplied paired antibody-antigen A3Ms, follow the official Biohub ESMFold2 tutorial example.`

The machine-readable [`examples/tutorial-use-cases.json`](examples/tutorial-use-cases.json) maps those prompts and their shorter tutorial-shaped aliases to the pinned official [mutation-scoring](https://github.com/Biohub/esm/blob/main/cookbook/tutorials/esmc_mutation_scoring.ipynb), [SAE interpretation](https://github.com/Biohub/esm/blob/main/cookbook/tutorials/esmc_sae_feature_interpretation.ipynb), and [ESMFold2](https://github.com/Biohub/esm/blob/main/cookbook/tutorials/esmfold2.ipynb) workflows. It records plugin-specific corrections, compatibility rules, route/call-count boundaries, exact target-disclosure rules, and which routes run directly versus which ask before spending.
## Local validation

Run these commands from the repository root, which is the marketplace directory.
The development harness and contract tests live under `plugins/biohub-esm/tests/` and travel with the complete plugin source.
The source-owned runtime builder excludes the development harness, its own development-only helper, ignored Python bytecode, Ruff and test caches, and untracked files.
Tests remain tracked in the repository but are not included in runtime packages.

```bash
PYTHONPATH=plugins/biohub-esm python3 -m unittest discover -s plugins/biohub-esm/tests -p 'test_*.py' -v
python3 plugins/biohub-esm/scripts/validate_starter_examples.py
python3 plugins/biohub-esm/scripts/biohub_esm.py preflight
.venv/bin/python plugins/biohub-esm/scripts/biohub_esm.py preflight --endpoint fold_all_atom
python3 plugins/biohub-esm/scripts/build_runtime_package.py \
  /absolute/new/path/biohub-esm \
  --commit HEAD
```

Development-only live-smoke details live in `tests/README.md`. Installed copies remain self-contained and do not rely on the development-only test directory.

The upstream OpenAI repository owns the maintainer release workflow.
This mirror keeps the checked-in runtime builder separately from the installed plugin.

The complete plugin component inventory is recorded in [`references/component-contract-audit.md`](references/component-contract-audit.md). The managed and Atlas endpoint matrix, coverage boundaries, and known discrepancies inside the published references are in [`references/api-contract-audit.md`](references/api-contract-audit.md).
