# Input and output logic

## 1. Normalize the request

Create an internal brief with these fields:

| Field | Meaning | Default when absent |
|---|---|---|
| Objective | Observable outcome | Infer cautiously and label |
| User/audience | Who uses and receives output | User / unspecified audience |
| Environment | Chat, API, agent framework, platform | Generic new chat |
| Inputs | Briefs, files, links, datasets, variables | Only the request |
| Constraints | Time, budget, tools, jurisdiction, style | None inferred |
| Exclusions | What must not occur | Preserve verbatim in meaning |
| Deliverables | Required artifacts | One copy-ready prompt |
| Success criteria | How quality is judged | Correct, usable, portable |
| Autonomy | Ask-first versus proceed | Proceed on reversible assumptions |
| Research | Current facts needed? | Add conditional research protocol |
| Risk | Consequence of error | Normal unless evidence says otherwise |

Do not show this table unless it helps the user.

## 2. Decide whether to ask

Ask a question only if at least one condition holds:

- Different answers select different artifact types.
- A legal, safety, financial, medical, or external-action boundary is unclear.
- The requested deliverable cannot be made usable without the missing value.
- A user preference would materially alter scope, cost, or architecture.

Otherwise use `{{variable}}` placeholders or labeled assumptions. Ask no more than three questions at once.

## 3. Artifact scoring

Score each true statement:

- Persistent behavior across tasks: System +3
- One portable, broad task package: Master +3
- Ordered phases or recurring SOP: Workflow +3
- Tools, permissions, state, handoffs, retries: Agent +3
- Mostly policy/voice/boundaries: System +2
- Mostly rich project context and deliverable: Master +2
- Branching/checkpoints/approval gates: Workflow +2
- Long-running autonomy/observability: Agent +2

Choose the highest score. If two types score at least 4 and solve genuinely different layers, create a prompt suite.

## 4. Research classification

Classify every factual dependency:

- `stable`: definitions, supplied facts, established methods.
- `unstable`: current tools, product capabilities, pricing, people, rules, market conditions, trends.
- `high-stakes`: medical, legal, financial, security, or consequential operational advice.

For unstable or high-stakes dependencies, the generated prompt must require:

1. checking current authoritative sources at execution time;
2. recording the research date or cutoff;
3. citing claims near the relevant text when the environment supports links;
4. preferring primary sources, then reputable secondary sources;
5. distinguishing verified facts, source-based inference, and proposals;
6. stating limitations if browsing or source access is unavailable;
7. never fabricating citations or pretending a source was checked.

## 5. Conflict priority

Embed this priority order when relevant:

1. Platform-level safety and system rules
2. Applicable law and explicit permission boundaries
3. User's confirmed objective and explicit constraints/exclusions
4. Supplied source material
5. Output and style preferences
6. Agent assumptions and optimization choices

Require the executor to flag irreconcilable conflicts.

## 6. Output contract

Define:

- exact sections and order;
- data schema or table columns where structure matters;
- length or depth controls;
- citation and evidence format;
- language, tone, and audience;
- alternatives required;
- validation method;
- stop/approval conditions;
- fallback when inputs or tools are unavailable.

Avoid simultaneously demanding extreme brevity and exhaustive coverage without defining priority.

## 7. Delivery modes

- **Direct**: Deliver the finished prompt now.
- **Interview**: Deliver a short intake first, then generate after answers. Use only for materially underdefined work.
- **Adaptive**: Deliver a usable prompt with variables plus a short optional intake. Prefer this default.
- **Audit**: Return issues by severity, a repaired prompt, and a change summary.

## 8. Minimal quality report

Use this compact structure:

```text
Quality report
- Context isolation: PASS/FAIL — note
- Research policy: PASS/N/A/FAIL — note
- Role economy: PASS/FAIL — note
- Output contract: PASS/FAIL — note
- Verification and red team: PASS/FAIL — note
- Portability: PASS/FAIL — note
```
