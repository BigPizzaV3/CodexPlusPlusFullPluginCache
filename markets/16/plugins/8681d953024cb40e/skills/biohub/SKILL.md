---
name: biohub
description: Route Biohub requests to ESMC, ESMFold2, or the ESM Atlas on the Biohub MCP. Use for explicitly ESM or Biohub work, ESM mutation scoring, ESMFold2 folding, Atlas discovery, or showing a protein's 3D structure in the Biohub MCP's Mol* viewer. Also use when someone asks to design a protein binder, minibinder, or scFv, which this plugin declines. Do not use for unrelated non-ESM models, generic sequence alignment, or opening a local structure file in another viewer.
license: MIT
---

# Biohub router

The user's instructions take precedence over guidelines provided in a skill.
If explicit user instructions conflict with a skill's instructions, prioritize the user's instructions.

Use this as the implicit entry point. Identify the scientific goal, then load exactly the specialist it needs; ESMC, ESMFold2, and the Atlas are different things.
Every specialist answers through Biohub MCP tools, which need the user to be signed in to Biohub.

## Route

| User need | Specialist |
| --- | --- |
| Similar proteins, a protein name or accession, an Atlas record, clusters, SAE features of a protein, or bulk Atlas data | `$esm-atlas` |
| A protein's stored ESM Atlas structure, such as `Show me the ESM Atlas structure for P69905.` | `$esm-atlas` |
| Scores for named substitutions, or where a protein is constrained or tolerant | `$esmc` |
| To fold or see a protein, a complex, or a protein with DNA, RNA, or a ligand, such as `Could you display the 3D structure of GB1?` | `$esmfold2` |
| To see again a protein that `$esmc` analyzed in this conversation | `$esmc` |
| Installing the plugin, connecting the MCP, or signing in | `$biohub-setup` |

- For a protein name, let the specialist resolve it; never choose a chain, isoform, organism, or accession yourself first.
- A request that needs two specialists, such as a fold and then a mutation scan, loads both in order.

## Not offered

- Binder, minibinder, and scFv design: say plainly that this plugin does not offer it, name what it does cover, and stop. Hand it to no specialist.
- Folding with an MSA, modified residues, covalent bonds, or pocket constraints: the Biohub MCP does not take them. Say so and offer a plain fold with `$esmfold2`.
- Embeddings, raw logits, SAE activation extraction, fitted heads, or fine-tuning: the Biohub MCP does not return them. Point to the open ESMC weights, as `$esmc` describes.
- Other structure predictors, such as AlphaFold: this plugin does not run them. Answer a comparison question from what ESMFold2 returns, without claiming results for the other model.
- Private, offline, or data-resident sequences: the Biohub MCP sends sequences to Biohub. Say so before any call, and point to the open weights on Hugging Face for running on the user's own compute.

## Invariants

- Never ask for credentials in chat. Sign-in happens in the host's browser flow, as `$biohub-setup` describes.
- Folds and ESMC calls bill the user's Biohub account; the specialists say when to confirm first.
- The MCP writes no files, so every answer ends with a source line naming the tools called.
- Show structures only with the Biohub MCP viewer, as [Show a structure](../../references/show-a-structure.md) describes; never draw one yourself.
- Follow the shared [safety and provenance rules](../../references/safety-and-provenance.md).
