---
name: create-hr-policy
description: Draft a company HR policy in KPI Gamification's HR Policy Studio from the admin's choices on working days, leave, reporting time and shifts, salary deductions and overtime, probation and notice period, benefits and safety. Use when a company admin asks to create, draft or write an HR policy, leave policy, attendance policy or employee policy document. Asks the admin for their choices rather than inventing them, previews first, and saves a draft only after the user confirms. Never publishes.
---

# Draft an HR policy

The HR Policy Studio in KPI Gamification builds the company's policy document. This skill fills in the Studio's choices from a conversation and saves a **draft**. The admin then reviews, adjusts and publishes it in the Studio; publishing is what generates the PDF. It is free.

Tools: `preview_hr_policy`, `commit_hr_policy`.

## Rules you never break

1. **Ask, do not guess.** A policy is a company's legal and pay commitments. Every choice must come from the user. Do not fill gaps with typical values ("probably a one-month notice"). Leave a section out if the user has not decided; the server accepts a partial policy (at least one section).
2. **Use only the listed options.** Most fields accept only fixed values (see `references/options.md`). The server rejects anything else and tells you the fix.
3. **Do not ask for settings that live elsewhere.** Leave allowance, weekly offs, holidays, permission hours and the per-day salary method are taken from the company's live settings (Company Policies, Leaves and Payroll) when the PDF is made. Tell the user this if they ask; do not collect them here.
4. **Never overwrite.** The server refuses a title that already exists. Pick a new title (add the year or a version).
5. **Preview, show, confirm, commit.** Call `commit_hr_policy` only after the user has seen the summary and clearly said yes. Fresh UUID `request_id` per commit; reuse it only to retry the same commit.
6. **Team Member, not Employee,** in anything you write. You give no legal advice; if asked whether a choice is legally required, say they should check with their advisor.

## Steps

1. **Ask what they want covered**, one group at a time, in plain language. Suggested order, skipping groups the user does not want:
   - Working days and what a Team Member gets for working on a weekly off.
   - Leave: paid leave entitlement style, what happens to unused paid leave, custom leave types, holiday reward, restricted days.
   - Timing: single reporting time or shifts, shift length, lunch break, late-to-permission, auto half day, leave via check-in.
   - Salary: deductions, overtime, performance incentives.
   - Probation and notice period (one for all, or separate for labour, staff and core roles).
   - Benefits, safety measures, memos.
2. **Pick a title**, such as "Acme Retail HR Policy 2026".
3. **Call `preview_hr_policy`** with `title` and `policy` containing only the choices the user made. `companyName`, address, month and year default to the company's own details; only send them if the user wants something different.
   - `valid: false`: read `errors` (each has a `fix`), correct and call again. If an `existing` link comes back, a policy with that title exists: choose another title.
   - `ignored_fields` lists anything the server did not accept. Tell the user if it matters.
   - `valid: true`: show the summary: title, period, sections covered, working days, reporting time, probation, notice period, benefits, safety. Repeat the notes about live settings and that this creates a draft only.
4. **Ask for confirmation.** "Shall I save this as a draft HR policy?"
5. **Call `commit_hr_policy`.** Tell the user it is saved as a draft, share the link to the HR Policy Studio, and explain they review, adjust and publish it there.

## Errors

- `ALREADY_EXISTS`: a policy with that title exists; choose a new title.
- `PREVIEW_NOT_FOUND_OR_EXPIRED` (15 minutes): preview again, confirm again.
- `PREVIEW_ALREADY_USED`: already saved; do not save again.
- `RATE_LIMITED`: daily limit reached; try again tomorrow or continue in the Studio.
- `NOT_AUTHORIZED`: only a company admin of the connected company can do this.
