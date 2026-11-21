# PhygitAi — 3 × 2 first-use card selector

## Intended user-visible layout

Use short introduction then two equal-height rows of **three distinct interactive boxed cards** on desktop (not a markdown list or table):

[ AUDIT     ]  [ COMPARE   ]  [ INSPECT   ]
[ DETECT    ]  [ EXPLAIN   ]  [ IBR       ]

Card captions: `Audit: Full project review`, `Compare: Compare two projects`, `Inspect: Examine claims and sources`, `Detect: Find documented gaps`, `Explain: Understand a finding`, `IBR: Trace one design decision`.

## Supported rich-UI implementation hint (do not print code to user)

If the host supports the ChatGPT DIL component environment, render six `grid-item` siblings in a `<grid>` of **3 columns on desktop**, each containing a visible bordered/rounded `<card>` or `<pressable>` surface. Keep one pressable action per card; issue a real host turn on click using `GenUI.issueNewTurn(...)` with the literal matching instruction. Suggested prompts:

- Audit: `PhygitAi audit. Please help me begin a project review; ask for my project description.`
- Compare: `PhygitAi compare. Please help me compare two projects; ask for the two project descriptions.`
- Inspect: `PhygitAi inspect. Please ask what project claims or documents I want you to inspect.`
- Detect: `PhygitAi detect. Please help identify documented gaps or discrepancies; ask for my available evidence.`
- Explain: `PhygitAi explain. Please ask which existing assessment finding I want explained.`
- IBR: `PhygitAi ibr. Please help trace one design decision; ask for the decision context.`

A native grid might be expressed using `<grid columns={3}>` on a desktop view. The client should reflow to two or one column on narrower viewports; a layout with suitable `minChildWidth` is another option when its calculated width yields 3 columns in the desktop chat window. Do not render both an interactive grid and an extra Markdown list/table. These are implementation instructions, not a claim that the skill package itself can dictate host UI layout.

Keep text on each card short enough to fit; no nested click handlers on the same surface. If the host cannot render actionable cards, use its most visually compact, accessible alternative and never pretend static text is clickable.
