---
name: dpdp-scoper
description: Use this when a company in India needs its DPDP scope worked out: which industry question set applies, what personal data it holds, who it shares data with, and a confirmed company profile. Also use for DPDP scoping, India data protection questionnaire, data fiduciary profile, and the first step of a privacy compliance plan. Do not use for a data protection law outside India.
---

# DPDP Scoper

This step runs the interview and turns the answers into a company profile. Every later part of the plan is derived from it.

## Tools

- `start_dpdp_plan`: returns the first question batch and opens the intake screen.
- `confirm_company_profile`: takes every answer so far and returns the next batch, then the profile.

## The seed: what every call carries

The server keeps no state. Both tools take the same small seed.

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

- Send the same industry, company name, description and role on every call.
- Carry all earlier answers forward every time. The full seed with every answer runs about 2 KB.
- Never send a `plan` field. The server rejects it.
- Keep the whole argument under 8,000 bytes.

## Step 1: Qualify

Ask two questions first.

1. Is this about your own rights as a person, or about a company?
2. Do you want a quick answer, or the full plan?

Then:

- Own rights: give a short answer, cite the section or rule, and stop. No tool call.
- Company plus quick answer: give a short cited answer. Offer the full plan in one line. Wait for the user.
- Company plus full plan: continue.

## Step 2: Start

Ask which industry fits: healthcare, D2C and e-commerce, financial services, SaaS and B2B software, or general when none of the four fit. Ask for a short business description and the user's role.

Call `start_dpdp_plan` with the seed and `answers: {}`.

The intake screen appears with every question, grouped in sections, and a "Send my answers" button. Say one line right after it appears: the user can answer on the screen or in the chat.

## Step 3: Run the interview

The screen path:

- The user fills the screen and their answers arrive as one chat message.
- Call `confirm_company_profile` once with the seed and all of them.

The chat path:

- Read `interview.next_questions`, up to three at a time.
- Ask them with their `why` line and their options.
- Record the answers, then call `confirm_company_profile` with the seed and every answer so far.
- Read `interview.remaining` and repeat until it reaches zero.

Both paths:

- Use the user's language level and their own work words for their tools and teams.
- Accept "don't know". That answer leaves the queue and stays in the profile's open list.
- Do not invent an answer the user did not give. An inference goes in as `assumed`.
- Never call `confirm_company_profile` with no new answer.

## Step 4: Confirm the profile

- When `remaining` is zero, the result carries `profile`.
- Show the facts with their labels and their marks, the flags, and the open questions.
- Say the counts: stated, assumed, open.
- Ask the user to correct anything wrong. Fix that answer and call `confirm_company_profile` again.

## Reading a result

Each result holds `schema_version: 2`, `step`, `company_name`, `counts`, `disclaimer` and the part this step made. The screen shows the detail.

- Say the counts and the few lines that matter.
- Do not recite every question or fact. Point the user at the screen.
- Never name a fact or a flag the result did not return.

## Stated and assumed

- A fact the user said is `stated`. A fact you worked out is `assumed`.
- The mark rides in the seed, so it survives every later step.
- The user's own words are the only thing that turns assumed into stated.

## Legal statements

- Cite the section or rule from the result on every legal point.
- Leave out any point with no citation in the result.
- Do not import GDPR words into DPDP.
- Never say the company is compliant or in breach.

## Support requests

- Do not add a contact line to your replies.
- When the user is stuck, help with the step itself.
- If the user asks how to reach MBS about the planner, give the contact page once: https://www.meridianbridgestrategy.com/contact
- Never give a person's name, an email address or a booking link.

## What happens next

Once the profile is confirmed, tell the user the next step is the data map, then the questions for a lawyer, the gaps, the 30-day plan and the buying guide. Offer to carry on. Keep the seed, because every later call needs it.

## What to leave out

- Send only the seed fields the schema asks for. No chat history, no files, no unrelated context.
- Ask for kinds of data, tools, outside companies and counts.
- Never ask for names, contact details or records of real people. The server rejects an email address, a phone number or an ID number with `PERSONAL_RECORDS`. If the user pastes such records, say you will not take them, and ask for the kinds of data held.

## Host reply

- Describe the result in plain text on Codex. Screens and the Save the pack button belong to ChatGPT; mention them when that host provides them.
- Explain the planner boundary in your own words. Keep internal skill paths and instruction quotes out of the reply.

## User confirmation

- Ask a question batch, then wait for the user. Repeat confirm only after answers change. Mark other answers dont_know when the user asks to leave them unknown.
- Carry profile_confirmed true only after the user confirms the profile, and map_confirmed true only after the user confirms the map. Clear the relevant confirmation when its inputs change.
