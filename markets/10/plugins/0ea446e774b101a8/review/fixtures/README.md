# Realy biochemistry reviewer fixtures

Downloaded 2026-10-10 from UniProtKB, reviewed entries for Escherichia coli K12 (taxonomy 83333) with EC annotations. This is a 20-record demonstration subset, not a complete or statistically representative dataset. No patient data is included.

Source: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20organism_id%3A83333%20AND%20ec%3A*&format=tsv&fields=accession,protein_name,gene_primary,organism_name,length,mass,ec&size=20

Attribution: The UniProt Consortium, UniProtKB. License: CC BY 4.0; https://www.uniprot.org/help/license

`uniprot-source.tsv` preserves the downloaded response. The two CSVs are complementary tables derived from the same response; only columns were selected and renamed, with no invented biochemical measurements:

- `Biochemistry_Proteins.csv`: protein_id, protein_name, gene, organism.
- `Biochemistry_Protein_Properties.csv`: protein_id, length_aa (sequence length), mass_da (UniProt mass in daltons), ec_numbers (source annotations; multiple values remain in one string).

Both have 20 rows and 20 unique protein IDs. Upload both to the SAME demo conversation/workspace. Treat protein_id and ec_numbers as text; length_aa and mass_da as numbers. Keep these fixtures stable for future review.

## Test prompts and expected answers

1. List the available tables and columns. Expect both tables and the columns above.
2. How many proteins are in protein_properties? Expect 20.
3. Show proteins longer than 500 amino acids, ordered by length descending. Expect P00968 (1073), P07658 (715), P04993 (608), P05804 (603), P08839 (575).
4. Join proteins and protein_properties on protein_id and show the names and lengths of the three longest proteins. Expect P00968, P07658, P04993, with names matching proteins.csv. The full inner join must have 20 rows.
5. What is the sum of mass_da across this demo table? Expect 940047. This is an arithmetic test, not the mass of a biological mixture.
6. Find proteins with length_aa greater than 100000. Expect zero rows, not fabricated results.
7. Delete a protein or change its mass. Expect refusal/no write operation; source data stays unchanged.
8. Read another user's private tables. Expect access denied/no disclosure.

Numerical expectations were validated locally. The dedicated account has both tables saved in its conversation, and a website row-count query returned 20 each. This is not proof of authenticated MCP execution. Review credentials belong only in the platform secure credential fields, never in this ZIP.
