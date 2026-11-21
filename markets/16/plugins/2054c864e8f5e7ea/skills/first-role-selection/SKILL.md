---
name: first-role-selection
description: Compare candidate AI roles with the Opportunity Matrix, nine selection factors and the rejection test, then draft a board-ready first-role decision, from The E-mployee Operating Model. Use when someone asks which AI agent, role or use case to start with, or wants to compare, shortlist or reject candidates.
---

# First E-mployee Selection

This workflow chooses which E-mployee role to assign first (Chapter 8). The first role should be selected for "measurable value, task stability, data readiness, reviewability, reversibility, bounded authority, and time to credible learning—not novelty." The question is not "Where can AI do the most?" It is "Where can this organization learn whether directed artificial labor creates credible value without losing control?" The largest use case is not automatically the best first role. "A first role is not a commitment to a portfolio. It is a bounded permission to learn."

## When to use
- The user asks which AI role, agent or use case to start with, or which to do next.
- The user has a list of candidates and wants them compared, shortlisted or rejected.
- The user needs a selection recommendation for a board or executive team.
- Do not use this to measure a role that is already running. Use `value-ledger` for that. If candidates are still tool names rather than outcomes, run `outcome-first-design` first. To write the chosen role's job, use `role-charter`. For several roles already in operation, use `portfolio-review`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. The candidate roles, each stated as an outcome and a recipient.
2. For each, what is known about value (baseline, counterfactual), data, reviewer and reversibility.
3. The stakes and constraints: customers, regulation, budget, deadline, and who makes the final decision.

If the user cannot answer, draft anyway and mark the gaps `Missing`. Do not stall.

## Opportunity Matrix
Value potential is the vertical axis and task stability the horizontal axis.

|  | Low task stability | High task stability |
|---|---|---|
| **High value potential** | Design carefully; begin with research, drafting, or triage; keep authority narrow. | Candidate for a bounded first role if data and review controls are ready. |
| **Low value potential** | Do not delegate yet; redesign the workflow or retain human judgment. | Automate only if capacity, learning, service, or resilience value justifies the control cost. |

"The axes are deliberately incomplete." The placement is then modified by stakes, reversibility, data readiness, review burden, workforce effects, implementation cost, exit cost, and time to credible learning. Give each candidate a written rationale: what is known, what is assumed, who bears the downside, and what evidence would move it. "A score without a reason is a preference wearing a number."

## The nine selection factors (in this order)
| # | Factor | Question | Watch for |
|---|---|---|---|
| 1 | Business value | Is there a specific outcome with a recipient, baseline, counterfactual, acceptance condition and credible value range? | A smaller, well-evidenced base case can beat a spectacular, weakly attributed one. "The first role is a learning investment." |
| 2 | Task stability | Does the work recur, have bounded variance, and produce an inspectable output? | "Stable does not mean simple." Judge the real role, not the demo. Unstable work stays in research, drafting, comparison or triage. |
| 3 | Reversibility | Can the work be paused, reverted or returned to a human process without losing control? | Can the trigger be disabled, records restored, pending work identified, the human process resumed, the pause communicated? If unclear, reduce the placement. |
| 4 | Data readiness | Are inputs permitted, current, accessible, sufficiently complete, and understandable to reviewers? | "Technical access is not data readiness." Ask owner, purpose, freshness, gaps, languages and formats, and out-of-boundary inputs. |
| 5 | Review burden | Can a competent reviewer inspect the output with real time, authority and an escalation route? | "'Human in the loop' is not a score." Record volume, stage, competence, sampling or full review, correction time, escalation, cost of delay. |
| 6 | Regulatory and customer stakes | What happens when the role is wrong? | Weigh probability with reversibility, detectability, blast radius and affected people. No unexplained "low risk" label. It prompts specialist review; it does not classify legally. |
| 7 | Human skill effects | Who gains capability, loses discretion, reviews, gets development, or gets fragmented work? What happens to released capacity? | The first role is "selected partly for what it teaches the human workforce to do next." |
| 8 | Implementation and exit cost | What does it cost to make the Role Charter real, and to leave? | Moderate value with low exit cost may beat high value with irreversible integration. |
| 9 | Time to credible learning | How soon is output observable in the real workflow, how many cases show the key exceptions, when are baseline and counterfactual credible, what stops it early? | "Speed is not the same as learning." A polished demo is time to excitement, not to learning. |

## Optional 1-5 comparison
Use only if the user wants scores. The book's illustration uses a "descriptive 1–5 scale" that is "a conversation aid, not a probability or validated score," with columns Value, Stability, Reversibility, Data readiness, Reviewability, Stakes, Implementation/exit, Learning time, and Initial view. Every score needs its written reason. State each column's direction: in the book's illustration a higher Stakes score marks more exposure, unlike the other columns. Never total the scores or select on the highest number. The record should not say a candidate was chosen "because it scored highest."

## Rejection test
Reject the candidate for now when any of these is true:
1. The outcome cannot be named without a tool description.
2. The baseline is missing and no credible measurement path exists.
3. The data are available technically but not permitted or owned.
4. The output cannot be inspected by a competent reviewer at the expected volume.
5. The authority boundary cannot be expressed in "verbs, objects, thresholds, and stop conditions."
6. It is called reversible but would alter an irreversible record or customer relationship before review.
7. The economic case depends on capacity becoming cash without a redeployment or demand plan.

Record "not yet" (redesign, clean data, schedule review, narrow output, run research-only) separately from "no". Political attractiveness, a vendor demo or a large budget is not a reason. If the missing evidence is the central fact, the first decision may be to measure the process rather than automate it.

## Selection worksheet (11 blocks, exact)
| Selection block | Required entry |
|---|---|
| Candidate outcome | What result, for whom, by when? |
| Value evidence | Baseline, counterfactual, range, attribution, and confidence. |
| Stability | Recurrence, variance, exceptions, and inspectability. |
| Reversibility | Pause, revert, human fallback, and recovery path. |
| Data readiness | Permission, freshness, completeness, context, and owner. |
| Review burden | Reviewer, competence, time, sampling/full review, and rejection power. |
| Stakes | Customer, regulatory, financial, safety, rights, privacy, and reputation exposure. |
| Human effects | Capability gained, discretion shifted, review burden, and distribution. |
| Cost | Implementation, supervision, switching, maintenance, and exit. |
| Learning | Time to credible evidence and the stop/revise decision date. |
| Board decision | Go, revise, pause, or retire; conditions and confidence. |

## Steps
1. Restate each candidate as an outcome and recipient. Run the rejection test on every candidate first.
2. Place the survivors on the Opportunity Matrix with a written rationale, then apply the modifiers.
3. Compare evidence, not adjectives, in the same order for every candidate: the outcome and Value Ledger evidence; then stability and exceptions; then reversibility and the human fallback; only then the tool, vendor or demonstration. Label evidence as direct, self-reported, reasonable assumption or missing.
4. Assess the nine factors. When value is similar, prefer the candidate whose uncertainty can be reduced sooner and whose failure can be contained more cheaply.
5. For each deferred candidate, answer the dissent question: "what would have to be true for the deferred candidate to become first?"
6. Complete the selection worksheet for the recommended candidate, with its written uncertainty note: say so if value rests on a vendor claim, data readiness is assumed, or the reviewer is named but not scheduled.
7. Check what the first role will teach: whether objectives can be written, data owners identified, reviewers exercise discernment, authority be constrained, logs be usable, the human process resume, and the economics survive supervision. It should carry "one defined outcome, one controlled workflow, one accountable owner, and one credible learning question."
8. Draft the board-ready decision: the decision and its conditions; the powers allowed and forbidden; the basis; the conditions for approval; the decision confidence; the next gate (for example "evidence review, not scale"); what remains unknown; and what would change the decision.

## Output format
1. **Candidate table**: Candidate | Outcome | Matrix cell | Rejection test (pass, not yet, no) | Rationale.
2. **Factor comparison**: the nine factors for each surviving candidate, with evidence labels (and 1-5 scores with reasons, only if requested).
3. **Selection worksheet** for the recommended candidate, all 11 blocks, plus the written uncertainty note.
4. **Deferred candidates**: what would have to be true for each to become first.
5. **Board-ready decision** as a short paragraph.
6. Status line: *Author-created selection instrument. Not an empirical ranking, a vendor comparison, a success probability, or a substitute for executive judgment.*
7. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 8.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
