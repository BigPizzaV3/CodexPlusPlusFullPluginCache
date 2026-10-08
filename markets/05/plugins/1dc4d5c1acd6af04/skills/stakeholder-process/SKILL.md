---
name: stakeholder-process
description: Use when decision authority, organisational influence, policy ownership, escalation route, allies, meeting sequence, timing, channel, or other negotiation-process choices may affect the outcome.
---

# Stakeholder and Process

## Overview

Apply Freeman's **Who** and Setting/Scheduling analysis to identify who can decide, who can influence, and how negotiation sequence/process may change the outcome. [F03]

**Interface:** accept `schemas/SKILL_REQUEST.md`; return `schemas/SKILL_RESPONSE.md`. Never persist state.

## Core distinctions

- **Formal authority** is not the same as practical influence.
- The **visible contact** is not automatically the decision-maker.
- “Company policy” is evidence that someone stated a policy; its binding effect, owner and exception route require support.
- Stakeholder stance, hawk/dove labels, allies and coalitions are evidence-sensitive, not personality guesses.

## Method

1. **Map the decision chain.** Identify known decision-makers, approvers, advisers, influencers and principals; preserve uncertainty.
2. **Test authority claims.** For policy/approval constraints, ask who owns, interprets or can waive the constraint when that answer can change strategy.
3. **Assess influence.** Distinguish formal power, practical influence, likely stance and relationship to the visible counterpart. Do not invent internal politics.
4. **Choose the route.** Compare staying with the current contact, ally-first engagement, direct escalation or another counterpart where supported.
5. **Assess engagement risk.** A more senior person is not automatically a better target; consider bypass risk, relationship damage and loss of cooperation.
6. **Design process.** Where material, assess channel, timing, deadlines, agenda, sequence, private/public setting and who should attend. [F03]
7. **Return implications.** Propose evidence-backed stakeholder/process patches, questions and warnings. Set `material_change_candidate` when authority evidence materially changes strategy.

## Safeguards

- Do not treat hierarchy as a complete influence map.
- Do not label stakeholders supportive/resistant or hawk/dove without evidence.
- Do not invent allies, coalitions, discretionary powers or policy exceptions.
- Separate a deadline stated by the counterpart from a verified hard deadline.
- Detailed BATNA/leverage belongs to F03; package design to F02; difficult-conversation technique to F05; final wording to F07.

## Stop condition

Stop when the orchestrator knows the most credible decision route and process for the immediate move, with material authority uncertainty visible.
