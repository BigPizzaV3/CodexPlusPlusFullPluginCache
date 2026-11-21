# Pattern 21: Fetch-Once-Per-Run Cache

When an agent chains multiple skills over the same project and date range (e.g. a Weekly QS
Pack running `progress`, `labour`, `access`, and `delay-analysis` back to back), each skill
would otherwise re-fetch the same `getCachedReport` or `getShiftRecords` data independently.
Avoid the repeated identical fetch:

1. **Cache key.** `(project UUID, report name or "shiftRecords", from, to)`.
2. **Location.** `.gather-cache/<project>/<report>_<from>_<to>.json`, relative to the working
   directory — git-ignored (see `.gitignore`). This is local scratch state for one agent run or
   session, not a durable store.
3. **Write once.** The first skill in a chain that needs a given key fetches it from the Gather
   MCP and writes the raw JSON response to that path before using it.
4. **Read thereafter.** Any later skill in the same run or session that needs the identical key
   reads the cached file instead of calling the MCP tool again. Confirm the file's `(project,
   report, from, to)` matches exactly before trusting it — a near-miss (different date range,
   different project) is always a fresh fetch, never adjusted from a cached one.
5. **Invalidation.** Treat a cached file as stale and re-fetch when either holds: (a) more than
   24 hours have passed since it was written, or (b) a re-run is being done specifically to pick
   up new data — in that case call `getShiftRecords` with `modifiedSince` set to the cache's
   write time (Pattern 4) rather than trusting the stale file.
6. **Never cross projects.** A cache entry is scoped to exactly one project UUID. Never reuse or
   merge cache entries across projects, even where a directory holds multiple project profiles.
7. **Not a substitute for citation.** Data read from the cache is cited exactly as if freshly
   fetched (report name, date range, data date) — the cache is a token-saving mechanism, never a
   reason to omit provenance.
