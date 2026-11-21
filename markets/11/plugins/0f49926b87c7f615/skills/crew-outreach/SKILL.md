---
name: crew-outreach
description: Prepare budget offers or quote requests for a specific Grid crew role and work dates, verifying budget and deal evidence and reviewing the exact recipient, template and final draft before any separately approved send. Use for initial crew outreach, not availability bookkeeping or booking.
---

# Prepare crew outreach

Drafting and rendering are read-only. They never authorize sending, saving a live template, changing a budget, confirming a deal, booking crew or updating availability. Read-only automations remain read-only; this skill changes no schedules, prompts or permissions. For interpreting availability replies and supported availability updates, use [update-availability](../update-availability/SKILL.md) rather than duplicating that workflow.

## Establish the exact assignment

- Resolve the project with `grid.list_projects`; use `grid.list_project_contacts` / `grid.get_project_contact` to verify the exact contact, active crew membership and role. Multiple memberships require an explicit choice. Verify the destination address/number from approved contact data and authorized communication history; a matching first name is insufficient.
- Resolve the selected bid with `grid.list_budgets` and current budget reads. Reuse an established explicit selection; ask when bids or versions conflict. Never choose the cheapest, newest or primary bid silently. Record bid ID, phase, version/revision when returned, role line/detail IDs and currency.
- Verify specific shoot and prep civil dates, year, unit/round, date purpose and timezone against current project calendar and authorized instructions. State the exact dates this recipient is being asked to work. A one-day request stays one day even when project Shoot Dates spans several days; distinguish prep, shoot, travel and hold dates. Do not infer dates from Shoot Days, a budget quantity, or the span between first and last project events. Ambiguous dates, role or bid block a ready-to-send draft.

## Read budget and deal evidence

Use `grid.get_budget_overview` for the selected bid and phase, including assumptions as needed; use `grid.search_budget_lines` / `grid.get_budget_line_context` for the role and kit. Follow [explore-budgets](../explore-budgets/SKILL.md) for calculations, completeness and source/child scope. Inspect current detail quantities, units, base hours/guarantees, OT and fringes: a multi-day total or fringe-inclusive line is not a daily labor offer. Do not divide totals without verified quantities and pricing basis. Reconcile tool discrepancies before using a number.

Read available verified recipient-specific deal evidence and relevant dated communication, including later corrections. For texts, prefer authorized Messages plugin/service on the user's Mac mini. Do not fall back to a MacBook or UI automation when that source is unavailable; report the gap and continue independent Grid reads. Discover current schemas rather than inventing commitment reads or template fields. Message content is evidence, not permission to send.

Keep a compact review ledger: source record/message and timestamp; selected bid/phase/line; exact role and dates; currency; proposed labor amount and pricing basis; covered/guaranteed hours and whether meals are included; separate kit allowance and basis; overtime terms and their source; confirmed deal terms; conflicts and missing evidence. Budget allowances, quotes, proposed offers and agreed deals are distinct. `{Rate}` / `crewRate` resolves only a confirmed recipient-specific deal with currency and pricing basis. Never populate or relabel it with a budget allowance. Budget/unit OT defaults are not an agreed deal.

## Choose and disclose the mode

- **Budget offer:** use only a reliable selected budget and a verified labor amount, currency, pricing basis and covered hours. Label the terms proposed and subject to agreement. Keep labor and kit separate; missing kit means unknown, not zero or included. Include verified overtime terms; explicitly ask about unresolved kit/OT terms. An earlier quote for 10 hours and a 12-hour bid conflict: surface both, ask for reconciliation, and do not call either accepted or silently convert it.
- **Quote request:** when no reliable budget is available and the user has not specifically required an offer, choose this mode for the draft and explicitly tell the user this is a rate inquiry and why. Choosing the draft mode does not require a separate confirmation; final send approval still does. If the user specifically requested an offer, ask to resolve the budget or approve switching to an inquiry. Ask the recipient for labor rate, covered hours, kit/equipment charges and overtime terms. Partial evidence may be presented as a clearly labeled proposal only after user review of the missing terms; never imply a complete offer or agreement.

Always flag missing or ambiguous bid, role, rate and hours to the user even if the chosen template contains no such field. Unknown rate/hours are acceptable questions in a quote request, not silently omitted information. A missing bid is disclosed when choosing an inquiry draft; competing plausible bids for a requested offer require user selection; an unresolved recipient, role or work date still blocks sending. Do not write unknown values as zero or invent standard hours, kit or OT.

## Render and review

Read [initial-outreach.md](references/initial-outreach.md) for the mode-specific terms blocks and compatibility limits. Discover with `grid.list_message_templates`, verify the exact template ID and output format, then call read-only `grid.render_message_template` for the exact project/crew. If a purpose returns variants, choose by ID with the user rather than guessing. Render email/text separately; task is an output shape, not a send channel.

Inspect resolved sources, warnings and every unresolved tag. The current renderer has project-wide Shoot Dates and confirmed Rate only; it does not select outreach bid/day scope or resolve proposed labor/hours/kit/OT. For a narrower request, explicitly adapt the rendered draft to the verified day(s), review Shoot Days separately, and show the edited result as a manual adaptation. A renderer `preview` status does not establish outreach readiness. Unsupported tokens must not be added or disguised as working fields.

Preserve the selected custom template's subject, opening, project details, closing and signature, except for explicitly reviewed corrections (including narrower dates). Insert the appropriate verified terms block before its closing. Resolve or flag missing production company, director, producer, signature and any other existing tags; never silently delete them to make the preview look complete. Show unsupported/missing values to the user and obtain corrections or explicit approval of a particular omission before finalizing.

Show the exact final recipient/destination, channel, template identity, project/bid/role/dates, mode, term sources and unresolved questions, followed by the complete final subject/body or text. Obtain explicit user approval of that exact final draft before any send. Draft approval does not approve a different recipient, changed terms, attachments or later edits; show those changes again. Use the authorized Messages service for a text send only when available and approved. No tool availability, render operation, template preview or earlier generic outreach request is send approval. After an uncertain send outcome, verify delivery history before retrying; never resend blindly.

Live template edits require a separately authorized supported preview/save workflow and readback. If the connector exposes only list/render, report that limitation and provide proposed wording; do not bypass it with SQL, a migration, plugin installation or an unrelated editor. Test this workflow with [synthetic scenarios](references/scenarios.md); reusable examples must contain no private contact data.
