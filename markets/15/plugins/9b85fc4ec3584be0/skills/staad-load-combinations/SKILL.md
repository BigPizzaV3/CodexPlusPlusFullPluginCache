---
name: staad-load-combinations
description: Use for generating standard STAAD.Pro load combination syntax for Indian Standards (IS 800:2007 steel, IS 456:2000 concrete) from primary load case definitions, with automatic case detection (DL, LL, WL, EQ, CR) and limit-state factor generation.
---

# STAAD Load Combinations

Use the registered StructEngine MCP tool `generate_staad_load_combinations` as the calculation and syntax authority for generating STAAD.Pro load combination blocks.

## When to Use

Use this skill whenever a user:
- Requests STAAD load combinations according to Indian design codes (IS 800:2007 for steel or IS 456:2000 for concrete).
- Pastes primary load cases (e.g. `LOAD 1 DEAD LOAD`, `LOAD 2 LIVE LOAD`, `LOAD 3 WIND +X`, `LOAD 4 SEISMIC +X`) and asks to create combination load cases.
- Asks for Serviceability (SLS) and Ultimate / Strength (ULS) combinations formatted for the STAAD.Pro input file editor.
- Inquires about partial safety factors for load combinations per IS 800:2007 Table 4 or IS 456:2000 Table 18.

## Input & Execution Guidelines

1. **Tool Invocation**: Call `generate_staad_load_combinations` with `load_cases_text` containing the user's primary load case definitions.
2. **Design Code Selection**:
   - Default to `code="IS800_2007"` for steel structures, PEB buildings, warehouses, towers, and industrial structures.
   - Use `code="IS456_2000"` when the user explicitly requests reinforced concrete (RCC) or IS 456 combinations.
3. **Combination Types & Numbering**:
   - By default, both SLS (`include_sls=True`) and ULS (`include_uls=True`) combinations are generated.
   - Default starting ID numbers: SLS starts at `1000`, ULS starts at `2000`. If the user specifies custom starting IDs (e.g., 101 and 201), set `sls_start_id` and `uls_start_id` accordingly.
4. **Manual Overrides**:
   - If a load case title is ambiguous or the user specifies a particular category (e.g., "treat Case 4 as Crane Live Load"), pass `manual_overrides={"4": "CRL"}`.
5. **No Hallucinated Syntax**:
   - Do not manually construct STAAD combination lines with guessed load factors. Always rely on the deterministic output returned by the `generate_staad_load_combinations` tool.

## Presentation Guidelines

1. **Structured Breakdown**: Present the total count of generated combinations with the breakdown between Serviceability (SLS) and Strength (ULS).
2. **Primary Case Mapping**: Show a markdown table of recognized primary load cases, their detected categories (DL, LL, WL, EQ, CR, etc.), and detection confidence.
3. **Executable STAAD Block**: Format the generated STAAD syntax in a clean fenced code block (` ```staad `) so the engineer can directly copy and paste it into the STAAD.Pro editor.
4. **Engineering Verification**: State clearly that partial safety factors and combination rules follow the specified standard (e.g., IS 800:2007 Table 4), and advise the engineer to verify load factors against specific project design criteria and local code amendments before running analysis.
