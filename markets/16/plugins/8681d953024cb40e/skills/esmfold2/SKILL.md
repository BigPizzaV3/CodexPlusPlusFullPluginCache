---
name: esmfold2
description: Use when the user wants to fold or see the predicted structure of a protein, several protein chains, or proteins with DNA, RNA, or small-molecule ligands with ESMFold2, wants structure confidence such as pTM, ipTM, or pLDDT, or asks how ESMFold2 compares with other structure predictors. Not for MSAs or modified residues, dynamics, binding affinity, experimental structures, or ESM Atlas lookup or stored Atlas structure views.
license: MIT
---

# ESMFold2

The user's instructions take precedence over guidelines provided in a skill.
If explicit user instructions conflict with a skill's instructions, prioritize the user's instructions.

The Biohub MCP needs the user to be signed in to Biohub for every tool, including the ESM Atlas lookups.
If the fold tools are not in the catalog, say the Biohub MCP is not connected or the user is not signed in, and point to `$biohub-setup`; if that skill is not installed, tell the user to add the Biohub MCP at `https://biohub.ai/mcp` to their client, which signs them in to Biohub. If a tool returns an authentication error, say the user is not signed in to Biohub.

## Choose the tool

| The user wants | Call |
| --- | --- |
| To see a structure: one protein, a complex, or a protein with DNA, RNA, or a ligand | `ui_show_structure` |
| Confidence scores without a view, such as comparing several designs | `esmfold2_fold_complex` |
| The most accurate prediction, and can wait minutes to hours | `esmfold2_fold_max_accuracy` |
| The result of a fold that returned `queued` | `biohub_get_inference_run` with its `run_id` |

- `ui_show_structure` folds and shows in one call, and returns pTM and ipTM. Do not also call `esmfold2_fold_complex` for the same input; that bills a second fold.
- `esmfold2_fold_complex` uses the fast model by default. Pass `model_id: esmfold2-2026-05`, the larger model at the same price, for difficult complexes or when the user asks for it.
- `esmfold2_fold_max_accuracy` costs more, always queues, and is limited to a few runs a day. Confirm before calling it unless the user asked for maximum accuracy.

## Build the input

- Give one entity per molecule, in order: `protein`, `dna`, or `rna` with a `sequence`, or `ligand` with one `ccd` code or one `smiles` string.
- For identical chains, set `copies` on one entity in `ui_show_structure`, such as 2 for a homodimer; the fold tools take no `copies`, so repeat the entity there. Give each DNA strand as its own entity. Never concatenate chains.
- For a protein name or accession, get the sequence first with `esm_atlas_search_uniprot` or `esm_atlas_lookup_accession`.
- Use the user's own sequences. If an input is missing, ask for it instead of substituting a familiar example.
- `GB1` means the B1 domain of streptococcal protein G, PDB 1PGA chain A, 56 residues: `MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE`. Use it directly; a UniProt search returns the full-length protein instead.
- The tools take no MSA, modified residues, covalent bonds, or pocket constraints. Say so when the user asks for one, and do not approximate it by dropping or changing parts of the input.

## Cost and retries

- A `ui_show_structure` call with one protein entity is free. A call with more than one entity, and every `esmfold2_fold_complex` or `esmfold2_fold_max_accuracy` call, bills the user's Biohub account.
- Report the credit usage the tool returns; otherwise state that the tool did not report usage or cost, and never invent an estimate.
- Before folding more than one input in a request, such as comparing designs, say how many folds that is and ask a plain yes/no question.
- Each call starts new work and bills again. After a timeout or an unclear error, do not repeat the fold; if the call returned a `run_id`, read it with `biohub_get_inference_run`.
- A `queued` fold is normal. Give the user its `run_id`, read it again later, and do not call it in a tight loop.

## When a tool fails

Branch on the returned `code`, not on the message text.
- `rate_limited`: wait as the error advises, then retry once.
- `indeterminate`: the outcome is unknown; never retry. Read the `run_id` with `biohub_get_inference_run` if one was returned.
- `sequence_too_long_to_fold`: `ui_show_structure` has no stored Atlas structure for this protein and it is too long for the free on-demand fold. State the limit and the returned `actual_length`, and offer `esmfold2_fold_complex`, which bills, or a shorter domain; never clip the sequence.
- `restricted`: a safety restriction; do not work around it.
- A call the host blocks, for example by denying approval, is a failure, not a missing connection.
- For any other code, name the tool and the code, and never retry with different arguments.

## Interpret the result

- Scores are on a 0-to-1 scale. pTM is confidence in the overall fold, ipTM (interface pTM) is confidence in the contacts between chains, and pLDDT is per-residue confidence.
- A high pTM with a low ipTM means each part is confident alone but the contact is not.
- The result is a static computational prediction, not dynamics, binding affinity, or an experimental structure. Low confidence, disorder, interfaces, and ligands need extra caution and experimental validation.
- Report every returned warning. Never let a high score override a warning.

## Present the result

- After a successful fold the user asked to see, lead with the view rather than a description of what you are about to do.
- A single protein in `ui_show_structure` is the stored ESM Atlas structure when one exists, or the server's own prediction. Label it that way, and do not report its scores as an ESMFold2 prediction. When the user needs ESMFold2 confidence for one protein, call `esmfold2_fold_complex` instead of the view.
- Leave `include_png` unset for a plain request to see a structure; `preview_status: not_requested` is not a failure. Set `include_png: true` only when the answer depends on the structure's shape, or the client cannot render MCP Apps. Without an image, do not describe how the structure looks, and never draw or render a structure yourself.
- The MCP returns no PDB or mmCIF file. If the user needs coordinates, say so and point to the Biohub API at https://docs.biohub.ai.
- For private, offline, or unpublished sequences, say that the MCP sends sequences to Biohub, and point to the open `biohub/ESMFold2` weights on Hugging Face for running on the user's own compute.

Follow [Show a structure](../../references/show-a-structure.md) for entities, highlights, and viewer failures.

When the user asks to see a protein that `$esmc` analyzed in this conversation, do not fold it: `$esmc` shows it again with its highlights.

End the answer with one source line naming each tool called, the model, and any `run_id`, then one link, after the science: <https://biohub.ai/models/esmfold2>.

Follow the shared [biosafety and acceptable-use rules](../../references/safety-and-provenance.md#biosafety-and-acceptable-use); never work around a restricted input.
