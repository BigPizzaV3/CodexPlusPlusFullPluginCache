---
name: role-intake
description: Turn a job link, pasted job text or a few answers into a saved role, then hand it to the campaign builder. Use when the user wants to fill a role or hire for a job. Needs recruiting turned on for the workspace.
---

# Role Intake

Turns the job the user wants to fill into a saved role in Kenso, then sends them to the campaign builder for that role. A role holds the title, the hiring company, the place, the pay, and what a candidate must and should have. The recruiting campaign's search, qualification, segments and copy are all built from it.

Roles have no tool in this app: you write the role with the user here, and they save it in Kenso's campaign builder, which starts a recruiting campaign from it. Your part is the judgement: a complete, fair role with nothing invented.

Recruiting must be on for the workspace. When the builder offers no Recruiting choice, recruiting is off: say so, and offer a campaign that finds customers instead.

## 1. Get the job

Ask for one of three things: a link to the job post, the job text pasted in, or a few answers.

- Pasted text: read the title, employer, place, work mode, pay, must-haves and nice-to-haves from it yourself. Note each field the post does not give.
- A link: ask them to paste the post's text here. If they would rather not, the builder reads the link itself (step 4), and you help with the gaps it leaves.
- Neither: ask the questions in step 2 yourself.

## 2. Fill the gaps

Ask about every field the post left out, in one message and in this order: the job title; which company is hiring (the workspace's own company unless they say otherwise); where the role is based, and whether it is onsite, hybrid or remote; what it pays, and per year, month, day or hour (they may skip it); what a candidate must have to be considered (three to five lines); the level, such as Senior or Lead.

Never invent pay, must-haves or a location. When the user skips pay, leave it out.

Rewrite a must-have about age, gender, race, religion, disability, family status or nationality into what the job needs, or drop it: "young and energetic" is not a requirement, and "native English speaker" becomes "Fluent English". Say once, plainly, what you changed and why.

## 3. Confirm and save

Show the role as a short list (title, company, place and remote policy, pay, must-haves, nice-to-haves) and ask for changes. When they confirm:

- A new role: send them to the builder in step 4 with the confirmed role, laid out field by field as the builder names its fields, so they can paste each one: Title, Employer, Employer website, Job link, Location, Work mode (On-site, Hybrid or Remote), Seniority, Pay from, Pay to, Currency, Per (Year, Month, Day or Hour), Must-haves (one per line), Nice-to-haves (one per line), Description. Leave out a field they did not give.
- A role they already have: it lives in its recruiting campaign's settings. Find the campaign with `list_campaigns()`, then send them to `https://app.ken.so/<workspace id>/demo/campaigns/<campaign id>?tab=settings`, the role section, with only the fields that change.

The user saves it there. Then say what they should see, for example "The role Senior Backend Engineer is saved on the campaign."

## 4. Hand off to the builder

Share the builder link and stop there: https://app.ken.so/<workspace id>/demo/campaigns/build?kind=recruiting. It opens with Recruiting picked: they choose With AI or Manually and name the campaign. In Role details, they paste the post or its link into "Job post or link" and click "Fill in", then check each field against the role you confirmed and fix what differs. The builder saves the role and plans the candidate search, the LinkedIn-first sequence and the copy from it. Never start a campaign build for customers in its place.

## Errors

Tools return a normalized error envelope (`success: false`, `error.category`). On `plan_limit` or `billing`, surface `error.message` and `error.recovery.summary`; never retry blindly. When the builder will not save a field, ask the user what it says and fix that field.
