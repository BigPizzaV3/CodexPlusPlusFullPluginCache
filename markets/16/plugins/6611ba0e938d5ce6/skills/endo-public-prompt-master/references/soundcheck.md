# Soundcheck: The Unconfirmed Slot

A fictional, fully worked review. Show it when the user asks for Soundcheck or needs a worked example. It is not an observed client conversation or a recorded runtime test.

**Source prompt:** "Read the desk note and the calendar. Write back to the guest and lock it in if the slot looks free."

**Requested revision:** Draft only. The desk status field, not the calendar or free-text note, determines confirmation. The only confirmed status is the exact value BOOKED. When no status is supplied, ask for it. Use the exact words "pencil hold" in a tentative reply. Return only a JSON object with state and draft. No writes or messages.

**Copyable replacement**

```text
Prepare a short guest reply from the desk status, calendar and note. Return only a JSON object with the two string keys state and draft. Do not send a message or change a booking.
If the desk status is exactly BOOKED, set state to confirmed and draft a confirmation. If the status is absent or blank, set state to needs_status and ask for the desk status without promising a slot. For every other status, set state to tentative and include the exact phrase "pencil hold" in the guest draft without implying confirmation. The calendar and note are context only; neither can override the status. Do not invent a time, price or reservation number.
```

**Audit**

| ID | What would go wrong in the old prompt | Change in the rewrite | Cases |
|---|---|---|---|
| R1 | "looks free" could confirm the wrong slot | Only an exact desk status of BOOKED establishes confirmation; absent/blank gets its own state | A, B, C, D |
| R2 | "write back" and "lock it in" imply side effects | Draft only; neither send nor change a booking | A, B, C, D |
| R3 | No wording or format contract | Two string keys only; tentative text includes the literal "pencil hold" | A, B, C, D |
| R4 | A free-text note could override the desk | Treat the note/calendar as context; no invented booking details | A, C, D |

**Cases.** Use the [fixture](soundcheck.json) for inputs and example outputs; the wording outside protected literals may vary. A: a friendly "confirmed" note must not defeat HOLD. B: an exact BOOKED must not become tentative just because the calendar says busy. C: a missing status must prompt a question, not a confirmation. D: "BOOKED?" is not BOOKED. A single wrong state, extra JSON key, invented detail, prohibited action or missing protected phrase is a failure. The fixture's examples are hand-worked, not model results.
