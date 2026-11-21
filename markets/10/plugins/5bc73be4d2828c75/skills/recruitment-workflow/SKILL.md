---
name: recruitment-workflow
description: "Coordinate a recruitment assignment from intake to candidate presentation, select the appropriate recruiter skill, and track evidence, owners, approvals, and next actions."
license: MIT
metadata:
  version: "0.2.4"
---

# Recruitment workflow

## Establish the assignment

Identify the role, client, workspace if connected, hiring owner, existing progress, and desired outcome. Reuse the actual current stage rather than restarting intake. Read only the records required for the assignment. Do not turn a request for one email into a full recruiting project.

## Route the next step

| Situation | Skill | Required handoff |
| --- | --- | --- |
| Requirements are unclear | `job-intake` | Brief and hiring-owner decisions |
| Evaluation criteria are missing | `hiring-scorecard` | Agreed criteria, evidence, and anchors |
| Need relevant candidates | `sourcing-strategy` | Search plan, approved channels/spend, provenance |
| Have profiles to assess | `candidate-screening` | Evidence report and recruiter decision |
| Need to approach a candidate | `candidate-outreach` | Verified facts, draft, recipient history |
| Interview is the agreed next step | `interview-invitation` | Confirmed/proposed logistics and booking state |
| Interviewers need a plan | `interview-kit` | Timed questions and assessment guidance |
| Client needs a candidate summary | `candidate-presentation` | Evidence and approved sharing scope |

Load only the relevant installed skill. Skills may be installed individually; never assume a sibling directory is present. If a needed skill is missing, explain its purpose and use `bunx skills add vitaedotai/agent --skill <name>` only when installation is within the user's request. Otherwise give a concise manual handoff. Do not claim that delegation or installation happened when it did not.

## Maintain state

Keep a compact record with: assignment ID or descriptive label, current stage, artifact/version, evidence source, responsible person, unresolved questions, approval state, and next action with due date if supplied. Use actual Vitae records/tasks when verified tools support the requested persistence. Otherwise return a handoff table for the recruiter to save; do not claim chat memory is durable project state.

Possible states are draft, ready for review, awaiting user decision, authorized, queued, completed, and failed. They are not interchangeable. Before resuming a send, record creation, import, or workflow after a timeout, inspect the current state to avoid duplication.

## Execution boundaries

An agreed job brief does not authorize paid searches, candidate outreach, rejection, or public sharing. Honor explicit authorization already supplied for the same action and scope, and preserve Vitae's server approval gates. Do not repeatedly ask approval for ordinary reads or writing a requested draft.

Do not auto-reject or make employment decisions. Use job-related evidence and human review. Keep candidate information out of public artifacts. If a connector lacks a needed action, produce the artifact and identify the exact manual step; do not substitute another tool with broader effects.

## Beyond the initial catalog

The first release covers intake through candidate presentation. Offers, reference checks, rejection communication, placement handover, and post-placement follow-up remain explicit recruiter-owned steps. Record their owner and due action; do not invent missing specialist skills or claim those stages are automated.

## Example handoff

Assignment: Northbank backend engineer. Stage: screening. Completed: brief v2 and calibrated scorecard. Missing: incident-leadership evidence for Alex. Next action: recruiter reviews the screening report and chooses whether to invite Alex. Outreach: not sent. Booking: not created. No candidate stage change has been executed.

## Completion

Report completed artifacts and confirmed actions, open decisions, failed or unavailable capabilities, and the next owner. Stop at the requested outcome; a full assignment remains open while agreed stages still require action.
