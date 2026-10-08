---
name: full-company-analysis
description: Use for full public-company initiations, deep stock research, maximum-depth underwriting, or requests to follow the complete institutional analyst manual end to end.
---

# Full Company Analysis

Use this skill when the request matches the description above. Explicit user instructions determine scope and output format. Do not silently weaken source, calculation, falsification, or completion controls required by the loaded manual references.

## Mandatory references

- Modules: M001, M002, M003, M004, M005, M006, M007, M008, M009, M010, M011, M012, M013, M014, M015, M016, M017, M018, M019, M020, M021, M022, M023, M024, M025, M026, M027, M028, M029, M030, M031, M032, M033, M034, M035, M036, M037, M038, M039, M040, M041, M042, M043, M044, M045, M046, M047, M048, M049, M050, M051, M052, M053, M054, M055, M056, M057, M058, M059, M060, M061, M062, M063, M064, M065, M066, M067, M068, M069, M070, M071, M072, M073, M074, M075, M076, M077, M078, M079, M080, M081, M082, M083, M084, M085, M086, M087, M088, M089, M090, M091, M092, M093, M094, M095, M096, M097, M098, M099, M100, M101, M102, M103, M104, M105, M106
- Appendices: Appendix A, Appendix B, Appendix C, Appendix D, Appendix E, Appendix F, Appendix G, Appendix H, Appendix I, Appendix J, Appendix K, Appendix L, Appendix M
- Master Labs: Master Lab 01, Master Lab 02, Master Lab 03, Master Lab 04, Master Lab 05, Master Lab 06, Master Lab 07, Master Lab 08, Master Lab 09, Master Lab 10, Master Lab 11, Master Lab 12, Master Lab 13, Master Lab 14
- Operating rules: `references/operating-rules.md`

The bundled DOCX is the canonical methodology. The Markdown files in `references/` are retrieval-oriented mirrors generated from that source. If an extracted reference appears malformed or ambiguous, consult the canonical DOCX when available rather than inventing missing content.

## Full workflow

1. Read `references/operating-rules.md`, `references/universal/front-matter-and-universal-standards.md`, and `references/module-router.json` first.
2. Define the decision question, security scope, valuation date, research horizon, and materiality threshold.
3. Build the source log and assumption register before drawing material conclusions.
4. Execute the Master 12-Step Research Workflow from the manual in sequence. Use the exact module references for each step rather than substituting a summary.
5. Identify the primary sector playbook and any genuinely material secondary playbook. Read `references/universal/sector-playbooks-common-protocol.md` before sector modules.
6. Use the applicable appendices and Master Labs for model build, valuation, forensics, risk, memo construction, and review.
7. For arithmetic, valuation, scenario aggregation, price-volume bridges, and liquidity calculations, prefer `scripts/finance_engine.py` when its inputs match the required definitions. Keep sourced inputs and units visible.
8. Maintain a two-layer output: a concise decision layer and a full evidence layer. Use `assets/full-research-output-template.md` as the deliverable skeleton unless the user asks for another format.
9. Run all applicable module failure tests and completion tests. Then run Appendix M. Record open gates in the completion audit.
10. Do not label the research complete when any mandatory gate remains open. Return the completed work plus a clearly separated unresolved-items section if public evidence is unavailable.

## Evidence and output controls

- Distinguish reported facts, management claims, external estimates, analyst calculations, and analyst judgments.
- For current claims, verify freshness and state the as-of date.
- Cite material factual inputs to the actual source used.
- Recalculate important arithmetic rather than copying unexplained outputs.
- State unresolved questions and the strongest contrary case.
- Define specific falsification or thesis-break evidence for material conclusions.
- Do not execute securities transactions.

## V2 live-research and audit controls

For current-company work, read ../../references/v2/source-policy.md before research. Deep work must also use ../../references/v2/evidence-system.md, ../../references/v2/state-and-gates.md, and ../../references/v2/audit-protocol.md. Use the V2 schemas and deterministic scripts where applicable. Do not claim completion while a mandatory dependency, material contradiction, stale critical input, or unreconciled calculation remains open.
