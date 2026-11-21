# Question payloads

Use the live tool schema as the authority. A basic question is:

```json
{
  "question_text": "A mass $m$ experiences force $F$. Find its acceleration.",
  "question_type": "MCQ_SINGLE",
  "options": ["$F/m$", "$m/F$", "$Fm$", "$F+m$"],
  "correct_option": "A",
  "solution": "Newton's second law gives $a = F/m$.",
  "subject": "Physics",
  "chapter": "Laws of Motion",
  "topic": "Newton's second law",
  "difficulty": "medium",
  "marks": 4,
  "negative_marks": 1
}
```

MCQ_SINGLE uses one letter; MCQ_MULTI uses comma-separated letters such as A,C;
NUMERICAL uses the answer as a string. DESCRIPTIVE uses a written solution.
Options contain the text only, without A)/B) prefixes. Difficulty is easy,
medium or hard. Check correctness and consistency of answers before uploading.

For bilingual questions, put English first followed by ` #LS# ` and the regional
translation in question_text, each option and solution. Preserve LaTeX in both
language parts. Do not send an extra # after the separator.

Use simple Markdown pipe tables with a header separator row inside question_text
or solution. JSON newlines separate table rows. Avoid merged cells.

For sectioned uploads use sections with section_title and a questions array.
Never send both sections and a flat questions array. Respect tool batch limits;
obtain approval for the complete batch before performing multiple uploads.
