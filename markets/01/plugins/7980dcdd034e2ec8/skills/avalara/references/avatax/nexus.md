# AvaTax: nexus and where you report tax

Navigation: Settings > Where you report tax. Older material and some screens say "Where
you collect tax", which is the same area. Requires administrator access; a Viewer sees it read-only.

Confirm the company selector before changing anything.

## Traps

- **Nexus changes are not retroactive.** Tax calculates against the tax date, while
  reports present transactions by document date. Sales entered before a nexus change was
  saved keep their original zero-tax result and later surface as no-nexus exemptions in
  reports. Identify earlier sales that may need recalculation, then obtain authorization
  for the specific records and tax changes. Changing nexus alone does not authorize
  recalculation or prove that previous transactions were wrong.
- **Missing nexus produces zero tax rather than an error.** A nexus gap looks identical to
  a legitimate exemption in transaction data. When investigating "why was no tax
  charged," check nexus and the tax date before concluding anything about certificates.
- **Nexus is a legal determination.** Economic thresholds are an input to a decision the
  user or their tax professional makes. Never add or remove a jurisdiction because sales
  data crossed a number, and never present a threshold as establishing an obligation.
- **Some jurisdictions need a sub-choice.** Local jurisdictions and tax type (sales versus
  seller use) may each require selection. Getting the state right and the sub-choice
  wrong produces confidently incorrect tax.
- **Nexus changes have filing consequences.** Adding a jurisdiction may create an
  expectation of returns. Show the visible filing impact before finalizing, and see
  [filing](../returns/filing.md) for what happens downstream.

## Diagnosing "no tax was charged"

Work in this order, because the cheap checks rule out the expensive ones:

1. Is nexus active for that jurisdiction, and does the transaction's tax date fall inside
   the active start and end dates?
2. Was it calculated before a nexus change? If so, check whether recalculation under the
   intended effective dates is needed rather than changing the configuration again.
3. Only then look at customer exemption and certificates. See [certificates](../ecm/certificates.md).

Report which step produced the answer. "No nexus" and "valid exemption" produce the same
zero, and the user's remediation is completely different.
