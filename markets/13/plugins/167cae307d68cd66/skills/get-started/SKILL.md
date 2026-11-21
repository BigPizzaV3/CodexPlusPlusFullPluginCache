---
name: get-started
description: First steps with Prehrana after connecting it. Checks that the connection works, shows today's diary and goal, and explains how to log food by describing it.
---

# Get started with Prehrana

Use this workflow right after the user connects Prehrana, or when they ask how to start using it.

1. Read today's diary with `dnevni_pregled`, using today's date in the user's time zone. Tell the user in one or two sentences what is already logged today and how many calories are left against the goal. If nothing is logged yet, say so.
2. Read the goals with `dohvati_ciljeve`. If there is no active goal, tell the user they can set a daily calorie, protein, carbohydrate, fat and target weight goal. Set a goal with `postavi_cilj` only after the user has given or approved the numbers.
3. Explain how logging works, in the user's language, with one example: the user describes what they ate in plain words, for example "two eggs and a slice of wholegrain bread for breakfast", and the meal is saved to their Prehrana diary with estimated calories and nutrients. Mention that a wrong amount can be corrected and an entry can be deleted by asking.
4. Offer two or three things to try next, such as logging the last meal, logging water, or showing this week's overview with `tjedni_pregled`.

Keep the reply short. Nutrient values are estimates. Do not give medical advice, diagnoses or treatment recommendations; for health questions, suggest a doctor or a registered dietitian.

Only the user's own diary is read in this workflow. Meals of group members are read only when the user asks about a specific member, and only if that member has chosen to share meals with assistants.
