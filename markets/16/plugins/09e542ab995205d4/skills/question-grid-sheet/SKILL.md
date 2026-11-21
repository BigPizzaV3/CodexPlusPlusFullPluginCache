---
name: "question-grid-sheet"
description: "Build a spreadsheet grid of tracked questions against each AI app, with position, named or not named, branded or non-branded, and topic."
---

# Question grid sheet

Use this guidance to build one grid of every tracked question against every AI app. A person reads it at a glance and sees where the business is named and where it is not.

## Build the sheet

1. Call `get_questions` for the project and the scan in the request. Call it again with `include_branded: false`.
2. Make one row for each question in `topics[].questions`. The row key is the question `id`. Put it in the last column and never change it.
3. Fill the Frontmost AI columns:

| Column | Value |
|---|---|
| Question | `text` |
| Topic | the `topic` of its group |
| Branded | "Non-branded" when the second call returns the question `id`, else "Branded" |
| One column for each AI app | from the `by_app` entry for that app |
| Named | `named` of `answers`, such as "3 of 6" |
| Named First | the business that `named_first` gives in the most AI apps, with its count |
| Change | `result`: Won or Lost since the previous scan, else empty |
| Link | `url` |

4. Fill each AI app cell with one value:
   - The `position` number when `named` is true and a position exists.
   - "Named" when `named` is true and `position` is null.
   - "Not named" when `named` is false.
   - "No answer" when `status` is not ok. Do not count this cell as a loss.
5. Color the cells. Named cells get a light green fill. "Not named" cells get a light red fill. "No answer" cells get a gray fill.
6. Group the rows by Topic. Inside a topic, put the questions with the fewest named answers first.
7. Above the grid, write two lines: non-branded questions named in X of Y answers, and branded questions named in X of Y answers. Add the counts from the rows of each group.

## Refresh the sheet

1. Call `get_questions` again for the latest scan, in both question scopes.
2. Match each question to a sheet row by the question `id`. Rewrite only the Frontmost AI columns.
3. Keep each column that the person added, and keep its cells.
4. Add a row for a new question. For a question that the data no longer returns, keep the row and write "Not tracked now" in Change.
5. Write the scan date above the grid.

## Rules

- Never join branded and non-branded questions in one rate. A branded question names the business in its own text, so its rate is high for every business.
- Report each rate with its counts.
- A position is the place of the business in the answer's list. 1 is first. Do not average positions across the two question scopes.
- An empty cell is never a zero. Write the status.
- Use the names of the AI apps as the data gives them.
- Ask before you change a question in Frontmost AI. This sheet reads only.

## Output

A spreadsheet file with one grid, the two count lines above it, and the scan date. If the AI app cannot make a file, return the grid as CSV and state the color rule in one line.
