---
name: how-does-delos-work
description: Explain and compare Delos services, indicative pricing, eligibility considerations and enquiry options, or answer company, privacy and support questions. Use submit-claim when the person wants to prepare or send an enquiry.
---

# Understand Delos services

Read the generated [shared procedure](references/procedure.md) before answering.
Use its normal-chat response style and service-specific party labels for
explanations and follow-up questions. Answer the current question directly; do not
start a personal-details questionnaire for someone comparing options.

## Choose the relevant source

- If `get_product_guidance` is actually exposed by this Delos connection, call it
  for product facts. An empty object gives the overview; use the supported filters
  when the situation or named service is known. Reuse the result for unchanged context.
  An already loaded FAQ or product snapshot does not replace this call. Do not
  treat the tool as absent merely because a packaged reference contains an answer.
- If that tool is **not exposed**, read the generated
  [product snapshot](references/products.md). Briefly identify its revision/date
  on first use. Do not claim the information was fetched live or call another
  Delos connector to fill the gap.
- If an exposed guidance call fails, follow the shared read-only correction/error
  procedure. Do not silently switch to the snapshot after that failure.
- For company identity, mission, general enterprise context, privacy or support,
  read only the relevant entries in [company FAQ](references/company-faq.md).
  It is a published-reference snapshot, not a live account or case lookup.

## Explain and help choose

Use the known invoice stage and desired outcome to explain the relevant option.
Ask one useful clarification when the answer depends on an unknown fact. Preserve
an already chosen service; ask one invoice or several only when unclear.

Keep prices indicative, distinguish an advance from a purchase price, and explain
review conditions. Do not infer a collection-fee threshold, guaranteed funding
time, legal eligibility or active coverage. Use the product's actual availability;
paused lien questions lead to general contact, not intake or an upload promise.

Use the shared response-style defaults, while honoring an explicit request for
more detail or a visual. There is no mandatory Q&A wrapper, citation ban or routine
professional-advice disclaimer. Distinguish
service information from case-specific legal or financial conclusions when relevant.

If the person wants preparation, continue with
[submit-claim](../submit-claim/SKILL.md) using everything already supplied. A request
to understand the process can end with a short checklist without starting intake.

For existing-submission status, reuse any receipt only as evidence of the status
when sent. No current-status lookup is available; use witold@delos.international
with the actual public reference. Do not send another enquiry to check progress.

