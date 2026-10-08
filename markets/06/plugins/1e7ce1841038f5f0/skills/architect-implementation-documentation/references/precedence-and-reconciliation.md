# Source of truth, precedence, and reconciliation

## Precedence matrix

Precedence is field- or scope-specific, never a vague total ordering. Each row states:

- decision or implementation area;
- controlling artifact and exact version;
- applicable sections;
- lower-precedence or conflicting artifacts;
- reason and decision owner;
- effective date;
- unresolved exceptions.

If two current artifacts can control the same choice and no matrix row resolves them, record `ENTSCHEIDUNGSLÜCKE` and block that area.

## Reconciliation sequence

1. Locate the exact contradictory claims and their sources.
2. Classify whether the conflict is factual, temporal, scope-based, version-based, or a genuine decision conflict.
3. Apply an already approved, scope-specific precedence rule if one exists.
4. If none exists, identify the decision owner and obtain the decision; do not infer authority from recency alone.
5. Update the responsible source artifact through its authoring skill.
6. Mark displaced artifacts or sections `OVERRIDDEN`, `SUPERSEDED`, `HISTORICAL`, or `DO NOT IMPLEMENT` as appropriate; preserve them.
7. Update artifact, decision, dependency, precedence, and change registers.
8. Re-run affected document checks and the suite audit.

## Source-first questioning

Before asking the user, inspect the declared source register, decision log, approved specifications, referenced assets, and their versions. Ask only for a decision that remains absent, inaccessible, contradictory, or outside existing authority. Cite exactly what was checked.
