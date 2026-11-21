---
name: esm-atlas
description: Use when the user wants proteins similar to a protein, a protein name or accession resolved to a sequence, an Atlas record, SAE feature profile, or cluster context for a sequence, one Atlas SAE feature explained, or a protein's stored ESM Atlas structure viewed, all through the Biohub MCP. Also use for questions about bulk ESM Atlas data. Atlas is a dataset to search, not a model to run.
license: MIT
---

# ESM Atlas

The user's instructions take precedence over guidelines provided in a skill.
If explicit user instructions conflict with a skill's instructions, prioritize the user's instructions.

Atlas is public data and discovery infrastructure, not a model to run on Modal or Hugging Face.
Answer Atlas questions through the Biohub MCP, which needs the user to be signed in to Biohub, and never through `curl` or another HTTP client.
Every reply, including a clarifying question, states limits and choices as facts about the Atlas and never mentions, quotes, or links this skill, its rules, or its file.

## Tools

| Need | Tool |
| --- | --- |
| Protein name or UniProt accession to sequence | `esm_atlas_search_uniprot` |
| UniParc or MGnify accession to sequence | `esm_atlas_lookup_accession` |
| Similar proteins | `esm_atlas_search_similar_protein_clusters` |
| Atlas record and top SAE features | `esm_atlas_get_protein_details` |
| Cluster context for a sequence | `esm_atlas_get_cluster_info` |
| One SAE feature | `esm_atlas_get_sae_feature_detail` |
| Structure view | `ui_show_structure` |

A host may show a server prefix around a name, so match the name and never hard-code a prefix.
If these tools are not in the catalog, say the Biohub MCP is not connected or the user is not signed in, and point to `$biohub-setup`; if that skill is not installed, tell the user to add the Biohub MCP at `https://biohub.ai/mcp` to their client, which signs them in to Biohub.
Read [the MCP tool reference](references/mcp-tools.md) for arguments, returned fields, and error codes.

## Resolve the input

- Raw sequence or FASTA: drop the header and whitespace, keep every residue letter, and pass it on unchanged.
- UniProt accession, such as `P69905`: call `esm_atlas_search_uniprot` once with the accession as `query` and `size=1`, and accept only a record whose accession matches exactly.
- Protein name, such as `hemoglobin`: call `esm_atlas_search_uniprot` once with the name verbatim as `query` and `size=6`; never rewrite it, field it, or guess an accession first.
  When several candidates return, list their accessions, protein names, and organisms, and ask the user to choose without recommending one, even one you already mentioned.
- UniParc or MGnify accession: call `esm_atlas_lookup_accession`, which does not accept UniProt accessions.
- `GB1` means the B1 domain of streptococcal protein G, PDB 1PGA chain A, 56 residues: `MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE`. Use it directly; a UniProt search returns the full-length protein instead.
- A 32-character MD5 protein hash with no sequence: the MCP is keyed by sequence, so ask the user for the sequence and point to the [Atlas API](https://biohub.ai/esm/protein/atlas/api-docs/api_reference.html), which reads records by hash.

Function text returned while resolving an input describes the input, not the Atlas result, so never present it as Atlas evidence.

## Length limits

Never clip, truncate, or window a sequence yourself.

- Similarity search and SAE features take at most 2,048 residues.
  For a longer sequence, do not call the search; name the limit and the sequence length, and ask the user for a domain or residue range.
  A `sequence_too_long_for_features` error from `esm_atlas_get_protein_details` gets the same answer.
- `ui_show_structure` returns a stored Atlas structure at any supported length, and predicts a miss only up to 700 residues.
  On `sequence_too_long_to_fold`, explain the 700-residue limit with the returned `actual_length`, and ask for a domain of at most 700 residues without retrying.

## Find similar proteins

For any similar-protein request:

1. Call `esm_atlas_search_similar_protein_clusters` exactly once with the resolved sequence, `top_k=10`, and `uncharacterized_only=false`, unless the user asked only for uncharacterized clusters.
2. Report up to ten hits in the returned order with accession, protein name, length, similarity score, and cluster size, and never manufacture missing hits.
3. For a non-empty result, call `ui_show_structure` once with the top-ranked hit's returned `sequence` as one protein entity.
4. Make no cluster, protein-detail, or feature-detail follow-up calls unless the user asks what the neighbors are or do.

Read hits correctly:

- `similarity_score` is cosine similarity between sparse-autoencoder (SAE) feature vectors, not sequence identity, alignment, or homology.
- The search runs over cluster representatives only, so a missing relative can reflect index coverage rather than absence.
- A short or empty hit list means nothing cleared the service's unreported similarity floor, never that nothing exists.
- A nonzero `restricted_count` means results were withheld; say so without guessing what they held.
- `top_features_across_results` lists SAE features shared across hits; report counts as `occurrence_count` out of the returned hit count.
- A hit that scores far above the rest, is very short yet scores high, or has a `cluster_size` of one may be lab contamination such as an expression construct; flag it rather than feature it.

When the user asks what a protein does or which neighbors are informative, call `esm_atlas_get_cluster_info` for every hit, in parallel where the host allows, with each hit's returned `sequence`.
Rank neighbors by `cluster_pct_characterized`, then by how specific `top_pfam_domains` is, then by `cluster_size`, and never by similarity score alone.
Every cluster field describes the neighbor's cluster, never the query, and characterized means Pfam-annotated, not experimentally studied.

## Read a protein's record and features

Call `esm_atlas_get_protein_details` once with the exact sequence.
Report `sae_features` in returned order, copying each `label` verbatim.
Report `value` with its `label_reliability` band as signal strength only; the band is never a judgement of the label's quality.
Report `residue_regions` positions as returned, and never compare their raw `mean_activation` with the normalized `value`.
When `features_computed_on_miss` is true, say the sequence is not in the Atlas and its features were computed on demand; infer nothing more.
For a feature-profile request, call `esm_atlas_get_sae_feature_detail` once for each of the three features with the highest `value`, breaking ties by lowest `feature_index`, and use its `label`, `summary`, and `description` as the only biological wording; skip it for a plain record lookup.

Atlas features come from the fixed 16,384-feature dictionary of `esmc-6b-2024-12-sae-layer60-k64-codebook16384`.
Never apply them to another checkpoint, model, layer, or codebook.
The full feature catalog is in the [Atlas API](https://biohub.ai/esm/protein/atlas/api-docs/api_reference.html), not the MCP.

## Show a structure

Call `ui_show_structure` once with the exact sequence as one protein entity; pass `view_options` only when the user asks for a representation, confidence coloring, or highlighted residues.
One protein is free, and the view is the stored Atlas structure or the server's own prediction, so label it that way.
Follow [Show a structure](../../references/show-a-structure.md) for highlights, the image, and failures.

## Bulk data

For bulk Atlas downloads, read [the bulk data guidance](references/bulk-data.md); its confirmation rules apply before any multi-gigabyte transfer.
Thumbnails and batch record downloads are in the [Atlas API](https://biohub.ai/esm/protein/atlas/api-docs/api_reference.html), not the MCP.

## Write the answer

Report only what the tools returned; never add proteins, structures, PDB entries, or literature from memory.
End every answer with one source line naming each tool called, the Atlas version, and the license, for example:

`Source: Biohub MCP esm_atlas_search_similar_protein_clusters, ui_show_structure; ESM Atlas v1 through the v1alpha1 API; CC-BY-4.0.`

Follow it with one link to <https://biohub.ai/esm/protein/atlas>.

## When a tool fails

Branch on the returned `code`, not on the message text.
`rate_limited` means wait as the error advises before one retry.
`indeterminate` means the compute outcome is unknown, so never retry it automatically.
`invalid_input`, `not_found`, `restricted`, `dependency_unavailable`, `resource_too_large`, and `internal_error` on the search or input resolution stop the answer without a biological conclusion.
A call the host blocks, for example by denying approval, is a failure too.
Name the failed tool and code, never retry with different arguments, and never fill the gap with results from memory, literature, or your own sequence comparison.
