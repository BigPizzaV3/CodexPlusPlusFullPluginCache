---
name: dpdp-30-day-plan
description: Use this when a company in India wants a dated DPDP action plan: what to do in week one, week two, week three and week four, who owns each action, and what proves it is done. Also use for DPDP roadmap, 30 day privacy plan, data protection remediation plan, and where to start on India's data protection law. Do not use for a law outside India.
---

# DPDP 30-Day Plan

This step turns the gap register into four weeks of work with an owner and a proof for every action.

## Tools

- `start_dpdp_plan` and `confirm_company_profile`: run the interview and return the profile.
- `build_data_map`: builds the map.
- `assess_dpdp_gaps`: returns the gap register the plan is built from.
- `build_30_day_plan`: returns the four weeks.

## The seed: what every call carries

The server keeps no state. It derives the profile, the map, the note, the gaps and the plan from a small seed every time.

- `industry`: one of `healthcare`, `d2c`, `financial-services`, `saas`, `general`
- `company_name`, `business_description`, `role`
- `answers`: every answer so far, keyed by question id, each `{ value, basis }`
- `map_changes`: every map edit so far
- `model_added_gaps`: optional, any gap added at the gap step

Rules:

- `basis` is `stated` for a fact the user gave and `assumed` for anything you worked out. Use the value `dont_know` for an unknown.
- Carry all answers, all map changes and all added gaps forward on every call. The full seed runs about 2 KB.
- Never send a `plan` field. The server rejects it.
- Keep the whole argument under 8,000 bytes.

## Getting here from an empty seed

The server derives the plan from the seed, so the interview and the map run first.

1. Call `start_dpdp_plan` with the industry, a short business description, the user's role and `answers: {}`.
2. The intake screen appears with every question and a "Send my answers" button. Say the user can answer on the screen or in the chat. Screen path: call `confirm_company_profile` once with all their answers. Chat path: ask the `interview.next_questions` batch, call `confirm_company_profile` with every answer so far, and repeat until `interview.remaining` is zero.
3. Show the profile and have the user confirm it.
4. Call `build_data_map` with `map_changes: {}` to get the node keys, show the map, ask what is right, what they lack, their own tool names, the owners, what sits outside India and which outside companies have signed data terms. Call it again with those corrections in `map_changes`.

Keep that catch-up short, then come back here.

## Step 1: Build the plan

- Call `build_30_day_plan` with the seed, `map_changes` and any `model_added_gaps`.
- The weeks follow a fixed order. Week 1 names owners and lists what exists. Week 2 takes the questions to a lawyer and decides. Week 3 fixes notices, contracts and access. Week 4 sets up the request route, the breach route and training, then tests them.
- A gap you added at the gap step enters week one.

## Step 2: Show the plan

For each of the four weeks show the `theme`, then the actions. Each action carries:

- `action`, the thing to do
- `owner_role`, the job that owns it
- `proof_of_closure`, what proves it is done
- `gap_id`, the gap it closes

Say the counts from the result: weeks and actions.

## Step 3: Make it usable

- Ask the user to put a job title against each `owner_role`. Use job titles. Do not record people's names.
- Say which actions wait on the lawyer, so the user books that meeting in week 1.
- Offer the buying guide for the gaps that need a tool.

## Reading a result

Each result holds `schema_version: 2`, `step`, `company_name`, `counts`, `disclaimer` and the four weeks. The screen shows the detail.

- Say the counts and read out week 1.
- Do not recite every action in the chat. Point the user at the screen.
- Never name an action or a gap id the result did not return.

## What you must never say

- Never say finishing the plan makes the company compliant.
- Never predict a penalty, a fine or an outcome.
- Never promise a date the law does not set.
- Show the `disclaimer` from the result with the plan.

## Legal statements

- Cite the section or rule the result gives on every legal point.
- Leave out any point with no citation in the result.
- Do not import GDPR words into DPDP.
- An action built on an assumed gap carries that mark.

## Support requests

- Do not add a contact line to your replies.
- When the user is stuck, help with the step itself.
- If the user asks how to reach MBS about the planner, give the contact page once: https://www.meridianbridgestrategy.com/contact
- Never give a person's name, an email address or a booking link.

## What to leave out

- Send only the seed fields the schema asks for. No chat history, no files, no unrelated context.
- Never ask for names, contact details or records of real people. The server rejects them with `PERSONAL_RECORDS`. If the user pastes such records, say you will not take them, and ask for the kinds of data held.

## Host reply

- Describe the result in plain text on Codex. Screens and the Save the pack button belong to ChatGPT; mention them when that host provides them.
- Explain the planner boundary in your own words. Keep internal skill paths and instruction quotes out of the reply.

## User confirmation

- Ask a question batch, then wait for the user. Repeat confirm only after answers change. Mark other answers dont_know when the user asks to leave them unknown.
- Carry profile_confirmed true only after the user confirms the profile, and map_confirmed true only after the user confirms the map. Clear the relevant confirmation when its inputs change.
