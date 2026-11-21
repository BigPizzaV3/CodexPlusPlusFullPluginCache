---
name: esmc
description: Use when the user wants ESMC to score named substitutions such as W43F, or to find where a protein is most constrained or tolerant to mutation, or wants to see an analyzed protein's highlighted residues again. Sequence only; not for folding, Atlas lookup, or measured fitness. Embeddings, raw logits, SAE activation extraction, and fine-tuning need the open weights.
license: MIT
---

# ESMC

The user's instructions take precedence over guidelines provided in a skill.
If explicit user instructions conflict with a skill's instructions, prioritize the user's instructions.

ESMC is a sequence-only masked protein language model, and it runs on the Biohub MCP.
Every tool needs the user to be signed in to Biohub.
If the tools are not in the catalog, say the Biohub MCP is not connected or the user is not signed in, and point to `$biohub-setup`; if that skill is not installed, tell the user to add the Biohub MCP at `https://biohub.ai/mcp` to their client, which signs them in to Biohub.

## Choose the tool

| The user wants | Call |
| --- | --- |
| Scores for substitutions they named, such as W43F or a list from a paper | `esmc_score_mutations` |
| Where a protein is most constrained or tolerant, with no substitutions named | `esmc_scan_mutation_tolerance` |
| To see the analyzed protein with the singled-out residues | `ui_show_structure` |

- Use each tool's default model unless the user names one of `esmc-300m-2024-12`, `esmc-600m-2024-12`, or `esmc-6b-2024-12`.
- Pass one protein chain of one-letter codes. Do not pass structures, DNA, RNA, or ligands, and never clip a long sequence; the tool refuses what it cannot score and suggests a window.
- For a protein name or accession, get the sequence first with `esm_atlas_search_uniprot` or `esm_atlas_lookup_accession`.
- Use the user's own sequence. If it is missing, ask for it instead of substituting a familiar example.
- `GB1` means the B1 domain of streptococcal protein G, PDB 1PGA chain A, 56 residues: `MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE`. Use it directly; a UniProt search returns the full-length protein instead.
- Positions are 1-based, and each substitution names the wild-type residue it expects; the tool checks it. If it does not match, say so and ask which numbering the user meant.

The MCP does not return embeddings, hidden states, raw logits, or SAE activations, and it cannot fit or fine-tune heads.
For those, point to the open `biohub/ESMC-300M`, `biohub/ESMC-600M`, and `biohub/ESMC-6B` weights on Hugging Face and the [ESMC model page](https://biohub.ai/models/esmc).
For "what has ESMC learned about this protein", hand off to `$esm-atlas`, whose protein record lists the top SAE features of a sequence.
For private, offline, or unpublished sequences, say that the MCP sends sequences to Biohub, and point to the same open weights.

## Cost and retries

- Every call bills the user's Biohub account: one ESMC call per scored or scanned position.
- Report the credit usage the tool returns; otherwise state that the tool did not report usage or cost, and never invent an estimate.
- Before scoring or scanning more than one protein in a request, say how many calls that is and ask a plain yes/no question.
- Each call starts new work and bills again. After a timeout or an unclear error, do not repeat it.
- A scan can return partial results at its time limit or on a rate limit; report which positions it did not scan and offer to scan only those.

## When a tool fails

Branch on the returned `code`, not on the message text.
- `rate_limited`: wait as the error advises, then retry once.
- `indeterminate`: the outcome is unknown, and it may have billed; never retry.
- `invalid_input`: say what the tool rejected, such as a wild-type mismatch or too many positions, and ask the user how to proceed.
- `restricted`: a safety restriction; do not work around it.
- A call the host blocks, for example by denying approval, is a failure, not a missing connection.
- For any other code, name the tool and the code, and never retry with different arguments.

## Interpret the result

- A substitution's score is `ln P(substituted) - ln P(wild type)` with that position masked. Positive means ESMC finds the new residue more likely there.
- Each substitution is scored alone on the wild-type sequence, not as part of a combined variant.
- A scan ranks positions by entropy in bits over ESMC's full output vocabulary by default, where low means constrained, or by the share of the 19 other amino acids that score below the wild type. Name the metric you report.
- Low entropy or a negative score can suggest constraint, but neither is measured fitness, stability, activity, or binding. Do not compare raw scores across models without calibration.

## Show residues on the structure

After an analysis of one protein that singles out residues, call `ui_show_structure` once with the exact analyzed sequence as one protein entity, which is free:

- Tolerance scan: highlight the most constrained positions in `#D55E00` and the most tolerant in `#009E73`.
- Named substitutions: highlight the mutated residues when the user asks where they sit.

Highlight each residue on chain `A` by its 1-based position in the analyzed sequence, with `expected_residue` set to its wild-type three-letter code.
The highlights show where the model score is, not a measured effect.
The view is the stored Atlas structure or the server's own prediction of that sequence, not an experimental structure, so say that.
When the user asks to see the structure again, call the view again with the same sequence and highlights; do not fold the protein with ESMFold2 and do not rerun the scoring.
A failed view never changes the analysis, and never permits drawing a structure yourself.
Follow [Show a structure](../../references/show-a-structure.md) for highlights, the image, and failures.

## Write the answer

Lead with the science:

1. The result: the scores or the constrained and tolerant positions, and the structure view when there is one. Never ask permission to show a result.
2. Two or three sentences a scientist can react to: which positions or regions are constrained, which are tolerant, what stands out.
3. One line of scientific status: this is a model hypothesis, not an experimental measurement, and it needs validation.
4. One source line naming each tool called, the model, and the credits billed, then one link: <https://biohub.ai/models/esmc>.

Do not open with a plan or a list of the calls you intend to make. If the user asks for a dry run or a planning-only answer, describe the plan and say plainly that no tool was called.
Follow the shared [biosafety and acceptable-use rules](../../references/safety-and-provenance.md#biosafety-and-acceptable-use).
