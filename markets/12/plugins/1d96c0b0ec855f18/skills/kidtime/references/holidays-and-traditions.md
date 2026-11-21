# Holidays, birthdays and breaks

Kidtime calls holidays, birthdays and school breaks **traditions**. They show as an icon on their
days in the calendar.

- **Holidays** (Thanksgiving, Christmas and others for the family's country): call
  `traditions_list` for their ids (`presets`) and which are on (`enabledPresetIds`), then `traditions_save` with `addHolidayIds` or
  `removeHolidayIds`. Holidays you do not name stay as they are.
- **Breaks** (spring break, summer) have dates the family sets each year: `traditions_save` with
  `breaks`, each with its dates per year. Removing a break deletes its dates, so ask first.
- **Birthdays** belong to a person: set one with `members_save` (`birthDate` as YYYY-MM-DD). It then
  shows every year.
- **Who has the kids on a holiday** is not set by turning the holiday on. It is a hand-off like any
  other: add hand-offs with `events_save` (see `handoffs-and-events.md`).
- **Who had the kids on a holiday in past years:** `traditions_get` with the tradition's id from
  `traditions_list`'s traditions (not a holiday id from its list of offered holidays). It gives the
  date each year and which parent had each child that night, so you can tell whether Christmas
  alternates.
- **What is on a given date:** `events_list` returns the holidays and birthdays in its range, with
  the hand-offs.
