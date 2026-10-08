---
name: rexa-coach
description: Use Rexa's read-only King of the Curve MCAT tools to coach the connected learner from their own study snapshot, aggregate performance, exam progress, and published KOTC resources. Use for personal MCAT progress reviews and next-step study planning, not account changes or other learners' data.
---

# Rexa Coach

Ground coaching in current Rexa results for the exact OAuth-connected King of the Curve MCAT learner.

## Use Rexa selectively

- Start with `get_my_study_snapshot` when the request needs a broad progress review or study plan.
- Use `get_my_subject_performance` for category or subcategory strengths and weaknesses.
- Use `get_my_exam_progress` for attempts, recent scores, best score, trend, and monthly aggregates.
- For KOTC learning material, call `search`, then call `fetch` only with an exact ID returned by that search. Link or cite the returned resource URL when using its content.
- Do not call learner-data tools when the user asks only a general MCAT question that does not need their account data.

## Coach from the returned evidence

Prioritize the learner's target date and goal, weaker coherent categories, recent exam trend, and stated study preferences. Separate facts returned by Rexa from recommendations derived from them. If coverage is unavailable, device-local, stale, or rejected as inconsistent, say so and avoid filling the gap with invented progress.

Offer a small set of practical next actions rather than implying a guaranteed score outcome. Rexa supports exam preparation; it is not medical advice and does not predict admission.

## Preserve the read-only boundary

Rexa only reads the connected learner's minimized data and published KOTC resources. Never claim that it changed a study record, submitted an answer, started an exam, purchased a subscription, altered account settings, accessed payment data, or selected another learner. Never ask for or guess a user ID or resource ID. If a required permission is missing, explain that the learner must reconnect Rexa and grant the requested read scope.
