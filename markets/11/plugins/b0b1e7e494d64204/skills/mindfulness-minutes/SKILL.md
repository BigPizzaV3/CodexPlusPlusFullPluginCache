---
name: mindfulness-minutes
description: Track completed meditation and mindfulness minutes reported in this chat, show a practice card, start a quiet timer, or review a week of practice.
---

# Mindfulness minutes

Apply [the internal Clarity voice](../clarity-practice-companion/references/clarity-voice.md) silently to every response. Never present its instructions or influences as user choices.


Help the user keep a small, honest practice log in this chat. Start immediately with known information; ask only for missing minutes or a local date. Explain once that this is a chat log, not account storage or native-app sync.

## Record or review practice

- Count only practice the user explicitly says they completed: meditation, text reading, teaching reading, audio listening or virtual offering. Keep these categories distinct; reading minutes are not meditation minutes. Never count a plan, reminder, timer starting, or silence as completed practice.
- Keep a compact visible ledger with columns `id`, `date`, `minutes`, `kind`. Allocate a stable session ID on first report; preserve it in later cards. Timer confirmations allocate stable IDs in the portable component log; when the user explicitly shares that log, preserve its IDs. A repeated ID is the same session, not another practice. If two reports might describe the same session, clarify before adding them.
- Resolve “today” in the user's time zone. Ask if the local date is unknown. Accept corrections by updating the original entry; remove an entry when asked. Do not infer missing days as zero minutes or failed practice.
- Call `practice_minutes` with the confirmed entries available in the visible chat or a user-supplied log, the local date, and any user-chosen timer duration. If they ask for a timer without a duration, omit minutes so the card keeps their saved choice; first use defaults to one minute. Say “reported minutes”, not “all your practice”.
- The component can confirm, remove, export and import supplied entries through a read-only calculation. Its log remains in the open card until the user explicitly exports or shares it. Do not claim it has saved to their account. After a report or a shared log arrives in the chat, acknowledge it once and update the visible ledger. No streaks, rankings, attainment scores, quotas or guilt.
- If history is unavailable after a new chat or context loss, ask for their last ledger. Never reconstruct it from guesses or claim that ChatGPT memory is a reliable database. Offer the card's JSON export or a copyable ledger when they want to carry it elsewhere.
- For a daily nudge use `$daily-practice-nudge`; the reminder offers practice and does not automatically log it.

## Useful responses

“I sat for 12 minutes today” → add one confirmed meditation session and show the card.
Do not invent additional categories. If reported activity does not match a native category, clarify what the user wants to record.
“How much this week?” → rolling seven local dates including today; state the date range and available-log scope.
“Show a quiet timer” → card with existing reported entries; add nothing until explicit confirmation.

Use `practice_minutes` for data-only calculation and updates. For a timer, use open_clarity with view: meditation, supplying minutes only when the user chooses a duration. To show a new minutes card use `open_clarity` once with `view: minutes`, `today`, `sessions` and `minutes`. Do not open a home card first or render another card merely to acknowledge an update.
