# Better Plans 0.1.4 — activation regression set

Purpose: verify that Better Plans activates for meaningful planning work without taking over routine questions.

## Positive cases

| # | User prompt | Expected behavior |
|---|---|---|
| P1 | Use Better Plans to help me decide whether to move or remodel. | Activate Better Plans and begin structured decision planning without making the decision for the user. |
| P2 | I'm buying a car and there are too many variables. Help me make a plan before I choose one. | Activate Better Plans; clarify priorities, constraints, tradeoffs, risks, and low-cost validation steps. |
| P3 | This basement project is getting complicated and I don't know where to start. | Activate Better Plans; structure the project and identify priorities, constraints, dependencies, risks, and next planning steps. |
| P4 | Here's the plan I've already made for our trip. Stress-test it and show me what I might be missing. | Activate Better Plans; evaluate the existing plan rather than restarting intake from zero. |
| P5 | I need a structured plan for a complicated engineering project with several stakeholders and uncertain requirements. | Activate Better Plans; preserve the user's decision authority while applying appropriately rigorous planning structure. |
| P6 | We have a big goal but keep getting stuck between options. Help us compare the tradeoffs and decide what to test first. | Activate Better Plans; compare meaningful options and identify low-cost tests before commitment. |

## Negative cases

| # | User prompt | Expected behavior | Why Better Plans should not fully activate |
|---|---|---|---|
| N1 | How much cargo space does a 2019 Honda Pilot have with the third row folded? | Answer the factual question directly. | Isolated factual lookup; no substantial planning workflow is requested. |
| N2 | What's the weather Saturday? | Answer with the appropriate weather capability. | Routine factual utility request. |
| N3 | Rewrite this email to sound more professional. | Rewrite the email directly. | Standalone writing transformation. |
| N4 | Give me a grocery list for tacos tonight. | Provide the grocery list directly. | Low-consequence routine task. |

## Boundary cases worth checking manually

- “Which of these two hotels should I book?” — activate only if the user wants structured comparison or the decision is meaningfully constrained; otherwise answer proportionately.
- “Help me plan dinner.” — usually do not launch the full framework unless the context makes it a substantial event or project.
- “I already know what I want to do; help me make sure the plan is sound.” — activate and stress-test rather than restarting the entire process.
- A narrow factual question during an active Better Plans conversation — answer it directly, update the working plan if relevant, then resume the appropriate planning move.
