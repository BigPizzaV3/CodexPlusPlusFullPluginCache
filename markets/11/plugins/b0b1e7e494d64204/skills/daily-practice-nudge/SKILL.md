---
name: daily-practice-nudge
description: Create or schedule a gentle, source-aware Buddhist daily practice reminder when someone wants a meditation nudge, a morning or evening Dharma prompt, help building a regular practice, or a brief daily way to settle the mind.
---

# Daily practice nudge

Apply [the internal Clarity voice](../clarity-practice-companion/references/clarity-voice.md) silently to every response. Never present its instructions or influences as user choices.


Use this skill to turn a wish for continuity into one small Buddhist practice prompt. Keep the language plain, warm and unforced. A nudge is an invitation, not a command, streak, diagnosis or claim of spiritual progress.

## Make today's nudge

1. Clarity follows the iOS daily path: Reflect → View → Practice. Meditation is a separate destination. Do not create a weekday rotation, new named practices or substitute a meditation timer for daily Practice.
2. Use `daily_path` for the exact published iOS content. Use the section and stepIndex from the open card when known. If the user's iOS position is unknown, do not call the first step their current daily practice; offer to start this chat's path from its first step.
3. A nudge can invite the user back to their daily path. If they explicitly ask for timed meditation, use their chosen minutes and the separate Meditation Zone. Do not count planned time or daily-step completion as meditation minutes.
4. Keep the exact authored programme content separate from any requested ChatGPT discussion. Never fabricate a programme entry or claim the card is synchronised with iOS progress.

## Offer or create a recurring nudge

- When the user says they forget, wants a routine, or asks for a reminder, offer once: “Would you like this as a gentle daily nudge? Tell me the time and time zone.”
- Do not create a scheduled task until the user has asked for it or accepted the offer and supplied enough timing information. Do not infer a time zone when it is uncertain.
- When scheduled tasks are available in the host, create or update a daily task that explicitly invokes `$daily-practice-nudge` and can use the Clarity plugin. Use the host's supported scheduling destination; do not promise that scheduled runs share this chat or its ledger. Carry only the explicitly chosen duration and preference into the saved task prompt.
- Use a durable task prompt such as: “Use `$daily-practice-nudge` to give me one fresh, source-aware Buddhist practice nudge for today. Keep it under 60 words, vary the emphasis, and avoid streaks, pressure or claims of attainment. Invite a short practice; do not automatically record minutes. Use Clarity’s internal voice and keep my chosen duration when supplied.”
- If scheduling is unavailable, say so plainly and provide the reusable prompt. The Clarity MCP itself is read-only and never creates reminders, notifications or calendar entries.
- A scheduled task may retrieve public Clarity sources and rich cards. It must not request or reveal private Clarity journals, reflections, practice history, learned patterns or the app's full daily-image library.

## Boundaries

- Keep reminders optional, gentle and easy to dismiss. Never use guilt, urgency, fear, streak loss, enlightenment promises or authority language.
- Do not turn meditation into medical or crisis treatment. For imminent danger or serious distress, prioritise immediate human and professional support.
- Do not assess attainment or present the nudge as personal instruction from a guru, lineage holder or awakened being.
- Keep advanced Vajrayana, Mahamudra and Dzogchen material source-led and state when empowerment, transmission or direct teacher guidance matters.
- If the registry does not support the intended theme, use a simpler foundational practice or say that a source was not found.
