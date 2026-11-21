---
name: ololand-dd-industrial-diligence
description: Use when the OloLand deal target is an industrial, manufacturing, distribution,
  logistics, or hard-goods business. Loads industrial-specific KPI discipline (gross-margin
  walk, working-capital cycle, capex intensity, customer/supplier concentration) and
  the verifier checklist for asset-heavy diligence.
---

# Industrial diligence

Industrial deals live or die on working capital, gross-margin durability, and capex intensity.

## Canonical KPIs

| KPI | Definition | Mistake to avoid |
|---|---|---|
| **Adjusted gross margin** | Revenue − COGS (materials + direct labor + freight-in + overhead), one-time/pricing items disclosed | Excluding freight or overhead absorption |
| **Inventory turns** | COGS ÷ avg inventory | Using sales in numerator |
| **DSO / DIO / DPO** | Days sales / inventory / payables outstanding | Quarter-end snapshot vs T-12 avg |
| **Cash conversion cycle** | DSO + DIO − DPO | Reported as positive when net negative is accurate |
| **Capex intensity** | Capex ÷ revenue | Reporting maintenance capex separately to deflate |
| **Maintenance vs growth capex** | Replacement vs new capacity | Sponsor classifies growth as maintenance |
| **OEE** | Availability × Performance × Quality | Plant-level avg masks bottleneck |

## Verifier checklist

- [ ] Gross-margin walk by SKU / product family (price, mix, volume, input cost, productivity quantified)
- [ ] BOM-level cost validation for top-20 SKUs reconciles to standard cost in GL
- [ ] PPV + material usage + labor variance trends
- [ ] Inventory quality (aged inventory E&O reserve adequacy, slow-mover analysis, costing methodology)
- [ ] Most recent physical count + shrinkage %
- [ ] Customer concentration (top-10 % of revenue, contract terms, single-point-of-failure)
- [ ] Supplier concentration (top-10 % of COGS, sole-sourced inputs, supplier financial health)
- [ ] Working-capital seasonality (24-month monthly view; peak-to-trough; RCF utilization)
- [ ] Open POs for capex + in-progress projects + deferred maintenance backlog
- [ ] Phase I/II ESA, RCRA, OSHA recordables, TRIR trend, EPA notices
- [ ] DB pension funded status; multi-employer withdrawal liability
- [ ] Union/CBA expirations within 24 months; prior strikes; wage escalation
- [ ] HTS codes for top imports → tariff (232/301/IEEPA) exposure

## Common red flags

- Gross-margin expansion attributed to "mix" with no SKU walk
- Standard cost not updated in > 12 months → favorable PPV that won't repeat
- Maintenance capex < 2% of revenue → deferred maintenance
- "One-time" add-backs > 15% of EBITDA recurring across years
- Top customer > 25% on month-to-month / evergreen
- Sole-sourced critical input (semi, specialty chem, OEM-spec) with no qualified alt
- Inventory turns declining while revenue grows → channel stuff or aged inventory
- Multi-employer pension funded < 80% → withdrawal liability is a real number

Pair forensic battery + working-capital normalization (T-12 avg, not month-end). CapEx figures MUST distinguish maintenance from growth; if undisclosed, mark "maintenance capex assumed = X% per industry benchmark."


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
