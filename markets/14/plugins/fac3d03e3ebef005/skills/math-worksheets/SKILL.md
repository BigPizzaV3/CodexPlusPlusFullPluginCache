---
name: math-worksheets
description: Make printable math worksheets (addition, subtraction, times tables, division, missing numbers, basic fractions) as a PDF with an answer key using Zovo Math Worksheet Maker; every answer is computed exactly.
---

# Zovo Math Worksheet Maker

Call `generate_math_worksheet` right away when the user asks for math worksheets, a times tables drill, long division practice, missing number practice or fraction practice. Pass what they said; leave the rest out (defaults: 20 problems, Letter, answer key on).

- `operation`: addition, subtraction, multiplication, division, "division with remainders", mixed, "addition and subtraction", "missing number", "adding fractions", "subtracting fractions", "multiplying fractions".
- `grade` (K to 6) sets number sizes. `digits` like 2 or "3x1" overrides it. `within` 20 for "within 20". `table` 7 for the 7 times table.
- `regrouping`: "none" for "no regrouping / no carrying / no borrowing", "required" for "with regrouping".
- `count`, `versions` (different sheets with the same rules), `paper` (letter or a4), `title`.
- To reprint the same sheet, pass the `seed` (set number) from the earlier result. For new problems, pass a different seed.
- If the user pastes or photographs their own problems, copy each one into `problems` as a string like "45 - 18" or "7 + ? = 12". The tool computes the answers.

After the tool returns: give a one-line summary (title, count, pages) and the PDF link. Mention any note (for example a shortened sheet). Do not list the answers unless the adult asks for them.

Do not use this tool for word problems, explaining a method, solving a single homework question, or grading a finished worksheet.
