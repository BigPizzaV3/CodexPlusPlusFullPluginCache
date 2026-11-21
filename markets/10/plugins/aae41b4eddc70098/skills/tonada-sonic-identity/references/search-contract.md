# Public sample search, version 1

Tool: `search_catalog_samples`. Default limit 3; permitted limit 1–5. It does not take a brand ID and does not access the user's Tonada library.

Tool: `get_vocabularies` (no input). Returns the allowed values for `moods`, `genres`, `energies`, `tempos` and `instruments`, keyed by those names. Call it once before the first search; every tag below comes from its lists.

```json
{
  "sonic_profile": {
    "filters": {
      "moods": ["warm", "calm"],
      "genres": ["jazz", "downtempo"],
      "energies": ["low", "medium"],
      "tempos": ["slow", "medium"]
    },
    "preferences": {
      "bpm": { "min": 82, "max": 98 },
      "instruments": ["rhodes"],
      "vocal_presence": { "max": 0.3 }
    },
    "constraints": {
      "instrumental_only": false,
      "excluded_genres": []
    }
  },
  "limit": 3
}
```

All three profile sections are optional. Omit unspecified filters/preferences instead of sending empty arrays. There is no required minimum number of attributes.

| Input                                                      | Meaning                                                                                                                             |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `filters.moods`, `filters.genres`                          | 1–5 canonical tags from `get_vocabularies`. OR within a field, AND across fields. Describe candidate collections, not every track.  |
| `filters.energies`                                         | 1–3 of `low`, `medium`, `high`; collection categories.                                                                              |
| `filters.tempos`                                           | 1–3 of `slow`, `medium`, `fast`; collection categories, not defined BPM ranges.                                                     |
| `preferences.bpm`                                          | Range with `min` and/or `max`, each between 20 and 300.                                                                             |
| `preferences.instruments`                                  | 1–5 canonical instrument tags from `get_vocabularies`; soft preference.                                                             |
| `preferences.vocal_presence`, `energy_level`, `brightness` | Ranges with `min` and/or `max`, each between 0 and 1.                                                                               |
| `constraints.instrumental_only`                            | Requires the track's instrumental flag to be true; a track without it is excluded. The measured vocal presence plays no part.       |
| `constraints.excluded_genres`                              | Up to 10 canonical genre tags from `get_vocabularies`. Tracks with an excluded genre or without usable genre evidence are excluded. |

Ranges require `min <= max`. Unsupported properties are rejected. The API may broaden soft collection filters if too few usable samples remain; it never relaxes hard constraints. Missing track metadata cannot establish a match.

There is no enforced free-text `avoid`, artist/song similarity, texture, production, rhythm, acoustic/electronic balance, explicit-lyrics filter, or saved-library filter. These may guide the conversation, but cannot be claimed as checked by this tool. Do not translate an exclusion into unrelated filters just to fill the schema.

The response provides:

- `matches`: up to five distinct tracks, each with title, collection, preview URL, safe track metadata, `match_evidence`, `unverified_preferences`, `unmet_preferences`, and `explore_url` (the track's Tonada collection page, where the visitor can listen again and learn more).
- `relaxed_filters`: requested collection facets not satisfied by some selected results.
- `unverified_preferences`: requested preferences for which some selected tracks lack metadata.

Use the result's URLs verbatim. Do not call `search_brand`, `get_asset`, or write/link tools to bypass a shortage of public samples. No returned track should be described as an exact match if its evidence says otherwise.
