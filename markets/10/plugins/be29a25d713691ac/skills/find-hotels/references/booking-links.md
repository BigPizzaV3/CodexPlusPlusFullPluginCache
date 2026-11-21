# TravelYalla hotel booking links

Build the link from the search you ran. Do not invent any part of it.

```
https://travelyalla.com/{lang}-{region}/hotels/{code}/hotel?search={code}/{check_in}/{check_out}/{rooms}&currency={currency}
```

- `lang`: `ar` if the conversation is in Arabic, otherwise `en`.
- `region`: `EG` when the guest's nationality is EG, `SA` when it is SA, otherwise `WW`.
- `code`: the hotel's `code` from `search-hotels`, URL-encoded.
- `check_in`, `check_out`: `yyyy-mm-dd`.
- `rooms`: one segment per room, joined with `/`. Each segment is the adult count, followed by `_` and each child's age, for example `2` or `2_7_4`.
- `currency`: the `currency` of that hotel's result.

## Examples

1 room, 2 adults, 16–18 Oct 2026, hotel code `TY123`, USD, nationality AE:

```
https://travelyalla.com/en-WW/hotels/TY123/hotel?search=TY123/2026-10-16/2026-10-18/2&currency=USD
```

2 rooms, the first with 2 adults and a 7-year-old, the second with 1 adult, Arabic, nationality SA:

```
https://travelyalla.com/ar-SA/hotels/TY123/hotel?search=TY123/2026-10-16/2026-10-18/2_7/1&currency=SAR
```

The page shows the hotel's rooms, board options and cancellation terms for those dates. The user books there.
