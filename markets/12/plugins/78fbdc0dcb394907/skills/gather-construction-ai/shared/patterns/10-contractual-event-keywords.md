# Pattern 10: Contractual Event Keywords (Canonical List)

The single source of truth for event-detection keyword scanning. The `events` skill, `cost-to-complete` risk scan, and the `getShiftRecords` hook prompt in `hooks/hooks.json` must stay in sync with this list (the hook inlines a copy — update it in the same commit as this pattern).

| Category | Keywords |
|---|---|
| Access/possession | "no access", "access denied", "access restricted", "late possession", "possession not given", "could not access", "waiting for access" |
| Instructions/changes | "instruction", "variation", "scope change", "design change", "redesign", "additional work", "omission", "rework", "abortive" |
| Standing/delay | "standing time", "standing", "stood down", "idle", "waiting", "unable to proceed", "delay", "delayed", "disruption", "held up", "no work available" |
| Physical conditions | "unforeseen", "unexpected ground", "contamination", "asbestos", "utilities found", "services found" |
| Third party | "statutory undertaker", "utility company", "other contractor", "interference" |
| Information | "waiting for information", "drawing not issued", "design incomplete", "RFI", "query outstanding" |
| Weather | "weather", "rain", "wind", "storm", "flood", "snow", "ice", "fog" |

**False-positive rule:** a keyword hit qualifies only if the sentence describes work being prevented, disrupted, or changed. Discard matches describing routine operations ("waiting for concrete to cure", "toolbox talk instruction", "delivery delayed 10 minutes").
