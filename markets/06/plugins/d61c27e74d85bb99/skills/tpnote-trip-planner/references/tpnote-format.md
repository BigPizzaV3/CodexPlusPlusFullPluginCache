# TPNote Portable Format

Current format: `tpnote-plan`; current schema: `6`. The file is UTF-8 JSON with extension `.tpnote`.

Schema 6 has no booking-attachment collection. Export preserves booking text and links but omits provider-issued QR screenshots, ticket images, and PDF tickets, which remain in the live CloudKit trip. Do not encode attachment bytes into booking notes or invent attachment fields in a schema 6 file.

## Required root keys

`format`, `schemaVersion`, `exportedAt`, `plan`, `days`, `items`, `notes`, `places`, `bookings`, `moneyEntries`, and `details`. New files should also include `reminders` and `legs` as arrays.

All timestamps use ISO 8601. Prefer UTC values ending in `Z`. Every record has a globally unique UUID. References must resolve to records in the same file.

## Main relationships

- `items[].dayID` references `days[].id`, or is `null` for an unscheduled idea.
- `items[].parentItemID` references another item or is `null`; parent chains cannot cycle.
- `items[].placeID`, `bookingID`, and `moneyEntryID` reference their matching arrays or are `null`.
- `notes[].dayID` is required; `parentItemID` may reference an item.
- Booking, money, and detail `itemID` values may reference an item or be `null`.
- `reminders[].itemID` references an item.
- A leg references one day and two items through `dayID`, `fromItemID`, and `toItemID`.
- A linked booking is reciprocal: the event's `bookingID` identifies the booking and that booking's `itemID` identifies the same event.

## App-ready quality

Schema validity only means TPNote can parse the archive. Finished plugin output must also pass the app-ready audit.

- Link each in-person scheduled event to a canonical place. Place and item snapshots need the same verified name, complete address, coordinates, provider data, public contact fields, and Google Place ID when one was genuinely resolved.
- A missing Google Place ID is acceptable when no trusted lookup is available; keep provider `Manual`, leave provider IDs blank, and retain verified location facts. TPNote can attempt Google identity enrichment after import.
- Create commute legs between consecutive scheduled events on the same day when their place IDs differ. The portable leg stores endpoints and mode, not route geometry or ETA. Research realistic travel time separately and leave enough room in the event timeline.
- Store reservation facts in a linked booking instead of event details. Confirmation data, contacts, and costs must come from the user or source material, never inference.
- Schema 6 does not include booking attachment files. Deliver user-supplied QR images and PDFs as companion files for post-import attachment.

Run `scripts/validate_tpnote.py --app-ready FILE` for finished plans. Ordinary validation remains useful for inspecting old exports that were not designed to meet this stronger contract.

## Reusable privacy templates

A template is a new sanitized archive, not the user's private export with a different filename. Re-key every record and reference, replace the owner with `Traveler`, remove confirmation/contact/payment/reminder/attachment data, and semantically review all free text. Remove or generalize homes and residential origins while retaining public trip-specific place and route information. `scripts/create_trip_template.py` performs the structural first pass; an AI or human must still review meaning and context.

## Event titles versus place names

- `items[].name`: event title, such as `Check in at Conrad Tokyo`.
- `places[].name`: actual place name only, such as `Conrad Tokyo`.
- `items[].subtitle`: legacy field used as the place-name fallback, not a descriptive subtitle. Set it to the linked place name or blank if unknown.
- `items[].details`: event notes and instructions. Store reservation numbers, contact names, and stay dates in `bookings`.
- Never put `3 nights`, `Confirmation 12345`, `Tokyo - Unscheduled idea`, or traveler-specific reservation labels in a place name or subtitle. Use `dayID: null` and status `Idea` for unscheduled events.
- TPNote build 22 prefers a nonblank linked place name for its place card and map pin; event titles remain in the itinerary. Older subtitles remain stored, so repairs must preserve descriptive text in `details` before replacing a subtitle.
- A validator warning about mismatched subtitle/place names requires review before delivery. Matching text alone cannot prove a real place name; verify its meaning too.

## Enum strings

- Theme: `sakura`, `ocean`, `forest`, `sunset`, `graphite`
- Item type: `Activity`, `Hotel`, `Flight`, `Train`, `Food`, `Note`, `Payment`, `Reminder`, `Custom`
- Status: `Idea`, `Planned`, `Booked`, `Done`, `Skipped`
- Timeline role: `Scheduled Event`, `Background Context`
- Category: `Hotel`, `Food`, `Activity`, `Transit`, `Shopping`
- Place provider: `Apple Maps`, `Google Places`, `Manual`
- Note kind: `Note`, `Booking`, `Payment`, `Reminder`
- Payment status: `Planned`, `Paid`, `Refunded`, `Disputed`
- Detail type: `Note`, `Checklist`, `Link`, `Confirmation`, `Payment`, `Weather`, `Attachment`, `Custom Text`
- Reminder delivery: `Standard`, `Time Sensitive`
- Transport mode: `Public Transit`, `Walking`, `Driving`, `Cycling`, `Flight`

## Important invariants

- Reuse a single place record for repeat visits to the same known POI. All linked item location/contact fields must match it, including coordinates, address, provider, provider IDs, phone and website. Item category describes the event and may differ from the place category.
- Nullable relationship fields may be omitted or written as `null`. TPNote's Swift encoder normally omits them when no relationship exists; the app and validator accept both representations.

- Plan title is nonblank.
- Day time zones are valid IANA identifiers, such as `Asia/Tokyo`.
- Coordinates are finite and within latitude `-90...90`, longitude `-180...180`.
- Item end time is not earlier than start time.
- Item, note, and detail `orderRank` values are finite.
- Reminder `minutesBefore` is a nonnegative integer.
- Maximum size is 20 MiB; maximum combined record count is 100,000.

Use the bundled `assets/Minimal-Trip.tpnote` as the canonical minimal example. The bundled validator performs the complete structural and cross-reference checks.
