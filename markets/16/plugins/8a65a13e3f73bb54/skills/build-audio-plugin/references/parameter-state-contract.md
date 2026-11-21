# Controls and saved-state contract

Write this contract before implementing a new control or altering an existing
parameter schema. It is a worksheet, not an APVTS implementation or proof that
automation/session recall works. The fixed gain example still has no state extension.

For each control, record:

| Field | Why it matters |
|---|---|
| Stable identifier and display name | Host/session identity must survive harmless label changes |
| Type and legal values | Continuous, stepped, toggle or choice; include the actual step/choices |
| Stored range and default | Distinguish persisted representation from what the user sees |
| Display mapping and units | Record forward/inverse mapping and mode-specific meaning |
| DSP mapping | Record effective processing value after any tuning or mode selection |
| Update behavior | When a new value takes effect; ramp/transition policy if required |
| Automation and gesture behavior | Which changes are automatable and how editing begins/ends |
| Saved-state behavior | Versioning, missing fields, invalid values and migration policy |

Trace stored value through mapping, tuning, mode selection and DSP use, then
compare labels and documentation. A tooltip can expose a discrepancy but cannot
prove the effective range. Test mapping endpoints and representative interior
values, including inverse/round-trip behavior where an inverse is promised.
Do not silently change a parameter ID, choice ordering or normalization in an
existing product; define compatibility and migration first.

Separate parameter values from preset identity. Restoring a preset label must
check both valid index bounds and the expected name, and must preserve edited
parameter values rather than reloading a factory preset. An unknown/renamed
preset should not silently replace the saved sound.

Select a small set of cases relevant to the change:

- Default state, boundary values and a non-default edited state.
- Missing, unknown or invalid fields under the declared migration rules.
- Old supported state reopened by the new version without unintended changes.
- An automation edit using legal values and balanced begin/end behavior.
- Save, close normally, reopen and compare actual loaded values and rendered
  sound in the named host when host acceptance is required.

Keep source/unit round trips and host session recall as separate evidence.
Record which values are intentionally transient, such as meters or UI animation.
Never write a product's licence credentials, customer identifiers or unrelated
private data into the reusable state example.
