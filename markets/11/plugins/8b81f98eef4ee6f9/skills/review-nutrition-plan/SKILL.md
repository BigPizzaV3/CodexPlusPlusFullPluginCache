---
name: review-nutrition-plan
description: Review how the signed-in user, or a client they coach, is following their Liftory nutrition plan, from the meals logged, skipped, and eaten beside the plan, and weekly adherence for a client. Use when the user asks how eating is going, what was logged, or how well a client follows their menu, before or without changing it.
---
# Review how a nutrition plan is followed

The user's explicit instructions take priority over this skill. The steps below are the default when the user has not said otherwise; when they ask for a different order, fewer questions, or another format, follow them, as long as the request stays within what the Liftory tools allow. An explicit instruction to save, activate, or send counts as the approval a step asks for. Always reply ENTIRELY in the user's own language: detect it from their latest message and write every word and sentence in that language. Never switch language part way through a reply, not even for a single sentence or phrase. Identifiers in tool results (client, plan, conversation, exercise, food and technique ids) are internal and only for tool calls. Never show one to the user, not even after a plan is created or when clients or conversations are listed: refer to people, plans and conversations by name, date or position in a list, and to exercises, foods and techniques by name. The one exception is the address of a link into the app: an id may sit inside the link's address, never in the text the user reads.

Liftory gives general fitness guidance, not medical or dietary advice. Health information is never asked for:
- Never ask about medical conditions, pain, injuries, pregnancy, eating disorders, medication, or body measurements, and never make one of them a question in a step.
- When the user brings one up on their own, give only general information, recommend a qualified professional for anything that depends on it, and do not ask follow-up questions about it. When a plan is being built, the exercises that put heavy load on the area they mention (each catalog exercise lists its high-load areas) are left out, and so are any exercises or foods they name.
- Do not store it: never write it into a plan, a menu, or a rationale, and do not repeat it back in later replies.
- Leave out every exercise or food the user asks to leave out. The reason is not needed and is not recorded.

## Whose log

Every tool acts as the signed-in Liftory user. Decide whose data the request is about before reading or writing anything:
- The user's own data: call the tools without clientId.
- A client the user coaches: call list_clients, find the client by the name the user gave, and give that client's clientId. When several clients match or none does, show the candidates and ask; never guess a clientId, never reuse one remembered from another conversation, and never pass the user's own id as a clientId.
- Unclear whether it is for the user or a client: call whoami, which says whether the user coaches clients, and ask only when they do.
- list_clients is empty: the user coaches no one, so only their own data is reachable. Say so instead of looking for the person another way.

## Steps

1. Decide whose log it is, as above.
2. Call get_last_nutrition_plan for that person, so the meals in the log can be read against the menu.
3. Call get_nutrition_log with the same clientId. The default period is the last 7 days; set from and to (year-month-day) when the user names another period, at most 31 days.
4. For a client, when the question is about how well they follow the plan over weeks, call get_nutrition_adherence with their clientId.
5. Report what the log shows: meals logged, skipped, and expected, the options chosen most often, foods left out, amounts changed, and extras eaten beside the plan. Say nothing the log does not show.
6. When the user then wants the menu changed, follow the build-nutrition-plan skill.

## Rules

Never invent facts:
- Every id (clientId, planId, exerciseId, techniqueId, foodId, sessionId) comes from a tool result in this conversation, never from memory or a guess.
- Clients, exercises, techniques, and foods are named only as a tool returned them or as the user wrote them.
- Numbers (sets, reps, durations, rest, loads, amounts, calorie and macro targets) come from the user, from their document, or from a design you showed them and they approved. Never state a body weight, a training load, or a target that neither the user gave nor a tool returned (get_body_progress reads only what the person logged; never suggest a target weight).
- When a fact you need is missing, ask for it instead of assuming it.

When a tool fails or returns nothing:
- "You are not this person's trainer, or their coaching access has ended.": stop working on that person and tell the user in plain words. Do not retry with another id or as the user's own data.
- "Your Liftory connection was revoked or has expired.": stop and ask the user to reconnect Liftory in their assistant's connection settings. Do not retry until they have.
- A null or empty result means there is nothing there: say so plainly. Never fill the gap with content of your own.
- Any other error: tell the user what Liftory answered, in plain words, and ask how to continue.

For which direction to take next (more load, sets or reps, a deload, a menu change), the check-progress skill reads the progress reports and grounds the suggestion.

## Output

A review gives the period, the counts of logged, skipped, and expected meals, then day by day what was eaten or skipped and any extras, and, for a client, adherence by week. It describes the log and does not judge the person.

After a write succeeds, end the confirmation with one markdown link to where it can be seen, its text naming the place and the id only inside the address, filled from the tool result:
- A training plan for themselves: [the plan](https://liftory.ch/app/training/week/PLANID), also under the Plans tab or menu then Training Plans.
- A training plan for a client: [the plan](https://liftory.ch/app/admin/training-editor/edit/PLANID?subscriberId=CLIENTID), also under the client on the coach dashboard, then Training.
- A nutrition plan for themselves: [your nutrition day](https://liftory.ch/app/nutrition), once it is the active one; otherwise [the plan](https://liftory.ch/app/admin/nutrition-editor/edit/PLANID).
- A nutrition plan for a client: [the plan](https://liftory.ch/app/admin/nutrition-editor/edit/PLANID?subscriberId=CLIENTID), also under the client on the coach dashboard, then Nutrition.
- A message: [the conversation](https://liftory.ch/app/messages).
The link opens the app on a phone where it is installed, and the browser elsewhere.
