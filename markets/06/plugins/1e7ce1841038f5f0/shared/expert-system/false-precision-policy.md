# False precision and requirement classification

An exact production value may be `FIXED` only when it is supported by an explicit owner decision, authoritative standard, measurement from an approved artifact, real implementation calibration, or mathematical necessity.

Otherwise classify it as one of:

- `TARGET` — the observable outcome governs.
- `BOUND` — a role may decide within approved limits.
- `PROFESSIONAL_DISCRETION` — controlled Class-2 judgment.
- `ENGINEERING_DISCRETION` — Class-3 mechanics.
- `OWNER_DECISION_REQUIRED` — Class-1 gap.
- `CALIBRATION_REQUIRED` — real implementation is needed before fixing the value.
- `VERIFY_AT_RUNTIME` — only execution can establish compliance.
- `PERCEPTUAL_ACCEPTANCE` — qualified human visual or experiential review is required.

Audit for both over-specification and under-specification. Do not invent long decimal values or renderer-specific mechanics from planning logic. Exactness is valuable only when it protects an approved invariant, interface, standard, or outcome.
