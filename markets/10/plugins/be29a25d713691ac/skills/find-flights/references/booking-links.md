# TravelYalla flight booking links

Build the link from the search you ran. Do not invent any part of it.

```
https://travelyalla.com/{lang}-{region}/flights/{legs}/{adults}-{children}-{infants}/{class}
```

- `lang`: `ar` if the conversation is in Arabic, otherwise `en`.
- `region`: `EG` when the traveller's nationality is EG, `SA` when it is SA, otherwise `WW`.
- `legs`: one `{FROM}-{TO}-{yyyy-mm-dd}` per leg, joined with `_`.
- `class`: `economy`, `business` or `first`.

## Examples

Round trip Dubai to London, 16–18 Oct 2026, 1 adult, economy, nationality AE:

```
https://travelyalla.com/en-WW/flights/DXB-LHR-2026-10-16_LHR-DXB-2026-10-18/1-0-0/economy
```

One-way Cairo to Jeddah, 2 adults and 1 child, Arabic, nationality EG:

```
https://travelyalla.com/ar-EG/flights/CAI-JED-2026-11-02/2-1-0/economy
```

The link opens the search results on the website, where the user picks the same flight and books it.
