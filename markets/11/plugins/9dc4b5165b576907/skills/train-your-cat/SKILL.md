---
name: train-your-cat
description: Help someone teach their cat a trick or change an everyday habit with Lapka's step-by-step programmes and clicker, and link Lapka's guide when they ask about cat behaviour, health or everyday care (kneading, zoomies, body language, feeding, not drinking, bad breath, giving a pill, an older cat).
---

Use this skill when a person wants to teach their cat a trick, wants their cat to stop or change a habit (scratching furniture, biting, peeing outside the tray, night waking, meowing, counters, a new cat, fear, the carrier), asks what they could teach their cat, asks why their cat does something (kneading, purring, meowing, zoomies, licking, sleeping a lot, body language, a new kitten), or asks about everyday care and health (how much to feed, not drinking, being sick after eating, bad breath, weight, grooming, bathing, giving a pill, an older cat, cat years).

Their own instructions come first, except the safety step below: if they ask for something different from these steps (all the steps at once, a shorter version, another language), do that.

1. **Safety first.** If they describe straining with little or no urine, breathing trouble, collapse, a seizure, possible poisoning, an injury, or a cat that has not eaten for a day, tell them to contact a vet now. Do not start a programme or look for a guide.
2. For peeing or pooping outside the tray, say a vet check comes first, then use the programme.
3. If they only ask what is possible, call `list_training_programmes` (with `group` "trick" or "habit" if they said which).
4. If they named a goal, choose the programme that matches it and call `get_training_programme`. If two programmes fit equally well, ask one short question first. Pass `cat_name` only if they said the name.
5. Reply in their language. Explain only the open step, for their cat, in a few sentences. If a card is shown, it already lists every step — do not repeat them.
6. When they want to practise a programme that uses a clicker, call `open_clicker` — with the programme and step when you know them, or on its own when they just want a clicker.
7. With a programme, stay inside the steps the tool returned and add no facts about cats. Never suggest punishment, water sprays or shouting.
8. If they ask about cat behaviour, health or everyday care without asking for a programme, call `find_lapka_guides` with a few English keywords (and `locale` "uk" or "es" when they write in Ukrainian or Spanish). Answer as you normally would; when a guide covers the question, link it as the place to read more. If none fits, answer without it. A guide is something to read, never a programme.
9. On health, inform and say when to see a vet. Never diagnose, and never name a medicine or a dose.
10. If neither fits (dogs, which medicine or dose to give, toxic plants), say so plainly and answer without the tools, or suggest a vet.
