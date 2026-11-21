---
name: which-pressing
description: Narrow a vinyl record down to its pressing with VinylAI from details the user types or reads off the record (catalog number, label, runout/matrix lines, barcode, country, year), and show every version of the album. Use when the user asks which pressing they have, gives a catalog number or runout, or asks to see all versions or the earliest pressing.
---

# Which pressing

Use this skill when the user types what is on their record, or asks about pressings and versions. Explicit instructions
from the user take priority over this skill, except the rules marked **always**.

## Steps

1. Call `find_pressing` with every detail the user gave: `catno`, `label`, `matrix` (each runout line as its own array
   item, written exactly as the user typed it), `barcode` (digits), `artist`, `title`, `country`, `year`. At least one
   is needed. Don't invent fields the user didn't give.
2. Answer at the `level` the tool returned, never higher (`album`, `pressing_group`, `release`, `unmatched`). For a
   group, say how many pressings match and what still differs between them; then ask for the one detail that would
   settle it — usually the **runout** (the text etched in the dead wax), sometimes the country on the label
   ("Made in …").
3. Say which fields matched (`matched_fields`). A pressing matched only on artist and title is an album match, not
   a pressing.
4. To show every version of the album, or for "is this a first press / the earliest?", call `get_release` with the
   release id. It returns up to 50 versions (year, then country), the total, and `earliest_in_catalog`.
   - Quote the earliest pressing **as catalog data**: "the earliest pressing of this album in the catalog: 1973, UK,
     Harvest SHVL 804". Don't say the user's copy is a first press unless the result is `release` and that release is
     the earliest one.
   - A release with no other versions is a "single release".
   - `not_in_catalog`: say the release isn't in the current catalog (it may have been merged or removed) and give the
     Discogs link. It's not an error.
5. Give both links: the Discogs page and "Open in VinylAI".

## Rules

- **Always: no prices, no values,** no "this pressing is worth more", no "rare = expensive". For price questions say
  prices aren't available here and give the Discogs page link and "Open in VinylAI".
- **Always: never invent a catalog number, runout or pressing.** If you remember a catalog number for the album, don't
  present it as what's on the user's record; ask the user to read theirs.
- Normalisation is handled by the tool: "SHVL 804", "shvl-804" and "SHVL804" are the same. Pass what the user typed.
- If nothing matches, say so and ask the user to double-check the catalog number or type the runout; offer the closest
  albums only as "not an exact match".
