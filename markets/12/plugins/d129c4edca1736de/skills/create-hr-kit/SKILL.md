---
name: create-hr-kit
description: Generate an HR Kit for one existing KPI Gamification gamecard, covering the job description, roles and responsibilities, skill matrix, assessment questions and standard practices. Use when a company admin asks for a job description, JD, role definition, skill matrix, interview or assessment questions, or an HR Kit for a role that already has a gamecard. Previews first and saves a draft only after the user confirms. Do not use to design the gamecard itself.
---

# Create an HR Kit

An HR Kit is the set of HR documents for one role, generated from that role's gamecard: job description, roles and responsibilities, skill matrix, assessment questions and standard practices. The server writes all the content from the gamecard with KPI Gamification's own generator. You only choose the gamecard and pass the role details the user gives you. It is free, and it saves a **draft**; no PDF is generated.

Tools: `list_gamecards`, `preview_hr_kit`, `commit_hr_kit`.

## Rules you never break

1. **Do not write the document yourself.** The content comes from the server. Do not paste or rewrite a job description in chat as if it were the saved document.
2. **Ask, do not guess,** the optional role details (department, location, reports to, pay range). Leave a field out rather than inventing it. Pay figures especially: only use numbers the user gave you.
3. **Preview, show, confirm, commit.** Call `commit_hr_kit` only after the user has seen the summary and clearly said yes. Use a fresh UUID as `request_id`; reuse it only to retry the same commit.
4. **Team Member, not Employee,** in anything you write.
5. You cannot publish, email or assign anything. The user finishes in KPI Gamification.

## Steps

1. **Find the gamecard.** Call `list_gamecards`. If the user named a role, match it to a gamecard and confirm which one. If there is no gamecard for the role, say so and offer the `create-game-card` skill first. Gamecards that already have an HR Kit are flagged: there is one kit per gamecard, so tell the user and give them the link instead of starting a second.
2. **Collect optional details** in one message: role title (defaults to the gamecard name), department, location, who the role reports to, employment type (defaults to Full-Time), salary range and whether it is monthly or annual, incentives range, allowances range. Skip anything the user does not want to share; do not press for pay.
   - Set `include_incentives` or `include_allowances` to true only if you also give the matching min or max.
3. **Call `preview_hr_kit`.**
   - `valid: false`: read `errors` (each has a `fix`), correct, and call again. If an `existing` link is returned, tell the user the kit already exists and share the link.
   - `valid: true`: show a short summary: the role, the responsibilities generated (title and points), the number of skills and assessment questions, and that a draft with serial `HRK-<year>-NNNN` will be created.
4. **Ask for confirmation.** "Shall I save this HR Kit as a draft?"
5. **Call `commit_hr_kit`** with `preview_id` and a new `request_id`. Tell the user it is saved as a draft with its serial number, and share the link so they can review, edit and generate the PDF in KPI Gamification.
6. Offer a follow-up: an SOP that covers this role (`create-sop` skill).

## Errors

- `NOT_FOUND` or "no active gamecard": call `list_gamecards` again and use an id it returns.
- `ALREADY_EXISTS`: a kit already exists for this gamecard; share the link in the error.
- `PREVIEW_NOT_FOUND_OR_EXPIRED` (previews last 15 minutes): preview again and confirm again.
- `PREVIEW_ALREADY_USED`: it was already saved; do not save again.
- `RATE_LIMITED`: daily limit reached; try again tomorrow or continue in the app.
- `NOT_AUTHORIZED`: only a company admin of the connected company can do this.
