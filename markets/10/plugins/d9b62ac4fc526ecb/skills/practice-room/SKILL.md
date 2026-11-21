---
name: practice-room
description: Use when someone wants to practice, rehearse or role-play what they plan to say to their partner (boyfriend, girlfriend, husband, wife). Opens the HeyBonds Practice Room.
---

# HeyBonds Practice Room

When the user wants to rehearse a conversation with their romantic partner, call `rehearse_partner_conversation` with:
- `topic`: what they want to bring up, 1 short sentence in their words
- `partner_name` only if they said it
- `partner_gender`: infer it from words like wife, girlfriend, she, husband, boyfriend, he. If they only said "partner" and gave no clue, ask in 1 short question first ("Is your partner a man or a woman? So their voice fits."). Use `unspecified` only if they prefer not to say
- `context`: 1 to 3 sentences of background they already shared, nothing else
- `partner_style` only if they described how their partner usually reacts

If they ask for today's HeyBonds Daily (or a daily challenge), call `rehearse_partner_conversation` with `daily: true` and `topic: "daily challenge"`. The room shows that day's light everyday scenario.

After the tool opens, reply with 1 short sentence inviting them to answer their partner's opening line in the practice room, or tap Talk it out loud to say it with their voice. Do not role-play the partner in chat unless they ask.

When they come back with their score, help them write the final version in their own voice.

Do not use it for: crisis situations, self-harm, threats, violence or fear of a partner, anything sexual, or diagnosing anyone. In those cases respond with care and point to real help.
