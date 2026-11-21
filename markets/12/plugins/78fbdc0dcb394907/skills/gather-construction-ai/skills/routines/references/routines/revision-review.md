## revision-review

**Cadence:** Event-driven — run immediately after each new programme revision is imported (pair it with the import, not the calendar)
**Surface:** Desktop
**Prerequisites:** versioned baseline history (`programme/programme-baseline-<rev>.json` — programme-import v2 creates this); `ce-register.md` kept current; `{{FOLDER}}/routine-state/revision-review/last-run.md`
**Priority:** Standard

**Instructions:**
```
A new programme revision has just been imported for {{PROJECT}}. Run the Programme Advisor's
Revision Review (Mode 4): $programme-compare between the last accepted revision (per
routine-state/revision-review/last-run.md) and the new one, judged against the 31.3
acceptance grounds scoped to WHAT CHANGED.

Lead with float/TRA erosion on critical and near-critical activities — both revisions' STORED
values, never recomputed — and cross-reference every eroded activity against ce-register.md:
an erosion with no corresponding CE is the headline finding ("no corresponding CE found"),
stated plainly, while whoever produced the revision can still explain it.

Update routine-state/revision-review/last-run.md with the revision compared and the erosion
table. If this is the first import (no prior revision), say so in three lines and just record
the baseline position for next time.
```
