---
name: create-game-card
description: Design a KPI gamecard (the scorecard for one role) in KPI Gamification. Use when a company admin asks to create, draft or design a gamecard, scorecard or KPI set for a job role such as sales executive, store manager, telecaller or accountant. Gathers the role details, builds a complete 100-point KPI design with real scoring details, previews it, and saves it only after the user confirms. Do not use for HR Kits, SOPs, HR policies or company health checks.
---

# Create a gamecard

A gamecard is the monthly scorecard of one role. It has KPIs that add up to exactly **100 points**. You design it; the KPI Gamification server validates it, shows a preview, and saves it only after the user confirms.

Tools: `preview_gamecard` (free, saves nothing) and `commit_gamecard` (saves, free). `list_gamecards` shows what already exists.

## Rules you never break

1. **Ask, do not guess.** The server never invents scoring details. Targets, slabs, checklist tasks, audit questions and productivity tasks must come from the user or be proposed by you and then confirmed. Never present an invented number as the user's.
2. **Preview before commit, always.** Show the user the preview summary and warnings, then wait for an explicit yes ("save it", "go ahead"). Silence, "looks good so far" or a question is not a yes.
3. **One commit per confirmation.** Generate a fresh UUID as `request_id` for each new commit. Reuse the same `request_id` only to retry the exact same commit after an error or timeout.
4. **Change after preview means preview again.** If the user edits anything, call `preview_gamecard` again and ask again. `commit_gamecard` saves exactly what the last preview showed.
5. **Descriptions are read by Team Members.** Never write notes to the admin inside the card ("please correct", "adjust if you prefer"): say that in your reply. Audit and feedback KPIs have 5 to 10 questions. Productivity and cycle time task names are plain ("Ticket Resolution"), not "(per ticket)".
6. **Use "Team Member", never "Employee"**, when you write names, descriptions and replies.
7. **Stay in scope.** You cannot assign the gamecard to people, invite users, change roles or plans. If asked, tell the user to do it in KPI Gamification (the commit result includes a link).

## Step 1: Understand the role

Ask only what you do not already know, in one short message:

- Job title and what the role is for (sales or non-sales, customer-facing or back-office).
- Is the role measured on a monthly target (revenue, units, leads)? What number?
- What does good work look like daily? (tasks done, tickets closed, calls made, errors to avoid)
- Does anything need a checklist, an audit, or customer feedback?

If the user gives a one-line request ("gamecard for a retail sales executive"), propose a design from the structure below and ask them to correct the targets, rather than interrogating them.

## Step 2: Build the structure

Order: **Attendance, Timing, Core KPIs, Reports (always last).**

- **Attendance**, **Timing** and **Reports** are fixed categories (not KPI types). The usual split is **Attendance 10, Timing 10, Core KPIs 70, Reports 10**; when the role needs more core KPIs, take each of the three to **5**. Include all three. Use `category` "Attendance", "Timing", "Reports". Leave `attendance_rules` out unless the user asks for different penalties. If the company already has gamecards (`list_gamecards`), follow their standards.
- Every other KPI has `category: "Core KPIs"` and a `kpi_type`.
- Weightages are **multiples of 5**. Total exactly 100. No decimals. Do not split equally; give important KPIs more.
- Core KPIs share the remaining 70 points (85 when Attendance, Timing and Reports are 5 each). Ideal per KPI is 10, important ones 20, smaller ones 5.

Guidance by type (points are guidance, not limits). These are this company's house rules:

| kpi_type | Use for | Points |
|---|---|---|
| Goal-ProRata | Revenue or other BIG numbers (needs `target_value`, `dkr_field`) | 10, up to 20 |
| Goal-Slab | SMALL counts such as number of customers (needs `goal_config.slabs`, `dkr_field`) | 5 to 10 |
| Goal-Average | Averages such as calls or visits per day (needs slabs, `dkr_field`) | 5 to 10 |
| Conversion | Percentage with slabs, for example 70% and 80% (needs `conversion_config`, `dkr_field`) | 10 |
| Occurrence | Errors or incidents. Points fall with the count: weightage 10 gives 10 for none, 8 for one, 5 for two. For serious offences (medical errors, safety) one occurrence already drops to 5 | 5 to 10 |
| Audit-Feedback | An internal management audit (type `internal`) on almost every card. External feedback (type `external`) for roles that serve people outside the team: customer feedback (sales, service), patient feedback (nurse, doctor), parent or student feedback (teacher). Name it for who gives it and word the parameters for the role; learn parameters from the company's other gamecards. Not for back-office roles | 10 each |
| Checklist | Almost every card. Daily, weekly, bi-weekly and monthly tasks as fits the role | 10, up to 20 |
| ToDo-List | Almost every card | 10 |
| Productivity | Non-sales desk and office roles: accountants, purchase, admin, HR (task list with standard times) | 20, up to 30 only with a filled task list |
| Productivity, cycle time | Manufacturing and machine operators. A role with cycle time gets no separate Productivity KPI | 20 |
| Leadership | Managers and leads: their team average | 5 to 10 |

Defaults by role type:

- **Sales:** Goal KPIs (Pro-Rata for revenue, Slab for small counts, Average for calls or visits), usually Conversion, and customer feedback.
- **Service and care roles:** external feedback from the people they serve (customers, patients, parents).
- **Desk or office roles:** Productivity. **Machine operators:** cycle time instead.
- **Managers and leads:** Leadership.
- **Everyone:** internal Audit-Feedback, Checklist, ToDo-List. External feedback only when the role serves people outside the team.
- Weight ranges: Audit / Feedback 5 to 10, Checklist 5 to 15 (10 typical), Productivity 10 to 25 (20 common), Cycle time 5 to 20, To-Do 5 to 10, Leadership 10 (5 when crowded). Slabs: Attendance, Timing and Reports 2 each (the server fills them from the weight), Goal Pro-Rata 70% MQR, Goal Slab 2 or 3, Goal Average 2, Conversion 2 (80% and 70%), Occurrence 2 levels.
- A proper card is complete: do not drop useful KPIs or checklist tasks just to keep it short. To fit 100, take Attendance, Timing and Reports to 5 each first, then use 5-point weights for the smaller KPIs. Drop a KPI only if the user asks.
- Talk to the user in the app's names (Goal (Pro-Rata), Goal (Slab), Goal (Average), Audit / Feedback, To-Do List, Productivity / Cycle Time); the tool takes the internal values listed in the table.

The exact shape of every KPI type, with a full worked example, is in `references/kpi-types.md`. Read it before building a type you are unsure about.

## Step 3: Call `preview_gamecard`

Send `title`, `category` (required: the role family, one of Sales, HR, Finance, Marketing, Operations, Customer Service, IT, Production & Manufacturing, Quality, Purchase, Warehouse & Inventory, Admin & Front Office, Logistics & Delivery, Field Service, Trainer / Instructor / Faculty, Labours & Helpers, Security & House Keeping, Management & Core Team, Healthcare, Food & Beverage, Real Estate & Construction, Education), optional `description` (up to 500 characters) and `metrics`.

- `valid: false`: the result lists `errors`, each with a `path` and a `fix`. Correct them and call again. Do not tell the user about trivial fixes; do tell them if a fix changes the design (for example, a weightage you had to move).
- `valid: true`: you get a `preview_id`, a summary, and possibly `warnings`. Show the user the summary as a short table (KPI, type, points, target) and mention any warnings in plain words.

Ask: "Shall I save this gamecard?"

## Step 4: Commit only after a clear yes

Call `commit_gamecard` with `preview_id` and a new `request_id` (UUID). Then tell the user:

- It is saved as a gamecard template and is **not assigned to anyone yet**.
- Give them the link from the result to open it in KPI Gamification, review it, and assign it there.
- Offer the natural follow-ups: an HR Kit for this gamecard (`create-hr-kit` skill) and an SOP covering it (`create-sop` skill).

## Errors

- `RATE_LIMITED`: daily limit reached; suggest continuing tomorrow or in the app.
- `NOT_AUTHORIZED`: only a company admin of the connected company can do this.
- `PREVIEW_NOT_FOUND_OR_EXPIRED` (previews last 15 minutes): run `preview_gamecard` again and ask for confirmation again.
- `PREVIEW_ALREADY_USED`: that preview was already saved. Do not save again; use `list_gamecards` to find it.
- `REQUEST_ID_CONFLICT`: the `request_id` was used for something else. Use a new UUID only if the user really wants a second commit.
- `DB_REJECTED`: the database refused the design (the message says which rule). Fix the design, preview again, ask again.
- If a commit errors and you are unsure whether it saved, retry with the **same** `request_id`; it is safe and will not charge twice.
