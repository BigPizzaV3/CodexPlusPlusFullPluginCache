# Read a solicitation package and build a compliance matrix

Goal: a requirements and compliance view built from the complete, controlling documents, with citations an evaluator-minded reviewer can check.

## Steps

1. Identify the opportunity and version. Open it with `g2x_get_record`. A file named "final" is not necessarily controlling; check notice, amendment and attachment context.
2. List what is on file. Call `g2x_opportunity_documents` with the opportunity id. Note each document's category, readiness and version, and keep its SAM.gov, G2X and parsed links.
3. Read whole documents. For each document that matters, call `g2x_opportunity_attachment_text` without `page`, and follow its cursor to the last byte. Verify the byte count and SHA-256 agree across chunks. Use `format: "json"` when tables, pages and structure matter. A single page read is for a citation check only.
4. Compare amendments. Read both versions. Report old then new for deadline, instructions, scope, quantities, evaluation criteria and requirements, with file, page and section citations. List any document or page you could not read.
5. Choose who analyzes. Default: extract requirements and build the matrix in this agent from the full text. Include instructions, evaluation factors and amendments, not only the statement of work. Mark each row with its citation and whether company evidence exists, is partial or is missing. Never mark a row compliant because it was extracted.
6. Or use G2X analysis, only when the user chooses it. Before starting, check completed runs and any run IDs already returned or saved with the selected record; an empty opportunity history does not invalidate a known extraction run. Confirm document preparation, extraction and qualification separately when they have not already been authorized. Use `g2x_prepare_opportunity_documents` only when preparation is needed, then `g2x_shred_opportunity` with the selected attachment IDs for requirements extraction. Keep its run ID and read the cited requirements with `g2x_get_analysis_run`; an extraction run is not a compliance matrix. For an authorized fit and compliance assessment, use `g2x_qualify_opportunity` against the selected company profile and read that same qualification run with `g2x_get_analysis_run`. Use `g2x_compliance_matrix` only with a completed qualification or supported compliance run ID, or a workspace that actually has a stored matrix. Never pass an extraction run ID to the matrix reader, and never start qualification merely to read extracted requirements.
7. Save where the user asked. A draft in chat, a saved workbook and a structured G2X result are different outcomes. Name the destination and verify by reading back.

## What to tell the user

Deliver the matrix or brief, the documents and versions it rests on, the gaps that could rule the company out, and the next decisions. Keep extracted requirements, fit assessment and response coverage separate. The bid decision stays with the user.
