---
name: paper-money-serials
description: Answer questions about US paper money serial numbers with the SerialHunt tools (whether a bill is worth keeping, the print run behind a star note, fancy serial patterns and their odds, the rarest star runs, which series the figures cover) and report the numbers honestly (run size is the measure of a star's scarcity, no prices, no authenticity claims). Use whenever the user gives a serial number from a US bill, asks if a star note or a serial is rare or valuable, asks what a radar, repeater, ladder or other fancy serial is, or asks which star notes to look for.
---

# US paper money serials with SerialHunt

The `serialhunt` MCP server gives read-only access to SerialHunt's star note print runs, built from the Bureau of Engraving and Printing's production reports (through the uspapermoney.info archive for Series 1963 to 2017A), and to its 17 fancy serial patterns, each counted exactly over all 100,000,000 possible eight-digit serials. This skill is about choosing the right tool and reporting what it says honestly.

## Pick the tool

- **One bill** ("is MB 123 45678 C worth anything?", "I got a star note B 033 12345 ★"): `check_serial` with `serial` as printed (`*` or `★` for the star), plus `denomination` and `series` when the user gives them. A star note's print run needs the denomination; ask for it if missing. When the result has `series_candidates`, the serial alone does not settle the series: ask which series is printed beside the portrait and call again.
- **Which stars to hunt for** ("rarest $2 star notes", "smallest star runs in Series 2021"): `find_star_runs`, filtered by `denomination`, `series` or `district` (the Federal Reserve Bank letter). Runs printed only for uncut collector sheets never circulate and are left out unless `include_sheet_runs` is true.
- **What a pattern means or how rare it is** ("what is a radar note?", "how rare is a solid serial?"): `list_serial_patterns`.
- **Whether a series is covered** ("do you have 1950 notes?", "how current are the figures?"): `get_coverage`.

## Read the numbers correctly

- **A star note is as scarce as its run.** `notes_printed` is how many star notes shared the run. Very rare is 320,000 or fewer, rare 640,000 or fewer (the line collectors use for a premium), scarce 1,600,000 or fewer. Quote `compared` ("smaller than 85% of the star runs on record") rather than inventing a reading.
- **When sources disagree** about a run, `notes_printed` is the larger reading, so rarity is understated rather than overstated; `sources_disagree` says so.
- **Not printed is a real answer.** A star serial in a stretch the press skipped was never issued, so suggest checking the digits and series. Past the last serial on record usually means the note is newer than the figures, not that it is fake.
- **Pattern odds are exact counts**, and the patterns do not overlap (a solid is not also a radar). `strength` is exceptional above 1 in 100,000, strong from 1 in 5,000, modest below that.
- **`verdict`** is keep for a strong pattern or a star from a run of 1,600,000 or fewer, notable for anything else found, ordinary otherwise. It says whether to set the bill aside, not what it is worth.
- **The Federal Reserve Bank** is certain only when `certain` is true: older silver certificates and United States Notes use the same serial shape and have no district.

## What not to say

- **No prices.** SerialHunt gives none on purpose: no US paper money price guide can be licensed. If the user wants a value, say the run size and patterns are what a dealer or an auction record would price, and suggest checking recent sold listings.
- **No authenticity judgement.** A serial cannot show whether a note is genuine.

## Good answers look like this

Placeholders in angle brackets stand for values from the tool results.

- "<serial> is a star note from run <run_number> of <note>. Only <notes_printed> were printed, which counts as <rarity_band>: <compared> Worth keeping. Full details: <url>."
- "No collector pattern in those digits, and it is not a star, so it is an ordinary <denomination> note."
- "That serial falls in a stretch the press skipped, so no star note was issued with it. Check the digits and the series printed on the note."
- Link the `url` when the user wants the full page on SerialHunt.
