# Observable ownership

Every material observable has one primary source owner. Other documents reference it instead of independently specifying competing values.

Record:

```text
OBSERVABLE_ID
DESCRIPTION
PRIMARY_SOURCE_OWNER
REQUIREMENT_TYPE
VALUE_OR_TARGET
DEPENDENT_ARTIFACTS
MEASUREMENT_OR_REVIEW_METHOD
ACCEPTANCE
REPRESENTATION_ID
CALIBRATION_CHECKPOINT
STATUS
```

Examples include hero frame coverage, visual dominance, interaction latency, contrast, camera composition, material response, or error recovery. `REPRESENTATION_ID` and `CALIBRATION_CHECKPOINT` are conditional links for material perceptual work, not required ceremony for every observable. A calibration checkpoint may bind accepted values only within its approved scope and cannot silently change the primary source target or bounds. Detect duplicate observables when different documents control the same visible or functional result. If values conflict, stop under Class 1; do not silently reconcile them.
