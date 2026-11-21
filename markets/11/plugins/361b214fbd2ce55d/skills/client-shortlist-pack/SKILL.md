---
name: client-shortlist-pack
description: Build the client shortlist pack (client submission, candidate slate) for a search - a candidate profile for each shortlisted candidate in the firm's template, a branded shortlist deck, and a cover email draft for the client that the user reviews and sends themselves. Use when a recruiter or executive search consultant says "put together the shortlist for the client", "shortlist pack", "slate for the hiring manager", "client presentation of candidates" or "submit these candidates to the client".
---

# Client shortlist pack

Done when: the user has (1) candidate profiles in the firm's template, (2) a
shortlist deck, and (3) a cover email draft shown in the chat or saved as a draft
in their mail - and nothing has been sent to anyone.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language; documents follow the template's language.
- Use only facts from the CVs and the user's notes. Never invent ratings, fit
  scores, compensation, notice periods, readiness or reasons for interest. If the
  user gave no rating for a criterion, leave that criterion out.
- Cost: profiles 1 credit per candidate; shortlist deck 0.5 credits. Before starting,
  state the total (for example "3 candidates: 3 credits for profiles + 0.5 for the
  deck") and wait for a yes unless the user already asked for the whole pack.
- `request_id` on every credit-using call; reuse on retry.
- Confidential search: `brief.confidential = true`, `client_name` (used only to check
  the output) and `client_descriptor`. Never write the client's name in documents.

## Steps

1. **Gather.** Role title, client (or confidential descriptor), the shortlisted CVs,
   and the user's notes per candidate (fit against must-haves, readiness, notice,
   compensation only if the user gives it). Ask once for anything essential that is
   missing (the role title, which candidates); do not ask for optional details.
2. **Profiles.** Follow the format-cvs steps: `find_template` (or the template the
   user named) -> `get_template_schema` -> one `fill_template` call with all
   candidates for a `cvtobios` template, or `format_cv` per CV. Keep each
   `record_id`.
3. **Deck.** `render_search_document` with `template_key` `shortlist-deck`,
   `brief` (`role`, plus what the user gave) and `candidates`: `name`,
   `current_role`, `current_company`, `location`, `summary_points` (2-4 short facts
   from the CV), `fit` (`criterion`, `rating` 1-5, only where the user rated it),
   `readiness`, `notice`, `compensation`. Use `kit_id` from `list_brand_kits` only
   if the user wants the client's brand.
4. **Cover email draft.** Write it yourself in the user's language and the firm's
   voice: who is attached, one or two factual lines per candidate, next step the user
   proposed (for example interview slots). No claims beyond the user's notes.
   - Show the draft in the chat. If the user asks and has Gmail or Outlook connected,
     save it as a draft there. **Never send it**, even if asked to "just send it" -
     say the user sends it after checking the documents.
   - Formatix links expire after an hour: tell the user to download the files and
     attach them, not to paste the links into a client email.
5. **CRM / ATS (optional).** If the user asks and has HubSpot, Salesforce, Recruit CRM
   or Manatal connected, you may read the job and candidate records to fill gaps the
   user confirms, or add a note that the shortlist was prepared. Never change
   pipeline stages or send messages from those apps without the user's yes.
6. **Report.** Links to the profiles and the deck (Word/PowerPoint + PDF), the email
   draft, and what was left out for lack of facts.

## Repeats and corrections

A correction to a profile is free: fix-a-document. If Formatix answers
`looks_like_correction`, ask before re-sending with `confirm_new_document=true`.
