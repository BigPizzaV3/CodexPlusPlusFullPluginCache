# Trip audit rubric

Score 100 points:

| Area | Points |
| --- | ---: |
| Requirement fidelity | 15 |
| Research quality and provenance | 20 |
| Hidden-gem distinctiveness and feasibility | 15 |
| Route and itinerary coherence | 15 |
| Budget integrity | 15 |
| Accessibility, safety, and uncertainty | 10 |
| Multi-agent synthesis and contradiction handling | 5 |
| User-facing usefulness | 5 |

95-100 is decision-ready with disclosed verification points; 90-94 is excellent with minor gaps; 80-89 needs manual review; below 80 is not ready.

Automatic caps:

- Fabricated availability, price, hours, accessibility, or booking: 59.
- Missing a stated hard constraint: 69.
- Unexplained budget variance above 5%: 69.
- Accessibility-dependent recommendation without verification status: 69.
- Marketplace ranking presented as independent validation: 79.

For a trip with mobility, allergy, medical-equipment, or medication constraints, any unknown or incompatible critical chain link makes the plan **not ready** regardless of score. Require a pass/fail table for each stated hard constraint and count per-day scheduled commitments when the user set a cap.

Audit graceful degradation: if a key source is unavailable, the plan must label the gap and offer a verification path rather than infer a fact.
