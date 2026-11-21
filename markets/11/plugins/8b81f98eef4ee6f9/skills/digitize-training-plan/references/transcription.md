# Mapping a training document onto Liftory

## Days and weeks

- Each training day of the document is a day, labelled as the document labels it. A day printed across two pages is one day.
- A document with several weeks gives every day of every week its own entry with its week number. The weeks list the same exercises in the same order.
- A week the document marks as a different emphasis gets that day's intensity field (Volume, Intensity, Strength, or Deload); a week with no mark leaves it empty.

## Rows

- sets and reps are copied as written. A rep scheme that changes per set stays a scheme. A rep cell that is a word rather than a number is a technique when the catalog has one for it; the reps field still needs numbers, so ask the user which number to store and say that it is a placeholder.
- A cell written as a time is the sets as written plus durationSeconds per set, with reps left empty.
- Rest is in seconds, as written. When the document gives no rest, leave it at 0 so the app uses its default, unless the user gives one.
- A comment beside an exercise that no technique expresses is the exercise's note, word for word. A technique is never repeated as a note, and sets, reps, and rest are never restated in a note.

## Excluded rows

- A row the coach struck out, blacked out, or covered for one week means the exercise is excluded that week. It stays in that week with disabled true, carrying the previous week's sets, reps, and rest as inert values, with no technique and no note. It is never dropped, so the weeks stay aligned row for row. Whatever is still legible under the cover is not content.

## Linked exercises

- Exercises the document pairs or groups to be done back to back take the linking technique from list_techniques on the FIRST exercise of the pair, with the partner row directly after it. Represent each pairing exactly as printed; never add or remove a pairing.
- A technique that carries a count (a number of drops, for example) uses the catalog technique with that count, and when the catalog has none with that count, ask.
