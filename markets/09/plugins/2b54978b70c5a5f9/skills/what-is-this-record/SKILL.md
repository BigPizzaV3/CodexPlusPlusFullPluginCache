---
name: what-is-this-record
description: Identify a vinyl, shellac or flexi record from a photo of its cover, label, back, barcode or runout with VinylAI, and say honestly how far the photo narrows it down (album, pressing group or exact pressing). Use when the user shares a photo of a record and asks what it is, which pressing it is, or whether it is a first press.
---

# What is this record

Use this skill when the user attaches a photo of a record (front or back cover, label, barcode, the runout in the dead wax)
and wants to know what it is. Explicit instructions from the user take priority over this skill, except the rules marked
**always**.

## Steps

1. Call `identify_record` with the attached photo(s) (up to 4 in one call). Pass a short `hint` only if the user said
   something useful ("it's a Japanese pressing").
2. Read the `level` in the result and answer at **that level, never higher**:
   - `album` — say which album it is and how many record pressings the catalog has. Do not name a single pressing.
   - `pressing_group` — say how many pressings match what was read and what still differs between them
     (country, year, label, format). Do not pick one of them.
   - `release` — the exact pressing, and the fields that decided it (`matched_fields`).
   - `unmatched` — say that nothing in the catalog matches what was read. Mention the closest albums only as
     "not an exact match".
   - `not_a_record` — say VinylAI identifies vinyl, shellac and flexi records. Do not guess what the object is worth
     or invent a match.
3. Report what was read on the photo. A field with `seen: false` was **not visible on the photo**: call it
   "suggested", never "read" or "on your record". **Always.**
4. If `next_step` is set, ask for exactly that: a photo of the **label** (`label_photo`), a photo of the **runout** — the
   text etched in the dead wax near the centre (`runout`) — or the **catalog number** typed from the label or spine
   (`type_catno`). Do not ask for a barcode first; most records have none.
5. When the user then types a catalog number, runout or barcode, use the "which-pressing" skill (`find_pressing`).
6. Give both links from the result: the Discogs page and "Open in VinylAI".

## Rules

- **Always: no prices, no values.** If the user asks what it is worth or costs, say prices aren't available in this
  plugin, and give the Discogs page link and "Open in VinylAI". Never give a number, a range, or "rare, so it's
  valuable".
- **Always: never invent a release.** Every album or pressing you name must come from the tool result.
- "Is this a first press?" — answer only with what the catalog supports: call `get_release` for the matched pressing
  and quote `earliest_in_catalog` as **catalog data** ("the earliest pressing of this album in the catalog is …").
  If the user's record isn't narrowed to one pressing, say the runout would confirm it.
- If the photo can't be read, or the AI read fails, ask for a clearer photo of the label, or for the catalog number or
  runout typed out.
- If the user wants to keep the record, use the "my-collection" skill.
