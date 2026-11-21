# Source status and conflict resolution

Review date: 2026-11-05. Use this file when sources conflict, a feature is absent, or a user asks about completeness. Article notes are original paraphrases with links, not a verbatim documentation archive.

## Contents

- Current feature changes
- Resolved document links
- Retired or unavailable material
- Source precedence
- Inventory boundaries

## Current feature changes

**Sales Assistant:** LinkedIn's current [next-steps notice](https://scommunity.linkedin.com/p/sales-assistant-next-steps) explicitly says the Sales Assistant beta is no longer available. The notice was read in full. Cached topic a461001 advertises 19 articles and older marketing/training pages still describe a beta. Do not recommend enabling that retired beta or use old setup instructions as current guidance. This is distinct from the Salesforce package's similarly named LinkedIn Sales Navigator Assistant admin app, which appears in current CRM setup documentation.

Historical Sales Assistant material described daily pre-screened leads, feedback, warm-introduction paths and Message Assist drafts. Cached learning-center descriptions mention product/service selection, an account list of at least five accounts and must-have/nice-to-have criteria. Historical hub text says enabling it enabled Lead IQ, Message Assist and messaging preferences. These are historical observations, not instructions for a presently available product. Sources: [former hub](https://scommunity.linkedin.com/p/sales-assistant), [setup course description](https://training.sales.linkedin.com/setting-up-your-sales-assistant). Course video content was not reviewed.

**Embedded Profiles:** Current dedicated guidance requires Advanced Plus, superseding older Advanced/Team/Enterprise wording. Do not infer full CRM Sync from a partner widget or installed app package.

**Security:** The 2016 EDI whitepaper's lack-of-SOC claim and old Safe Harbor/Privacy Shield references are historical. Modern embedded/Teams security articles point to current certifications and the [Trust Center](https://linkedin.safebase.us). The 2020 SSO guide's SHA1 default is historical, not a present security recommendation. Review exact current controls before configuration.

**Billing:** Current Admin Center guidance includes Sales Navigator. Older activation/illustrated guides excluded Sales during rollout. A default payment method applies future purchases; assigning a method to an existing contract is separate. Cancellation, restore-before-expiry and repurchase-after-expiry have different consequences.

**SCIM:** Identity-provider-controlled fields and license/group state must be updated in the IdP; local admin roles and supported local-only fields remain separate. Okta Push Now does not reconcile membership added manually in LinkedIn. Do not mistake provisioning for license activation.

**CRM schema and timing:** Sync cadence, quotas and write permissions differ by vendor and feature. Use current field tables and observed account state rather than a generic limit copied from an older PDF. Widget mapping storage is not the same as full CRM Sync's imported record storage.

## Resolved document links

| Original source | Verified destination or replacement |
| --- | --- |
| Classic/Lightning install launchers a104002, a106036 | Redirect to CRM hub a8037044; current admin guide a16260001 reviewed |
| Salesforce sync/security a107025, a108046; hidden fields a182193 | Redirect to a8037044; current setup, security a16429009, FAQ and troubleshooting reviewed |
| Embedded security a106017 | Redirect to a8037044; current embedded guide a16507013 reviewed |
| Sandbox guide link in a443840 | Full testing article a125962 reviewed |
| Dynamics installation a107070 | Microsoft Learn installation guide reviewed |
| Dynamics enablement/security a108047, a107057 | Current hub supplies complete sync, validation and security PDFs; text and substantive diagrams reviewed |
| HubSpot launcher a6214977 | Full enablement PDF and screenshots reviewed |
| SSO launcher a105136 | Full eight-page PDF and screenshots reviewed |
| EDI a149084 legacy attachment | Broken old attachment replaced by the same-titled PDF linked from a1450539; eleven pages and binding diagram reviewed |
| Admin Center PDF in a1466287/a1472036 | Full two-page guide and screenshots reviewed |
| Unavailable old transfer article a107026 | Current transfer options and transfer matrix, plus each supported source/destination route, reviewed |
| Unavailable feature article a440001 | Current overview a108023 and plan matrix a104003 reviewed |
| Unavailable renewal article a552279 | Current restore a1565162 and reactivate a548327 reviewed |

Confirmed numeric URL aliases are recorded in coverage.json. Do not count an alias as another unique article.

## Retired or unavailable material

The 19-article Sales Assistant topic is unavailable; only the cached topic titles/excerpts and selected historical material were recoverable. The retirement notice resolves present feature availability, but does not make unread former article bodies “read.”

The optional Custom Lists SCORM tip sheet returned HTTP 403. Its current workflows are covered by the fully read custom-list, sharing, notes, matching and outreach-activity help articles. Do not claim the SCORM lesson or videos were reviewed.

Some LinkedIn-hosted screenshots returned HTTP 403 even when their complete article text was available. Affected articles are enumerated in coverage.json and their notes. Full procedural text, tables and alternate current guides remain available; verify exact visual controls against the live account. PDF diagrams listed as reviewed in implementation-guides.md were actually rendered and inspected. Do not confuse alt text with viewing an image.

The Corporate Billing general landing index a444019 denied retrieval; relevant Sales Navigator billing dependencies were read individually. Topic inventory and shared billing coverage are not a claim to have read all Hiring, Ads or Learning documentation.

## Source precedence

1. Check the current account and current feature-specific official page.
2. Use current vendor setup/security guides for that CRM, IdP and package version.
3. Use current replacement pages reached through redirects.
4. Retain older releases/PDFs for context, with version/date caveats.
5. Treat cached snippets and inferred replacements as partial evidence, never full review.

Do not automatically equate a 404 with retirement. Sales Assistant retirement is supported by an explicit official notice; other broken URLs are recorded as unavailable with current task guidance, not asserted deleted.

## Inventory boundaries

The earlier deduplicated topic inventory contained 352 article IDs; every one remains represented. Final public topic reconciliation checked 36 accessible indexes with 356 unique linked article IDs and found zero missing article texts. This collection also includes independently discovered cross-references, all five articles in the reviewed SCIM topic and all six in the Teams topic, and shared identity/billing dependencies. source-index.txt gives the exact reviewed article count and mapping.

No current global Help Center export or authoritative fixed total was available. coverage.json therefore keeps the global exhaustive-review flag false. It separately records full text coverage of the enumerated baseline. Never replace this with a fabricated “100% of LinkedIn documentation” claim. Optional training videos, community discussions, release slide decks and unrelated LinkedIn product documentation are not part of the written-help article count.
