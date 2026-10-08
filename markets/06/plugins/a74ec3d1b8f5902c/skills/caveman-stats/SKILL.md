---
name: caveman-stats
description: Use when the user asks for Caveman usage, cost, savings, score, or workflow statistics from available Caveman
  evidence.
---
## Host capability adaptation

1. **Native host capability:** when ChatGPT/Codex exposes a native tool or connected source that satisfies this task, use it.
2. **Original external runtime:** when the upstream runtime named by this skill is actually available, use it as documented below.
3. **Instruction-only fallback:** when neither is available, perform only the reasoning/instruction portion that remains valid, state the limitation, and never fabricate tool output, successful execution, or persisted state.

Use the original external runtime only when it is actually available; otherwise provide the valid instruction-based fallback and clearly disclose that execution was not performed.


In Claude Code, `src/hooks/caveman-mode-tracker.js` resolves `src/hooks/caveman-stats.js` next to itself and runs it on `/caveman-stats`. The hook does not block the prompt: it supplies the report through `hookSpecificOutput.additionalContext` with an instruction to print it verbatim inside a fenced code block. Do exactly that, and do not calculate, recompute or re-round the numbers yourself.

In Gemini CLI, direct the user to `/stats model` for current session token usage or `/stats session` for session statistics. Gemini custom commands are prompts; they cannot invoke the built-in command or read its live session metrics. Never read Claude Code transcripts as Gemini usage. In other hosts, use a native usage report if one is available; otherwise say that current session usage is unavailable. The Claude reader and its lifetime history apply only to Claude Code. Savings remain unknown in every host without a measured comparison.

The report shows recorded output and cache-read tokens, response counts, and mode attribution where available. Savings are unknown: the transcript has no measured comparison without Caveman. Do not infer saved tokens, percentages, dollars, rule overhead, or a net result from output counts or the current mode.

`--all` and `--since 7d` aggregate the latest recorded output count per session. `--share` reports observed usage with savings unknown. Historical `est_saved_*` fields are ignored; their original history rows remain on disk. The statusline shows the active mode without the retired savings badge.

Original/current memory-file pairs are reported by their measured byte sizes. Those file-size differences do not establish provider token or billing savings. See `docs/HONEST-NUMBERS.md`.
