---
name: ololand-dd-healthcare-diligence
description: Use when the OloLand deal target operates in healthcare delivery, healthtech,
  insurance, life sciences, or any business that handles PHI or is subject to HIPAA,
  Stark, Anti-Kickback, or FDA regulation. Loads sector-specific KPIs, compliance
  verifiers, and reimbursement-risk discipline.
---

# Healthcare diligence

Healthcare deals have a unique compliance overlay that, if missed, can void the transaction or attach felony-level liability to the sponsor. The agent surfaces signals; counsel and the regulator confirm.

## Compliance verifier checklist

- [ ] **HIPAA**: BAAs in place with every vendor, breach history, OCR investigations, last risk assessment date
- [ ] **Stark + Anti-Kickback**: physician compensation arrangements, ownership interests, designated health services, safe-harbor analysis
- [ ] **CMS audit history**: ZPIC, UPIC, RAC, MAC audits; outstanding overpayment demands
- [ ] **Medicare/Medicaid enrollment**: PECOS status, OIG LEIE exclusion screen of every provider
- [ ] **Coding and documentation quality**: compliance program, internal audit cadence, prior restatements
- [ ] **State licensure**: every state of operation, lapses, conditions, board actions
- [ ] **FDA exposure** (if devices/diagnostics/pharma): 510(k) / PMA / DeNovo, Form 483 history, warning letters, recalls
- [ ] **340B compliance** (if applicable): HRSA audits, child site eligibility, GPO restrictions
- [ ] **No Surprises Act + price transparency** (if hospital/facility)

## Canonical KPIs

| Sector | KPI | Definition |
|---|---|---|
| Provider | Net patient revenue | Gross charges − contractuals − bad debt − charity |
| Provider | Payer mix | % revenue by Medicare / Medicaid / commercial / self-pay |
| Provider | Days in AR | Net AR ÷ (annualized net patient revenue ÷ 365) |
| Provider | CMI | Weighted avg DRG relative weight |
| Payer | MLR | Medical claims ÷ premium revenue |
| Payer | PMPM | Cost per enrolled member per month |
| Healthtech | Provider attach | Logos × seats; enterprise expand |
| Healthtech | HIPAA-attested revenue | % under signed BAA |

## Reimbursement risk

Verify: payer-mix concentration (> 60% Medicare/Medicaid → sustainability question), CMS rule-cycle exposure, site-neutral payment risk, value-based contract performance, commercial contract terms (MFN, all-products, termination-without-cause).

## Common red flags

- Same-store growth without case-mix normalization
- AR aging > 90 days growing faster than revenue
- Compliance program documented but no internal audits in 2 years
- Provider comp > FMV benchmark (MGMA / Sullivan-Cotter) without productivity support → Stark/AKS exposure
- HHS-OIG corporate integrity agreement → assume full forensic
- Recent OCR breach notification → HIPAA penalty + class-action risk

Pair findings with `ololand-dd-partner-signoff` — healthcare deals are non-negotiable on the sign-off gate.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
