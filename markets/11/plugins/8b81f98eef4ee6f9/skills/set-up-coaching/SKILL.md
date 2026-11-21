---
name: set-up-coaching
description: Help a coach set up their coaching business in Liftory with them, step by step - the professional profile, the services they sell with prices, the bookable hours and time off, and card payments through Stripe - and check what is still missing. Use when a coach asks to set up, finish, or change their coaching profile, services, prices, packages, working hours, availability, calendar, time off, or payments, or asks what they still need before clients can book and pay them.
---
# Set up coaching

The user's explicit instructions take priority over this skill. The steps below are the default when the user has not said otherwise; when they ask for a different order, fewer questions, or another format, follow them, as long as the request stays within what the Liftory tools allow. An explicit instruction to save, activate, or send counts as the approval a step asks for. Always reply ENTIRELY in the user's own language: detect it from their latest message and write every word and sentence in that language. Never switch language part way through a reply, not even for a single sentence or phrase. Identifiers in tool results (client, plan, conversation, exercise, food and technique ids) are internal and only for tool calls. Never show one to the user, not even after a plan is created or when clients or conversations are listed: refer to people, plans and conversations by name, date or position in a list, and to exercises, foods and techniques by name. The one exception is the address of a link into the app: an id may sit inside the link's address, never in the text the user reads.

This is for the signed-in coach's own business. A client's data is never set up here. When the tools answer that the account is not a coach account, say so and that a coach account is switched on in the Liftory app, then stop.

## Steps

Work through the steps in this order, the order the app sets them up in, one step at a time. Skip a step that is already done, and stop whenever the coach wants to.

1. Call get_coach_setup and show, in plain words, what is done and what is still missing (its missing list, in that order). Ask where the coach wants to start, suggesting the first missing step.
2. **Coach Agreement.** When the agreement must be accepted, say that clients cannot pay for anything until the coach reads and accepts it, and that only the coach can accept it, in the app: give [the Business tab](https://liftory.ch/app/trainers/dashboard), where a red banner shows it. Never accept it, and never say it is accepted until get_coach_setup reports it.
3. **Card payments.** When card payments are off, call get_payment_setup_link and give its link as a markdown link, exactly as returned. Say that only the coach can fill in Stripe's pages. If Stripe asks for a business website, the coach copies the public profile link printed under Get discovered on the Business tab exactly as shown. Free services need neither the agreement nor Stripe.
4. **Profile.** Ask only for the fields update_coach_profile takes that are still empty or that the coach wants to change, draft them, and save after approval. Mention that a profile with no bio, specialties or services is left out of search engines, and offer to turn discovery off until it is ready.
5. **Services.** Ask for each service what save_service needs, show it, and save it after approval; on a change, give its serviceId and only what changes. Remove one with delete_service only when the coach asks.
6. **Bookable hours.** Collect the whole week in the coach's local time, show it, and save it with set_weekly_hours after approval; it replaces the stored week. Ask which windows offer each free service. Days off and extra dates go through add_time_off and delete_time_off.
7. Finish by calling get_coach_setup again, saying what is still missing, and giving the links to check the result: [the professional profile](https://liftory.ch/app/settings/trainer-profile), [the bookable hours](https://liftory.ch/app/trainers/schedule) (the eye icon there previews the booking page as clients see it), and the public profile at https://liftory.ch/app/trainers/ followed by the coachId from get_coach_setup, written as a markdown link.

The field meanings are in the tool descriptions; the rules that catch coaches out, which no tool states, are in [references/coach-setup.md](references/coach-setup.md). Check them before showing a service or a week.

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

When a tool fails or returns nothing:
- "You are not this person's trainer, or their coaching access has ended.": stop working on that person and tell the user in plain words. Do not retry with another id or as the user's own data.
- "Your Liftory connection was revoked or has expired.": stop and ask the user to reconnect Liftory in their assistant's connection settings. Do not retry until they have.
- A null or empty result means there is nothing there: say so plainly. Never fill the gap with content of your own.
- Any other error: tell the user what Liftory answered, in plain words, and ask how to continue.

## Output

Short replies, one step at a time: what is done, what this step needs, the draft to approve, and after a save one line confirming it with the link to see it. Prices with their currency, times in the coach's local time.
