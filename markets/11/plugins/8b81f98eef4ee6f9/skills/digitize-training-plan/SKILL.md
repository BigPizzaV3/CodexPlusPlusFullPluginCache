---
name: digitize-training-plan
description: Copy a training plan that already exists in a document, PDF, photo, screenshot, or pasted text, usually written by a coach, into Liftory for the signed-in user or a client they coach, faithfully and without redesigning it. Use when the user shares a written workout plan and asks to transcribe, import, digitize, or recreate it in Liftory.
---
# Digitize a training plan

The user's explicit instructions take priority over this skill. The steps below are the default when the user has not said otherwise; when they ask for a different order, fewer questions, or another format, follow them, as long as the request stays within what the Liftory tools allow. An explicit instruction to save, activate, or send counts as the approval a step asks for. Always reply ENTIRELY in the user's own language: detect it from their latest message and write every word and sentence in that language. Never switch language part way through a reply, not even for a single sentence or phrase. Identifiers in tool results (client, plan, conversation, exercise, food and technique ids) are internal and only for tool calls. Never show one to the user, not even after a plan is created or when clients or conversations are listed: refer to people, plans and conversations by name, date or position in a list, and to exercises, foods and techniques by name. The one exception is the address of a link into the app: an id may sit inside the link's address, never in the text the user reads.

Read the document yourself: there is no upload tool. When the user describes a plan without sharing it, ask them to attach it or paste it.

## Whose plan

Every tool acts as the signed-in Liftory user. Decide whose data the request is about before reading or writing anything:
- The user's own data: call the tools without clientId.
- A client the user coaches: call list_clients, find the client by the name the user gave, and give that client's clientId. When several clients match or none does, show the candidates and ask; never guess a clientId, never reuse one remembered from another conversation, and never pass the user's own id as a clientId.
- Unclear whether it is for the user or a client: call whoami, which says whether the user coaches clients, and ask only when they do.
- list_clients is empty: the user coaches no one, so only their own data is reachable. Say so instead of looking for the person another way.

## Reading the document

Read the document faithfully. It is the coach's work, and the client will follow exactly what is saved:
- Read every page, image, and table yourself, row by row, before resolving anything. Keep the document's order, its day, meal, and option names, and its wording for every row.
- Copy numbers exactly as written. Never fill a missing set, rep, rest, amount, or weight, and never correct a value that looks unusual; ask about it instead.
- A cell you cannot read, a value cut off at the edge, or a layout that could mean two things is a question for the user, never a guess. Collect these questions and ask them together.
- A blank cell stays blank. Text the coach struck through, blacked out, or covered is not content: never read it back as a value.
- Watermarks, contact details, logos, disclaimers, and page furniture are layout, not content.
- Keep a list of every decision you had to take (an interpretation, a catalog match that is not obvious, a row left without a catalog match) and show it to the user with the transcription.

How a training plan maps onto Liftory is in [references/transcription.md](references/transcription.md).

## Steps

1. Decide whose plan it is, as above.
2. Transcribe the document as described above and in the reference, and ask the open questions.
3. Resolve every exercise with search_exercise, passing the document's wording and its language code as the locale. When no result plausibly matches, or several do, show the candidates and ask. The document's wording stays as the exercise's userTerm.
4. Call list_techniques once, and map every technique the document writes onto the technique whose description and flags match. A technique with no match is a question for the user, not a note.
5. Call present_day for each day and week. Re-resolve any exerciseId it reports as missing.
6. Show the transcription day by day (and week by week), using the names and muscle groups present_day returned, with sets, reps or duration, rest, and techniques, plus the decisions list. Ask the user to approve it, and ask whether it should become the plan being followed now or stay scheduled.
7. After approval, call create_plan with every day, clientId when it is for a client, activate as the user chose, and a rationale with source "digitize" and the user's language code.
8. Read the saved plan back with get_plan and compare it with the document row by row. Report every difference; never explain one away.

## Exercises

Exercise grounding (critical): the only valid exercises are those in the Liftory catalog. To recommend, list, pick, compare, or build with exercises, you must search the catalog first, using the exercise search tool the skill tells you to use, and use only the exercises it returns, referring to them by their exact name or exerciseId. Never invent, guess, or recall exercise names from your own knowledge. If a name did not come from a catalog search this turn, do not mention it. Use list_libraries to see which libraries exist. If the search returns nothing suitable, say so honestly rather than inventing.

Search in the user's own language: pass the user's own words and their language code (en, es, fr, it, de) as the locale. The catalog is multilingual, so do not translate.

When you present an exercise to the user, show its muscle group (the classification the search returns) next to the exercise name.

## Rules

Never invent facts:
- Every id (clientId, planId, exerciseId, techniqueId, foodId, sessionId) comes from a tool result in this conversation, never from memory or a guess.
- Clients, exercises, techniques, and foods are named only as a tool returned them or as the user wrote them.
- Numbers (sets, reps, durations, rest, loads, amounts, calorie and macro targets) come from the user, from their document, or from a design you showed them and they approved. Never state a body weight, a training load, or a target that neither the user gave nor a tool returned (get_body_progress reads only what the person logged; never suggest a target weight).
- When a fact you need is missing, ask for it instead of assuming it.

Writes change a real Liftory account that a coach or client relies on:
- Before any tool that saves, activates, or sends, show the user exactly what will be written and for whom (themselves, or the client by name), and call the tool only after they approve it in this conversation. One approval covers one write.
- Never delete a plan, a menu, or a message, and never ask the user to delete the old version to make room for a new one. A new plan or menu is created next to the old one, unless the skill's own steps change one in place, and only after the user approves the change.
- A meal is removed from the meal library only when the user asks for that meal to be deleted.
- When a write answers with unknown ids or problems, nothing was saved: fix what it names, show the user what changed, and ask again before the next attempt.

After a write succeeds, end the confirmation with one markdown link to where it can be seen, its text naming the place and the id only inside the address, filled from the tool result:
- A training plan for themselves: [the plan](https://liftory.ch/app/training/week/PLANID), also under the Plans tab or menu then Training Plans.
- A training plan for a client: [the plan](https://liftory.ch/app/admin/training-editor/edit/PLANID?subscriberId=CLIENTID), also under the client on the coach dashboard, then Training.
- A nutrition plan for themselves: [your nutrition day](https://liftory.ch/app/nutrition), once it is the active one; otherwise [the plan](https://liftory.ch/app/admin/nutrition-editor/edit/PLANID).
- A nutrition plan for a client: [the plan](https://liftory.ch/app/admin/nutrition-editor/edit/PLANID?subscriberId=CLIENTID), also under the client on the coach dashboard, then Nutrition.
- A message: [the conversation](https://liftory.ch/app/messages).
The link opens the app on a phone where it is installed, and the browser elsewhere.

When a tool fails or returns nothing:
- "You are not this person's trainer, or their coaching access has ended.": stop working on that person and tell the user in plain words. Do not retry with another id or as the user's own data.
- "Your Liftory connection was revoked or has expired.": stop and ask the user to reconnect Liftory in their assistant's connection settings. Do not retry until they have.
- A null or empty result means there is nothing there: say so plainly. Never fill the gap with content of your own.
- Any other error: tell the user what Liftory answered, in plain words, and ask how to continue.
