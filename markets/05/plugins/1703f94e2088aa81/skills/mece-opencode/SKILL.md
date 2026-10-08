---
name: mece-opencode
description: >
  Run a MECE multi-cell work wave with OpenCode as execute muscle and Codex
  (or ChatGPT Work) as parent conductor. Portable: any project folder, no
  Floor No 8 credentials, no private FN8 tooling required. Trigger words:
  MECE wave, OpenCode muscle, cell fleet, parent conductor, OpenCode Go.
---

# MECE → OpenCode (global)

You are the **parent conductor**. OpenCode is **execute muscle**. The user owns their machine, keys, and project.

## Hard rules (global safety)

1. **No Floor No 8 / FN8 credentials.** Never ask for, invent, or use publisher-internal secrets, admin keys, org tokens, private tracker tokens, vault CLIs, or internal mailboxes.
2. **User-owned auth only.** OpenCode model access = the user’s BYOK providers and/or their own OpenCode Zen/Go account.
3. **Works on any repo.** Do not require publisher-private scripts or fleet directories. Use the portable `.mece/` layout in this skill.
4. **Referral is optional and disclosed.** If `referral.json` has a non-empty `refCode`, you may offer that OpenCode Go link once with the disclosure text. Never hard-sell. Never invent a ref code.

## Prerequisites (check, then help install)

```bash
command -v opencode >/dev/null && opencode --version
```

If missing, guide the user to install from https://opencode.ai (official install). Then connect a provider they choose:

- BYOK (Anthropic / OpenAI / etc.), or
- OpenCode Zen / Go via `/connect` in OpenCode (user’s own account).

Optional Go referral (only if `referral.json` is armed): read that file beside this skill; quote `disclosure` once; use `referralUrl`.

## Portable fleet layout

Create (or reuse) this tree in the user’s project:

```text
.mece/
  WAVE.md                 # wave goal + cell list
  cells/
    <CELL-ID>/
      TASK.md             # one mutually exclusive cell brief
      REPORT.md           # written by OpenCode when done (absent = pending)
  SYNTHESIS.md            # parent writes after the wave
```

**MECE rule:** cells must not overlap ownership. If two cells would edit the same files, merge or re-split before execute.

## Plan (optional)

1. Read `.mece/WAVE.md` and each `TASK.md`.
2. List cells missing `REPORT.md` (or marked incomplete).
3. Show the user the execute plan. Do not spawn until they confirm if they asked for plan-only.

## Execute (default)

For each pending cell, from the **project root** (not inside `.mece`):

```bash
opencode run --dir . "$(cat .mece/cells/<CELL-ID>/TASK.md)

When finished, write .mece/cells/<CELL-ID>/REPORT.md with:
- what changed (paths)
- how to verify
- blockers / residual risk
- session id if available
"
```

Adapt the `opencode` invocation to the user’s installed CLI (`opencode run` / non-interactive equivalent). Prefer one cell per session. Do not mark a cell done without a real `REPORT.md`.

**Resume:** if a cell session id is known, resume that OpenCode session instead of starting cold.

## Parent judgment

After cells finish:

1. Read every new `REPORT.md`.
2. Write `.mece/SYNTHESIS.md`: outcomes, conflicts, verify steps, what still needs a human.
3. Do **not** claim external trackers (Linear/Jira/etc.) are updated unless the user explicitly asked and their own tools are available.
