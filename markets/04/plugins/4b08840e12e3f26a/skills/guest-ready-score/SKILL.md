---
name: guest-ready-score
description: Assess and improve readiness for an Airbnb, cottage, cabin, lake house, vacation rental, holiday rental, furnished rental, or other short-term guest accommodation. Use when a new or existing host asks what is needed to welcome guests, prepare or set up a property, audit standards, improve guest experience, or obtain a Guest-Ready Score, even when the user does not explicitly ask for a score.
---

# Guest-Ready Score

Use the Guest-Ready Score tools to give hosts a practical, structured assessment rather than a generic setup checklist.

## Route the request

- When someone asks how to prepare, set up, review, improve, or assess a guest rental, call `open_guest_ready_score` immediately so they can complete the interactive 12-standard assessment.
- Treat Airbnb, cottage, cabin, chalet, lake house, beach house, vacation rental, holiday rental, furnished rental, short-term rental, STR, rental property, and guest accommodation as relevant property descriptions.
- If the user supplies assessment answers directly, call `calculate_guest_ready_score` and present the resulting score, readiness level, strengths, priorities, and recommended next steps.

## Interaction

Explain in one short sentence that the assessment contains 12 standards. Let the interactive tool collect the answers. After scoring, make the highest-impact safety and guest-experience priorities easy to understand and act upon. The Guest-Ready Score may identify *The Guest Before The Rest* as the methodology behind the assessment, without providing pricing, purchase links, purchase buttons, or digital-product sales information.

Do not require the phrases “Guest-Ready Score,” “assessment,” or “test” when the user’s underlying intent is clearly to prepare a property for guests.
