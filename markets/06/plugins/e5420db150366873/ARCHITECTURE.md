# Architecture

## Design goals

1. Preserve every source procedure and reference.
2. Use progressive disclosure so a narrow question does not load hundreds of pages.
3. Keep full-company research capable of loading the entire corpus.
4. Make calculations deterministic where practical.
5. Make completion status auditable rather than rhetorical.
6. Preserve version history and provenance.

## Runtime layers

### Layer 1: Canonical manual
The original DOCX is the binary authority. Raw-block JSONL enables text-level diffs. Markdown mirrors support model retrieval.

### Layer 2: Skill routing
Fifteen skills represent distinct user goals and success criteria. Each Skill contains only the manual material relevant to its workflow, except full-company-analysis which contains the entire corpus.

### Layer 3: Deterministic computation
`finance_engine.py` supplies reusable DCF, WACC, reverse-growth, ROIC, FCFF, working-capital, accrual, price-volume-mix, dilution, scenario, and liquidity calculations. The language model still must source and normalize the inputs.

### Layer 4: Research state and gates
JSON Schemas formalize source logs, assumptions, model changes, decision journals, risks, and completion gates. Mandatory gates that fail remain open.

### Layer 5: Deliverables
Deep work uses the two-layer model from the manual: concise decision layer plus full evidence layer.

## V2 MCP boundary

A future MCP server should provide controlled current-data tools, not duplicate methodology. Candidate read-only tools include SEC filing retrieval, XBRL/company facts, ownership forms, market snapshots, historical prices, yield curves, macro series, regulator datasets, and sector datasets. Calculation logic should remain deterministic and source-aware.
