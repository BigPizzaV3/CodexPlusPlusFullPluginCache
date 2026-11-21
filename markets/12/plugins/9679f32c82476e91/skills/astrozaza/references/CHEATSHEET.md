# AstroZaza CLI Cheat Sheet

Notes:
- Options below are taken from source in this repository.
- Formats shown are the required input formats used by each script.

## azz.py (natal chart)

CLI options:
- --date YYYY-MM-DD
- --time HH:MM
- --tz IANA timezone (e.g., Europe/Amsterdam)
- --lat Latitude (float)
- --lon Longitude (float)
- --debug
- --aspects {major,all}
- --include-points
- --max-aspects N
- --aspects-to {planets,angles,all}
- --out OUTPUT_FILE
- --selftest
- --interactive

Example commands:
- Interactive prompts:
  - `python azz.py`
- Non-interactive:
  - `python azz.py --date 1990-01-01 --time 12:00 --lat 52.37 --lon 4.90 --tz Europe/Amsterdam`
- Include all aspects/points:
  - `python azz.py --date 1990-01-01 --time 12:00 --lat 52.37 --lon 4.90 --tz Europe/Amsterdam --aspects all --include-points --aspects-to all`
- Save output to file:
  - `python azz.py --date 1990-01-01 --time 12:00 --lat 52.37 --lon 4.90 --tz Europe/Amsterdam --out chart.txt`
- Self-test:
  - `python azz.py --selftest`

## syn.py (synastry)

CLI options:
- --date YYYY-MM-DD
- --time HH:MM
- --tz IANA timezone (e.g., Europe/Amsterdam)
- --lat Latitude (float)
- --lon Longitude (float)
- --debug
- --aspects {major,all}
- --include-points
- --max-aspects N
- --aspects-to {planets,angles,all}
- --orb FLOAT
- --include-wide
- --top N
- --out OUTPUT_FILE
- --selftest
- --interactive

Notes:
- Chart A can be provided via flags or prompts.
- Chart B is always prompted interactively.

Example commands:
- Interactive prompts for both:
  - `python syn.py`
- Provide chart A via flags, then prompt for chart B:
  - `python syn.py --date 1990-01-01 --time 12:00 --lat 52.37 --lon 4.90 --tz Europe/Amsterdam`
- Wider synastry aspects:
  - `python syn.py --include-wide --orb 2.5 --top 20`

## tazz.py (transits against natal)

CLI options:
- --date YYYY/MM/DD
- --time HH:MM (24h)
- --country Country name
- --city City name
- --lat Latitude (float)
- --lon Longitude (float)
- --tz IANA timezone (e.g., Europe/Amsterdam)
- --interactive
- --year YYYY
- --quarter {Q1,Q2,Q3,Q4}
- --mode {snapshot,peaks}
- --on YYYY-MM-DD
- --at HH:MM
- --top N
- --coarse-step-hours N
- --refine-step-minutes N
- --refine-window-hours N
- --exact-eps FLOAT
- --orb-max FLOAT
- --include-wide
- --debug
- --debug-orb

Example commands:
- Quarter snapshot:
  - `python tazz.py --date 1996/06/13 --time 21:44 --country Nederland --city Amsterdam --year 2026 --quarter Q1 --mode snapshot`
- Quarter peaks:
  - `python tazz.py --date 1996/06/13 --time 21:44 --country Nederland --city Amsterdam --year 2026 --quarter Q1 --mode peaks --top 10`
- Day snapshot (transits on a specific date/time):
  - `python tazz.py --date 1996/06/13 --time 21:44 --country Nederland --city Amsterdam --on 2026-01-28 --at 12:00`

## lalune.py (lunation calendar)

CLI options:
- --year YYYY (required)
- --max-hits N
- --orb FLOAT
- --tz IANA timezone
- --collective
- --seasons

Example commands:
- Natal lunation calendar (interactive location prompts):
  - `python lalune.py --year 2026`
- Collective calendar:
  - `python lalune.py --year 2026 --collective --tz Europe/Amsterdam`

## global.py (collective transits)

CLI options:
- --from YYYY-MM-DD
- --to YYYY-MM-DD
- --year YYYY
- --quarter {Q1,Q2,Q3,Q4}
- --mode {snapshot,peaks}
- --tz IANA timezone
- --aspects
- --orb FLOAT
- --aspect-set {major,major+quincunx}
- --format {default,compact}
- --coarse-step-minutes N
- --refine-step-minutes N
- --refine-window-hours N
- --exact-eps FLOAT
- --max-hits N

Example commands:
- Snapshot:
  - `python global.py --from 2026-01-28 --to 2026-01-29 --mode snapshot`
- Snapshot + aspects:
  - `python global.py --from 2026-01-28 --to 2026-01-29 --mode snapshot --aspects`
- Snapshot + aspects (compact):
  - `python global.py --from 2026-01-28 --to 2026-01-29 --mode snapshot --aspects --format compact`
- Quarter peaks:
  - `python global.py --year 2026 --quarter Q1 --mode peaks --max-hits 20`
