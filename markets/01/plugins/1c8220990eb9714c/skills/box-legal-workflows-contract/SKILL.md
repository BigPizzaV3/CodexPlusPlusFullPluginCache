---
name: box-legal-workflows-contract
description: "Review contracts in Box, compare them with an approved template or playbook, identify candidate differences for attorney review under firm-supplied criteria, create cited variance reports, and scan for renewals or expirations. Use for individual contract review, NDAs, MSAs, contract metadata, or variance analysis."
---

# Contract review in Box

Use the `box` skill for authentication and operations. For mechanics, use `box/references/mcp-search.md`, `box/references/ai-and-retrieval.md`, `box/references/content-workflows.md`, and `box/references/collaboration.md` as relevant.

## Review

1. Resolve the contract and the applicable template, playbook, or jurisdictional addendum. Record each Box file ID and version; ask only when multiple plausible baselines remain.
2. Compare the contract and baseline together. Identify added, missing, and changed provisions and cite both sources. Report unreadable, truncated, or unrepresented sections instead of claiming complete comparison.
3. Extract factual fields with standard structured extraction. Use enhanced extraction only when the user explicitly requests it.
4. Apply documented firm criteria as preliminary analysis, then create and upload a cited variance report that separates source facts, analysis, and attorney decisions. Verify and record its Box ID.
5. After presenting the analysis, ask whether the user wants metadata written if the request did not already decide that. If yes, inspect the firm's current template first; when none exists, ask whether to propose fields or create a template before continuing.
6. Post a routing comment or add attorney access only when requested. Check the file's audience first; keep privileged analysis and internal playbook text in a restricted artifact when the source has broader collaborators. A plain Box comment does not guarantee a targeted mention or notification.



## Variance report

Create one entry per independent difference with: issue, contract position and citation, baseline position and citation, factual difference, preliminary impact under documented criteria, and the attorney or firm decision still needed. If the baseline is silent, label the item **uncovered** or **attorney review**, not a variance.

Example:

```text
Issue: Limitation-of-liability cap
Contract: Section 12.2 — cap is three times fees paid
Baseline: Playbook Section 4.1 — approved position is fees paid
Difference: Contract cap is three times the approved position
Preliminary impact: Outside the documented fallback
Decision needed: Attorney approval or counterproposal
```



## Metadata and date scans

- **Extracted facts:** parties, contract type, effective and expiration dates, renewal language, notice period, value, and governing law.
- **Firm decisions:** status conventions, risk rating, review disposition, and next action.
- **Operational state:** reviewed version, review date, next review date, and alert history.

Treat these as examples and use the live firm schema. Parameterize metadata searches through `query_params` for new contracts, expiration windows, counterparty, or approved ratings.

When requested, run an expiration or renewal scan and report contracts requiring action. Persistent monitoring requires an explicit cadence, state store, and idempotency key; track the alert date or window and reviewed version rather than a permanent yes/no flag.

## Boundaries

- Risk, materiality, favorability, and approval of a deviation are firm or attorney decisions. When approved criteria are absent, report factual differences and unresolved questions rather than assigning a rating.
- Write only approved ratings into final-decision fields, and keep source versions, citations, report IDs, and any write failures in the audit trail. If a source changes during review, state that the result applies to the recorded version.

