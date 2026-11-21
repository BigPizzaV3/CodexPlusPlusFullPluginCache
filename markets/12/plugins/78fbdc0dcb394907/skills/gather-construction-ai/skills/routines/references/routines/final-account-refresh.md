## final-account-refresh

**Cadence:** Monthly, {{ASSESSMENT_DAY}} plus 2 days (after the month-end close), and ad hoc before any settlement meeting
**Surface:** Desktop
**Prerequisites:** `commercial-profile.md` (Pattern 14); `ce-register.md` kept current; `{{FOLDER}}/routine-state/final-account-refresh/last-run.md`
**Priority:** Standard

**Instructions:**
```
Run $final-account for {{PROJECT}}.

Read {{FOLDER}}/routine-state/final-account-refresh/last-run.md (last month's recorded
position: records-supported net, claimed net, negotiation gap, per-CE statuses and grades) and
lead the reply with what MOVED since then: CEs that changed status (unagreed → agreed, newly
notified), evidence grades that changed, movement in the negotiation gap, and any open risk
that is new or now urgent (a 61.3 bar inside 2 weeks, a deemed-acceptance clock that became
available). The full statement follows the movement summary, not the other way round.
If nothing moved, reply in three lines and stop — a static final account is a finding.
Never blend records-supported and claimed totals; no settlement predictions.
Update routine-state/final-account-refresh/last-run.md with this month's position (both nets,
the gap, per-CE status/grade list) for next month's movement line.
This output is internal — the negotiation appendix is never issued to the other party.
```
