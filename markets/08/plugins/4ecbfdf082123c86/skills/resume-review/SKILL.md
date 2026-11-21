---
name: resume-review
description: Score and review a resume or CV against an ATS rubric, then explain the highest-impact fixes. Use when the user shares a resume and wants feedback, a score, an ATS check, or asks "how good is my resume".
---

# Reviewing a resume

Use JobSprout's rubric-based scorer, not a freehand opinion: `score_resume` returns a deterministic 0-100 score with a category breakdown and a percentile against real scored resumes, rendered as a report card. That is the point of this skill.

## Workflow

1. Get the resume as text or a file. If the user only described their background, ask them to paste the resume or attach the file first. Do not review a LinkedIn URL or a job posting as if it were a resume.
2. Call `score_resume` with the resume text (or the file). The tool renders the score card with the full breakdown and top fixes. Do not rebuild that breakdown as text, a table or your own card.
3. In one or two sentences, name the weakest area and the single most useful fix from the tool's result. Go deeper only if the user asks.
4. Offer a next step:
   - To produce an improved, properly typeset version, use the **build-a-resume** skill (`build_resume`).
   - If the user has a linked JobSprout account and a specific job in mind, offer to tailor a saved resume with `tailor_cv_to_job` (see **tailor-and-apply**).

## Boundaries

- Never invent or estimate a score yourself. The score comes only from `score_resume`; identical text returns the identical score.
- Never review a LinkedIn profile, a portfolio, or a job description as a resume.
- Never search for jobs, list openings, or claim to apply on the user's behalf. These tools do not do that.
- Do not fabricate the user's experience when suggesting fixes; suggest how to strengthen what is real.

## Do not trigger on

- Requests to find or apply to jobs.
- General career advice with no resume shared.
