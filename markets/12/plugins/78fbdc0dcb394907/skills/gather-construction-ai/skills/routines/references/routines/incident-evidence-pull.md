## incident-evidence-pull

**Cadence:** Event-driven — API trigger from site-ops tooling, posting the incident text
**Surface:** Cloud ☁ (API trigger requires a cloud routine's `/fire` endpoint)
**Prerequisites:** none — stateless by design; Gather connector attached, plugin repo attached if `$*` skills are to run
**Priority:** Standard

**Instructions:**
```
An incident has been reported — see the appended text ({{INCIDENT_TEXT}}) for the project,
date, and description. Using the Gather connector, pull site diary, labour, and weather records
for the affected project for that date ±2 calendar days (explicit dates derived from the
incident text, not "recent" records).
Compile a dated evidence chronology: record ID, date/time, source (diary/labour/weather),
and the relevant excerpt — sorted chronologically. Do not assert causation, fault, or
contractual entitlement — this is records and timings only, for someone else to assess.
This run is stateless — there is no previous run to diff against; a fresh chronology every time
is correct behaviour for an incident-triggered pull, not a failure of delta discipline.
```
