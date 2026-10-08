# Phase 0–1 workshop question bank

Canonical source: [Messaging framework template (copy for a new company)](https://app.notion.com/p/a71d860597c24d5ea7574b933e4d6fee), fetched 2026-08-04.

## Runtime rules

- Show only the current step’s guidance, prompt, and question.
- Render the text under **Template guidance** and **Template prompt** verbatim.
- If a step has no **Template prompt**, use only its current canonical field placeholder from **Output shape** as the prompt. Do not show the help-mode diagnostic until the user asks for help.
- Show phase-level guidance once when entering that phase. Do not repeat it on every step.
- End questions with: `Reply with your answer. You can also say “example,” “help,” “skip,” “back,” or “pause.”` These are text commands, not buttons.
- After a user answer, apply the quality bar. If it fails, ask the focused follow-up once; use the help diagnostic only when requested.
- Never promote an example into user content. If the user asks to use it, save it as `hypothesis / model inference`.
- Prefix every example exactly:

> Fictional example — illustrative only, not your answer

- ExampleCo quotes, metrics, prices, proof, and market facts are invented. They demonstrate format only and are never valid evidence.

# Phase 0: Company snapshot

## Shared Phase 0 guidance

Display this exact guidance once when Phase 0 begins. On later Phase 0 steps, show only the current field placeholder from that step's **Output shape**:

> **Five lines, no more.** The sales motion line decides how the whole framework gets used:
>
> - **Self-serve** — the website closes the deal. Message the person who'll use the product, promise a small win they can verify today, and let the CTA start right now ("Start free").
> - **Sales-led** — a person closes the deal. Message the person who signs off, promise the bigger outcome, and let the CTA book the conversation ("Book a call").
>
> The bigger the promise and the price, the more you need a human to carry it.

## Phase 0 · Step 1 of 5 — What the company sells

**Status:** Required

**Template prompt:** None.

**Ask**

1. What can a customer actually buy from the company?
2. Who buys or uses it, and what concrete job does it help them complete?

**Quality bar**

- One plain line.
- Names a recognizable product, service, or category.
- Includes the principal audience or job where useful.
- Avoids slogans, feature lists, and unsupported superiority claims.

**Focused follow-up**

> What would appear on the proposal or invoice, and what job made the customer look for it?

**Help-mode diagnostic**

> Complete: “We sell a **[product/service]** for **[buyer or user]** who need to **[job]**.”

**Output shape**

```markdown
- **What the company sells:** <one plain line>
```

> Fictional example — illustrative only, not your answer
>
> ExampleCo Legal sells a legal matter-management workspace that lets litigation teams run deadlines, owners, documents, and decisions from one live matter plan.

## Phase 0 · Step 2 of 5 — Sales motion

**Status:** Required

**Template prompt:** None.

**Ask**

1. Can a customer complete a normal purchase without speaking to anyone?
2. Who or what actually closes the deal: the website or a person?
3. What normally happens from serious interest to payment or signature?

**Quality bar**

- Selects one primary motion: `self-serve` or `sales-led`.
- Describes how the normal deal closes, not how leads are generated.
- A hybrid business chooses the motion responsible for the main offer.
- Records the purchase path as supporting context without expanding the five-line template field.

**Focused follow-up**

> At the moment money or a signed agreement changes hands, did the website close the normal deal or did a person?

**Help-mode diagnostic**

> If a buyer must speak to sales before purchasing, choose **sales-led**. If they can begin and pay entirely online, choose **self-serve**.

**Output shape**

```markdown
- **Sales motion:** <self-serve — the website closes / sales-led — a person closes>
```

> Fictional example — illustrative only, not your answer
>
> **Sales-led — a person closes.**

## Phase 0 · Step 3 of 5 — Typical deal

**Status:** Required

**Template prompt:** None.

**Ask**

1. What does a normal contract look like, including term and price range?
2. Which roles normally participate in the buying group?
3. How long does an ordinary deal take from serious interest to purchase?

**Quality bar**

- Includes both price range and time to close.
- Uses the normal case, excluding unusually small, large, fast, or slow deals.
- Unknowns remain clearly marked instead of being invented.
- Records contract shape and buying group as supporting context for later persona work without expanding the five-line template field.

**Focused follow-up**

> Looking only at the last three ordinary wins, what was the lowest and highest price, and roughly how many days did each take?

**Help-mode diagnostic**

> Start with the most recent normal contract. State its price and days to close, then widen into a cautious range.

**Output shape**

```markdown
- **Typical deal:** <price range + time to close>
```

> Fictional example — illustrative only, not your answer
>
> **Invented:** US$18,000–$45,000 annual contract; 30–60 days to close.

## Phase 0 · Step 4 of 5 — How buyers find you

**Status:** Required

**Template prompt:** None.

**Ask**

1. How did the last three strong-fit buyers first discover the company?
2. Which channels repeatedly produce serious buying intent?

**Quality bar**

- Lists observed discovery channels, not aspirational ones.
- Uses specific channels where known.
- Keeps the line brief.

**Focused follow-up**

> Which source produced the last three prospects you would most want to clone?

**Help-mode diagnostic**

> Check recent wins and classify their first touch: search, referral, community, outbound, event, partner, or another observed source.

**Output shape**

```markdown
- **How buyers find you:** <search / referrals / communities / outbound / events>
```

> Fictional example — illustrative only, not your answer
>
> Referrals, legal-operations communities, targeted outbound, and searches for legal matter-management software.

## Phase 0 · Step 5 of 5 — Conversion action

**Status:** Required

**Template prompt:** None.

**Ask**

1. What single next action should an interested website visitor take?
2. Which action most directly advances the selected sales motion?

**Quality bar**

- One concrete action.
- Matches the sales motion.
- Describes what the visitor does, not the company’s internal goal.

**Focused follow-up**

> What is the smallest commitment that reliably moves a qualified visitor toward purchase?

**Help-mode diagnostic**

> For sales-led, begin with “Book…” or “Request…”. For self-serve, begin with “Start…” or “Create…”.

**Output shape**

```markdown
- **Conversion action:** <book a call / start free trial / watch a demo>
```

> Fictional example — illustrative only, not your answer
>
> Book a matter-workflow review.

# Phase 1: Product marketing strategy

## Phase 1 · Step 1 of 15 — Background

**Status:** Required

**Template guidance**

> **What to write here**
>
> - 3–6 sentences on the market context your company operates in.
> - Include the “why now” and the shift or constraint creating urgency.
> - Avoid company-specific features. Keep it about the world your buyer lives in.

**Template prompt**

> “In the last <time period>, <industry> has shifted from <old> to <new> because <drivers>.”

**Ask**

1. What changed in the buyer’s world, from what old state to what new state?
2. What caused that shift?
3. What constraint makes the old approach harder to tolerate now?

**Quality bar**

- Three to six sentences.
- Explains market context, shift, drivers, and urgency.
- Stays in the buyer’s world and contains no company features.
- Facts have sources; uncertain claims are labeled hypotheses.

**Focused follow-up**

> What prevents the buyer from continuing exactly as before, and why is that more urgent now than a year ago?

**Help-mode diagnostic**

> Fill the four blanks in the template prompt first: time period, industry, old state, new state, and drivers.

**Output shape**

```markdown
## Background

**[Insert background paragraph here]**
```

> Fictional example — illustrative only, not your answer
>
> **Invented market context:** Mid-sized litigation firms are moving from individually managed case files toward shared, continuously updated matter operations. Distributed teams and faster client-status expectations make it harder to reconstruct deadlines, decisions, and ownership from email. Firms still rely on familiar tools, but the cost of assembling a reliable matter picture grows as cases and contributors multiply.

## Phase 1 · Step 2 of 15 — Industry problems the company solves

**Status:** Required

**Template guidance**

> **What to write here**
>
> - Bullet the pains that made this product necessary.
> - Focus on symptoms buyers recognize, not internal causes.
> - Include raw customer language where available: exact phrases from sales calls, emails, reviews, support tickets, or interviews.

**Template prompt**

> “When <buyer> tries to <job to be done>, they struggle with…”

**Ask**

1. When the buyer attempts the important job, what repeatedly goes wrong?
2. Who feels each problem, and what happens when it occurs?
3. What exact customer language supports it?

**Quality bar**

- Three recognizable symptoms rather than abstract causes.
- Each problem identifies the job, affected role, and practical consequence.
- Any quoted language is verbatim and has a named source.

**Focused follow-up**

> Think of the last customer who experienced this: what were they doing, what broke down, and what did it cost them?

**Help-mode diagnostic**

> Recall the last complaint, escalation, workaround, or missed handoff. Describe only what the buyer could see happening.

**Output shape**

```markdown
- **Problem 1:** <describe>
- **Problem 2:** <describe>
- **Problem 3:** <describe>
```

> Fictional example — illustrative only, not your answer
>
> - **Problem 1:** Deadline changes get buried in email, leaving matter coordinators unsure which date and owner are current.
> - **Problem 2:** Litigation leaders rebuild status from spreadsheets and meetings before they can answer a client.
> - **Problem 3:** Documents and decisions live apart from the plan, so teams repeat work and lose the reasoning behind a handoff.

## Phase 1 · Step 3 of 15 — Customer language

**Status:** Optional

**Template guidance**

> Only fill this if you have real quotes. Max 3 each. Skip rather than invent.

**Template prompt:** None.

**Ask**

1. What exact phrases have customers used to describe the problem or desired outcome?
2. Where did each phrase come from?
3. Which words do buyers reject, misunderstand, or never use?

**Quality bar**

- Maximum three phrases and three words to avoid.
- Phrases are copied verbatim, not polished or paraphrased.
- Each phrase can be traced to a call, email, review, ticket, or interview.
- Skip when no real quotes exist.

**Focused follow-up**

> Can you point to the call, email, review, ticket, or interview containing those exact words? If not, we should skip this section.

**Help-mode diagnostic**

> Search one recent call transcript or customer email and paste the exact sentence without correcting it.

**Output shape**

```markdown
### Phrases they use

- <exact phrase>
- <exact phrase>
- <exact phrase>

### Words to avoid

- <word or phrase>
- <word or phrase>
- <word or phrase>
```

> Fictional example — illustrative only, not your answer
>
> These are intentionally invented customer-style phrases and would not qualify as evidence in a real workshop:
>
> **Phrases they use**
>
> - “We have six versions of the truth.”
> - “I spend Friday rebuilding the matter update.”
> - “The deadline changed, but the spreadsheet didn’t.”
>
> **Words to avoid**
>
> - “Legal transformation”
> - “Synergy”
> - “Next-generation operating system”

## Phase 1 · Step 4 of 15 — Map pains to needs

**Status:** Required

**Template guidance**

> For each pain above, write the underlying need (what the buyer is trying to achieve).

**Template prompt:** None.

**Ask**

1. For each pain, what is the buyer ultimately trying to achieve?
2. What would successful resolution let them do differently?

**Quality bar**

- One need maps to every stated pain, in the same order.
- Needs describe an outcome or progress, not a requested feature.
- The connection between pain and need is explicit.

**Focused follow-up**

> You named a feature. What would that feature allow the buyer to accomplish?

**Help-mode diagnostic**

> Finish: “They need this pain removed **so that they can…**”

**Output shape**

```markdown
| Pains | Needs |
|---|---|
| <pain> | <corresponding need> |
| <pain> | <corresponding need> |
| <pain> | <corresponding need> |
```

> Fictional example — illustrative only, not your answer
>
> | Pain | Corresponding need |
> |---|---|
> | Deadline changes disappear in email. | One trusted view of every current deadline and owner. |
> | Leaders rebuild status manually. | Answer matter-status questions without a reconstruction meeting. |
> | Decisions live apart from the plan. | Preserve the context behind assignments and changes. |

## Phase 1 · Step 5 of 15 — Competitive alternatives

**Status:** Required

**Template guidance**

> **What to write here**
>
> - If your company didn’t exist, what would customers do instead?
> - This is also where you choose the primary comparator: the alternative the positioning should be anchored against.
> - Comparators can be direct competitors, incumbents, horizontal tools, internal builds, manual workflows, agencies, consultants, spreadsheets, or “do nothing.”
> - Include internal workarounds, incumbents, and “do nothing.”

**Template prompt**

> “Today, our buyers typically solve this by…”

After the table, display this exact rule:

> 👉 The “Unique attributes” section below should summarize the third column — not start a fresh brainstorm.

**Ask**

1. If the company disappeared, how would buyers complete this work next Monday?
2. Where does each alternative fail in terms the customer would recognize?
3. What concrete capability closes each gap?

**Quality bar**

- Includes relevant manual, incumbent, direct, indirect, internal-build, and do-nothing alternatives.
- Describes observed buyer behavior, not merely a competitor list.
- “Where it falls short” is specific.
- The third column contains capabilities, not benefits or slogans.

**Focused follow-up**

> If the product vanished tonight, what would this buyer actually open, hire, build, or tolerate tomorrow?

**Help-mode diagnostic**

> Check these possibilities one at a time: email or spreadsheet, existing vendor, horizontal tool, internal build, outside service, and do nothing.

**Output shape**

```markdown
| Alternative (what they’d do instead) | Where it falls short | What we can do that it can’t |
|---|---|---|
| <DIY / manual workaround> | <specific failure> | <capability that closes the gap> |
| <Incumbent / vendor category> | <where it falls short> | <what we do that it can’t> |
| <Direct competitor> | <where it falls short> | <what we do that it can’t> |
| <Indirect competitor> | <where it falls short> | <what we do that it can’t> |
| Do nothing / tolerate the pain | <what staying put costs them> | <why acting now beats waiting> |
```

> Fictional example — illustrative only, not your answer
>
> | Alternative | Where it falls short | What ExampleCo can do that it can’t |
> |---|---|---|
> | Email plus matter spreadsheets | Dates, owners, and decisions drift into separate versions. | Connect each deadline, owner, document, and decision in one live matter plan. |
> | Legacy legal matter-management system | Records the matter but does not give the litigation team a fast shared execution view. | Turn the matter record into role-specific working views. |
> | Horizontal project-management tool | Requires teams to translate litigation concepts into generic tasks. | Model matters, deadlines, evidence, and legal ownership directly. |
> | Internal custom tracker | Becomes another system the firm must design and maintain. | Provide a ready legal workflow with controlled configuration. |
> | Do nothing | Teams continue paying for status reconstruction and avoidable handoff ambiguity. | Establish one current operating picture without another reconciliation process. |

### Primary comparator (part of Step 5)

**Status:** Required substep

**Template guidance**

> This is also where you choose the primary comparator: the alternative the positioning should be anchored against.

Display the exact field rule:

> **Primary comparator:** <the one alternative positioning is anchored against — not “other solutions”>

**Template prompt:** None beyond the competitive-alternatives prompt.

**Ask**

1. Which single alternative most often appears in the buyer’s real decision?
2. Which alternative makes the product’s meaningful difference easiest to explain?

**Quality bar**

- Exactly one specific alternative.
- Never uses “competitors,” “other solutions,” or a mixed list.
- Must match `What it replaces` in Product type.

**Focused follow-up**

> If this buyer could not choose your product, which one approach would they most likely keep or buy?

**Help-mode diagnostic**

> Review the alternatives for frequency, stakes, and explanatory contrast. Choose the one with the strongest combination.

**Output shape**

```markdown
- **Primary comparator:** <one specific alternative>
```

> Fictional example — illustrative only, not your answer
>
> **Primary comparator:** Email-and-spreadsheet matter tracking.

## Phase 1 · Step 6 of 15 — Product type

**Status:** Required

**Template guidance**

> **Pick one.** This locks what you compare against in positioning and messaging.
>
> | Product type | What it replaces |
> |---|---|
> | **Clear upgrade** | Existing software in the category |
> | **New Way** | Combo of workflows, tools, services, or processes |
> | **Vertical Solution** | A horizontal tool not built for your audience |
> | **Buy vs. Build** | Building and managing it in-house |

Display this exact check after the fields:

> **Check:** your Primary comparator (in Competitive alternatives above) should be the same thing as “what it replaces.” If they don’t match, fix one of them.

**Template prompt:** None.

**Ask**

1. Is the product a Clear upgrade, New Way, Vertical Solution, or Buy vs. Build?
2. What one specific incumbent, workflow, horizontal tool, or internal build does it replace?
3. Does that exactly match the primary comparator?

**Quality bar**

- Selects exactly one allowed product type.
- Names one specific replacement.
- Primary comparator and replacement match.

**Focused follow-up**

> Are buyers replacing category software, a bundle of workflows and tools, a horizontal tool, or an in-house build?

**Help-mode diagnostic**

> Map the current alternative directly: existing category software → Clear upgrade; mixed workflow/tool stack → New Way; horizontal tool → Vertical Solution; internal build → Buy vs. Build.

**Output shape**

```markdown
- **Product type:** <Clear upgrade / New Way / Vertical Solution / Buy vs. Build>
- **What it replaces:** <one specific line>
- **Check:** <matches primary comparator / revise>
```

> Fictional example — illustrative only, not your answer
>
> - **Product type:** New Way
> - **What it replaces:** Email-and-spreadsheet matter tracking
> - **Check:** Matches the primary comparator.

## Phase 1 · Step 7 of 15 — Switching dynamics

**Status:** Required

**Template guidance**

> Use the JTBD Four Forces to understand what makes buyers move or stay stuck.
>
> - **Push:** What frustration drives them away from the current approach?
> - **Pull:** What makes this company’s solution attractive now?
> - **Habit:** What keeps them using the old workflow?
> - **Anxiety:** What worries them about switching?

**Template prompt:** None.

**Ask**

1. What pushes buyers away from the current approach, and what pulls them toward the new one?
2. What familiar behavior keeps them stuck?
3. What risk or uncertainty makes them hesitate?

**Quality bar**

- Covers all four forces.
- Push and habit describe the current state; pull and anxiety describe the move.
- Habit is an established behavior, while anxiety is a feared switching consequence.
- Uses concrete buyer language where sourced.

**Focused follow-up**

> Even after agreeing the current workflow is broken, what makes the buyer say, “not this quarter”?

**Help-mode diagnostic**

> Ask one at a time: “What are they fed up with?”, “What attracts them?”, “What routine is easy to keep?”, and “What might go wrong if they switch?”

**Output shape**

```markdown
- **Push:** <frustration with current approach>
- **Pull:** <appeal of new solution>
- **Habit:** <existing behavior or process inertia>
- **Anxiety:** <risk, uncertainty, or switching concern>
```

> Fictional example — illustrative only, not your answer
>
> - **Push:** Matter leaders lose confidence when dates and owners conflict across email and spreadsheets.
> - **Pull:** One live matter plan gives the team a shared current view without rebuilding status.
> - **Habit:** Every lawyer already knows how to forward an email and update a personal tracker.
> - **Anxiety:** The firm worries about migration effort, lawyer adoption, permissions, and creating another system that must be updated.

## Phase 1 · Step 8 of 15 — Unique attributes (capabilities)

**Status:** Required

**Template guidance**

> **What to write here**
>
> - Capabilities you have that alternatives don’t.
> - Keep it as “what the product can do,” not the benefit yet.

**Template prompt**

> “Unlike alternatives, we can…”

**Ask**

1. Which capabilities recur in the third column of the alternatives table?
2. What can the product demonstrably do that the primary comparator cannot?
3. Could each capability be shown in a short product demonstration?

**Quality bar**

- Usually three capabilities.
- Every capability traces to the alternatives table.
- Describes what the product can do, not an outcome such as “save time.”
- Concrete and demonstrable.

**Focused follow-up**

> “Faster” is a benefit. What does the product specifically do that makes it faster?

**Help-mode diagnostic**

> Complete: “Unlike **[primary comparator]**, the product can **[verb + object]**.”

**Output shape**

```markdown
- <Unique capability 1>
- <Unique capability 2>
- <Unique capability 3>
```

> Fictional example — illustrative only, not your answer
>
> - Connect deadlines, owners, documents, and decisions as linked parts of one live matter plan.
> - Generate role-specific matter views from the same underlying plan.
> - Preserve the history and reasoning behind deadline, ownership, and status changes.

## Phase 1 · Step 9 of 15 — Value and proof

**Status:** Required

**Template guidance**

> **What to write here**
>
> - Quantifiable outcomes (even if ranges or directional at first).
> - Add proof points: customer quotes, benchmarks, internal data, pilots.

**Template prompt**

> “Customers should expect to see <metric> improve by <range> because…”

**Ask**

1. Which measurable outcome should change, in what direction or range?
2. What named quote, benchmark, dataset, pilot, or customer record supports it?
3. Which capability explains why the outcome should change?

**Quality bar**

- Every outcome has a metric, direction or range, and named source.
- Directional or estimated outcomes are clearly labeled.
- A claim with no named source remains a hypothesis and cannot pass the Proof test.
- Never converts a fictional example into evidence.

**Focused follow-up**

> Where could another reviewer open or inspect the evidence behind this number?

**Help-mode diagnostic**

> Pick one workflow. Define how it is measured before and after, then name the record that contains the comparison.

**Output shape**

```markdown
- **Outcome 1:** <metric + improvement> — proof: <source>
- **Outcome 2:** <metric + improvement> — proof: <source>
- **Outcome 3:** <metric + improvement> — proof: <source>
```

> Fictional example — illustrative only, not your answer
>
> The figures below are invented hypotheses and deliberately have no valid proof:
>
> - **Outcome 1:** Time spent assembling matter-status reports decreases 30–50% — **proof:** none; invented hypothesis requiring a pilot.
> - **Outcome 2:** Deadline-related handoff corrections decrease 20–40% — **proof:** none; invented hypothesis requiring operational data.
> - **Outcome 3:** Routine client-status questions can be answered in under 15 minutes — **proof:** none; invented hypothesis requiring customer validation.
>
> This fictional section must receive `REVISIT` on the Phase 3 Proof test.

## Phase 1 · Step 10 of 15 — Target customers

**Status:** Required

**Template guidance**

> **What to write here**
>
> - Define who has the pain intensely and frequently.
> - Include firmographics (size, stage, industry) and triggering events.

**Template prompt**

> “This is for <type of company> who are trying to <goal> and are blocked by <pain>.”

**Ask**

1. Which company type experiences this pain intensely and frequently?
2. What firmographics and triggering events identify that company?
3. When is a prospect clearly not a fit?

**Quality bar**

- Includes industry plus useful size, stage, operating-model, or complexity criteria.
- Ties the profile to pain intensity and frequency.
- Names observable trigger events and a concrete anti-fit condition.
- Does not confuse a company profile with an individual persona.

**Focused follow-up**

> Which recent customer or prospect experiences this problem every week, and what makes its situation different from a weak-fit prospect?

**Help-mode diagnostic**

> Describe the last organization you would want ten more of: industry, size, operating complexity, triggering event, and urgent pain.

**Output shape**

```markdown
- **Best-fit customer profile:** <describe>
- **Trigger events:** <e.g., scale, audit, migration, acquisition>
- **Not a fit when:** <describe>
```

> Fictional example — illustrative only, not your answer
>
> - **Best-fit customer profile:** Mid-sized litigation firms with multiple active teams, a legal-operations leader, and frequent cross-office matter coordination.
> - **Trigger events:** Rapid growth in active matters, a new legal-operations mandate, multi-office expansion, a missed handoff, or a client-reporting escalation.
> - **Not a fit when:** A solo or very small practice runs only a few simple matters and has no recurring coordination burden.

## Phase 1 · Step 11 of 15 — Personas (who you message to)

**Status:** Required for this B2B workshop

**Template guidance**

> List the 3–6 key roles. Prioritize the personas so messaging has a clear primary audience instead of trying to speak equally to everyone.
>
> For each: job-to-be-done, what they care about, objections, audience awareness level, and whether they are the focus audience for positioning.
>
> - **Problem-aware:** They know something is broken, but may not know the category or solution yet. Lead with pain, symptoms, and stakes.
> - **Solution-aware:** They know solutions exist and are comparing approaches. Lead with category, differentiation, and why this approach is better than the comparator.
> - **Product-aware:** They already know the company or product. Lead with proof, use case, urgency, or conversion action.

**Template prompt:** None.

**Ask**

1. Who uses, champions, approves, pays for, or can block the purchase?
2. Which role is the primary positioning audience, and what is the priority order?
3. For each role, what is its JTBD, desired outcome, main objection, and awareness level?

**Quality bar**

- One to six relevant roles. Prefer three to six when buyer, user, champion, approver, payer, or blocker are genuinely different people.
- One consolidated persona is valid when the user confirms that the same person uses, buys, approves, and pays, especially for low-cost self-serve offers. Record that consolidation and do not invent extra decision-makers to fill the table.
- Priorities are explicit, with one primary focus audience.
- Awareness level and messaging implication agree.
- Each row includes a distinct JTBD, outcome, and objection.

**Focused follow-up**

> If the homepage could speak to only one person, whose recognition and approval would move the deal furthest?

**Help-mode diagnostic**

> Name the people who use it, champion it, sign off, pay, and review security or implementation. One person may hold several roles. If one person handles the whole decision, say so and use one consolidated persona.

**Output shape**

```markdown
| Persona | Priority | Focus audience for positioning? | Awareness level | Messaging implication | JTBD | Cares about | Objections |
|---|---:|---|---|---|---|---|---|
| <role> | 1 | Yes | <level> | <implication> | <job> | <metrics/outcomes> | <concerns> |
| <role> | 2 | No | <level> | <implication> | <job> | <metrics/outcomes> | <concerns> |
```

> Fictional example — illustrative only, not your answer
>
> | Persona | Priority | Focus? | Awareness | Messaging implication | JTBD | Cares about | Objections |
> |---|---:|---|---|---|---|---|---|
> | Head of Legal Operations | 1 | Yes | Solution-aware | Lead with category, contrast to email-and-spreadsheet tracking, and implementation proof | Standardize matter execution across teams | Reliable status, cycle time, risk, adoption | Migration effort; partner adoption |
> | Litigation Practice Leader | 2 | No | Problem-aware | Lead with missed handoffs, client stakes, and matter control | Keep matters moving without chasing updates | Deadlines, client confidence, team accountability | “Our current process works” |
> | Litigation Operations Coordinator | 3 | No | Product-aware | Lead with the working view, use case, and proof | Maintain current dates, owners, documents, and decisions | Less reconciliation and duplicate entry | Fear of another system to update |
> | IT/Security Reviewer | 4 | No | Solution-aware | Lead with architecture, access controls, integrations, and implementation | Approve a governable deployment | Security, permissions, data handling | Data residency; integration burden |

## Phase 1 · Step 12 of 15 — Optional use cases by persona

**Status:** Optional

**Template guidance**

> Write these as mini-stories: “As a <persona>, when <scenario>, I need <need> because <reason>.”

**Template prompt:** The mini-story sentence above is the exact prompt.

**Ask**

1. Which persona and triggered scenario should this use case cover?
2. What do they need at that moment, and why does it matter?

**Quality bar**

- Uses the exact persona/scenario/need/reason structure.
- The scenario is a concrete triggering event, not an always-on responsibility.
- The need describes progress, not merely a product feature.

**Focused follow-up**

> What event makes this person open the product today rather than on an ordinary day?

**Help-mode diagnostic**

> Pick one persona, then finish: “When **[specific event]**, I need **[outcome]** because **[stake]**.”

**Output shape**

```markdown
- **As a <persona>**, when <scenario>, I need <need> because <reason>.
- **As a <persona>**, when <scenario>, I need <need> because <reason>.
```

> Fictional example — illustrative only, not your answer
>
> - **As a Head of Legal Operations**, when a client requests an urgent portfolio update, I need a current view across matters because rebuilding status from each team delays the response.
> - **As a Litigation Operations Coordinator**, when a court date changes, I need every affected owner and document connected to the update because a corrected date alone does not repair the handoff.

## Phase 1 · Step 13 of 15 — Translate features into benefits

**Status:** Required

**Template guidance**

> Pick your top 5–10 features and translate each into an outcome.
>
> - Feature: what it does
> - Benefit: why it matters
> - Value: how the business wins

**Template prompt:** None.

**Ask**

1. Which five to ten capabilities most influence the customer’s decision?
2. What does each capability enable for the user?
3. How could that user benefit create business value?

**Quality bar**

- Contains five to ten rows.
- Feature is a capability, benefit is a user consequence, and value is a business result.
- Every arrow is causally plausible.
- Unsupported business results are labeled as hypotheses.

**Focused follow-up**

> You named a generic benefit. What changes in the user’s work, and what measurable business consequence could follow?

**Help-mode diagnostic**

> For one feature, complete two transitions: “This means the user can…” and “That matters to the business because…”

**Output shape**

```markdown
- **Feature:** <feature> → **Benefit:** <benefit> → **Value:** <value>
```

> Fictional example — illustrative only, not your answer
>
> - **Feature:** Linked deadlines and owners → **Benefit:** Every deadline has visible accountability → **Value:** Fewer handoff corrections and less coordination risk.
> - **Feature:** One live matter plan → **Benefit:** Teams work from the same current status → **Value:** Less time reconstructing reports.
> - **Feature:** Linked documents and decisions → **Benefit:** The reason behind a change stays with the work → **Value:** Less repeated analysis and smoother reassignment.
> - **Feature:** Role-specific views → **Benefit:** Each contributor sees relevant work without maintaining a separate tracker → **Value:** Lower duplicate-entry burden.
> - **Feature:** Change history → **Benefit:** Teams can see what changed, when, and why → **Value:** Faster review and stronger operational accountability.
>
> All stated value effects remain fictional hypotheses until supported by named evidence.

## Phase 1 · Step 14 of 15 — Market categories research

**Status:** Required

**Template guidance**

> **Goal:** Choose a category that helps buyers understand you quickly.

**Template prompt**

> “Buyers already budget for <category> solutions. We fit because <reasons>. We differ because <differentiation>.”

**Ask**

1. Which familiar categories do buyers search for, compare, or budget against?
2. What are the strongest two category options?
3. What is the comprehension benefit, constraint, and differentiation angle of each?

**Quality bar**

- Evaluates at least two credible options.
- Each option has a concrete pro, con, and differentiation angle.
- Favors buyer comprehension over a novel category invented without evidence.
- Category claims trace to customer, search, sales, or procurement evidence where available.

**Focused follow-up**

> What would the buyer type into search or put on a budget request before knowing the company exists?

**Help-mode diagnostic**

> Review customer calls, competitor comparisons, search terms, analyst language, and procurement labels. Capture the terms buyers already use.

**Output shape**

```markdown
- **Category option 1:** <name>
  - Pro: <pro>
  - Con: <con>
  - Differentiation angle: <angle>
- **Category option 2:** <name>
  - Pro: <pro>
  - Con: <con>
  - Differentiation angle: <angle>
```

> Fictional example — illustrative only, not your answer
>
> - **Category option 1:** Legal matter-management workspace
>   - **Pro:** Signals legal context plus a shared place for active matter work.
>   - **Con:** Buyers may confuse it with a system of record.
>   - **Differentiation angle:** A live execution workspace rather than a passive matter database.
> - **Category option 2:** Litigation workflow software
>   - **Pro:** Clearly associates the product with active litigation work.
>   - **Con:** May sound narrower than the eventual product scope.
>   - **Differentiation angle:** Connects deadlines, owners, documents, and decisions instead of managing generic tasks.
>
> **Working fictional choice:** Legal matter-management workspace.

## Phase 1 · Step 15 of 15 — Trends

**Status:** Optional

**Template guidance**

> Only include trends if they *clarify* your message. Avoid trend-chasing.

**Template prompt:** None.

**Ask**

1. Which external change makes the buyer’s problem easier to understand or more urgent?
2. What dated source supports it?
3. Why does it help positioning, and what risk arises if the trend changes or becomes clichéd?

**Quality bar**

- Includes only trends that materially clarify the message.
- A factual trend has a named, dated source.
- Unsourced trends are labeled hypotheses.
- Includes a concrete positioning implication and risk.
- Skip when the product’s message is clearer without it.

**Focused follow-up**

> Could the positioning stand without this trend? If yes and the trend only adds fashionable language, skip it.

**Help-mode diagnostic**

> What external change do buyers themselves mention when explaining why the problem matters now? Find its source before including it.

**Output shape**

```markdown
- Trend: <trend>
  - Why it helps positioning: <why>
  - Risk: <risk>
```

> Fictional example — illustrative only, not your answer
>
> - **Trend:** Mid-sized litigation teams are becoming more distributed while clients expect faster status visibility.
>   - **Why it helps positioning:** It explains why reconstructing matters from local spreadsheets and email is harder to tolerate.
>   - **Risk:** The claim is an invented market hypothesis with no named source; it must be validated or removed before publication.
