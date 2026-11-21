# Pattern 17: Correspondence Register (imported notices and emails)

The Gather API holds site records, not the paper trail — notification dates, PM replies, and
instructions live in email and document systems. `$correspondence-import` parses exported
correspondence (`.eml`, PDF, pasted text; `.msg` is refused with export instructions) and writes
a local register that evidence-consuming skills cite instead of relying on user-asserted dates.

**File convention:** `correspondence/correspondence-register.md` in the working directory.
Created and updated ONLY by `$correspondence-import`. One row per item:
`[COR-NNN]` | date sent/received | direction (in/out) | from → to | subject | **type as
user-confirmed** (CE notification / early warning notification / PM reply / instruction /
quotation submission / general / UNCLASSIFIED) | linked CE ref (user-confirmed against
`ce-register.md`) | key excerpt (as recorded) | source filename.

**Rules for consuming skills:**
1. Cite items as "[COR-NNN] ([date], [from] → [to], "[subject]")". Excerpts are quoted **as
   recorded — never paraphrased into a stronger claim** than the words carry.
2. **Classification is user-confirmed at import, never inferred by a consumer.** An
   UNCLASSIFIED item is "correspondence dated [date]", not "the clause 61.3 notification" —
   whether an email legally constitutes a notice is a judgement the user (or their lawyer)
   makes, not the plugin.
3. The register **proposes** `ce-register.md` date/status updates; they are applied only on
   explicit user confirmation, and never on a non-interactive run.
4. Absent register → consumers fall back to user-supplied dates exactly as before (say so
   once); a procedural claim with neither register item nor user date stays NO RECORDS.
5. **Privilege and sensitivity:** correspondence in a live or contemplated dispute may be
   legally privileged — the importing skill reminds the user to clear dispute correspondence
   with their legal advisers before importing it into any tool (see `docs/rics-ai-standard.md`
   §3.1), the file stays local (gitignore), and register content is never included in outputs
   destined for the other party.
6. Only `$correspondence-import` writes the register. A register whose `project` does
   not match is ignored (say so).
