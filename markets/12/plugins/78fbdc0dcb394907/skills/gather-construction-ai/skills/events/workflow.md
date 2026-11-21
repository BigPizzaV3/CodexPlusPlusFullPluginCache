---
name: events
description: 'Identifies potential contractual events — compensation events (NEC),
  Relevant Events (JCT), FIDIC claims — from site diary data. Triggers: find potential
  CEs, event register, claims significance.'
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Contract Event Identification

Search Gather site diary data for events that may have contractual significance — potential compensation events (NEC), Relevant Events (JCT), or claims (FIDIC). This skill mines narratives, access records, and worklog events to identify situations that may entitle the Contractor to additional time and/or cost.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination); `../../shared/patterns/05-contract-type-resolution.md` (contract type resolution); `../../shared/patterns/06-notification-compliance.md` (notification compliance); `../../shared/patterns/07-event-to-clause-mapping.md` (event-to-clause mapping).

**Important boundary:** This skill identifies potential events from site records. It does not have access to a formal CE/EWN register, variation register, or claim register. Events identified here are candidates — they require human review and contractual analysis before any notification is issued.

---

## Step 1: Resolve Parameters

Extract from `the user’s request`:
- **Project name** — resolve using Pattern 1
- **Date range** — resolve using Pattern 2 (default: last 4 weeks)
- **Contract type** — resolve using Pattern 5

If the contract type is not specified, ask: "Which contract form is this project under? (NEC3, NEC4, JCT SBC, JCT DB, FIDIC Red Book, FIDIC Yellow Book, or other)"

---

## Step 2: Define Search Terms by Contract Type

Based on the contract type, define the keyword categories to search for:

### NEC (Compensation Events / Early Warnings)
- **Access/possession:** "no access", "access denied", "late possession", "possession not given", "access restricted", "could not access", "waiting for access"
- **Instructions/changes:** "instruction", "changed", "redesign", "additional work", "omission", "variation", "scope change", "design change", "rework", "abortive"
- **Standing time / delay:** "standing", "stood down", "idle", "waiting", "no work available", "unable to proceed", "delay", "delayed", "disruption", "held up"
- **Weather:** "weather", "rain", "wind", "storm", "flood", "snow", "ice", "fog"
- **Physical conditions:** "unforeseen", "unexpected ground", "contamination", "asbestos", "utilities", "services found"
- **Third party:** "statutory undertaker", "utility company", "other contractor", "interference"
- **Information delays:** "waiting for information", "drawing not issued", "design incomplete", "RFI", "query outstanding"

### JCT (Relevant Events / Relevant Matters)
- Same search terms as NEC, plus:
- **Statutory:** "planning", "building control", "statutory requirement", "regulation change"
- **Specified Perils:** "fire", "lightning", "explosion", "flood", "earthquake"

### FIDIC (Claims)
- Same search terms as NEC, plus:
- **Unforeseeable conditions:** "unforeseeable", "unexpected", "differed from site information"
- **Engineer:** "Engineer's instruction", "Engineer directed"

---

## Step 3: Retrieve Data (parallel calls)

Make the following three `getCachedReport` calls **in parallel** for the resolved project and date range:

### 3a: Narratives (`dashboardNarrative`)
Search the narratives for each keyword category defined in Step 2. Record:
- The date of the shift record
- The narrative text containing the keyword
- Which category the keyword falls into
- The shift record ID (for cross-referencing) — if the narrative report does not expose record IDs, locate the record via `getShiftRecords` filtered to the same date (follow Pattern 4)

**Filter false positives:** discard matches where the keyword describes routine operations rather than an impediment to progress (e.g. "waiting for concrete to cure", "toolbox talk instruction", "delivery delayed 10 minutes"). A hit qualifies only if the sentence describes work being prevented, disrupted, or changed.

### 3b: Access Data (`dashboardAccessPossession`)
Look for:
- Possessions not granted on time
- Possessions cancelled
- Access restrictions
- Overruns

Cross-reference with narrative findings — access issues identified in narratives should correlate with access data.

### 3c: Worklog Events (`dashboardWorklogEvents`)
Look for logged events that may have contractual significance — disruption events, safety events, environmental events.

---

## Step 4: Categorise and Assess

For each potential event identified, assess:

1. **Clause mapping** — use **Pattern 7 (Common Event-to-Clause Mapping)** from `../../shared/patterns/07-event-to-clause-mapping.md` to map each event to the applicable contract clause. For events not in the common categories, consult the full contract knowledge skill.

2. **Confidence rating:**
   - **HIGH** — clear evidence in narratives, corroborated by access/worklog data, unambiguous event
   - **MEDIUM** — evidence in narratives but not corroborated, or event is ambiguous
   - **LOW** — inferred from indirect evidence, single mention, may have alternative explanations

3. **Notification status check:** Apply **Pattern 6 (Notification Compliance Check)** from `../../shared/patterns/06-notification-compliance.md` to determine whether the event is within the notification window.

4. **Recurring vs one-off** — is this a single event or a pattern (e.g., recurring access delays)?

---

## Step 5: Present the Event Register

### Output Format

```
CONTRACT EVENT REGISTER — [Project Name]
Ref: EV-[NNN]
Contract: [type and edition]
Period: [start] to [end]
Generated: [today's date]

POTENTIAL EVENTS IDENTIFIED: [count]
```

Apply **Pattern 8 (Report Numbering)** for the `EV-[NNN]` reference.

#### Event Table

| # | Date(s) | Category | Description | Clause | Confidence | Notification Window |
|---|---|---|---|---|---|---|
| 1 | [date] | [category] | [brief description from narrative] | [clause ref] | HIGH/MED/LOW | [within/outside/N/A] |

#### Summary

```
By category:
- Access/possession: [count] events
- Instructions/changes: [count] events
- Standing time: [count] events
- Weather: [count] events
- Physical conditions: [count] events
- Third party: [count] events
- Information delays: [count] events
- Other: [count] events

By confidence:
- HIGH: [count]
- MEDIUM: [count]
- LOW: [count]

Notification alerts:
- [count] events approaching notification deadline ⚠️
- [count] events past notification deadline ⚠️⚠️
```

#### Detailed Findings

For each HIGH and MEDIUM confidence event, provide:
- **Date(s):** [range if recurring]
- **Category:** [type]
- **Narrative evidence:** [exact text from diary record]
- **Shift record(s):** [IDs for cross-reference]
- **Contractual analysis:** [which clause applies and why]
- **Notification status:** [within window / approaching deadline / past deadline]
- **Recommended action:** [notify / investigate further / monitor]

---

## Step 6: Caveats

Always include:

> **Important notes on this event register:**
> - Events are identified from recorded data — narratives, access records, and worklog events. Events not recorded in shift diaries will not appear.
> - Clause mapping is indicative — the actual contractual basis requires review against the specific contract conditions (including any amendments or special provisions).
> - LOW confidence events are inferred from indirect evidence and should be verified before any action is taken.
> - This register identifies potential events only. It does not constitute a formal notification or claim. The user must review each event and issue notifications through the proper contractual channels.
> - Notification window calculations are based on today's date and the event date in the diary. The actual "date of awareness" may differ.

---

## Related Skills

- `$ce-builder` — Build a formal claim/CE narrative for a specific event identified here
- `$delay-analysis` — Build a comprehensive delay register
- `$narrative-search` — Deep search for evidence on a specific event
- `$access` — Detailed access and possession analysis
- `$weather-impact` — Quantify weather impact for weather-related events
