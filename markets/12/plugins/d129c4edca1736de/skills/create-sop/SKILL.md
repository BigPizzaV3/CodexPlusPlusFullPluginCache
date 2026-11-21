---
name: create-sop
description: Generate a Standard Operating Procedure (SOP) or company-wide employee handbook from a company's KPI Gamification gamecards and HR Kits. Use when a company admin asks for an SOP, standard operating procedure, process document, handbook or escalation matrix for one or more roles. Previews first and saves a draft only after the user confirms. Needs at least one existing gamecard.
---

# Create an SOP

An SOP describes how work is done for the roles it covers: purpose, scope, roles involved, process steps, escalation matrix, tools and annexures. The server builds it from the company's gamecards (and HR Kits, if they exist) with KPI Gamification's own generator. You choose the category, the title and which roles it covers. It is free and saves a **draft**; no PDF is generated.

Tools: `list_gamecards`, `preview_sop`, `commit_sop`.

## Rules you never break

1. **Do not write the SOP yourself.** The content comes from the server. Do not present your own text as the saved document.
2. **Ask which roles and which category** instead of choosing for the user.
3. **Preview, show, confirm, commit.** Call `commit_sop` only after the user has seen the summary and clearly said yes. Fresh UUID `request_id` per commit; reuse it only to retry the same commit.
4. **Team Member, not Employee.**
5. You cannot publish or assign anything; the user finishes in KPI Gamification.

## Steps

1. **Call `list_gamecards`** to see what exists. If there are none, say an SOP needs a gamecard and offer the `create-game-card` skill.
2. **Choose the category** with the user. `category` is one of `company-wide`, `sales`, `marketing`, `operations`, `hr`, `finance`, `customer-service`, `it`, `other`. `company-wide` is the employee handbook for everybody (leave `gamecard_ids` empty to cover all roles). Every other category is a process SOP and needs at least one gamecard.
3. **Choose the roles** (`gamecard_ids`), up to 25, using ids from `list_gamecards`. Confirm the names with the user.
4. **Choose a title**, for example "Sales Process SOP". Propose one if the user has no preference.
5. **Call `preview_sop`.**
   - `valid: false`: read `errors` and their `fix`, correct, call again.
   - `valid: true`: show the summary: title, category, roles covered, purpose, process steps (as a numbered list), escalation rows, tools, annexures, and that a draft with serial `SOP-<year>-NNNN` will be created.
6. **Ask for confirmation.** "Shall I save this SOP as a draft?"
7. **Call `commit_sop`** with `preview_id` and a new `request_id`. Tell the user it is saved as a draft with its serial number, and share the link so they can review, edit and generate the PDF.

## Errors

- A gamecard not found: call `list_gamecards` again and use returned ids.
- `PREVIEW_NOT_FOUND_OR_EXPIRED` (15 minutes): preview again, confirm again.
- `PREVIEW_ALREADY_USED`: already saved; do not save again.
- `RATE_LIMITED`: daily limit reached; try again tomorrow or continue in the app.
- `NOT_AUTHORIZED`: only a company admin of the connected company can do this.
