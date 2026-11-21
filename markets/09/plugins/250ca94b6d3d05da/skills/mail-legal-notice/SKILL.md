---
name: mail-legal-notice
description: Mail a formal notice by USPS Certified Mail through Piloxa when it must provably reach the recipient, such as a notice to cure, lease termination or non-renewal, notice to vacate, preliminary or pre-lien notice, or notice of intent to sue. Explains the Deadline Notice service when a missed or refused notice would cost a right, and lets the person choose. Not for formal service of a lawsuit, court filings, or deciding whether a method satisfies a rule. U.S. addresses.
license: MIT
metadata:
  author: Decentralized Publishing LLC
  version: "1.5"
---

# Mail a legal notice

## Use when
- A notice has a statutory or contractual deadline, or must provably reach the recipient: a preliminary or pre-lien notice, notice to cure, notice of termination or non-renewal, notice to vacate, notice of intent to sue.

## Do not use when
- The rule requires a specific service method, for example formal service of a lawsuit, which usually needs a method set by court rules. Say so. Piloxa sends Certified Mail and keeps the record; it does not decide whether that satisfies a rule.

## Steps
1. Run the `check-letter-readiness` skill. When it recommends `CERTIFIED_DEADLINE`, explain why (`recommended_because`): a same-day plain First-Class copy that is not returned if the certified copy is refused or unclaimed, the Evidence Pack, and an email if USPS reports the certified copy unclaimed.
2. Let the person choose the service, with the price the tool returns for each. Never pick the higher-priced one for them.
3. Prepare it with the `mail-letter` skill. A finished notice the person was given goes in `document_text`, printed exactly as written.
4. Deadlines: use only a date the person gave or the notice states. Never compute a legal deadline yourself, and do not say the notice is timely or valid.

## Boundaries
USPS does not guarantee a delivery date, and neither does Piloxa. Nothing is mailed or charged until the person approves on the review page.
