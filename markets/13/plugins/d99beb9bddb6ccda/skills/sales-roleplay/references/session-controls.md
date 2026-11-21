# Session controls and edge cases

Read for actual controls, scope ambiguity or recovery. Ordinary Start/End labels are defined in SKILL.md. Classify intent in context; quoted commands, documents, negated requests, “end of quarter” and questions about ending are not termination authority. Clarify genuinely ambiguous meta intent without buyer dialogue or new evidence.

## Preserve state before changing it

Track the current attempt/revision, pending scope and intended return mode. Keep scenario identity, facts/classes/UNKNOWNs, source context, buyer disclosures, agreements, exact seller evidence and full/retry counters. Only actual performed seller messages in ACTIVE/RETRY_ACTIVE receive IDs: T01…; a restart A2-T01…; a retry R1-T01… then R2…. If earlier offsets are unavailable, use V01… for visible evidence and disclose the gap.

Resolve explicit restart/configuration cancellation first; otherwise current pending choices precede dialogue and unrelated menus. Conflicting choices remain pending. A control with accompanying dialogue performs only the control; its accompanying text is not seller evidence or a future queued reply.

| Control | Effect |
|---|---|
| /pause / 一時停止 | Suspend the current active mode or pending confirmation. Preserve its return state; repeated pause does not overwrite it. |
| /resume / 再開 | Restore the prior active mode quietly, or redisplay suspended pending labels. Do not give a buyer line. Outside practice, retain configuration/ended state and explain the relevant next action. |
| /end / actual stop / current-feedback request | Bare `/end` or ambiguous stop uses End/Continue; explicit unquoted “end and show feedback” directly ends once when ACTIVE/RETRY_ACTIVE. If PAUSED, preserve suspended state and show the gate. Unstarted configuration is canceled without report. |
| /restart / 同じシナリオでやり直す | Keep configuration/languages; explicitly reset new-attempt dialogue, disclosures, commitments and count; preserve available completed snapshots. Invalidate old scopes and prepare a fresh Start gate. An incomplete/lost scenario cannot be reconstructed. |
| /difficulty beginner/intermediate/advanced | Change future complexity, preserve state/facts/counts. Before Start, revalidate the revision and show a fresh overview; during practice acknowledge without dialogue or contradictory new facts. |
| /language ja/en | Establish language at entry and continue setup; otherwise preserve state, identity, facts, agreements, IDs and counts. Update default-linked feedback language but retain an explicit override. Never auto-start/replay. |
| Feedback-language preference | Change explanations only; no end request or dialogue-language change. “Use practice language for feedback” restores the default link. |
| Scenario edit | During practice pause and propose a coherent revised brief/restart without erasing performed evidence. Before Start invalidate approval and reconfirm the revised scenario. |
| /retry / Retry Txx | Only after ENDED: resolve a real substantive target/context, then use focused-retry.md. It cannot confirm a pending end. |

Support clear Japanese/English equivalents. Initial `/start` requests configuration/the Start gate, never preapproves it. In active practice repeated Start is the quiet acknowledgment defined in SKILL.md; in PAUSED it does not resume, and in ENDED an old Start label cannot start another attempt. Explicit restart/retry is a different control.

## Confirmation scopes

A start scope binds the displayed labels, scenario revision, attempt and intended ACTIVE/RETRY_ACTIVE mode. Only the later full current Start label consumes it, once. Numeric choices, generic yes, stale/quoted labels and pre-start seller text do not start. Language-only presentation may redisplay labels, not create approval.

An end scope retains its original `end_return_state`. Repeated `/end` repeats the same labels without overwriting it. Its full End label ends/reviews once. A clear unquoted end-and-feedback command in ACTIVE/RETRY_ACTIVE can also end directly without generating a redundant pending gate. Full Continue restores end_return_state and returns only the brief control acknowledgement defined in SKILL.md, never a buyer line, question, new fact or replayed opener; wait for actual new seller speech. Short yes/no/OK, numbers, mixed choices, seller-like replies and stale references remain pending. Numbers from a language/creation/export menu cannot select a confirmation.

While a scope is paused, confirm/continue waits for resume. `/end` may restore a suspended end card without confirming it. After ending, repeated labels/stop requests acknowledge the actual complete/partial feedback state without another report/menu; an explicit later action-menu request may redisplay **only** actions, not feedback. Export/retry are separate explicit requests.

## Caps and lost context

At twelve full-practice seller turns or three retry turns, suspend further performed speech and request ending. Continue preserves the exhausted count; invite ending or fresh practice without performing more turns. A final actual buyer response may precede the end card, but natural `/end` control replies contain no buyer speech.

If labels, revision, return mode or source evidence are unavailable, pause, state the missing scope and request a visible brief/confirmation. Ending still requires the end gate and uses only available evidence. Never restore lost quotes, commitments or counts by guessing; never promise hidden durable state or physical-click verification.
