---
name: interview-pack
description: Prepare a branded interview pack (interview brief, interviewer guide) for a client interview - fit against the must-haves with evidence from the CV, risk flags to probe, screening questions with what a strong answer sounds like, highlights, and compensation and notice from the consultant's notes. Use when a recruiter or executive search consultant says "interview pack", "prep the client for the interview", "interview guide for the hiring manager" or "questions to ask this candidate".
---

# Interview pack

Done when: the user has the interview pack (Word + PDF) for one candidate and one
role, built only from the CV and their notes, with the gaps listed.

Explicit instructions from the user take priority over this skill.

## Ground rules

- Reply in the user's language; write the pack content in the language the user
  wants (default: theirs).
- Evidence comes only from the CV and the consultant's notes. Never invent
  achievements, ratings, compensation, notice or interview dates. A rating is the
  consultant's or yours from stated evidence - say which in the chat.
- Cost: 0.5 credits. Say so if the user did not ask for the pack outright.
- `request_id` on the call; reuse on retry.

## Steps

1. **Gather:** the candidate's CV, the role and its must-haves (from the user, a
   position specification or job description), the client, the interview date and
   interviewer if known, and the consultant's notes (motivation, concerns,
   compensation, notice). If the must-haves are missing, ask for them once.
2. **Draft the payload** for `render_search_document` with `template_key`
   `interview-pack` and `brief` `{role}`:
   - `candidate_name`, `role_title`, `client` (a descriptor on a confidential
     search), `interview_date`, `interviewer` - only if known
   - `fit_summary`: two or three sentences
   - `fit_points`: one per must-have - `must_have`, `evidence` (from the CV, with
     employer and years), `rating` like "4/5"; leave out a must-have with no evidence
     and list it as a question instead
   - `risk_flags`: `flag`, `why` (gaps in dates, short tenures, missing must-haves)
   - `screening_questions`: 5-8, each with `strong_answer`
   - `highlights`: `text`, `source` ("CV" or "consultant notes")
   - `comp_and_notice`: only what the notes say
3. **Show** the fit points and risk flags briefly if the user wants to review first;
   otherwise render.
4. **Render**, then give the links and the list of gaps (for example "no notice
   period in the notes"). Remind the user that the pack is for the client's
   interviewers and must be checked before it goes out.

Several candidates: one pack per candidate (0.5 credits each); say the total first.
