# Show a structure with the Biohub MCP

Every Biohub skill shows structures with one Biohub MCP tool, `ui_show_structure`.
Hosts that render MCP Apps show an interactive Mol* viewer the user can rotate, recolor, and select residues in.
The tool writes no files and creates no link.
Match the tool name in the connected catalog, because a host can add a server prefix.

## Call it

- Pass `entities`, one per molecule, in order: `protein`, `dna`, or `rna` with a `sequence`, or `ligand` with one `ccd` code or one `smiles` string.
  Chains are labelled A, B, C, ... in that order. For identical chains, set `copies` on one entity, such as 2 for a homodimer, and never concatenate chains.
- One protein entity is free. It shows the stored ESM Atlas structure, or the server's own prediction for up to 700 residues.
  A longer protein with no stored structure returns `sequence_too_long_to_fold`: state the limit with the returned `actual_length` and ask for a domain of at most 700 residues. Never clip the sequence, and never retry it.
- Anything else is a new ESMFold2 fold billed to the user's Biohub account, so call it once per request.
  Showing the same complex again folds and bills again.
  Report the credit usage the tool returns; otherwise say it did not report usage or cost, and never invent an estimate. A planning-only or no-network request means no call.
- Pass `view_options` only for what the answer needs: `representation` (`cartoon` or `surface`), `color_by` (`chain` or `confidence`), and up to 32 `highlights`.

## Highlight residues

- A highlight takes `chain_id`, `author_residue_number`, `expected_residue`, and an optional `color`.
- `author_residue_number` is the residue's one-based position in the sequence passed for that chain.
  Convert other numbering, such as PDB author numbering or a zero-based index, to that position first.
- Set `expected_residue` to the residue's three-letter code, such as `TRP`.
  If the call returns `invalid_input` because a highlighted residue does not match, correct the numbering once; never remove `expected_residue`.
- When an analysis singles out more than 32 residues, highlight the 32 it ranks highest and say how many it left out.
- The viewer draws chain A in blue, so use `#D55E00`, `#009E73`, and `#CC79A7`, in that order, unless a skill names other colors.

## Read the result

- The result lists each entity's chain IDs, the view's pTM and ipTM, and any warnings. Report every warning.
- A single protein shows the stored ESM Atlas structure or the server's own prediction. Label it that way, do not report its scores as an ESMFold2 prediction, and use the Atlas link.
- The result has no image unless `include_png` is true, and `preview_status: not_requested` is not a failure.
  Set `include_png: true` only when the answer depends on the structure's shape, or the client cannot render MCP Apps.
- Without an image, do not describe how the structure looks. Never draw, render, or write viewer code for a structure yourself, and never show other coordinates, such as an experimental PDB entry, in its place.
- Every structure is a computational prediction, not an experimental structure. When the user asks for an experimental method, resolution, or citation, say the view does not provide one.

## When it fails

- If the tool is not in the catalog, say the Biohub MCP is not connected or the user is not signed in, and point to `$biohub-setup`.
- A call the host blocks, for example by denying approval, is a failure, not a missing connection.
- On `rate_limited`, wait as the error advises before one retry. On `indeterminate`, never retry. For any other code, name the tool and the code.
- A failed view never changes the result of the analysis it was showing.

## Point back to the source

End the answer with one source line naming each tool called, the model, and any `run_id`, then one link to what produced the result, after the science:

- ESMC results: <https://biohub.ai/models/esmc>
- ESMFold2 results: <https://biohub.ai/models/esmfold2>
- Atlas results: <https://biohub.ai/esm/protein/atlas>

When one answer spans models, use the link for the model behind the main result. Do not stack the links, and do not turn the line into marketing.
