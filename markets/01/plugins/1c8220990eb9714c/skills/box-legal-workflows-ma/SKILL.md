---
name: box-legal-workflows-ma
description: "Build and operate M&A deal rooms in Box: design a transaction-specific due-diligence structure, populate and classify documents, manage scoped access, audit sharing, and answer cited cross-document diligence questions. Use for M&A, VDRs, deal rooms, transaction due diligence, mergers, or acquisitions."
---

# M&A deal rooms in Box

Use the `box` skill for authentication and operations. For mechanics, use `box/references/bulk-operations.md`, `box/references/content-workflows.md`, `box/references/collaboration.md`, `box/references/mcp-search.md`, and `box/references/ai-and-retrieval.md` as relevant.

## Workflow

1. Distinguish a request to plan or analyze from a request to build or modify the room. Use the firm's approved deal-room template when available. Otherwise analyze the transaction prompt, propose a practical numbered folder tree, and confirm it before creating folders.
2. Classify source documents from names and metadata, using content analysis when those are insufficient. Then add, move, or copy them according to the intended record model. Preserve originals when classification is uncertain, and record both IDs when a copy is intentional.
3. Apply internal access at the narrowest useful folder level: deal leads and legal teams may need broader editing access, while finance and other specialists receive their functional subset. MCP cannot grant Co-owner; use Editor or direct the user to a supported Box UI/path.
4. Scope diligence to the request. For a targeted question, use folder-scoped search and then report the analyzed file IDs, versions, and cited findings. For a room-wide review, inventory the expected file IDs and versions and report exclusions, unreadable files, or failures; do not claim complete-room coverage unless that inventory was assessed. Use standard structured extraction when extracting terms.
5. After presenting diligence findings, ask whether the user wants extracted terms or summaries persisted to the firm's metadata schema if the request did not already decide that.
6. Keep a manifest for build and access work: relevant folder IDs, source file IDs and versions, collaboration IDs with audience/scope/role, and unresolved failures.
7. Share externally only at the end of the workflow. Audit the target and relevant ancestors first, then apply the specified audience, folder scope, role or link settings, and expiration and verify the result. Ask only for missing consequential choices; do not claim a complete audit when collaboration listing has partial failures.

## Folder and diligence examples

Derive the tree from the transaction type, requested workstreams, source documents, and user roles. Number folders for stable ordering, but do not create generic categories that the deal does not need.

Example for a software-company acquisition:

```text
Project Cedar VDR/
├── 01 - Corporate & Governance/
├── 02 - Financial & Tax/
├── 03 - Material Contracts/
├── 04 - Employment & Benefits/
├── 05 - Intellectual Property & Technology/
└── 06 - Regulatory & Compliance/
```

Return each diligence finding with the question, assessed file scope, cited finding, coverage gap, and attorney decision needed.

```text
Question: Which contracts require change-of-control consent?
Scope: 42 files in 03 - Material Contracts; 2 unreadable
Finding: Three agreements contain consent language [file and section citations]
Coverage gap: Two unreadable files remain unassessed
Decision needed: Attorney interpretation of whether each clause is triggered
```

## Boundaries

- Folder access covers current and future descendants; do not grant root access when a curated subset is sufficient.
- External counsel receives an appropriate working area, auditors the relevant financial subset, and a prospective buyer a curated subset rather than root access by default.
- Initial collaboration creation does not set expiration. When expiration is required and supported by enterprise policy, update the returned collaboration ID afterward.
- Deal risk, materiality, privilege, and term interpretation remain attorney decisions. The model may identify facts, differences, and preliminary issues under documented criteria.
- Keep the manifest and verification results as the audit trail.
