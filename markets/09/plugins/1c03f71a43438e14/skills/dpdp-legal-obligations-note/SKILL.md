---
name: dpdp-legal-obligations-note
description: Use this when a company in India needs the DPDP questions a lawyer must answer: which basis applies to each use of data, what the notice must say, what the consent record must hold, how long data is kept, and what the contracts with outside companies need. Also use for questions for counsel, DPDP legal review, data protection legal questions, and what to take to a lawyer. This skill produces questions and never a legal opinion. Do not use for a law outside India.
---

# DPDP Legal Obligations Note

This step gives the user the questions a lawyer must answer for their company, with the evidence to carry into that meeting.

## Tools

- `start_dpdp_plan` and `confirm_company_profile`: run the interview and return the profile.
- `build_data_map`: builds the map. The note's questions hang off its flags.
- `draft_obligations_note`: returns the questions for counsel and the sample opinion outline.

## The seed: what every call carries

The server keeps no state. It derives the profile, the map and the note from a small seed every time.

- `industry`: one of `healthcare`, `d2c`, `financial-services`, `saas`, `general`
- `company_name`, `business_description`, `role`
- `answers`: every answer so far, keyed by question id, each `{ value, basis }`
- `map_changes`: every map edit so far

Rules:

- `basis` is `stated` for a fact the user gave and `assumed` for anything you worked out. Use the value `dont_know` for an unknown.
- Carry all answers and all map changes forward on every call. The full seed runs about 2 KB.
- Never send a `plan` field. The server rejects it.
- Keep the whole argument under 8,000 bytes.

## Getting here from an empty seed

The server derives the note from the seed, so the interview and the map run first.

1. Call `start_dpdp_plan` with the industry, a short business description, the user's role and `answers: {}`.
2. The intake screen appears with every question and a "Send my answers" button. Say the user can answer on the screen or in the chat. Screen path: call `confirm_company_profile` once with all their answers. Chat path: ask the `interview.next_questions` batch, call `confirm_company_profile` with every answer so far, and repeat until `interview.remaining` is zero.
3. Show the profile and have the user confirm it.
4. Call `build_data_map` with `map_changes: {}` to get the node keys, show the map, ask what is right, what they lack, their own tool names, the owners, what sits outside India and which outside companies have signed data terms. Call it again with those corrections in `map_changes`.

Keep that catch-up short, then come back here.

## What this document is

- It is a legal obligations note. It holds questions.
- Call it a legal obligations note every time you name it.
- Say once, in plain words, that a lawyer gives the legal opinion.
- Show the `disclaimer` from the result with the note.

## Step 1: Draft the note

- Call `draft_obligations_note` with the seed and `map_changes`.
- Show the `intro` lines and group the questions by `topic`.

Each question carries:

1. `question`, the thing the lawyer must answer
2. `evidence_needed`, what the user carries into the meeting
3. `what_it_changes`, the part of the business the answer moves
4. `citation_ids`, resolved through the `sources` list in the same result
5. `basis`, which is `always` for a question asked of every company, or `stated` or `assumed` from the user's answers
6. `flows`, the map rows that raised it, and an empty list on a general question

Say the counts: questions and citations.

## Step 2: Offer the sample

When the user asks what an opinion looks like, show `sample_opinion` from the result. Say it is a sample outline for a fictional company. A real opinion is written by a lawyer on the company's own facts.

## Step 3: Hand it over

- Say the user can take the note to their lawyer as it stands.
- List the evidence lines together so they can collect it in one go.
- Keep the seed and the map changes. The gaps, the plan and the buying guide need them.

## Reading a result

Each result holds `schema_version: 2`, `step`, `company_name`, `counts`, `disclaimer` and the note. The screen shows the detail.

- Say the counts and read out the few questions that matter most.
- Do not recite every question in the chat. Point the user at the screen.
- Never name a question or a citation the result did not return.

## What you must never say

- Never call this a legal opinion, an audit, a certificate or a compliance report.
- Never tell the user they are compliant. Never tell the user they are in breach.
- Never predict a penalty, a fine or an outcome.
- Never answer a question in the note on the lawyer's behalf. You may explain what the question means.

## Legal statements

- Cite the section or rule the result gives. Use the label or the ref from the `sources` entry for that citation id.
- Leave out any point with no citation in the result.
- Do not import GDPR words into DPDP.

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
