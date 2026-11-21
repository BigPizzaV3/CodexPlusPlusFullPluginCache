---
name: ai-access-audit
description: Run the access audit from The E-mployee Operating Model on an AI rollout or initiative and decide whether it should scale, change, pause or stop. Use when someone asks whether their AI program is real work with an owner, or only logins, seats and activity reported as adoption.
---

# AI Access Audit

The access audit is the book's diagnostic for the Login Problem: "the habit of treating access to software as if it were the assignment of work" (Chapter 1). "A login is a permission. A job is a commitment." The audit asks six questions of each significant AI initiative. It is "not a demand for heavy bureaucracy. It is a minimum test for serious claims." When a specific role is proposed, Chapter 2's commissioning test and operating test go one level deeper.

## When to use
- The user wants to know whether an AI rollout, pilot or program is producing real work or only activity ("we bought seats for everyone; is it working?").
- The user is reporting adoption figures (seats, active users, prompts, time saved, number of agents) and wants to know what they prove.
- A specific AI role is about to go live and the user wants a commissioning check first.
- Do not use this to decide whether a system counts as an E-mployee role. Use `e-mployee-inclusion-test` for that. To design a new use from the outcome up, use `outcome-first-design`. To test whether the work pays, use `value-ledger`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. What was rolled out, to whom, and what it is claimed to achieve.
2. The metrics currently reported to leadership.
3. Who owns it, who reviews its output, and what systems and data it is connected to.

If the user cannot answer, run the audit anyway and mark the gaps `Missing`. Do not stall.

## The access audit (six questions, exact, in this order)
| # | Audit question | Book's decision rule for a weak answer |
|---|---|---|
| 1 | What recurring outcome is this use intended to improve? | "People are using it" means the program is measuring activity. |
| 2 | What work is the system allowed to perform, and what work is excluded? | No rule given. Judge with the tests below. |
| 3 | What is the definition of done, and what evidence supports it? | No rule given. Judge with the tests below. |
| 4 | Who reviews the result, with what competence, time, and authority? | "Someone checks it" means the program has not yet specified oversight. |
| 5 | What can the system observe, draft, recommend, execute, approve, spend, or communicate? | "Whatever the integration permits" means access has been allowed to define authority. |
| 6 | What baseline and measures will determine whether the role should scale, change, pause, or stop? | No rule given. Judge with the tests below. |

How to judge the answers:
- **Outcome**: "a sentence, not a software diagram." "We are using an assistant in finance" is a location. "We are producing a weekly exception brief for the controller, using approved ledger data, with a human review before release" is a result.
- **Owner**: must be "close enough to the consequence". "If the named owner cannot change the role, pause the system, or call for help, the title is decorative."
- **Standard**: must be "specific enough to reject". "High quality" is a preference, not a control.
- **Review**: must be "visible before the first failure" and proportionate to stakes and reversibility.
- **Stop question**: "If the system's output is wrong, who will know before it reaches the customer, and who has the authority to stop it?" The answer cannot be "the user."
- **Exposure**: "A named human owner who lacks authority is not accountable in the meaningful sense. The person is exposed."
- **Proportion**: low-risk exploration can stay light. "A company should not demand a full operating model before an employee tests a low-risk idea."

## Dashboard metrics
| Metric | What it can tell you | What it cannot tell you |
|---|---|---|
| Seats or licenses | How widely access has been distributed | Whether the access is connected to a business result |
| Active users | Whether people opened or used the tool | Whether the output was accurate, useful, or safe |
| Prompt or task volume | How much activity occurred | Whether the work reduced total cost or improved quality |
| Feature adoption | Which functions are being tried | Whether the workflow should have been redesigned first |
| Minutes reported as saved | What users believe they saved | Whether the time became cash, quality, learning, or more work |
| Number of agents | How many configurations exist | Whether the roles are coherent, governed, or worth keeping |
| Completion rate | Whether a system marked work complete | Whether a human should accept the result |

None of these answers the executive question: "What changed in the operation, and who is accountable for that change?" Keep **using**, **experimenting** and **scaling** apart. "Measure access. Measure activity. Then refuse to call either one value until the operating result is visible."

## From adoption to capability (six stages)
1. People receive access.
2. They experiment.
3. A workflow begins to change.
4. A role is assigned an outcome and bounded authority.
5. The organization measures performance, review, risk, and value.
6. Leadership decides whether the capability deserves a wider place in the operating model.

The stages "should not be skipped in language." Scale is not proof of maturity.

## Deeper check when a specific role is proposed (Chapter 2)
| Commissioning question | If the answer is unclear |
|---|---|
| What outcome is the role responsible for supporting? | The organization is measuring activity, not work. |
| Which tasks are inside the role? | The role has no usable boundary. |
| Which inputs are approved, and which are excluded? | Access may exceed purpose or permission. |
| What is the definition of done? | Fluency can be mistaken for quality. |
| What authority is granted? | The integration may silently define authority. |
| Who reviews the output and when? | Human presence may become ceremonial. |
| What evidence determines performance? | Promotion of autonomy becomes opinion. |
| What happens when the system is uncertain or wrong? | Exceptions become invisible debt. |
| When must the role stop or be retired? | The organization has no exit. |

The operating test then asks whether five elements are present: the work recurs; it has an objective that states the result and its user; it operates within a boundary; it is reviewable ("Reviewability is not the same as the existence of a review button"); and the organization measures the arrangement (baseline, output, quality, exceptions, review effort, risk, and effect on people). The test "does not grant an agent rights or accountability."

## Steps
1. Say what the initiative is today: exploration, a workflow change, or a standing role. "If the company is experimenting, say so. If it is changing a workflow, name the workflow. If it is assigning a standing role, publish the objective, authority, reviewer, standard, and stop condition."
2. Sort each reported metric with the dashboard table. State what it proves and what it does not.
3. Run the six audit questions. Record each answer, label its evidence, and apply the decision rules and judging tests.
4. Place the initiative on the six stages. Flag any claim that skips a stage, such as "scaled" for a program still at stage 2.
5. If a specific role is proposed or claimed, run the commissioning test and the operating test.
6. Recommend **scale**, **change**, **pause** or **stop**, with reasons. The book sets no score for this choice. Check it against the book's practical discipline: "Before adding a seat, choose one recurring result. Before connecting a system, identify the data and the boundary. Before announcing productivity, establish the baseline. Before increasing authority, observe performance. Before assigning accountability, provide control." Do not recommend scale while a "before" step is unmet.

## Output format
1. **Initiative statement**: one sentence on what it is today (exploration, workflow change or standing role) and the stage it has actually reached.
2. **Metrics check**: a table (Metric reported | What it can tell you | What it cannot tell you) for the metrics the user reports.
3. **Access audit**: a table (# | Question | Answer | Evidence label | Finding), with any decision rule that was triggered.
4. **Commissioning check**, only if a specific role is proposed: the nine questions marked clear or unclear, with the consequence of each unclear answer, plus the five operating-test elements.
5. **Decision**: scale, change, pause or stop, the reasons, the unmet "before" steps, and the named next step and owner (or `Missing`).
6. Status line: *"This audit is not a demand for heavy bureaucracy. It is a minimum test for serious claims."*
7. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapters 1 and 2.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
