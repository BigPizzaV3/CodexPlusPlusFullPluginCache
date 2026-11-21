# Feed validation — when a platform rejects your products

For "Google rejected my products", "Heureka says my feed has errors", "the platform can't download my
feed". Conviu validates the feed an export produces against that format's rules, so you can tell
whether the problem is the data, the feed, or the delivery.

## What these tools give you — and what they don't

**Be honest about this limit:** the MCP returns validation **counts and status**, not the list of
individual issues. You can tell the user *how many* errors a feed has and *why a validation run
itself failed* — you cannot enumerate which product broke which rule. For the item-by-item
breakdown, point them to the validation detail in the Conviu app. **Never invent specific validation
messages.**

| Tool | Takes | Returns |
|---|---|---|
| `get_data_writer_job_latest_validation` | `dataWriterJobUid` | `uid`, `validationId`, `state`, `createdAt`, `completedAt`, `errorCount`, `warningCount`, `infoCount` |
| `get_data_writer_job_validation` | `uid` = **the validation's** uid | adds `feedUrl`, `failureReason`, `failureMessage` |
| `trigger_data_writer_job_validation` | `uid` = **the export's** uid | runs a fresh validation (write op) |
| `get_data_writer_job_latest_download_logs` | `dataWriterJobUid` | recent download activity — who fetched the feed |

⚠️ **The `uid` trap:** three of these take a parameter literally called `uid`, but it means different
things — for `trigger_data_writer_job_validation` it's the **export's** uid; for
`get_data_writer_job_validation` it's the **validation's** uid (which you get from
`get_data_writer_job_latest_validation`). Swap them and you'll get "not found", or validate the wrong
thing.

## The flow

1. **Identify the export** — from context, or `list_data_writer_jobs` matched by name.

2. **`get_data_writer_job_latest_validation`** with the export's `dataWriterJobUid`. Read:
   - `state` — did the validation actually finish?
   - `errorCount` — above zero means the feed's content breaks the format's rules.
   - `warningCount` / `infoCount` — softer issues, often still worth a mention.
   - `completedAt` — how old is this? A validation from before the user's last fix proves nothing.

3. **Need more?** Take the `uid` from step 2 into `get_data_writer_job_validation`. It adds the
   `feedUrl` that was checked plus `failureReason` / `failureMessage` — these explain why the
   **validation run** failed (e.g. the feed couldn't be fetched), which is a different problem from
   the feed's contents being wrong. Don't conflate them.

4. **No validation, or a stale one?** Offer `trigger_data_writer_job_validation` (the export's uid).
   It's a write operation that consumes resources — say what it does, get a clear yes, then read the
   result once it completes.

5. **Platform can't download the feed?** That's delivery, not content. Check
   `get_data_writer_job_latest_download_logs` for recent fetch activity, and confirm the `feedUrl`
   from step 3 is the address the platform was actually given.

6. **Look upstream.** Bad data in, bad feed out. If the errors are about missing or wrong values,
   inspect the source import (`list_data_queries` → `get_data_source`) and the items themselves
   (`list_items` with an FQL filter — see `fql.md`). A field missing on 400 products is an import
   problem, not an export problem.

7. **Report in plain words.** "Your Heureka feed came back with 12 errors and 30 warnings in this
   morning's check" — then what you can do about it, and where in Conviu to see the item list.

## Three problems users all call "it doesn't work"

- **Content errors** (`errorCount` > 0) — the feed exists but breaks format rules → fix the data.
- **Validation run failure** (`failureReason` / `failureMessage`) — the check couldn't complete, often
  an unreachable feed → fix access, then re-validate.
- **Empty or blocked export** — there's no feed to validate at all → that's `diagnose.md` (check
  `active`, the run logs, and the "block export when…" guards).

Establish which one you're facing before proposing a fix.

## What a platform actually requires

If the user asks what Google/Heureka/Zboží demands for a given field, **don't answer from memory** —
call `search_documentation` and answer from what comes back, citing the page URL. Platform rules
change, and a confidently wrong answer costs the user real work.
