# Presenter selection and consistency

The presenter is the identity lock. Choose once, keep them across the ad and every
variation. Swapping mid-run is the fastest way to make a campaign look automated.

## What a presenter is defined by

Four attributes decide whether a presenter reads as credible for a category:

1. **Who they are** — apparent age band, look, energy level
2. **What they present** — the category they are plausible in
3. **Where they appear** — their default setting
4. **How they speak** — pace, warmth, vocabulary

Ask for the first two. Infer the rest and say what you assumed.

## Archetypes that work per category

| Category | Archetype that lands | Voice | Avoid |
|---|---|---|---|
| Consumer tech, apps | The friend who just discovered it | Casual, warm, no jargon, talks to camera like a friend | Salesperson energy; spec-sheet recitation |
| Marketing, B2B, SaaS | The practitioner with results | Punchy, fast, results-first, hooks hard | Vague thought-leadership |
| Startup, creator tools | Building in public | Energetic, scrappy, honest about the grind | Polished corporate delivery |
| Beauty, fashion, lifestyle | Effortless taste | Warm, radiant, genuinely joyful — never aloof or posed | Cold editorial detachment |
| Home, kitchen, practical goods | Competent and unfussy | Plain, direct, demonstrates rather than describes | Over-enthusiasm about an ordinary object |

Pick the archetype from the **product category**, not from what looks most attractive. A
luxury-coded presenter selling a $12 kitchen tool reads as a stock-photo ad.

## Consistency across a campaign

- **Same `avatar_id` everywhere.** Reuse it in variations, in follow-ups, in the next
  product's ad if the brand is the same.
- **Same setting family.** A presenter who appears in a different room every video reads
  as a stock model, not a person.
- **Same voice register.** If ad one is casual and ad two is corporate, they are two people.

When the user asks for a second ad, **reuse the existing presenter by default** and only
create a new one if they want a different audience segment.

## Creating a good one

`create_avatar`. Ask three things, then create:

1. Who they are — age band, look, energy
2. What they present — the category
3. The setting they usually appear in

Everything else is adjustable later with `update_avatar`. Do not run a questionnaire; the
picker flow already asks plenty.

## What a presenter is not

A generated presenter is a **host or demonstrator**. They are not a customer. They have not
bought, used, or benefited from the product. Any script implying otherwise fails the truth
gate in `SKILL.md` — see "No synthetic testimonials".
