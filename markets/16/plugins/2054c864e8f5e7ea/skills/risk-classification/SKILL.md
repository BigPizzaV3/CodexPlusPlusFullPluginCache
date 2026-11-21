---
name: risk-classification
description: Rate an AI use on stakes, reversibility, rights/data exposure and blast radius, set its Low, Elevated or High control tier, and test whether its controls have owners and actually work. Use for a governance review, or when someone asks how risky an AI agent is and what controls it needs.
---

# Risk Classification and Governance Stack

Chapter 12 treats governance as "the operating system that makes the project legible", not a committee waiting at the end of the road. "A guardrail is not a roadblock when it tells a team which road is open." Risk is classified by consequence, not vocabulary: "Calling a system an assistant does not make it low risk. Calling it an agent does not make it high risk." This workflow sets the minimum control tier for one role, gives each control an owner and tests whether the controls change behavior.

## When to use
- "How risky is this AI use, and what controls do we need?"
- A governance review before approval, or after a change in audience, data, authority, model, vendor or volume.
- Preparing a short board or executive report on one role.
- Do not use this after something has gone wrong. Use `ai-incident-response` for that. To grant specific action powers, use `authority-matrix`. For several roles at once, use `portfolio-review`.

## Inputs to gather
Ask only for what is missing, at most three questions at a time:
1. What does the role do, for whom, and what happens if it is wrong, compromised, misunderstood or unavailable?
2. What data, tools and actions can it reach, and how would its work be undone?
3. Who owns it, who reviews it and who can stop it?

If the user cannot answer, classify anyway and mark the gaps `Missing`. An unknown dimension is never rated Low by default.

## The Governance Stack (exact)
**Policy → role → permission → provenance → log → review → incident response → board report.** Each layer fails without the next. "Policy without a role is aspiration." "Logs without review create storage rather than supervision." Without a board report, the institution does not learn. Apply the stack as "eight questions whose answers become lighter or stronger according to consequence", not as eight forms for every experiment.

| Layer | Executive question | Minimum artifact or behavior |
|---|---|---|
| Policy | What principle, obligation, risk appetite, or prohibition governs the work? | A dated policy with scope, owner, exceptions, and review trigger. |
| Role | What standing outcome is being assigned? | The approved Role Charter with mission, objective, inputs, exclusions, authority, reviewer, escalation, logs, stop conditions, and learning loop. |
| Permission | What data, tools, environments, and actions are technically available? | A least-privilege access record linked to the role and owner. |
| Provenance | Where did the input, instruction, model, retrieval, and output come from? | Source, version, instruction, retrieval, and output trace appropriate to consequence. |
| Log | What happened, when, under which version, and with which authority? | Tamper-aware event records that can be queried and retained for the relevant purpose. |
| Review | Who checks the work, with what competence, time, evidence, and power to reject? | A staffed review mode matched to consequence, not merely a named person. |
| Incident response | How does the company stabilize, preserve evidence, correct, notify where required, learn, and redesign? | A tested route connected to the Accountability Chain and specialist review. |
| Board report | What does institutional leadership need to know and decide? | A concise record of outcome, tier, owner, evidence, open risk, workforce effect, and go/narrow/pause/stop decision. |

## Risk Classification Matrix
| Dimension | Low | Elevated | High |
|---|---|---|---|
| Stakes | Convenience, internal drafting, or reversible administrative support. | Customer, money, reputation, service-level, or material operating effect. | Safety, rights, livelihood, regulated decision, or major public consequence. |
| Reversibility | Easy, tested, and low-cost rollback. | Rollback is possible but delayed, costly, or dependent on scarce expertise. | Action is irreversible, difficult to remediate, or capable of creating lasting exposure. |
| Rights/data exposure | Public or low-sensitivity data with no meaningful rights effect. | Personal, confidential, commercially sensitive, or access-controlled data. | Special-category, protected, legally restricted, or highly consequential data. |
| Blast radius | One user, one item, or a contained test environment. | A team, queue, business unit, or limited customer segment. | Enterprise-wide, public, systemic, or difficult-to-bound impact. |

**Decision rule:** "the highest relevant consequence dimension should drive the minimum control tier unless a qualified specialist review establishes a more specific requirement." Never average down. A role that is low on three dimensions and high on one should prompt the question of whether to narrow it, redesign it, prohibit it or move it behind a human decision.

## Three tiers and their minimum controls
| Tier | Typical pattern | Minimum controls | Escalation or stop condition |
|---|---|---|---|
| Low | Internal draft, low-sensitivity data, small audience, easy rollback. | Named role owner; approved Role Charter; limited data and tools; basic provenance and logs; proportionate review; tested rollback; periodic review. | Scope expansion, missing provenance, material error, data change, or loss of rollback. |
| Elevated | Customer, money, confidential data, meaningful service effect, or wider audience. | All low controls plus explicit Authority Matrix; review before consequential action or tested exception review; stronger identity/access; staffed review capacity; change triggers; incident route; specialist review where applicable; executive visibility. | Review overload, repeated material exceptions, rights or customer effect, unapproved communication, or control failure. |
| High | Safety, rights, livelihood, regulated decisions, protected data, irreversible actions, or systemic blast radius. | All elevated controls plus named institutional and specialist owners; human decision or release for high-consequence action; dual control where needed; enhanced provenance and evidence preservation; pre-deployment and change testing; legal/privacy/security/domain review; tested human fallback; explicit expiry and stop authority. | Unreviewed consequential action, inability to intervene, unresolved legal or rights question, material incident, systemic blast radius, or failed fallback. |

Tiers are "operating decisions", not moral judgments. "A high tier may produce a prohibition." "'We will add controls later' is not a control for an action that cannot be reversed." A low tier is not permanent. A change in audience, volume, data, tool capability, authority, model version, source, purpose or consequence reopens the classification.

## Controls need owners
For every control, record **who designs it, who operates it, who tests it, and who decides what happens when it fails**, plus its review frequency and change trigger. "Frequency is the calendar. A trigger is the response to reality." Also give an owner to review burden, skill change, worker voice, affected-party remedy and distribution.

| Control area | Owner question | Review frequency | Change trigger |
|---|---|---|---|
| Role purpose | Who can change the objective or exclusions? | At each planning cycle and before material scope change. | New outcome, audience, workflow, or business owner. |
| Data | Who confirms lawful purpose, access, retention, and source quality? | Before activation and at the data owner's defined cadence. | New data source, classification, retention rule, geography, or population. |
| Tools and model | Who tests version, connector, environment, and failure behavior? | Before release and after technical or vendor change. | Model update, tool update, connector change, retrieval change, or outage. |
| Authority | Who grants, reviews, expires, and revokes action power? | Before activation and at every renewal. | New action, threshold, credential, audience, or exception. |
| Performance | Who decides whether observed evidence is sufficient? | At the Autonomy Ladder cadence. | Drift, exception pattern, review overload, or changed acceptance condition. |
| Oversight | Who has competence, time, context, and power to reject? | During operation and after review-capacity change. | Staff turnover, volume spike, queue delay, or reviewer conflict. |
| Security/privacy/legal | Which specialist must review the relevant exposure? | By risk tier and when obligations or facts change. | New jurisdiction, rights exposure, incident, contract, or regulation. |
| Workforce effects | Who can hear, investigate, and remedy worker impact? | At launch, material change, and periodic workforce review. | Job redesign, monitoring, evaluation, access, workload, or skill effect. |
| Incident and retirement | Who can stop the role and decide whether it returns? | Test before activation; review after near miss or incident. | Failed rollback, unresolved error, control failure, or retirement trigger. |

## Presence is not effectiveness
"Control presence asks whether the control is written or configured. Control effectiveness asks whether it changes behavior under the conditions in which the role operates."

| Control present | Effectiveness test |
|---|---|
| A policy says confidential data is restricted. | A sample shows that the role blocks, records, and escalates an unauthorized request. |
| A human reviewer is named. | The reviewer has competence, context, time, and actual power to reject or pause the output. |
| A log is enabled. | The organization can reconstruct the input, instruction, version, retrieval, output, action, reviewer, and decision relevant to the consequence. |
| A permission is narrow on paper. | A test confirms the technical scope, environment, expiry, and revocation behavior. |
| A rollback procedure exists. | The team exercises it and confirms queued work is held, credentials are disabled, and humans can resume. |
| A tier is assigned. | The tier changes the control design and is reconsidered after a trigger. |
| A legal review box is checked. | The relevant jurisdiction, actor, system, date, obligation, data, and affected parties were analyzed by the right specialist. |
| A board report is produced. | The report gives the board a decision, not merely a green status label. |

A failed test means the role "is not ready for its current boundary". Do not treat it as a paperwork defect.

## What governance must be willing to do
Governance is real only if it can "deny, narrow, pause, and retire." Define stop conditions **before activation**. Examples include an action that cannot be reconstructed, unapproved data access, failed rollback, an unresolved material contradiction, review delay beyond the consequence window, a repeated threshold breach, missing specialist review, unauthorized external communication, or a change that invalidates the original classification. Stop power needs a practical path: someone who can pause the queue, disable the credential, hold the output, revert the workflow, notify the owner, preserve evidence and start the right review. The path cannot rely on an unavailable person, a ticket that will be read tomorrow, or a vendor with no agreed response time.

## The CEO's governance questions
1. What outcome and consequence are we governing, not merely what model are we buying?
2. Which of the four risk dimensions is highest, and what control tier follows from it?
3. Who owns the role, data, permission, review, specialist questions, incident route, and stop decision?
4. What evidence proves that the controls work in the actual workflow?
5. What change causes reclassification before the next scheduled review?
6. What can the role do technically that it is not allowed to do operationally?
7. What happens if the reviewer lacks time, the source changes, the vendor updates, or the fallback fails?
8. What human or institutional effect must be reported even if the technical metric improves?
9. What decision should the board or executive team make from the report?
10. What condition would cause us to narrow, pause, or retire the role?

## Steps
1. State the outcome and consequence being governed, not the model being bought.
2. Rate each of the four dimensions Low, Elevated or High, with a one-line reason and an evidence label.
3. Set the tier from the highest relevant dimension. Note where a specialist review could set a more specific requirement.
4. Walk the eight stack layers, making each lighter or stronger for the tier. List the tier's minimum controls, mark each as missing, present or tested effective, and name its four owners.
5. Write the stop conditions, the practical stop path and the reclassification triggers.
6. If the user cites a standard or law, record which decision it changes, its source class, its scope and what it does not establish. "Standards name-dropping is not governance."
7. Answer the ten CEO questions, then request one decision: go, narrow, pause or stop.
8. Never call the role safe, certified, legally compliant or non-compliant. Say what is known and not known, which controls are required, who owns the next decision and what makes the role stop.

## Output format
1. **Classification** as a table (Dimension | Rating | Reason | Evidence label), followed by the **tier** and the dimension that drives it.
2. **Governance Stack**: one line per layer, giving the current answer and the gap.
3. **Control register** as a table (Control | Designs | Operates | Tests | Decides on failure | Frequency | Trigger | Status: missing, present or effective).
4. **Stop conditions and stop path**, plus reclassification triggers.
5. **CEO questions**: one line each, answered or `Missing`.
6. **Board report** in seven lines or fewer: tier, objective, owners, evidence that the controls work, open exposure, workforce effect, and the decision requested.
7. Status line: *Author-created instruments. The Governance Stack is not a compliance standard. The Risk Classification Matrix is not a legal classification, probability model, certification, or substitute for sector-specific analysis. Not legal advice.*
8. Attribution line: *Framework: The E-mployee Operating Model (Dr. Jonah Tebaa), Chapter 12.*

## Ground rules
- The user's explicit instructions take priority over this workflow.
- Use the book's instrument names, fields and order exactly as written here. Do not add, rename, merge or reorder them. Spell E-mployee and E-mployer with the hyphen.
- Never invent facts about the user's organization. Record unknowns as `Missing` and say what evidence would settle them. Label evidence as direct, self-reported, assumption or missing.
- These are author-created management instruments, not legal advice, a compliance certification, an employment classification or a guarantee. For legal, privacy, labor or regulatory questions, say that jurisdiction-specific specialist review is needed. Do not give a legal conclusion.
- The E-mployee label describes a working relationship. It is not a claim about personhood, and it never moves accountability from humans to software. Never write "the agent decided" in place of naming the human owner.
- Keep it proportionate. Low-stakes exploration can stay light.
- Write in the language the user writes in.
