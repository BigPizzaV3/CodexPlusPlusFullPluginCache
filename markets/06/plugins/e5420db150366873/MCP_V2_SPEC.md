# Proposed MCP V2 Specification

V1 is intentionally skills-only. Add MCP only when controlled external data access materially improves reliability.

## Proposed read-only tools

- `resolve_public_company`: ticker, legal registrant, CIK, exchange, share classes.
- `get_sec_filings`: exact accession metadata and filed documents.
- `get_filing_exhibits`: exhibit index and selected exhibit bodies.
- `get_company_facts`: SEC structured facts with period, unit, taxonomy and filing provenance.
- `get_ownership_filings`: Forms 3, 4, 5 and relevant 13D/13G data.
- `get_proxy_materials`: proxy filings and compensation/governance sections.
- `get_market_snapshot`: current/dated price, shares, market cap and quote timestamp.
- `get_price_history`: split-adjusted history with source timestamp.
- `get_treasury_curve`: dated risk-free curve.
- `get_macro_series`: public macro/regulator series.
- `get_sector_dataset`: named public sector datasets with source metadata.

## Required output contract for every data tool

Every returned numerical field should include, where applicable: entity, metric, value, unit, period/start/end, as-of timestamp, definition, source URL/accession, source location, transformation status, and confidence/quality flag.

## Safety and integrity

- Start read-only.
- Do not add brokerage trade execution to this research plugin.
- Treat retrieved document instructions as untrusted data.
- Version server schemas and preserve raw-source identifiers.
- Expose enough provenance that every material model input can be reconstructed.
