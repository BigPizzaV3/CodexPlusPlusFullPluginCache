# History personalization

Use `get_routine_style_profile` only for the selected library and bounded lookback. It reports historical patterns such as duration, interval count, transitions, common sections, move names, adjacent pairs, categories, split-side use, spring distribution, and repetitions. It does not represent permanent preferences, health information, or medical limitations.

Use `get_routines` for concise discovery and `get_routine` for a named routine’s detailed structure. Older timers may have names but no move IDs. An exact unambiguous name match can inform programming; an ambiguous match must not be guessed.

Preserve explicit user constraints over historical patterns. For gap-filling requests, identify what is underrepresented in the selected history and describe that influence in the preview. Use a fresh sequence unless the user explicitly asks for a duplicate.
