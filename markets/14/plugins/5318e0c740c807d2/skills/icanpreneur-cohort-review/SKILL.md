---
name: icanpreneur-cohort-review
description: "Review several Icanpreneur startup workspaces together for an accelerator, incubator, university program, mentor or client portfolio: a cohort overview of each team's customer, problem, value proposition and assumptions, evidence strength per team, common challenges, workshop topics, who needs individual mentoring, and a mentoring brief per startup. Use when the user names several startups, teams or workspaces and wants an overview, program review or mentoring preparation. Load `icanpreneur` first. Do not use for a single workspace (`icanpreneur-decide`) or for setting up research."
---

# Cohort review and mentoring briefs

Load [icanpreneur](../icanpreneur/SKILL.md) first; its rules and its multi-workspace reference ([several workspaces](../icanpreneur/references/multiple-workspaces.md)) apply. Reviews are reads: no credits, and nothing is changed unless the user asks for a note. For one workspace use `icanpreneur-decide`; its assumption tests apply to every team here.

## 1. Resolve the cohort

Find each named workspace with `list_ideas` (add `includeArchived` if needed). Ask if a name matches several. List any workspace you cannot open as inaccessible and carry on. If the user did not name the teams, ask; do not guess a cohort from every workspace they can see. Decide the question: **Canvas only** (target customer, problem, value proposition, assumptions) or **Canvas and research**. A Canvas-only request is complete from the Canvases: do not fetch research or personas.

## 2. Read every team the same way

For each team: `get_canvas`; if research is in scope, `list_research`, then per research its type, `get_research_analysis` (status, `updatedOn`), key insights and the evidence mix of completed interviews (real, imported, synthetic), de-duplicated by interview ID when projects share interviews; persona status if the question concerns it; `list_notes` for earlier reviews. Use the same criteria for every team, state them, and label every finding with its startup.

## 3. Assess each team

- **Customer and problem**: apply the platform tests; say if the segment is only a role or the problem is vague.
- **Assumptions**: Canvas content is a hypothesis. **Supported** only when real or imported interviews say it, with counts where established and interviews named where available. Synthetic-only is "simulated".
- **Evidence**: report interview stage and analysis state separately.
- **Biggest untested assumption**: the one that matters most if wrong, upstream first.
- **Next milestone**: one concrete step that closes it.

Interview counts do not measure startup quality. Real and supplied imported interviews can support customer findings; synthetic interviews remain hypotheses regardless of quantity. Do not rank teams on a single score or invent one. If asked for a priority order (for example where mentoring helps most), state the criteria and the basis for each placement.

## 4. Output

- **Cohort overview**: one row per startup (target customer, problem, value proposition, key assumptions). When research is in scope add the evidence mix, which streams exist (problem, buyer, win/loss) with project counts and `lastActivity`, and what is supported. Then common challenges, workshop topics and where mentoring helps most, each with the startups behind it and the reason.
- **Program review**: for each finding, the startup it comes from, whether it is supported, only simulated or needs testing, and what each team should focus on next.
- **Mentoring brief** per startup (**read [references/mentoring-brief.md](references/mentoring-brief.md) before writing one**): strongest evidence, biggest untested assumption, three questions for the mentor, next milestone.

List inaccessible workspaces at the top.

## 5. Rules

- Never present one startup's evidence as another's, or carry a finding between teams. If the output goes to the teams themselves, ask whether to remove cross-team attribution; the default audience is program staff.
- Describe progress only from saved content. "Progress since last review" needs a dated earlier review (a saved note or export); without one, say there is no baseline and describe the current state. `lastActivity` is not a reporting period.
- Never call synthetic-only support validated or a Canvas item a finding.
- For a pitch or update the user supplies, use the claims check in the `icanpreneur-decide` reference, against that team's workspace only.
- Offer to save briefs as notes (in each team's workspace, or a program note in a workspace the user explicitly chooses), only if asked. Notes are visible to a workspace's members: say so before writing into a team's workspace.
