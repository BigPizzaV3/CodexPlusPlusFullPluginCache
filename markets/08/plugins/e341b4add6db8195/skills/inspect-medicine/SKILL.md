---
name: inspect-medicine
description: Read and explain current TTMNG foreign medicine evidence across all 243 selected families, with exact products, source citations, original conditions and recorded research through the authenticated project service.
---

Use the current project tools, beginning with `ttmng_reference_catalog` kind=medicine and its page cursor. It covers all 243 selected families, with exact required targets and separately labelled supporting products. Select the exact reference_id/presentation_id from the catalog. Preserve ingredient/salt/strength basis, form, route, jurisdiction and identifier. Do not transfer a source to another formulation or use a Thai product as a current foreign target.

Read `ttmng_reference_answer` and follow next_offset when the requested scope needs further pages. Use `ttmng_evidence_record` for exact record_ids and `ttmng_evidence_batch` for bounded groups of independent reads. For an actual evidence question, use `ttmng_evidence_question` with the exact selection and relevant topic. Inspect the returned facts, original conditions, citations and recorded research before proposing any new search. Request only an indispensable unresolved product/context choice; no extra source, name, chemistry, release or repeated clinical approvals.

Lead with what the sources support and cite their exact dated versions. Preserve population, route, dose/formulation, renal/study/withdrawal limits, negative results, source conflicts and missing fields. A source-labelled regimen is reference evidence, not a patient-specific prescription or dose-adjustment instruction. Do not infer latest whole-PI coverage, current market stock, interchangeability, co-use safety or an unrecorded pathway from a family completion count.

When the existing evidence answers the question, use it without repeating research. For a real remaining gap, inspect recorded search scope/outcomes first and use available host primary-source tools if appropriate. The remote reader itself performs no new searches or canonical writes; state tool/access limits and do not claim new results were saved or reviewed. Historical ALTACE/LUPIN context retains its own conditions and never substitutes for the required TRIATEC France target.

All data calls require server-side approved access. Provisioned OpenAI reviewers have permanent account entitlement; ordinary users require owner approval. Never request passwords in chat, trust caller role flags, read private authoring files or invoke legacy 1.2 tools. `ttmng_reference_status` reports this release's actual counts/date and disabled legacy data dispatch.
