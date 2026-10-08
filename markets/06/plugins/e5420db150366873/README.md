# Institutional Public Equity Analyst Plugin

Version 1.0.0. Skills-only portable Agent Plugin.

This package converts the supplied **God-Level Public Company Financial Analyst Job Guide, Version 3.0** into a structured plugin without replacing the source manual with a summary.

## Preservation model

The package includes three layers of the source manual:

1. `canonical/God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx` - the untouched authoritative DOCX.
2. `canonical/manual-raw-blocks.jsonl` - exact paragraph text plus table-cell text in document order for integrity and diffing.
3. Retrieval-oriented Markdown mirrors split into 106 modules, 13 appendices, 14 Master Labs, universal front matter, and the sector common protocol.

If any Markdown conversion is ambiguous, the DOCX remains authoritative.

## Plugin architecture

- Root `plugin.json` uses the portable Agent Plugins schema.
- `skills/` contains 15 focused workflows.
- Each Skill carries its own relevant references so it does not depend on fragile cross-skill relative paths.
- Full-company analysis carries the complete corpus, deterministic scripts, schemas, and output template.
- V1 intentionally has no MCP server. Current facts are obtained through tools available to the host. A remote financial-data MCP can be added later without changing the methodology.

## Skills

- `full-company-analysis`: Run complete institutional public-company underwriting.
- `filings-primary-sources`: Retrieve and reconcile filings and primary evidence.
- `accounting-analysis`: Reconstruct statements and advanced accounting economics.
- `forensic-accounting`: Test earnings quality, accruals, non-GAAP and manipulation risk.
- `business-quality`: Deconstruct unit economics, pricing power and reinvestment.
- `industry-competition`: Map industry structure, TAM, moats, peers and disruption.
- `management-governance`: Assess management execution, incentives and capital allocation.
- `financial-modeling`: Build auditable driver-based integrated financial models.
- `valuation`: Run DCF, relative, reverse DCF, SOTP and scenario valuation.
- `earnings-events`: Analyze earnings, guidance and corporate events.
- `alternative-data`: Design and validate compliant channel and alternative-data work.
- `risk-decision`: Quantify downside, liquidity, thesis breaks and decision errors.
- `research-communication`: Write investment memos and defend research under review.
- `sector-analysis`: Apply one of 36 sector-specific analyst playbooks.
- `analyst-training`: Train and certify analysts using the manual mastery system.

## Local validation

From this plugin root:

```bash
python developer-tools/integrity_check.py
python -m pytest developer-tools/tests
```

The integrity check validates the canonical DOCX hash, module/appendix/lab counts, Skill presence, and manifested file hashes.

## Marketplace preparation

See `marketplace/MARKETPLACE_SUBMISSION.md` and `marketplace/PUBLISHER_TODOS.md`.

Current OpenAI plugin packaging documentation uses a root `plugin.json`, a root `skills/` directory, and optional MCP/resources. Skill metadata can be supplied in `agents/openai.yaml`. Marketplace submission currently requires listing details, verified publisher identity, starter prompts, positive and negative tests, availability, and release notes.
