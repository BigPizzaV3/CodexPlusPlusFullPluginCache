---
name: source-hierarchy
description: "Use when citing evidence for any material claim about a deal \u2014\
  \ ranks evidence sources by quality so the strongest available document is the one\
  \ cited. Required for institutional-grade DD."
---

# Source Hierarchy

Use the strongest available evidence for every material claim.

Priority order:

1. **CPA-audited financial statements** — audited 10-K, 10-Q, audited stand-alone financials with an unqualified opinion. Highest authority.
2. **Tax returns and bank/source-system exports** — Forms 1120 / 1065, signed bank statements, raw accounting system extracts (GL trial balance, AR/AP aging). Direct from the source system, not management's representation of it.
3. **Management models and CIMs** — sell-side CIM, target management's operating model, board decks. High utility, but the management lens biases presentation. Treat as management view, not independent.
4. **Third-party market data** — IBISWorld, S&P Capital IQ, PitchBook, sell-side research. Useful for context but not deal-specific.
5. **AI-extracted summaries** — anything OloLand's risk/financial extraction pipeline produced from upstream documents. Always derivative — trace back to the underlying source for any material claim.

## When sources conflict

Surface the conflict and prefer the higher-ranked source. Examples:
- 10-K reports $304.7M revenue (rank 1), management deck says $312M (rank 3) → cite both, lead with the 10-K, flag the $7.3M delta as a reconciliation item.
- Tax return shows a related-party transaction that the management model omitted → call out the omission; tax is higher rank than the model.

## When the highest-available source is degraded

State the degradation explicitly. Examples:
- Auditor issued a going-concern qualification or material weakness disclosure → the audited statement is still rank 1, but lower confidence; surface the qualification before quoting any number from it.
- Tax return is from a different fiscal year than the 10-K → flag the temporal mismatch.

## Output discipline

Never cite at a lower rank when a higher rank is available. If you cite an AI extraction (rank 5) when the same fact is in the 10-K (rank 1), the answer fails the verifier-stack standard.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
