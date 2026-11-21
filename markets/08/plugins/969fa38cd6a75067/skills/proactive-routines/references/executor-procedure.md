# Release C pilot executor procedure

1. Identify whether the user wants an explanation, a draft, activation, a change,
   or a stop. Complete only that scope. Reuse details already provided.
2. Ask one decision at a time for the routine's purpose, exact condition, days,
   local time/timezone, permitted sources and delivery destination. Clarify
   ambiguous AM/PM or a condition such as 'if I haven't logged' before scheduling.
3. Discover the host capabilities actually available: scheduler, relevant source
   connector, notification conditions, task inspection/update and durable context.
   Do not assume these from a product name or another user's account.
4. Before creating a dependent task, verify harmless authorized reads from Orendro
   and each required external source. Do not create a knowingly nonfunctional
   routine. Explain the exact missing dependency and prepare a useful fallback.
5. Show a compact preview of when it runs, what it reads, when it notifies and what
   it may write. Default unattended food/receipt checks to reading and proposing
   records. Do not add automatic food logging to an evidence-search permission.
6. If activation is authorized and supported, inspect relevant existing tasks and
   create/update the intended one through the host. Avoid duplicates. Use a
   self-contained saved prompt with its connection, timezone, condition and
   failure behavior. Do not mix time and event triggers when unsupported.
7. Verify the returned task ID, enabled state and schedule. Describe it as scheduled
   with first verification pending until an actual run succeeds. Saving a routine
   preference in Orendro is a separate operation and requires its own supported
   persistence contract.
8. If activation is unavailable, supply a ready-to-use configuration prompt and
   say clearly that no task has been created. Do not subscribe the user to a paid
   service, start a provider-owned worker or promise unsupported background access.
9. For receipt workflows, limit source/window, deduplicate evidence, distinguish
   purchases from consumption, and ask before saving candidate records unless a
   specific existing standing authorization covers that exact action. Do not alter
   the mailbox, send replies, or persist full email bodies as a default.
10. Support pause/stop/change through the actual executor. Do not imply that editing
    an Orendro note stops a task in ChatGPT or another bot. Report any remaining
    manual step accurately and show when executor state was last verified.

Runtime rules: no missing-record conclusion after a failed read; no guilt-based
wording; obey chosen quiet hours and notification limits; use the host's actual
quiet-result mechanism. If quiet conditional delivery cannot be guaranteed,
explain the limitation before activation. Keep the user's current explicit
instruction ahead of older preferences.
