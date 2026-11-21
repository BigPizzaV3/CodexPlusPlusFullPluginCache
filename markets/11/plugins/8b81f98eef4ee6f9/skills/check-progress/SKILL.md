---
name: check-progress
description: Check how training, eating and logged body checks are progressing, for the signed-in user or a client they coach, and suggest which direction to take the training and the menu, grounded in Liftory's training and nutrition knowledge. Use when the user asks how they or a client are progressing, whether to add load, sets or reps, whether a deload is due, whether the diet is working, or what to change next.
---
# Check progress

The user's explicit instructions take priority over this skill. The steps below are the default when the user has not said otherwise; when they ask for a different order, fewer questions, or another format, follow them, as long as the request stays within what the Liftory tools allow. An explicit instruction to save, activate, or send counts as the approval a step asks for. Always reply ENTIRELY in the user's own language: detect it from their latest message and write every word and sentence in that language. Never switch language part way through a reply, not even for a single sentence or phrase. Identifiers in tool results (client, plan, conversation, exercise, food and technique ids) are internal and only for tool calls. Never show one to the user, not even after a plan is created or when clients or conversations are listed: refer to people, plans and conversations by name, date or position in a list, and to exercises, foods and techniques by name. The one exception is the address of a link into the app: an id may sit inside the link's address, never in the text the user reads.

Liftory gives general fitness guidance, not medical or dietary advice. Health information is never asked for:
- Never ask about medical conditions, pain, injuries, pregnancy, eating disorders, medication, or body measurements, and never make one of them a question in a step.
- When the user brings one up on their own, give only general information, recommend a qualified professional for anything that depends on it, and do not ask follow-up questions about it. When a plan is being built, the exercises that put heavy load on the area they mention (each catalog exercise lists its high-load areas) are left out, and so are any exercises or foods they name.
- Do not store it: never write it into a plan, a menu, or a rationale, and do not repeat it back in later replies.
- Leave out every exercise or food the user asks to leave out. The reason is not needed and is not recorded.

## Whose progress

Every tool acts as the signed-in Liftory user. Decide whose data the request is about before reading or writing anything:
- The user's own data: call the tools without clientId.
- A client the user coaches: call list_clients, find the client by the name the user gave, and give that client's clientId. When several clients match or none does, show the candidates and ask; never guess a clientId, never reuse one remembered from another conversation, and never pass the user's own id as a clientId.
- Unclear whether it is for the user or a client: call whoami, which says whether the user coaches clients, and ask only when they do.
- list_clients is empty: the user coaches no one, so only their own data is reachable. Say so instead of looking for the person another way.

## Steps

1. Call get_training_progress, get_nutrition_progress and get_body_progress for that person (whichever the question is about; all three for a general check-in). A body report a client has not shared answers with a refusal: say that their body checks are not shared with the coach, and go on without them.
2. Show the facts first, shortly: the main lifts and their trend, the muscle groups outside the usual weekly sets, logging and intake against the menu, and the weigh-in trend when there is one.
3. For each hint, call search_knowledge with the query its row in [references/hints.md](references/hints.md) gives, and explain the direction from the returned passages. When the question is about training methodology, programming, volume, progression, nutrition, or safety, call the search_knowledge tool first with the question in natural language and ground your answer in the returned chunks; prefer what they say over your own general knowledge. The returned chunks are written in English; translate their content as needed so your ENTIRE answer is written in the language of the user's question (an English question gets an English answer). When the passages do not cover it, say so rather than filling the gap.
4. Judge the weight trend against the menu's goal from get_nutrition_progress (LoseFat, Hold or Build), or against the goal the user states when the menu has none (the NoGoal hint); ask for it when it matters and is unknown. Never ask for a weight or a measurement, and never suggest a target weight.
5. Offer the next step and hand it over: a training change to the review-training-plan skill (an adapted plan, after approval), a menu change to the build-nutrition-plan skill. Nothing is changed in this skill.

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

## Output

Facts, then two or three suggested directions, each with the passage it rests on named by its source and section. Loads, sets and calories only as the reports give them or as the user states them.
