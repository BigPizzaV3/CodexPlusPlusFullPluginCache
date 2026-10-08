---
name: box-legal-workflows-ocg
description: "Review outside counsel guidelines, billing guidelines, and outside counsel requirements in Box. Use to compare an OCG with a firm playbook, identify cited obligations or variances, recommend responsible teams, draft an issue register, or add one cited Box comment per issue."
---

# OCG review in Box

Use the `box` skill for authentication and operations. For mechanics, use `box/references/ai-and-retrieval.md` and `box/references/collaboration.md` as relevant.

## Assessment basis

- **Playbook comparison:** Use an applicable firm playbook, approved position, or review standard as the baseline. Report a variance only when a cited OCG term differs from a cited firm control, position, threshold, or process. If the playbook is silent, label the item **uncovered requirement**.
- **OCG-only operational assessment:** Use after the user confirms that no playbook will be used. An explicit statement such as “we do not have a playbook” is already confirmation—proceed without asking again. Identify obligations, ambiguities, internal conflicts, approvals, deadlines, and likely process effects; do not claim firm-policy deviation or noncompliance.

Choose the basis before issue analysis. If the user supplied a playbook, use it. If they explicitly said none exists or should be used, proceed OCG-only. Otherwise ask them to identify the applicable playbook; do not silently assume either basis.

## Workflow

1. Resolve the intended OCG and record its Box file ID and version. Apply the assessment-basis rule above, and record the baseline file ID and version when a playbook is used.
2. Review every section, subsection, schedule, and appendix. Maintain an internal ledger with section, locator, requirements, assessment basis, status, and issue IDs. Return a compact coverage summary unless the user asks for the full ledger.
3. If any material is unreadable, truncated, unsupported, or otherwise unrepresented, identify the gap and continue with the assessable sections without claiming complete review.
4. For each issue, cite the OCG and the playbook when applicable. Separate source facts, supported impact, model inference, and attorney decisions.
5. Recommend the team with the first concrete action. Use a firm ownership map when available; otherwise use the fallback below. Treat routing as a recommendation, not a binding assignment.
6. If the user asked only for review or drafting, return the issue preview and do not post comments. If they explicitly asked to add comments, create one self-contained comment per independent issue without another confirmation round, then verify and retain the comment IDs. Clarify only when write-back intent is ambiguous.
7. Report the assessment basis, source versions, coverage gaps, issue and written-comment counts, recommended teams, unresolved attorney decisions, relevant Box IDs, and failures. If a source changes during review, state that the result applies to the recorded version.

## Issue taxonomy and citations

Use the narrowest applicable label: **playbook variance**, **process change**, **approval or exception**, **deadline or reporting duty**, **ambiguity**, **internal conflict**, **uncovered requirement**, or **attorney decision**.

Split independent requirements when their impacts, owners, or resolutions differ. Keep related text together when separating it would make the issue misleading.

Prefer section or subsection number and heading, then a verified page, numbered paragraph or line, then a short identifying excerpt. Cite the original files rather than an AI answer and never invent locators.

## Fallback owner routing

- Rates, budgets, invoices, time-entry, e-billing: **Billing Operations**; support from Matter Team or Finance
- Staffing, matter plans, status reports: **Matter Team**; support from Legal Operations
- Engagement terms, conflicts, ethics, privilege: **Responsible Attorney**; support from Ethics or General Counsel
- Security, breach notice, access controls: **Information Security**; support from Privacy or Matter Team
- Personal data, transfers, privacy retention: **Privacy**; support from Information Security or Records
- Records, destruction, holds, file return: **Records Management**; support from Matter Team or Privacy
- Diversity or supplier reporting: **Legal Operations**; support from HR/DEI or Matter Team
- Taxes, payment terms, currency, expenses: **Finance**; support from Billing Operations
- Insurance: **Risk Management**; support from Finance or Responsible Attorney
- Publicity or client-name use: **Marketing/Communications**; support from Responsible Attorney
- Portals and technical onboarding: **IT**; support from Information Security or Legal Operations
- Client-owned business terms or obligations: **Client Legal/Business Team**; support from Matter Team

Use a firm-provided map instead. Add a supporting team only when needed. Never infer a person's identity; keep the team label when identity is ambiguous, and do not claim a plain comment creates a targeted mention or notification.

## Issue preview and comment format

For each issue include a stable ID, citation, requirement, variance or concern, concrete impact, suggested resolution, recommended owner, and any attorney decision.

Before commenting, check the file's audience. Do not expose confidential playbook text or privileged internal analysis in a comment visible to client or external collaborators; put detailed comparison in a restricted internal artifact when necessary.

Use this shape and shorten it to the current tool limit without dropping its required elements:

```text
Citation: [verified OCG locator; playbook locator only when appropriate for the audience]
Risk/impact: [supported consequence; label inference or attorney judgment]
Suggested resolution: [practical option and any required approval]
Recommended owner: [team label]
```

## Legal boundary

Describe concrete operational or legal-review impact, but do not provide final legal advice, approve a deviation, set a binding risk rating, or make a binding assignment.
