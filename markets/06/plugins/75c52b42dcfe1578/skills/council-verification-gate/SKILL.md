---
name: council-verification-gate
description: Use immediately before claiming Executive Council work is complete, fixed, sent, paid, deployed, updated, reconciled, migrated, or otherwise successful.
---

# Council Verification Gate

The current Google Drive Source of Truth, domain rules, platform/system instructions, and Samuel's explicit current request override this skill.

## Iron rule
No material completion claim without fresh evidence for the postcondition that makes the claim true.

## Workflow
1. Name the exact claim about to be made.
2. Define the postcondition that would prove it.
3. Choose the freshest direct verification available.
4. Run or read the verification.
5. Compare actual result with expected postcondition.
6. If verified, report completion with the relevant evidence.
7. If not verified, report the actual state and never upgrade "attempted" into "done."

## Examples
- Drive update → re-read the changed section/revision.
- Email sent → confirm sent state/destination when exposed.
- Calendar changed → re-read the event.
- Payment → verify provider transaction/payment state; checkout or intent is not payment.
- Software fix → reproduce the original symptom or run the relevant test.
- Deployment → verify the user-visible flow when material.
- Spreadsheet → reconcile totals/formulas and inspect the final artifact.
- Migration → verify the new surface recovers current state before abandoning the old one.

## Agent/subagent rule
An executor reporting "success" is evidence of an attempt, not proof of the postcondition. Verify independently whenever possible.

## Fail closed
If the proving signal is unavailable, label the result UNVERIFIED or PARTIALLY VERIFIED and state exactly what remains unverified.
