---
name: get-started
description: Show a new user what ATSPrep can do and start with a resume check.
---

# Get started with ATSPrep

1. Ask the user to paste their resume as plain text (or the text of a PDF or Word file). Don't ask for anything else first.
2. Call `check_resume` with it. If they also shared a job post or link, call `fetch_job_post` for a link, then pass `job_description` too.
3. The card shows the score and top fixes. Don't repeat them; offer one next step: tailor it to a job (`tailor_resume`), fix a bullet (`improve_bullet`), or practise interview questions (`interview_questions`).
4. Never invent experience, numbers or employers. Ask before adding any job-post keyword.
