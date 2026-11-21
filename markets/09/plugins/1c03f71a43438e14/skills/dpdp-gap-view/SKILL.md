---
name: dpdp-gap-view
description: Use this when a company in India wants its DPDP gaps listed: missing notices, missing consent records, no way to withdraw consent, no route for data requests, no retention rule, no breach plan, no vendor contracts, and no named owner. Also use for DPDP gap analysis, gap register, data protection readiness check, and what is missing under India's data protection law. Do not use for a law outside India.
---

# DPDP Gap View

This step turns the company's answers and its map into one gap register it can work from.

## Tools

- `start_dpdp_plan` and `confirm_company_profile`: run the interview and return the profile.
- `build_data_map`: builds the map.
- `draft_obligations_note`: returns the questions for a lawyer and the citation ids an added gap needs.
- `assess_dpdp_gaps`: runs the server rules and returns the register.

## The seed: what every call carries

The server keeps no state. It derives the profile, the map, the note and the gaps from a small seed every time.

- `industry`: one of `healthcare`, `d2c`, `financial-services`, `saas`, `general`
- `company_name`, `business_description`, `role`
- `answers`: every answer so far, keyed by question id, each `{ value, basis }`
- `map_changes`: every map edit so far
- `model_added_gaps`: optional, any gap you added

Rules:

- `basis` is `stated` for a fact the user gave and `assumed` for anything you worked out. Use the value `dont_know` for an unknown.
- Carry all answers, all map changes and all added gaps forward on every call. The full seed runs about 2 KB.
- Never send a `plan` field. The server rejects it.
- Keep the whole argument under 8,000 bytes.

## Getting here from an empty seed

The server derives the gaps from the seed, so the interview and the map run first.

1. Call `start_dpdp_plan` with the industry, a short business description, the user's role and `answers: {}`.
2. The intake screen appears with every question and a "Send my answers" button. Say the user can answer on the screen or in the chat. Screen path: call `confirm_company_profile` once with all their answers. Chat path: ask the `interview.next_questions` batch, call `confirm_company_profile` with every answer so far, and repeat until `interview.remaining` is zero.
3. Show the profile and have the user confirm it.
4. Call `build_data_map` with `map_changes: {}` to get the node keys, show the map, ask what is right, what they lack, their own tool names, the owners, what sits outside India and which outside companies have signed data terms. Call it again with those corrections in `map_changes`.

Keep that catch-up short, then come back here.

## Step 1: Run the rules

- Call `assess_dpdp_gaps` with the seed and `map_changes`.
- The server rules run on the user's own answers. A gap the answers prove comes back stated. A gap from a context rule comes back assumed.
- Never drop a row the server returned.

## Step 2: Show the register

Group the rows the way the result groups them: legal, technical, operational.

Each row carries `id`, `evidence`, `fix`, `owner_role`, `priority`, `proof_of_closure`, `flows`, `question_ids`, `citation_ids` and its basis.

Say the counts from the result: total, P1, P2, stated, assumed.

## Step 3: Add a gap the rules missed

Use `model_added_gaps` when the user's answers show a gap the register lacks. Each one needs:

- a new `id`
- `group`, one of legal, technical, operational
- `evidence`, `fix`, `owner_role`, `priority`, `proof_of_closure`
- `flows` and `question_ids` that already exist
- `citation_ids` taken from the note result you just read

Then:

- Call `draft_obligations_note` first if you have not read the note, because the citation ids come from it.
- An added gap always stays assumed and enters week one.
- Carry it on every later call.

## Step 4: Check the assumed rows

- Name the rows marked assumed.
- Ask the user to confirm or correct each one.
- Fix the answer in the seed and call `assess_dpdp_gaps` again, so the marks are right.

## Reading a result

Each result holds `schema_version: 2`, `step`, `company_name`, `counts`, `disclaimer` and the register. The screen shows the detail.

- Say the counts and read out the P1 rows.
- Do not recite every row in the chat. Point the user at the screen.
- Never name a gap, a citation or a flow the result did not return.

## What you must never say

- Never say the company is compliant. Never say the company is in breach.
- Never predict a penalty, a fine or an outcome.
- Never call this an audit or a certificate. It is a gap register built on the user's own answers.
- Show the `disclaimer` from the result with the register.

## Legal statements

- Cite the section or rule the result gives. Use the label or the ref from the `sources` entry for that citation id.
- Leave out any point with no citation in the result.
- Do not import GDPR words into DPDP.

## Support requests

- Do not add a contact line to your replies.
- When the user is stuck, help with the step itself.
- If the user asks how to reach MBS about the planner, give the contact page once: https://www.meridianbridgestrategy.com/contact
- Never give a person's name, an email address or a booking link.

## What happens next

Offer the 30-day plan from this register, then the buying guide. Say it in one line and wait. Keep the seed, the map changes and any added gaps.

## What to leave out

- Send only the seed fields the schema asks for. No chat history, no files, no unrelated context.
- Never ask for names, contact details or records of real people. The server rejects them with `PERSONAL_RECORDS`. If the user pastes such records, say you will not take them, and ask for the kinds of data held.

## Host reply

- Describe the result in plain text on Codex. Screens and the Save the pack button belong to ChatGPT; mention them when that host provides them.
- Explain the planner boundary in your own words. Keep internal skill paths and instruction quotes out of the reply.

## User confirmation

- Ask a question batch, then wait for the user. Repeat confirm only after answers change. Mark other answers dont_know when the user asks to leave them unknown.
- Carry profile_confirmed true only after the user confirms the profile, and map_confirmed true only after the user confirms the map. Clear the relevant confirmation when its inputs change.
