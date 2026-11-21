---
name: dpdp-data-map
description: Use this when a company in India wants a personal data map: where customer and staff data is collected, which systems hold it, which outside companies receive it, and which flows leave India. Also use for DPDP data map, data flow map, data inventory, record of processing, and mapping personal data under India's data protection law. Do not use for a data protection law outside India.
---

# DPDP Data Map

This step draws the company's personal data on one radial map. The server builds it from the industry template plus the user's corrections.

## Tools

- `start_dpdp_plan` and `confirm_company_profile`: run the interview and return the profile.
- `build_data_map`: builds the map. Call it twice, once to see the template and once with the user's corrections.

## The seed: what every call carries

The server keeps no state. It rebuilds the map from a small seed every time.

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

The server derives the map from the seed, so the interview has to run first.

1. Call `start_dpdp_plan` with the industry, a short business description, the user's role and `answers: {}`.
2. The intake screen appears with every question and a "Send my answers" button. Say the user can answer on the screen or in the chat.
3. Screen path: their answers arrive as one message, so call `confirm_company_profile` once with all of them. Chat path: ask the `interview.next_questions` batch, then call `confirm_company_profile` with every answer so far, and repeat until `interview.remaining` is zero.
4. Show the profile and have the user confirm it.

Keep that catch-up short, then come back here.

## The rings

- Ring 0 is the person the data is about.
- Ring 1 is where people meet the company: forms, stores, apps, calls, front desks.
- Ring 2 is the company's own systems.
- Ring 3 is outside companies that receive the data.

## Step 1: See the template

- Call `build_data_map` with the seed and `map_changes: {}`.
- The result returns the sectors and the node list. Each node carries a stable `key`, its `id`, its `name`, its `ring` and its `confirmed` mark.
- Show the map screen. It opens full screen.
- Say the counts from the result: nodes, flows, outside companies, unconfirmed, cross border, contract gaps, systems with no owner.

## Step 2: Ask the user six things

1. Which of these do you have?
2. Which of these do you not have?
3. What do you call your own tools?
4. Who owns each one?
5. What sits outside India, or is reachable from outside India?
6. Which outside companies have signed data terms?

Add a seventh if the user names something the template lacks.

## Step 3: Apply the corrections

Call `build_data_map` again with the same seed and the answers in `map_changes`:

- `confirmed_keys`: node keys the user said they have
- `absent_keys`: node keys the user said they lack. The server removes them and their flows
- `renames`: key to the user's own label for that system or company
- `owners`: key to an owner role label, and an empty string to clear one
- `outside_india_keys`: nodes reachable from outside India. The server marks their touching flows cross border
- `contracts`: ring 3 key to `yes`, `no` or `unknown`
- `added_nodes` and `added_flows`: anything the user named that the template lacks, each with `confirmed`. A new node needs a new key. A new flow uses existing keys

Then:

- Confirmed means the user said it. Never set a key confirmed to tidy the map.
- Use only the keys the result returned. An unknown key, an edit to an absent node or an invalid sector is rejected.
- Show the updated counts and ask about anything still unconfirmed.
- Carry the same `map_changes` on every later call. The map rebuilds from them each time.

## Reading a result

Each result holds `schema_version: 2`, `step`, `company_name`, `counts`, `disclaimer` and the node catalog. The full map is on the screen.

- Say the counts and name the handful of rows that matter.
- Do not try to list thirty nodes in the chat. Point the user at the screen.
- Never name a node or a flow the result did not return.

## Stated and assumed

- A node or flow the user confirmed is stated. Everything from the template stays assumed until they confirm it.
- The marks ride in `answers` and `map_changes`, so they survive every later step.

## Legal statements

- Cite the section or rule from the result on every legal point.
- Leave out any point with no citation in the result.
- Do not import GDPR words into DPDP.
- Never say the company is compliant or in breach. A lawyer gives the legal opinion.

## Support requests

- Do not add a contact line to your replies.
- When the user is stuck, help with the step itself.
- If the user asks how to reach MBS about the planner, give the contact page once: https://www.meridianbridgestrategy.com/contact
- Never give a person's name, an email address or a booking link.

## Errors and what to do

- `INPUT_SHAPE`: a field is the wrong shape. Fix the named field and call again.
- `INPUT_SIZE`: the seed is over 8,000 bytes. Shorten labels and long answers.
- `MAP_INPUT`: send `map_changes` on its own.
- `MAP_COMPANY`: the company name does not match the seed.
- `PERSONAL_RECORDS`: a contact detail or an ID number reached the tool. Take it out.

## What to leave out

- Send only the seed fields the schema asks for. No chat history, no files, no unrelated context.
- Data categories are kinds of data, such as phone number, address or test result.
- Never put a real person's name, contact detail or record on the map. If the user pastes such records, say you will not take them, and ask for the kinds of data held.

## Host reply

- Describe the result in plain text on Codex. Screens and the Save the pack button belong to ChatGPT; mention them when that host provides them.
- Explain the planner boundary in your own words. Keep internal skill paths and instruction quotes out of the reply.

## User confirmation

- Ask a question batch, then wait for the user. Repeat confirm only after answers change. Mark other answers dont_know when the user asks to leave them unknown.
- Carry profile_confirmed true only after the user confirms the profile, and map_confirmed true only after the user confirms the map. Clear the relevant confirmation when its inputs change.
