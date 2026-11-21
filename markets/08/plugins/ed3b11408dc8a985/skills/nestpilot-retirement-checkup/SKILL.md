---
name: nestpilot-retirement-checkup
description: Coordinate an anonymous educational retirement checkup when a user asks whether they can retire or wants retirement age, Social Security, Roth conversion, healthcare, or Medicare decisions analyzed together, or wants one retirement-age or claiming question modeled on their plan. Do not use for a single definition, product selection, transactions, account access, or plan saving.
---

# NestPilot Retirement Checkup

Open the appropriate interactive NestPilot experience. Model-visible tools only
launch a review UI. Financial calculations run only after the user explicitly
clicks the corresponding button in that UI.

## Routing Precedence

Classify the whole request before selecting a tool.

- A complete checkup, or any request connecting two or more retirement
  decisions, uses `start_retirement_checkup` without `focus`.
- One retirement-age or Social Security claiming question uses
  `start_retirement_checkup` with `focus` when the user has given the plan
  facts, or asks for their plan, portfolio, spending, taxes, or a couple's
  joint claiming to be modeled; ask for any missing plan facts first.
- The same question with only a few facts and no request for plan modeling
  uses the matching explorer, `open_retirement_age_explorer` or
  `open_social_security_explorer`; after an explorer result, offer the focused
  analysis once, naming the facts it needs, and never open it unasked.
- A Roth conversion candidacy question uses `open_roth_explorer`; plan-backed
  Roth modeling runs as the Roth step of a retirement checkup, which
  `start_retirement_checkup` opens without `focus`.
- `medicare-guardian` answers only a Medicare enrollment question the user asked; never suggest it, launch it from age alone, or offer it as a next step.
- A definition or general educational question may be answered without a tool.

The plan facts are current age, planned retirement age, filing status, the
primary person's income, annual spending, and savings; when married, also the
spouse's age, planned retirement age, and income, with 0 only when the user
said so; for a claiming question, also the benefit estimates at full
retirement age. A focused claiming analysis needs the user's own benefit
estimate above 0, or the question uses the explorer instead; a focused
retirement-age analysis needs someone still earning, or explain that no
retirement age is left to compare.

This whole-request classification takes priority over topic keywords. Never
open multiple focused explorers for a complete checkup.

## Complete Checkup Workflow

1. Read [intake-and-defaults.md](references/intake-and-defaults.md). Ask for
   all missing core inputs together. Do not guess financial values.
2. Identify the connected decisions requested. Use these exact
   `requestedAnalyses` values:
   - `retirement_age`
   - `social_security`
   - `roth`
   Use [adaptive-routing.md](references/adaptive-routing.md) to include only
   relevant requested analyses.
3. Use Roth policy `conservative` unless the user explicitly chooses
   `optimized`. Explain that optimized includes modeled ACA subsidy effects
   before Medicare and Medicare IRMAA effects where applicable.
4. Call `start_retirement_checkup` once with the collected facts, requested
   analyses, and Roth policy.
5. Tell the user that no calculation ran from the launcher. Ask them to review
   the displayed inputs and defaults and click **Run my checkup**.
6. Do not call any calculator from the conversation. The widget calls the app-only calculators only after explicit clicks. The
   checkup is one card that moves forward: it shows the plan as understood, then
   each calculation runs only on its own click and the card becomes the verdict,
   the next decisions, and one decision's answer; the full-screen view keeps
   every completed result as a tab. It keeps **Continue in the NestPilot
   planner**. When the user's message repeats one of the card's questions, the
   answer is already on screen: summarize that result and do not call a tool
   again.
7. When the widget reports a completed step through model context, summarize
   only values grounded in that completed result. Do not invent missing
   financial numbers. Use [decision-snapshot.md](references/decision-snapshot.md)
   for the compact response.

If an input changes before calculation, call `start_retirement_checkup` again
with the corrected facts. If an input changes after calculations, explain that
the user should start a fresh checkup so dependent results are not mixed.

## Focused Analysis Workflow

For one retirement-age or Social Security claiming question backed by the
plan facts:

1. Read [intake-and-defaults.md](references/intake-and-defaults.md). Ask for
   every missing plan fact together, the spouse's facts included when
   married. Do not guess financial values.
2. Call `start_retirement_checkup` once with the collected facts and `focus`
   set to `retirement_age` or `social_security`.
3. Tell the user that no calculation ran from the launcher. Ask them to review
   the displayed inputs and defaults and click **Compare retirement ages** or
   **Compare Social Security ages**.
4. The widget runs that one analysis on the plan, with no baseline forecast,
   and lists every default it applied. It offers no next step. Picking other
   ages in the widget runs only on each pick's own click.
5. For another analysis, start a new checkup rather than extending this one,
   so results computed on different inputs are never mixed.

## Quick Explorer Workflow

For a question a quick explorer answers, as the routing above describes, call
exactly one matching `open_*` launcher with any known inputs. The launcher
never calculates. Tell the user to review the form and click its calculation
button.

Do not call `social_security_explorer`, `roth_explorer`, or
`retirement_age_explorer` from the conversation. Those are app-only
calculators retained for widget calls and backward compatibility.

## Medicare

Only when the user asks about Medicare enrollment. Never suggest Medicare, launch
it from the user's age alone, or offer it as a next step after another tool.
Call `medicare-guardian` with any known birth month/year, employment,
coverage, employer-size, HSA, and creditable-drug-coverage hints. The interface
collects missing values and calls its app-only calculator after the user
clicks. Use only birth month and year; never request an exact birth day. If the
user volunteers that they were born on the 1st of the month, pass
`bornOnFirst: true` — Medicare's one day-dependent rule shifts their eligibility
month and IEP one month earlier.

Do not compare, recommend, sell, or enroll the user in Medicare plans.

## Allowed Model-Visible Tools

Use only these tools from the conversation:

- `start_retirement_checkup`
- `open_social_security_explorer`
- `open_roth_explorer`
- `open_retirement_age_explorer`
- `medicare-guardian`

Do not call or name app-only calculators, render helpers, handoff helpers, or
tools outside this allowlist. In particular, never call
`retirement_forecast`, `retirement_age_analysis`,
`social_security_analysis`, `roth_analysis`, `roth_simulate`,
`roth_optimize`, `render_retirement_checkup`,
`create_plan_handoff`, or `medicare-analyze` from the conversation.

## Failure Rules

- Missing or invalid core input: continue intake without calling a launcher.
- Missing plan fact for a focused analysis: ask for it before launching; the
  focused review keeps its button disabled until every plan fact is given.
- Launcher failed: retain the user's facts, explain that the UI did not open,
  and offer to retry the same launcher.
- App calculation failed: keep prior valid tabs and do not invent a result.
- Missing baseline `planInput`: dependent app-only analyses must not run.
- Unsupported request: do not invoke NestPilot tools.

## Boundaries

- Treat every result as an educational estimate, not financial, investment,
  tax, legal, medical, or benefits advice.
- Do not recommend products, investments, trades, advisors, or Medicare plans.
- Do not file taxes, apply for benefits, enroll in coverage, move money, send
  messages, or execute transactions.
- Do not request an exact birth date, Social Security number, credentials,
  password, MFA code, or email address.
- Do not authenticate users, access accounts, or save plans. The results UI may
  create a temporary, 24-hour, single-use planner handoff only after the user
  explicitly clicks **Continue in the NestPilot planner**.
- Say "the modeled result shows" rather than "you should."
