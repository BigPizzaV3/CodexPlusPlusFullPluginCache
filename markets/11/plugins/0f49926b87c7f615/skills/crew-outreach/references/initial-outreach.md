# Initial outreach terms blocks

These are wording specifications for an explicitly reviewed adaptation, not new merge fields or conditional template syntax. Replace the explanatory square-bracket slots with verified literal values before presenting a final draft; never send slots or unresolved tags. Include only supported facts, and show all missing terms separately for user review.

Keep the selected template's existing subject, opening, project details, closing and signature. Insert the selected block immediately before its “Let me know if you're interested and available!” closing, or the equivalent closing in that template. Correct project-wide dates to the explicitly requested work dates and review any Shoot Days count; disclose that adaptation. Do not append a proposed rate next to an existing agreed Rate in a way that obscures which is which.

## Budget offer

> For [exact role and work dates], our proposed terms, subject to agreement, are:
> Labor: [currency and amount] per [pricing basis], covering [verified hours and meal basis].
> Kit/equipment allowance: [currency and amount] per [verified basis].
> Overtime: [verified proposed terms and threshold].
> Please let me know whether these proposed terms work for you.

If kit or OT are unknown, replace only that line with a direct question about the missing term, and flag the partial offer to the user. If labor amount, currency, basis or hours are missing or conflicting, pause the complete-offer draft and resolve them or explicitly choose a quote request. Do not infer OT multipliers from a unit default, blend a kit allowance into labor, or call a budget an agreed deal. Include separately verified prep terms when prep is requested.

Synthetic example: one shoot day, November 3, 2026; proposed labor USD 500/day covering 12 hours including meals; kit allowance USD 150/day; OT unknown. Draft the two amounts separately and ask “What overtime terms would apply beyond the covered 12 hours?” Disclose unknown OT to the user. A USD 650/day combined line would lose the distinction.

## Quote request

> Could you share your labor rate, the hours it covers, any kit/equipment charge, and your overtime terms for this role?

Identify the exact role and dates in the surrounding draft. Tell the user why this mode was chosen (for example, no reliable selected budget). Do not imply an offer by calling an unknown amount “our rate.” A partial known allowance can be stated as proposed with its verified basis after user review; ask explicitly about missing terms.

## Shipped template and live custom templates

The repository's separate `crew-initial-quote` email seed is a quote-request starting point using existing supported fields. It has no Rate field and no proposed-term tokens. The existing `crew` seed and saved templates keep their contents and confirmed-deal Rate meaning. A quote template is never selected merely because a budget is missing: the skill must first disclose and choose the mode.

The current list/render tools neither save templates nor add proposed-term fields. Budget offers therefore require the reviewed literal adaptation above. Do not invent `{Proposed Labor Rate}`, `{Hours Basis}`, `{Kit Allowance}` or conditional syntax. A saved company-owned “Crew - Initial” update is a separate proposed content change, with no automatic seed migration or overwrite. New source templates do not alter that live template or publish a plugin release.
