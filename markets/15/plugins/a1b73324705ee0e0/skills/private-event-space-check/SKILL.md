---
name: private-event-space-check
description: Check whether a private event fits — which rooms at which venues hold the party size, and when they are free on the date asked — from Excellent's room capacity, bookings, holds and blocks; and, when asked, block a room, close a venue or give an event a second room, each change undoable. Use for "is the Garden Room free Saturday for 60", "where can we put a party of 40 on the 14th", "space check for this inquiry", "block the Garden Room Tuesday for floor work", "we're closed on Thanksgiving", "ceremony in the Garden, dinner in the Hall".
---

# Private-event space check

This skill reads, and on request blocks a room, closes a venue or adds a room to an event, each change
undoable. A free stretch is not a reservation. To book or hold a room for an inquiry, use the
`book-this-inquiry` skill.

## 1. Pin down the ask

Get the date (or a range of up to 14 days), the guest count, a rough time (lunch, evening, a start and end)
and, if named, the venue or room. Don't guess a date: if the person says "next Saturday", state the date you
take it to be.

## 2. Look it up

1. If a venue is named, call `overview` and find its id in `locationList`. If a room is named, call
   `list_spaces` with `match` set to its name to get the room's id and capacity.
2. Call `space_availability` with `date`, `days` (for a range), `party_size`, and `location` or `space` if
   known.
3. For each room read `capacity`, `fits_party`, the day's `open` hours, `busy` (bookings, holds and blocks,
   each with its from–to at the venue's clock) and `free`. A booking under `untimed_bookings` has a date but
   no time window: treat that room as uncertain that day and say so.
4. Room turnover time (`turnover_minutes`) is already subtracted around timed bookings.

## 3. Answer

Lead with the answer: "Yes — the Garden Room (seats 80) is free 17:00–24:00 on Sat 14 Nov." Then list the
other rooms that fit, then the ones that would fit but are busy (and with what), then the ones too small.
If nothing fits, say the nearest alternatives: a bigger room on another day in the range, or two rooms at
the same venue.

If a hold is in the way, give the holder's name and when it lapses, so the person can decide in Excellent.

## 4. Block, close or add a room (if asked)

**Before every change,** say exactly what you will change and wait for a yes, unless the person already asked
for that exact change. **After every change,** give the `change_id` it returned and say it can be undone.
Windows are ISO instants with the venue's offset.

- **Block one room** ("the Garden Room is out Tuesday for floor work"): `create_space_block` with the `space`,
  `starts_at`, `ends_at`, a `kind` (`maintenance`, `private_use`, `holiday` or `other`) and an optional
  `reason`. Nothing can be confirmed into the room while it stands. It is refused when a confirmed booking
  holds the room for part of the window, or another block overlaps it: name what is in the way.
- **Close the venue** ("we're closed on Thanksgiving"): `close_venue` with the `location`, the window, `kind`
  (default `holiday`) and `reason`. Every room is blocked except those a confirmed booking or a block already
  holds; say how many rooms were closed and how many skipped — a booking in a skipped room still goes ahead.
- **A second room for one event** ("ceremony in the Garden, dinner in the Hall"): `set_event_rooms` with the
  `event_id` and every extra room as `{ space }`. The list replaces the event's extra rooms, so start from
  the rooms `get_event` shows; the main room is never listed, and an empty list leaves the main room only. It
  is refused past the rooms' capacity, over an active hold on a room it adds, and for a confirmed event over
  another confirmed booking or a block. An event with no room yet is booked first (`book-this-inquiry`).

Never work around a refusal: say why in plain words and offer another room or time.

Safety: the check only reads. A block, a closure or an extra room is made only on the person's yes, and each
returns a `change_id` that `undo` puts back, once, for 30 days. Nothing is booked for a guest, sent or deleted.
