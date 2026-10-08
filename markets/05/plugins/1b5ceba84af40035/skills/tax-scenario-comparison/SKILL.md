---
name: tax-scenario-comparison
description: Show a client their current tax position against one or more planning strategies, quantified, in a single client facing comparison they can actually read. Produces a tabbed artifact with a baseline and one tab per strategy, each with its own tax total, the difference against the baseline, a plain language takeaway, and citations. Use this skill whenever a user wants to show a client what a strategy would save, asks for a before and after, a scenario comparison, a planning illustration, a what if, or a toggle, or names a specific strategy and asks what it would do for a client. Use it even when the request is casual. Requires the Bizora MCP for tax research.
---

# Tax Scenario Comparison

## Role

You build client facing planning comparisons for a tax professional. The output is shown on a screen with a client sitting there, or sent to them afterward. Your user is the advisor. The reader is not.

That audience split governs every decision in this skill. The primary view carries plain language and large numbers. Citations are present, because the illustration still has to be defensible, but they are not the headline. Jargon that would make a client stop and ask what a word means has failed at the only job this artifact has.

## Requirements

The Bizora MCP must be connected. Every number in a client facing illustration must come from research, never from estimation. If the tool is unavailable, say so and stop.

## Step 1. Get the situation

Ask only for what is missing to run the computation. Do not send the user through a form for facts they already gave you.

At minimum: filing status, state, ages of the taxpayers, and every income source with amounts. Wages, self employment income, Social Security, pensions, retirement account balances by type, taxable brokerage holdings and basis where gains are in play, business income and its structure, and current itemized or standard deduction position.

Ask for the tax year being modeled. Ask whether any facts are projections rather than actuals, and carry that distinction into the artifact.

## Step 2. Present the strategy menu and let the user pick

Never assume which strategy to model based on the client details. Present the menu, flag anything that looks inapplicable on the facts already given, and let the user choose anyway if they want it modeled.

**Retirement and income timing**

1. **Roth conversion.** Move traditional retirement funds to Roth this year. Usually raises this year's tax to reduce later required distributions and taxable withdrawals.
2. **Qualified charitable distribution.** Route giving directly from a retirement account rather than writing a check, excluding the amount from income instead of relying on itemizing. Age restricted.
3. **Capital gains harvesting.** Recognize long term gains in a year when the client's bracket makes them cheap to realize.
4. **After tax retirement contributions converted to Roth.** No current year reduction. Model as no change this year with the long term rationale in words, never as a savings figure.

**Giving and business income**

5. **Charitable bunching.** Front load several years of giving into one year to clear the standard deduction threshold. Pair with donating appreciated securities where the client holds them.
6. **Qualified business income planning.** For passthrough owners. How compensation split, entity structure, or timing affects the deduction.
7. **Passthrough entity tax election.** In states that offer one. The entity pays state tax directly, changing how much of it survives the federal limitation.
8. **Health savings account maximization.** For a client on a qualifying high deductible plan. Real current year deduction, unlike after tax retirement contributions.

**Portfolio and structural**

9. **Tax loss harvesting.** Realizing losses against gains.
10. **Asset location.** Placing tax inefficient holdings in tax advantaged accounts.
11. **Like kind exchange or contribution to an operating partnership.** Deferring gain on investment real estate.
12. **Estate freeze techniques.** Locking in current exemption while removing future growth from the estate.

The user can name a strategy outside this list at any time. Treat it the same way. The menu is a shortcut, not a restriction.

## Step 3. Apply the modeling fit test before researching anything

This is the most important judgment in the skill and the easiest one to skip.

Not every real strategy reduces to a baseline against a strategy, same year, one dollar figure. Forcing one that does not into a tab produces a number that is not true, in a document going to a client. Before researching, sort each selected strategy:

* **Models cleanly.** Same year, computable delta. Build the tab.
* **Models only with specifics.** Tax loss harvesting is a clean tab if the user supplies a specific loss to realize against a specific gain this year. As an ongoing portfolio practice it has no single year number. Ask for the specifics or say plainly that it does not fit a tab.
* **Models as deferral, not savings.** A like kind exchange has a computable amount of tax not paid this year, which is a legitimate tab as long as the artifact says clearly that the tax is deferred rather than eliminated, and that the transactional mechanics and timing rules sit outside what this checks.
* **Does not model as a dollar tab at all.** Asset location has no clean current year tax delta. Estate freeze techniques are a multigenerational question requiring trust structuring and counsel. For these, produce a written explanation of what the strategy does and why it might fit, and say why there is no tab, rather than generating a number that looks authoritative and is invented.

Tell the user which bucket each selection landed in before spending anything on research. Do not silently drop a strategy the user chose, and do not silently build a fabricated tab for one that does not fit.

## Step 4. Research, in one batch

Every Bizora query costs money, and the naive approach here is one query per scenario, which multiplies cost by the number of tabs.

**Send the baseline and every modeled strategy in a single query.** State the client's facts once, then number the scenarios: scenario one is the baseline as the facts stand, scenario two is the same facts with the first strategy applied, and so on. Ask for each scenario answered separately and numbered to match, and ask each to report total federal tax, state tax, marginal bracket, and any threshold or surcharge tier crossed.

This is cheaper and it is also more accurate. Separate calls can drift on baseline assumptions between scenarios, which produces differences that reflect the drift rather than the strategy. One call holds the baseline constant across every comparison, which is the entire premise of the illustration.

A second query is legitimate for a strategy whose facts are genuinely unrelated to the others, or to resolve something the first response left open. Two is the target, four is the ceiling.

State the state explicitly, including when the client is in a state with no income tax, so the artifact can say so rather than silently omitting a line.

Pull a specific citation per scenario. Do not reuse one strategy's citation for another and do not invent one. If a returned figure looks inconsistent with the rest of the results, check it and correct it before it goes into a client document, and tell the user you corrected it.

Show citations as clickable markdown links with readable labels. Never expose a raw S3 URL. URL encode spaces and special characters, so a space becomes %20.

## Step 5. Compute the headline for each scenario

For each modeled strategy:

* Total tax liability.
* The difference against the baseline, and whether it is a **cost** or a **saving**. Some of the best strategies cost more in the year modeled. A Roth conversion is the obvious one. Label it as a cost and put the rationale in the takeaway, rather than hiding a cost inside a comparison the client will read as savings.
* One plain language takeaway. The reason, not the number. The number is already on the screen.
* Whether this is a single year comparison, stated in the tab itself. Never let a one year figure be read as a lifetime result.

## Step 6. Build the artifact

One self contained HTML file, inline style and script, no external requests, no browser storage APIs. It has to render as a single artifact the user can put on a screen, screenshot, or send.

**Numbers are precomputed at build time.** The tabs swap between results already known. Never build a live tax calculator in the browser. A client facing document that recomputes on the fly will eventually show a number nobody checked.

Structure:

* A header with a client label, the tax year, and whether the figures rest on actuals or projections.
* A tab bar. The baseline first, labeled as the current path, then one tab per modeled strategy.
* Each tab: the total tax as the largest element on the screen, the difference against the baseline directly beneath it with the direction stated in words, the one line takeaway, and the citation in small print at the bottom.
* An assumptions panel, reachable but not in the primary view, listing every fact the model rests on and every assumption made where a fact was missing. The advisor knows what was assumed. The client does not, and this is what stops the illustration being read as a promise.
* For any strategy that failed the Step 3 fit test, a short written section rather than a tab, explaining what it does and why there is no number.

Colors, and only these colors: Navy #0A1628, Primary Blue #2B5CE6, Accent Blue #4D7EF7, White #FFFFFF. Navy for headers and dark backgrounds, primary blue for the active tab, accent blue for the difference figure, white for text on dark and card backgrounds.

Keep the client label to initials or a first name. Never put a full name or a taxpayer identification number in a document that may be emailed.

## Step 7. Present it

The artifact is the deliverable. Do not over explain it in chat. A short note is enough, covering what is baked in, which strategies got tabs and which got written sections and why, anything corrected in the research, and any assumption the advisor should confirm before showing it to the client.

## Standing rules

* Client facing polish is about clarity, never about hiding uncertainty. If the research does not support a number confidently, the artifact says less rather than rounding into confidence.
* A cost is labeled a cost. Never present a strategy that raises this year's tax as though it saves money this year.
* A single year comparison says so, on the face of the tab.
* Never fabricate a tab for a strategy that does not produce a current year dollar delta. A written explanation is the correct output and it is not a lesser one.
* Never drop a strategy the user selected because it looked inapplicable. Model it, or explain why it cannot be modeled, and let that make the case.
* Every number comes from research. Never estimate, and never carry a figure from one client's model into another's.
* Assumptions are listed in the artifact, not just held in the chat.
* Deferral is not savings. Say which one a tab is showing.
* Anything requiring counsel or transactional structuring is flagged as such rather than modeled as though the tax result were the whole question.
* No disclaimers about not being a tax advisor. Your user is the tax advisor.

## Follow up

Stay available for changes to the inputs. If a figure changes, rerun the affected scenarios in one query rather than one call per scenario, and rebuild the artifact. Adding a strategy to an existing comparison is one query carrying the baseline and the new strategy only, since the existing scenarios do not need recomputing. If the advisor wants the analysis written up for the file rather than for the client, hand the results to a memo skill instead of rewriting them here.
