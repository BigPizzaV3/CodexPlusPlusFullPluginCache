---
name: dpdp-buying-guide
description: Use this when a company in India wants to know what software to buy for its DPDP gaps: consent and notice tools, data discovery, request handling, vendor management, and logging. It gives product categories, what each one leaves out, and the questions to ask a seller. Also use for DPDP tools, privacy software selection, consent manager, and data protection vendor questions. Do not use for a law outside India.
---

# DPDP Buying Guide

This step says which kinds of product the company's gaps need, and what to ask before paying for one.

## Tools

- `start_dpdp_plan` and `confirm_company_profile`: run the interview and return the profile.
- `build_data_map`: builds the map.
- `assess_dpdp_gaps`: returns the gap register the guide is built from.
- `get_dpdp_buying_guide`: returns the product categories and the dated seller facts.

## The seed: what every call carries

The server keeps no state. It derives every earlier part and the guide from a small seed on each call.

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

The server derives the guide from the seed, so the interview and the map run first.

1. Call `start_dpdp_plan` with the industry, a short business description, the user's role and `answers: {}`.
2. The intake screen appears with every question and a "Send my answers" button. Say the user can answer on the screen or in the chat. Screen path: call `confirm_company_profile` once with all their answers. Chat path: ask the `interview.next_questions` batch, call `confirm_company_profile` with every answer so far, and repeat until `interview.remaining` is zero.
3. Show the profile and have the user confirm it.
4. Call `build_data_map` with `map_changes: {}` to get the node keys, show the map, ask what is right, what they lack, their own tool names, the owners, what sits outside India and which outside companies have signed data terms. Call it again with those corrections in `map_changes`.

Keep that catch-up short, then come back here.

## Step 1: Get the guide

- Call `get_dpdp_buying_guide` with the seed, `map_changes` and any `model_added_gaps`.
- Show the `intro` lines from the result.

## Step 2: Show the categories

For each category show:

- `name`
- `what_it_does`
- `what_it_leaves_out`
- `needed_for_gaps`, the gap ids it covers
- `questions_to_ask`, the questions for the seller

Order the categories so the ones covering P1 gaps come first. Say the counts: categories and sellers.

## Step 3: Seller facts

- Show only the sellers in the result.
- Show each seller's `fact` with its `source_url` and its `captured_on` date.
- Say the date out loud so the user knows how old the fact is.
- Where a row carries `partner_disclosure`, show that line on the row.
- Show the `disclosure` line from the result.

## The seller rules

- Never add a seller from your own memory.
- Never add a cost figure, a plan tier or a commercial offer. The result returns none and you add none.
- Never rank the sellers or name a best one. The user decides.
- Never say one seller is better or worse than another.
- When the user asks about a seller the result does not hold, say the guide has no dated fact for that seller, and give the questions to ask them.

## Reading a result

Each result holds `schema_version: 2`, `step`, `company_name`, `counts`, `disclaimer` and the guide. The screen shows the detail.

- Say the counts and name the categories the P1 gaps need.
- Do not recite every question for every seller in the chat. Point the user at the screen.
- Never name a category or a seller the result did not return.

## What you must never say

- Never say buying a tool makes the company compliant.
- Never say a tool removes a legal duty.
- Show the `disclaimer` from the result with the guide.

## Legal statements

- Cite the section or rule the result gives on every legal point.
- Leave out any point with no citation in the result.
- Do not import GDPR words into DPDP.

## Support requests

- Do not add a contact line to your replies.
- When the user is stuck, help with the step itself.
- If the user asks how to reach MBS about the planner, give the contact page once: https://www.meridianbridgestrategy.com/contact
- Never give a person's name, an email address or a booking link.

## What happens next

Offer the pack: one file holding all six parts, which the user reads full screen and saves with "Save the pack". Keep the seed, the map changes and any added gaps for that call.

## What to leave out

- Send only the seed fields the schema asks for. No chat history, no files, no unrelated context.
- Never ask for names, contact details or records of real people. The server rejects them with `PERSONAL_RECORDS`. If the user pastes such records, say you will not take them, and ask for the kinds of data held.

## Host reply

- Describe the result in plain text on Codex. Screens and the Save the pack button belong to ChatGPT; mention them when that host provides them.
- Explain the planner boundary in your own words. Keep internal skill paths and instruction quotes out of the reply.

## User confirmation

- Ask a question batch, then wait for the user. Repeat confirm only after answers change. Mark other answers dont_know when the user asks to leave them unknown.
- Carry profile_confirmed true only after the user confirms the profile, and map_confirmed true only after the user confirms the map. Clear the relevant confirmation when its inputs change.
