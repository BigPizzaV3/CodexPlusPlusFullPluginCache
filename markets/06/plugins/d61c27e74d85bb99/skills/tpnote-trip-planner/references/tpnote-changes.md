# TPNote AI Change Sets

Use a change set to propose reviewed changes to a trip that already exists in TPNote. The user approves proposals in **Review AI Changes** before TPNote applies them. Always derive the root `planID` and every existing record ID from a current app-exported `.tpnote` file.

Write the finished UTF-8 JSON to a file named `<trip-name>-changes.tpnotechanges` and attach that file to the response. The extension is a dedicated TPNote document type, but the contents remain the JSON structure documented below. Do not return only a fenced JSON block unless file creation is unavailable. The user opens **Review AI Changes**, chooses **Choose Change File**, and selects the downloaded file; Mac users may also drag it onto the review window.

## Root object

```json
{
  "version": 2,
  "planID": "PLAN-UUID-FROM-EXPORT",
  "summary": "Build and refine the arrival itinerary",
  "changes": []
}
```

Each change may include an optional UUID `id` and optional human-readable `reason`. TPNote creates a proposal ID when `id` is omitted. Keep independent field edits as independent changes so users can approve them separately.

## Existing and new records

Target an existing record with its exported UUID:

```json
{
  "entity": "stop",
  "entityID": "EVENT-UUID-FROM-EXPORT",
  "action": "update",
  "field": "details",
  "value": "Meet the driver at the south exit."
}
```

Create a record with a unique temporary `entityRef`. Other selected creation changes may refer to it. TPNote replaces temporary references with permanent UUIDs only after the complete accepted transaction validates.

```json
{
  "entity": "day",
  "entityRef": "arrival-day",
  "action": "create",
  "values": {
    "title": "Arrival in Tokyo",
    "date": "2026-11-20T05:00:00Z",
    "timeZoneIdentifier": "Asia/Tokyo"
  }
}
```

Temporary references are local to one change set. Make them short, descriptive, and unique. Put parent creation changes before children for readability, although TPNote resolves supported dependencies before applying them.

## Entities and create values

Supported `entity` values are `day`, `stop`, `note`, `place`, `booking`, `reminder`, and `leg`. A plan itself may be updated but not created or deleted by a change set.

### Place and event

```json
{
  "entity": "place",
  "entityRef": "conrad-tokyo",
  "action": "create",
  "values": {
    "name": "Conrad Tokyo",
    "address": "1-9-1 Higashi-Shimbashi, Minato City, Tokyo 105-7337, Japan",
    "latitude": 35.6605,
    "longitude": 139.7632,
    "provider": "Manual",
    "phoneNumber": "+81 3-6388-8000",
    "websiteURL": "https://www.hilton.com/",
    "category": "Hotel"
  },
  "reason": "Add the verified hotel once and reuse it across events"
}
```

```json
{
  "entity": "stop",
  "entityRef": "hotel-check-in",
  "action": "create",
  "values": {
    "name": "Check in and leave luggage",
    "details": "Ask the bell desk to hold checked bags.",
    "startTime": "2026-11-20T06:30:00Z",
    "endTime": "2026-11-20T07:30:00Z",
    "dayRef": "arrival-day",
    "placeRef": "conrad-tokyo",
    "category": "Hotel",
    "timelineRole": "Scheduled Event"
  }
}
```

An event may use `dayID` or `dayRef`; omit both to create it in Unscheduled. It may use `placeID` or `placeRef` to reuse a place. An unverified location may remain unlinked. Do not invent provider IDs, coordinates, contacts, or URLs. Use provider `Manual` when a trustworthy Apple or Google provider identity is unavailable.

### Note, booking, reminder, and transportation

```json
{
  "entity": "note",
  "entityRef": "arrival-note",
  "action": "create",
  "values": {
    "dayRef": "arrival-day",
    "time": "2026-11-20T06:00:00Z",
    "title": "Arrival checklist",
    "body": "Activate the transit card and message the hotel.",
    "kind": "Note"
  }
}
```

```json
{
  "entity": "booking",
  "entityRef": "hotel-booking",
  "action": "create",
  "values": {
    "stopRef": "hotel-check-in",
    "title": "Conrad Tokyo reservation",
    "provider": "Hilton",
    "confirmationNumber": "USER-PROVIDED-VALUE",
    "websiteURL": "https://www.hilton.com/",
    "notes": "Breakfast included"
  }
}
```

```json
{
  "entity": "reminder",
  "entityRef": "check-in-reminder",
  "action": "create",
  "values": {
    "stopRef": "hotel-check-in",
    "minutesBefore": 60,
    "isEnabled": true,
    "deliveryStyle": "Standard"
  }
}
```

```json
{
  "entity": "leg",
  "entityRef": "airport-to-hotel",
  "action": "create",
  "values": {
    "fromStopRef": "airport-arrival",
    "toStopRef": "hotel-check-in",
    "transportMode": "Public Transit"
  }
}
```

Both transportation endpoints must be events on the same date. TPNote stores the mode and recalculates live route information; never put route geometry or an unverified travel duration in a change set.

## Update fields

Use `action: "update"`, one `field`, and its string `value`.

- `plan`: `title`, `destinationSummary`
- `day`: `title`, `date`, `timeZoneIdentifier`
- `stop`: `name`, `details`, `startTime`, `endTime`, `category`, `timelineRole`, `allDay`
- `note`: `title`, `body`, `time`, `kind`
- `place`: `name`, `address`, `latitude`, `longitude`, `provider`, `providerPlaceID`, `phoneNumber`, `websiteURL`, `category`, `notes`
- `booking`: `title`, `provider`, `confirmationNumber`, `contactName`, `phoneNumber`, `email`, `websiteURL`, `startTime`, `endTime`, `notes`
- `reminder`: `minutesBefore`, `isEnabled`, `deliveryStyle`
- `leg`: `transportMode`

Use ISO 8601 for dates and times. An empty booking `startTime` or `endTime` clears that optional value. Boolean strings are `true` or `false`. Use exact enum values:

- `category`: `Hotel`, `Food`, `Activity`, `Transit`, `Shopping`
- `timelineRole`: `Scheduled Event`, `Background Context`
- `kind`: `Note`, `Booking`, `Payment`, `Reminder`
- `provider`: `Apple Maps`, `Google Places`, `Manual`
- `deliveryStyle`: `Standard`, `Time Sensitive`
- `transportMode`: `Public Transit`, `Walking`, `Driving`, `Cycling`, `Flight`

## Move, reorder, and link

Move an event or note to an existing date with `destinationDayID`, or to a newly proposed date with `destinationDayRef`. Omit both only when moving an event to Unscheduled. Notes always require a destination date.

```json
{
  "entity": "stop",
  "entityID": "EVENT-UUID-FROM-EXPORT",
  "action": "move",
  "destinationDayRef": "arrival-day"
}
```

Use `reorder` with a numeric `orderRank`. Keep ranks deterministic and ensure the event times and transportation endpoints still describe the intended order.

```json
{
  "entity": "stop",
  "entityID": "EVENT-UUID-FROM-EXPORT",
  "action": "reorder",
  "values": { "orderRank": 4.0 }
}
```

Link an existing event to an existing or newly proposed place:

```json
{
  "entity": "stop",
  "entityID": "EVENT-UUID-FROM-EXPORT",
  "action": "link",
  "values": { "placeRef": "conrad-tokyo" }
}
```

## Delete

Use `action: "delete"` with an exported `entityID`. Deletions are never selected by default in TPNote. Deleting a date also removes its events, notes, and their linked bookings, reminders, and transportation. Deleting an event also removes its linked booking, reminders, and transportation. The review UI shows this impact before approval.

```json
{
  "entity": "stop",
  "entityID": "EVENT-UUID-FROM-EXPORT",
  "action": "delete",
  "reason": "The user explicitly cancelled this reservation"
}
```

Only propose deletion when the user clearly requested it. Prefer moving an uncertain event to Unscheduled.

## Safety rules

- Never guess the root plan ID or any existing entity ID, even when names are unique.
- Never fabricate booking confirmations, place identity, coordinates, contacts, schedules, prices, or route durations.
- A polished change set must leave in-person events linked to complete canonical places, reservation facts in reciprocal booking relationships, and meaningful commute legs between consecutive different locations.
- Re-evaluate the day's timing whenever a place, order, start/end time, or leg changes. Preserve fixed reservations and allow verified travel time plus a practical buffer.
- Booking attachment binaries cannot be created through a schema 6 change set. Return user-supplied files as named companions and identify the post-apply attachment action.
- Use temporary references only for records created in the same change set.
- Do not create dangling children. If a parent creation is optional, keep its dependent changes independently understandable and warn that both must be selected.
- Keep fixed reservations unchanged unless the user explicitly changes them.
- Keep event end time at or after start time and preserve the intended local time zone.
- Keep place names factual. Put instructions in event details and reservation facts in bookings.
- Preserve the original export. A change set updates the live trip and enters its normal collaboration sync queue; it is not a replacement `.tpnote` file.
- Explain that additions and edits start selected, deletions require explicit selection, and **Undo Applied Changes** is available immediately after apply.

Version 1 update-and-move change sets remain accepted for backward compatibility.
