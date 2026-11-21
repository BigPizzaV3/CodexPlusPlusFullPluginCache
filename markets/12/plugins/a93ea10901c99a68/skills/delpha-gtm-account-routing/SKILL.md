---
name: delpha-gtm-account-routing
description: Use when a lead or company needs a GTM/CRM routing call — resolving its commercial parent and determining whether it should be treated as a new logo or routed under an existing account.
---

Use this skill when the user asks whether a company or lead is a new logo, an existing account, a subsidiary that should roll up to another account, or which parent/company should be used for GTM, CRM routing, territories, account ownership, or commercial hierarchy.

The user's explicit instructions take precedence over this skill.

## Goal

Use Delpha to resolve commercial identity, then turn the result into a concise GTM decision. Distinguish the commercial/GTM parent from a passive holding company, financial parent, legal operator, franchisee, or other entity that Delpha does not recommend for GTM routing.

## Workflow

1. Identify the company name and website from the user's request.
   - A website is required by `findAndValidateUltimateParent`.
   - If the website is missing and cannot be determined reliably from context, ask only for the website.
   - Use country when provided or when needed to disambiguate the entity.

2. Call `findAndValidateUltimateParent` with the company name, website, and country when relevant.

3. Use the returned `job_id` with `getUltimateParentResult`.
   - Do not create duplicate resolution jobs for the same request.
   - If `getUltimateParentResult` returns `status_code: 202`, wait before retrying; do not issue repeated rapid calls.

4. For sales, RevOps, GTM, territory, and CRM-routing questions:
   - Use `result.ultimate_parent` as the recommended commercial/GTM parent.
   - Use `result.relationship_type` as the relationship type.
   - Use `result.confidence` as the routing confidence.
   - If `result.ultimate_financial_parent` differs from `result.ultimate_parent`, treat that difference as meaningful. The financial parent is relevant for ownership/compliance; it does not replace the GTM parent for routing.
   - Use the ownership chain and `comment` only as supporting evidence. Do not replace Delpha's selected GTM parent with a different entity from the chain.

5. For a "new logo" decision:
   - A company is **not a distinct new logo** only when the user states, or an authorized CRM source confirms, that the resolved commercial/GTM parent already exists as an account/logo in the user's CRM.
   - If the resolved commercial/GTM parent is confirmed absent from the CRM, treat the lead as a new logo.
   - If CRM existence is unknown, do not guess. Resolve the commercial parent and state that the new-logo decision requires knowing whether that parent already exists in the CRM.

6. Confidence:
   - Display the Delpha confidence as a percentage when available, e.g. `0.95` → `95%`.
   - Treat `-1` as missing, not as low confidence.
   - If confidence is below `0.85`, make the uncertainty visible instead of presenting the routing decision as definitive.

## Output

For new-logo or GTM-routing questions, keep the complete answer concise, normally under 100 words.

Lead with the business decision. Then provide no more than these fields when available:

- **GTM decision:** New logo / Not a new logo / Cannot determine from CRM context
- **Commercial parent:** [Delpha `ultimate_parent`]
- **Relationship type:** [Delpha `relationship_type`]
- **Confidence:** [percentage]

Finish with one short routing sentence:

**Route:** [queried company] → **[commercial parent]**.

If a different financial/legal parent or operator is relevant, add one short sentence explaining the distinction. Do not narrate the full ownership chain unless the user asks for it.

## Preferred phrasing

When the commercial parent already exists in the CRM:

- **GTM decision: Not a new logo** — route under the existing [commercial parent] account.

When the commercial parent does not exist in the CRM:

- **GTM decision: New logo** — create or route as a new [commercial parent] account.

When CRM existence is unknown:

- **GTM decision: Cannot determine yet** — Delpha resolves the commercial parent as [commercial parent], but the new-logo decision depends on whether that account already exists in the CRM.

## Example

User:
`Starbucks Coffee Chile (starbucks.cl) is a new lead. We have Starbucks Corp in CRM. Is this a new logo?`

Desired response shape:

- **GTM decision: Not a new logo** — route under the existing Starbucks Corporation account.
- **Commercial parent:** Starbucks Corporation (US)
- **Relationship type:** Member Firm / Franchise
- **Confidence:** 95%

**Route:** Starbucks Coffee Chile → **Starbucks Corporation**. Alsea is the financial/legal operator, but not the recommended GTM parent.

## Guardrails

- Do not infer CRM account existence from public web data, brand familiarity, or the ownership chain.
- Do not use the absolute top legal/financial holding entity for GTM routing when Delpha returns a different `ultimate_parent`.
- Do not invent confidence, relationship type, CRM state, or ownership facts.
- For ownership/compliance/KYC questions rather than GTM routing, follow the financial/legal ownership information instead of applying the GTM-parent rule.
