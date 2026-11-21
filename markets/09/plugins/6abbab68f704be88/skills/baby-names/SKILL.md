---
name: baby-names
description: Answer US baby-name popularity questions with exact Social Security Administration data (1880-2025) and find baby names by letters, length, syllables, popularity, rising trend, vintage era or unisex split.
---

# Zovo Baby Names

Two read-only tools over the US Social Security Administration national baby-name files, 1880-2025.

## find_name_trend
Use for "how popular is <name>", "rank of <name> in <year>", "Emma vs Ava", "when did <name> peak".
- Pass 1 to 5 names in `names`. To choose a sex per name, write "Avery (boy)"; otherwise each name uses the sex with more births in 2016-2025.
- Add `year` when the user asks about one year.
- Quote the numbers exactly as returned: 2025 rank and births, 10-year change, peak year, highest rank, girls' share.

## find_baby_names
Use for name ideas and lists: "girl names starting with A", "unique boy names", "names ending in -lyn", "rising names", "vintage names", "unisex names".
- Map words to filters: "familiar but not common" = `popularity: familiar` (ranks 201-1,000); "unique" or "rare" = `popularity: uncommon` or `rare`; "trending" or "rising" = `rising_years` (default 10 if no period given); "old-fashioned" or "vintage" = `vintage: true`; "popular in the 1950s" = `era_from: 1950, era_to: 1959`; "gender-neutral" = `unisex: true`.
- Syllable counts are approximate; mention this if the user relies on them.

## Rules
- Data is US only; spelling variants are separate names; SSA omits a name in a year with fewer than 5 births of one sex.
- Ranks use SSA numbering (births descending, ties alphabetical). Past years are ranked within the top 1,000.
- Never invent ranks or counts. The tools have no name meanings, origins or astrology; answer those without claiming they come from this data.
