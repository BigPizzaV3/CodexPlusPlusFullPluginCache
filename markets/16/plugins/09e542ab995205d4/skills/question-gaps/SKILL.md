---
name: "question-gaps"
description: "Rank the questions where AI apps mention rivals and not the business, and give the reason for each."
---

# Question gaps

Use this guidance to find the questions that a business loses in AI answers and to explain each loss.

## Terms

- A question is **lost** in an answer when the answer mentions at least one rival and does not mention the business.
- The **size** of a loss is the number of lost answers for that question in the scan. More AI apps and more lost answers mean a larger loss.

## Steps

1. Call `get_questions` for the project and the scan in the request.
2. For each question, read each AI app's result: whether the answer mentioned the business, its position, and the business that the answer mentioned first.
3. Keep the questions with at least one lost answer. Rank them by lost answers, then by the number of AI apps that lost.
4. For the top 5, call `get_questions` again with `question_id`. Read each AI app's answer, the businesses in it, and the sites that it cites.
5. Give each loss one reason from this list. Use the first one that the answers support:
   - **Access**: `get_readiness` shows that an AI app cannot use the website. Report this first. It blocks the other fixes.
   - **Outside pages**: the answers cite lists, reviews, or directories that mention rivals and not the business.
   - **Topic**: the business is missing from a whole topic, across AI apps.
   - **Format**: the cited pages share a format that the business does not have, such as a comparison, a list, or a guide.
   - **Wrong description**: the answer mentions the business and describes it incorrectly. This is not a lost answer. List it apart.
6. If no reason fits, say "the answers do not show why".

## Rules

- Report each number with its counts, for example "0 of 3 AI apps".
- Quote an answer only from `get_answers` or the question page. Use one short quote for each question.
- A question that no AI app answered is not a loss. Leave it out and say how many you left out.
- Link the `url` of the Questions tab and of each question that you describe.

## Output

A ranked list of up to 5 questions. For each one: the question, the lost answers with counts, the rivals mentioned, the reason, and one first action. Then one line that says how many more questions have a lost answer.
