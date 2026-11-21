---
name: resume-pdf
description: Lay out resume facts the user gives into a one-column, text-based PDF (plus plain text and JSON copies) with generate_resume_pdf, and read the PDF text back to confirm each heading and bullet with check_resume_text.
---

# Zovo Resume PDF

Use `generate_resume_pdf` when the user wants their resume as a PDF and has given the facts (name plus at least one of summary, experience, education, skills, projects, certifications).

1. Pass only facts the user gave. Do not invent jobs, dates, numbers or skills, and do not rewrite bullets unless the user asked you to edit them first in the chat.
2. Dates: `start` and `end` as `YYYY-MM` (or a year); `end` may be `present`. Convert "March 2021" to `2021-03`. If a month is unclear, ask.
3. `contact` is a list of plain-text items such as an email, a phone number, a city and a profile link.
4. `template`: `classic` (default), `modern` or `compact`. `page_size`: `letter` (default) or `a4` (Europe, Asia, Australia).
5. Set `fit_to_one_page: true` when the user asks for one page. The result says whether it fit; if not, suggest which older roles or bullets to cut.
6. After the result, give the page count, any notes verbatim, and the PDF, text and JSON links. Say the links expire in about 1 hour.

Use `check_resume_text` with the same fields when the user asks whether the PDF is readable by applicant tracking systems or whether all bullets made it into the file. Report the result line, the reading order and any missing items. It checks text extraction; it does not score the resume or predict a specific system's ranking.

Do not use these tools for cover letters, Word (DOCX) files, two-column or photo resumes, or for reading a resume made elsewhere.
