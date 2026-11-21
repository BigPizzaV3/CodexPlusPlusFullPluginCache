# Observed 8D content; validate against the deployed app

These keys were observed in the earlier application, not guaranteed by the OpenAPI content-object schema. Confirm current structure through actual records/tool descriptors. Arbitrary JSON acceptance does not prove native display support.

| Step | Observed keys |
| --- | --- |
| D0 | emergencyResponseNeeded, emergencyResponseDescription, problemSummary, customerImpact, safetyRisk |
| D1 | investigationOwnerId, teamMemberIds, approverIds, externalParties |
| D2 | problemDescription, whatHappened, when, where, howDetected, extentAffected, risks |
| D3 | isSpreading, couldReachCustomer, couldCauseMoreDamage; separate containment actions |
| D4 | tool, fiveWhys, fishbone, trizNotes, causeEffectLinks, rootCauseSummary |
| D5 | notes; separate corrective actions |
| D6 | validationMethod, result; formal effectiveness decisions remain in the app |
| D7 | linkedProcessIds, preventionNotes |
| D8 | lessonsLearned, teamRecognition |

Observed tool values: 5whys, ishikawa, triz, cause_effect. Fishbone categories: man, machine, method, material, measurement, environment. Retain source spelling in actual API keys; choose user-friendly wording in discussion.

CAR creation seeds D0–D8. Retrieve the actual step IDs. Step content merges by top-level key, so a changed array/nested object may replace its previous value; merge deliberately in the approved preview. Do not store unverified hypotheses as established rootCauseSummary. When hypothesis/source fields are absent, propose a readable supported narrative convention; do not silently invent fields.
