---
name: month-end-close
description: Run a month-end close on an Exact Online administration by delegating to DataFlowr's hosted closing agent, then poll it, report its findings and record accept/dismiss decisions. Use when the user asks to close a period, run close checks, review a period for irregularities, or asks what is still open before closing the books.
---

# Month-end close

## Overview

Do **not** assemble a close out of individual ledger queries. DataFlowr hosts a
closing agent that runs a deterministic check battery and a ledger-wide scan for
irregularities against one shared context. Delegate to it and report what it
finds.

Four tools: `closing_agent` starts or continues a close, `closing_agent_status`
polls it, `closing_agent_report` returns the full picture, and
`closing_agent_decide` records a human decision on a finding.

## Steps

**1 — Resolve the division and the period.**
Call `exact_online_divisions` first (see the `dataflowr-erp` skill). The period
is a financial year and period (`FinYear`, `FinPeriod`), not a calendar month.
If the user did not name one, the agent defaults to the last closed period —
say which one you used.

**2 — Start the close.**
Call `closing_agent` with the division and the period. It returns a short
correlation key (`close-XXXXXX`). Keep it: every follow-up call needs it.

An ordinary close evaluates that one period. Only when the user asks for a
quarter or a whole financial year to be swept, add `period_from` (the first
period of the range, same financial year): the line-level checks and the
ledger scan then evaluate every listed period from `period_from` through
`period`, one transaction read per period, while balance checks still read
the closing balance through `period`. Say which periods were evaluated when
you report. Never widen the range on your own.

The check battery and the ledger scan both start on their own. Do not try to
trigger them.

**3 — Poll while it works.**
A close that outruns the synchronous budget comes back as `running`. Poll
`closing_agent_status` with the correlation key rather than starting a second
close — a duplicate start answers `CLOSING_RUN_IN_PROGRESS`.

Status carries intermediate results: the checks report so far and the findings
stream. Pass the `next_cursor` back as `since` to get only what is new. Narrate
progress from it instead of going silent.

**4 — Report.**
When the run is terminal, call `closing_agent_report` for the full picture and
summarise it: the verdict first, then findings by severity, then what was
decided already. Findings come from three sources — deterministic checks, the
ledger scan, and the agent's own judgment — and the report labels them; keep
that labelling, it tells the user how much to trust each one.

Watch the scan's completeness state. Only a **complete** scan lets silence mean
"nothing found"; anything else means "not looked at yet", and you must say so.

**5 — Record decisions.**
When the user accepts or dismisses a finding, call `closing_agent_decide` with
its `finding_key` and a short note. Decisions persist per close period and
survive re-runs, so re-running is a way to *prove* something was resolved rather
than to clear the slate.

## Hard stops

- No division, or a period the administration does not have → ask, do not guess.
- The run failed or stalled → report that plainly with the error the tool
  returned. Do not paper over it with a partial summary.
- The close proposes a correction booking → it needs explicit approval. Present
  the entry in full and wait; never approve on the user's behalf.
