---
name: dpdp-planner
description: Use this when a company in India wants a plan for the Digital Personal Data Protection Act and has no idea where to start. It runs the whole journey: a short interview, a personal data map, the questions a lawyer must answer, a gap register, a 30-day plan, a buying guide, and one pack the user saves. Also use for India data protection, data fiduciary duties, consent and notice records, privacy compliance planning, and DPDP readiness. Do not use for a data protection law outside India.
---

# DPDP Planner

The user arrives with no plan. They leave with their company's analysis and a list of what to do. Run the steps in order and finish each one before moving on.

## The eight tools

Call them by these exact names.

1. `start_dpdp_plan` returns the first question batch.
2. `confirm_company_profile` takes the answers so far and returns the next batch, then the profile.
3. `build_data_map` builds the map from the industry template plus the user's corrections.
4. `draft_obligations_note` returns the questions for a lawyer and the sample opinion outline.
5. `assess_dpdp_gaps` returns the gap register in three groups.
6. `build_30_day_plan` returns four weeks of actions.
7. `get_dpdp_buying_guide` returns product categories and dated seller facts.
8. `export_dpdp_plan_pack` returns the pack screen and the file name.

## The seed: what every call carries

The server keeps no state. It rebuilds the whole plan from a small seed on every call.

- `industry`: one of `healthcare`, `d2c`, `financial-services`, `saas`, `general`
- `company_name`: at most 160 characters
- `business_description`: at most 600 characters, a short business category
- `role`: at most 80 characters, a job label
- `answers`: every answer so far, keyed by question id

Each answer is `{ value, basis }`.

- `basis` is `stated` for a fact the user gave. It is `assumed` for anything you worked out.
- Use the value `dont_know` for an unknown, with `basis: "stated"`, because the user said they do not know.
- Each answer string stays under 300 characters. Up to 80 answers.

Rules:

- Send the same `industry`, `company_name`, `business_description` and `role` on every call.
- Carry all earlier answers forward every time. A dropped answer is a lost fact.
- Never send a `plan` field. The server rejects it.
- Keep the whole argument under 8,000 bytes. Shorten free text before you drop an answer.

## Reading a result

Each result holds `schema_version: 2`, `step`, `company_name`, `counts`, `disclaimer` and the part this step made. The step names are intake, profile, map, note, gaps, plan, buying, pack.

- The screen shows the detail. Say the counts and the few lines that matter.
- Do not try to recite every row. Point the user at the screen.
- Never name a row, a seller or a citation the result did not return.
- Earlier parts are gone from your view. The seed is what carries them.

## Step 0: Qualify

Ask two questions before any tool call.

1. Is this about your own rights as a person, or about a company?
2. Do you want a quick answer, or the full plan?

Then:

- Own rights: give a short answer, cite the section or rule, and stop. No tool call.
- Company plus quick answer: give a short cited answer. Offer the full plan in one line. Wait.
- Company plus full plan: continue to step 1.

## Step 1: The interview

- Ask the industry, a short business description and the user's role.
- Call `start_dpdp_plan` with the seed and `answers: {}`.
- The intake screen appears with every question, grouped in sections, and a "Send my answers" button. Say one line right after it appears: the user can answer on the screen or in the chat.

The screen path:

- The user fills the screen and their answers arrive as one chat message.
- Call `confirm_company_profile` once with the seed and all of them.

The chat path:

- Read `interview.next_questions`, up to three at a time. Ask them with their `why` line and their options.
- Record each answer into `answers`, then call `confirm_company_profile` with the seed and every answer so far.
- Read `interview.remaining` and repeat until it reaches zero.

Both paths:

- Accept "don't know". That answer leaves the queue and stays in the profile's open list.
- Never call `confirm_company_profile` with no new answer. Ask first, then call.
- The full seed with every answer runs about 2 KB, so carrying all answers on every call is cheap.

## Step 2: Confirm the profile

- When `remaining` is zero, the result carries `profile`.
- Show the facts, the flags and the open questions.
- Say the counts: stated, assumed, open.
- Ask the user to correct anything wrong. Fix the answer and call `confirm_company_profile` again.

## Step 3: The data map

- Call `build_data_map` with the seed and `map_changes: {}`. The result returns the sectors and the node list, each node with a stable `key`, its name, its ring and its confirmed mark.
- Show the map screen. It opens full screen.
- Then ask the user six things: which of these are right, which they do not have, what they call their own tools, who owns each one, what sits outside India, and which outside companies have signed data terms.
- Call `build_data_map` again with their answers in `map_changes`:
  - `confirmed_keys`: nodes the user said they have
  - `absent_keys`: nodes the user said they lack, which removes their flows
  - `renames`: key to the user's own label
  - `owners`: key to an owner role label, and an empty string to clear one
  - `outside_india_keys`: nodes reachable from outside India
  - `contracts`: ring 3 key to `yes`, `no` or `unknown`
  - `added_nodes` and `added_flows`: anything the user named that the template lacks, each with `confirmed`
- Confirmed means the user said it. Never set a key confirmed to tidy the map.
- Carry the same `map_changes` on every later call.

## Step 4: The legal obligations note

- Call `draft_obligations_note` with the seed and `map_changes`.
- Present it as a legal obligations note holding questions for a lawyer.
- Each question carries a basis: `always` means asked of every company, `stated` and `assumed` follow the user's answers.
- Never call it a legal opinion. Never say the company is compliant or in breach.
- Say once that a lawyer gives the legal opinion.
- Offer the sample opinion outline when the user asks what an opinion looks like.

## Step 5: The gaps

- Call `assess_dpdp_gaps` with the seed and `map_changes`.
- Show the three groups: legal, technical, operational. Say the counts.
- You may add a gap the answers show and the rules missed, through `model_added_gaps`. Each one needs a new `id`, its `group`, `evidence`, `fix`, `owner_role`, `priority`, `proof_of_closure`, `flows`, `question_ids`, and `citation_ids` taken from the note result you just read.
- An added gap always stays assumed and enters week one. Carry it on every later call.

## Step 6: The 30-day plan

- Call `build_30_day_plan` with the seed, `map_changes` and any `model_added_gaps`.
- Show four weeks. Each action carries an owner role, a proof of closure and its gap id.

## Step 7: The buying guide

- Call `get_dpdp_buying_guide` with the seed, `map_changes` and any `model_added_gaps`.
- Show the categories, what each does, what each leaves out, and the questions to ask a seller.
- Use only the seller facts in the result, with the source link and the capture date.
- Never add a seller, a cost figure or a ranking from your own memory.
- Show the `disclosure` line.

## Step 8: The pack

- Call `export_dpdp_plan_pack` with the seed, `map_changes` and any `model_added_gaps`.
- The result carries `pack.file_name` and `pack.counts`.
- Tell the user to read the pack full screen and use "Save the pack" on the screen.
- Report the stated and assumed counts from `pack.counts`.

## Stated and assumed

- A fact the user said is `stated`. A fact you worked out is `assumed`.
- The mark rides in the seed, so it survives every step.
- Never upgrade an assumed answer. The user's own words upgrade it.
- Say the counts whenever you show the profile, the gaps or the pack.

## Legal statements

- Cite the section or rule from the result. Note and gap rows carry `citation_ids`, and their sources are grouped under `sources`. Cite by the label or the ref the result gives.
- Leave out any point with no citation in the result.
- Do not import GDPR words into DPDP.
- Show the `disclaimer` with the note, the gaps and the pack.

## Support requests

- Do not add a contact line to your replies.
- When the user is stuck, help with the step itself.
- If the user asks how to reach MBS about the planner, give the contact page once: https://www.meridianbridgestrategy.com/contact
- Never give a person's name, an email address or a booking link.

## Errors and what to do

- `INPUT_SHAPE`: a field is the wrong shape. Fix the named field and call again.
- `INPUT_SIZE`: the seed is over 8,000 bytes. Shorten the description and the long answers.
- `PERSONAL_RECORDS`: an email address, a phone number or an ID number reached a tool. Take it out and send the kind of data.
- `MAP_INPUT`: send `map_changes` on its own.
- `GAP_CITATION`: an added gap used a citation id the note did not return. Use the ids from the note result.

## What to leave out

- Send only the seed fields the schema asks for. No chat history, no files, no unrelated context.
- Ask for kinds of data, tools, outside companies and counts.
- Never ask for names, contact details or records of real people. If the user pastes such records, say you will not take them, and ask for the kinds of data held.

## Host reply

- Describe the result in plain text on Codex. Screens and the Save the pack button belong to ChatGPT; mention them when that host provides them.
- Explain the planner boundary in your own words. Keep internal skill paths and instruction quotes out of the reply.

## User confirmation

- Ask a question batch, then wait for the user. Repeat confirm only after answers change. Mark other answers dont_know when the user asks to leave them unknown.
- Carry profile_confirmed true only after the user confirms the profile, and map_confirmed true only after the user confirms the map. Clear the relevant confirmation when its inputs change.
