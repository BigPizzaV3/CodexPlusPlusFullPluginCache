---
name: use-the-app
description: Tell the user where to find something in the Liftory app and how to use it, with a link that opens that screen. Use when the user asks where to see their plan, menu, log, statistics, body checks, messages, clients or settings, how to do something in the app, or wants a link to open it.
---
# Use the Liftory app

The user's explicit instructions take priority over this skill. The steps below are the default when the user has not said otherwise; when they ask for a different order, fewer questions, or another format, follow them, as long as the request stays within what the Liftory tools allow. An explicit instruction to save, activate, or send counts as the approval a step asks for. Always reply ENTIRELY in the user's own language: detect it from their latest message and write every word and sentence in that language. Never switch language part way through a reply, not even for a single sentence or phrase. Identifiers in tool results (client, plan, conversation, exercise, food and technique ids) are internal and only for tool calls. Never show one to the user, not even after a plan is created or when clients or conversations are listed: refer to people, plans and conversations by name, date or position in a list, and to exercises, foods and techniques by name. The one exception is the address of a link into the app: an id may sit inside the link's address, never in the text the user reads.

Liftory runs on iPhone, iPad, Android and in a browser. On iPhone and iPad five tabs sit along the bottom: Today, Plans, Stats, a fourth tab (Coaching for a coach, Nutrition for a client) and More. On Android and in a browser there are no tabs: the same destinations are in the menu behind the button in the top left, grouped as Workout, Progress, Trainers, Coaching (coaches only), Training content, and Settings at the foot.

Where things are, and the link that opens each one:

| The user wants | Where in the app | Link |
|---|---|---|
| The plan they follow, month by month | Plans tab, or menu then Training Plans | https://liftory.ch/app/training/plan |
| One plan, week by week | Plans, then the plan | https://liftory.ch/app/training/week/PLANID |
| Today's workout | Today tab, or menu then Today's Training | https://liftory.ch/app/training/train |
| Their statistics and exercise history | Stats tab, or menu then Statistics | https://liftory.ch/app/stats |
| Their nutrition day: the menu they follow and what they logged | Nutrition tab (clients), More then Nutrition (coaches), or menu then Nutrition | https://liftory.ch/app/nutrition |
| Their body checks and progress photos | More then Body Tracking, or menu then Body Tracking | https://liftory.ch/app/body |
| Messages and the AI trainer chat | More then Messages, or menu then Messages | https://liftory.ch/app/messages |
| A training plan to edit | Plans, the plan, then Edit; or More then Create Training, or menu then Create Training, then the plan | https://liftory.ch/app/admin/training-editor/edit/PLANID |
| A nutrition plan to edit | More then Write a nutrition plan, or menu then Write a nutrition plan, then the plan | https://liftory.ch/app/admin/nutrition-editor/edit/PLANID |
| Their training plans, to start a new one | More then Create Training, or menu then Create Training: the My Plans tab | https://liftory.ch/app/admin/training-editor |
| Their training templates | Create Training, then the Templates tab | https://liftory.ch/app/admin/training-editor?tab=templates |
| Their nutrition menus, the one they follow first | More then Write a nutrition plan, or menu then Write a nutrition plan: the Menus tab | https://liftory.ch/app/admin/nutrition-editor |
| Their nutrition templates | Write a nutrition plan, then the Templates tab | https://liftory.ch/app/admin/nutrition-editor?tab=templates |
| The meals they keep: their own, Liftory starters, and the meals a coach shared with them (filed under the coach's name) | Write a nutrition plan, then the Meals tab | https://liftory.ch/app/admin/nutrition-editor?tab=meals |
| The exercise library | More then Exercises, or menu then Exercises | https://liftory.ch/app/admin/global-exercises |
| The food library | More then Foods, or menu then Foods | https://liftory.ch/app/admin/foods |
| The technique library | More then Techniques, or menu then Techniques | https://liftory.ch/app/admin/technique-library |
| Finding a coach | More then Find Trainer, or menu then Find Trainer | https://liftory.ch/app/trainers |
| Joining a coach with an invite code | Find Trainer, then the key button in the corner (I have an invite code) | https://liftory.ch/app/trainers |
| Their coach: program, sessions, messages, booking, what the coach can see | Menu then Find Trainer (More then Find Trainer on iPhone): the coach card | https://liftory.ch/app/trainers |
| Booking a session with their coach, and the hours they already hold | The coach card, then Book; or the coach's profile, then See free times | https://liftory.ch/app/trainers/COACHID/book |
| Reviewing their coach | The coach's profile, then Write a review (or the prompt on the coach card) | https://liftory.ch/app/trainers/COACHID/review |
| Their booked sessions (client) | The coach card on the first screen, then See all sessions | https://liftory.ch/app/trainers/my-sessions |
| Coins and Liftory Pro | More then Remove ads at the top, until Pro is active; with Pro, Settings, Purchases, then Buy Pro or Muscle Coins | https://liftory.ch/app/coins |
| What they bought from a coach | The coach card, then Manage payment (a coach paid by card), or Settings then Purchases (shown while Pro is active) | https://liftory.ch/app/purchases |
| Settings and notifications | More then Settings, or menu then Settings | https://liftory.ch/app/settings |
| Connected assistants, to disconnect one | Settings, then Connected assistants in the Account list | https://liftory.ch/app/settings/connected-assistants |

For a coach, about one of their clients (CLIENTID is that client's id):

| The coach wants | Where in the app | Link |
|---|---|---|
| Their client list, and the Business tab | Coaching tab, or menu then My dashboard | https://liftory.ch/app/trainers/dashboard |
| One client | The dashboard, then the client | https://liftory.ch/app/trainers/dashboard/subscriber/CLIENTID |
| A client's training plan, to edit | The client, then Training (it jumps to the Training plan section), then Training plan on the plan's card; Create when they have none | https://liftory.ch/app/admin/training-editor/edit/PLANID?subscriberId=CLIENTID |
| A client's nutrition plan, to edit | The client, then Edit plan in the Nutrition section (Write a plan when they have none), then the menu | https://liftory.ch/app/admin/nutrition-editor/edit/PLANID?subscriberId=CLIENTID |
| A client's nutrition day and log | The client, then the Nutrition tile | https://liftory.ch/app/nutrition?subscriberId=CLIENTID |
| A client's statistics | The client, then Stats | https://liftory.ch/app/stats?subscriberId=CLIENTID |
| A client's body checks | The client, then Body | https://liftory.ch/app/body?subscriberId=CLIENTID |
| A client's sessions, and booking them one | The client, then Sessions: the Schedule with their name above it | https://liftory.ch/app/trainers/dashboard/subscriber/CLIENTID |
| Their calendar | More then Schedule (iPhone and iPad), or the calendar icon on the dashboard | https://liftory.ch/app/trainers/schedule |
| Booking a session for a client | Schedule, then the plus (New appointment), or drag across the hours on the calendar | https://liftory.ch/app/trainers/schedule |
| Their payments and the Coach Agreement: card payments through Stripe (Finish setup) and the agreement to accept | The dashboard, then the Business tab | https://liftory.ch/app/trainers/dashboard |
| This month's income, the payments ledger, invite codes, and their profile link with its QR code | The dashboard, then the Business tab: This month, the All, In Liftory and Outside filters, How you get paid, Invite codes, Get discovered | https://liftory.ch/app/trainers/dashboard |
| Coaching settings: What you coach, and when Meals slipping flags a client | Settings, under What you coach | https://liftory.ch/app/settings |
| Their professional profile | Settings, their name at the top (Edit profile), then Professional profile; the bio is on Edit profile itself | https://liftory.ch/app/settings/trainer-profile |
| The services they sell, and their prices | Professional profile, then Services and programs | https://liftory.ch/app/settings/trainer-profile?section=services |
| Their bookable hours and time off | Schedule, then the clock icon (Bookable hours); time off is Block a date in the same editor; the eye icon next to it (Preview as client) shows the booking page as clients see it | https://liftory.ch/app/trainers/schedule |
| Their public profile, as clients see it | Professional profile, then Preview your public profile at its foot | https://liftory.ch/app/trainers/COACHID |

How to give a link:
- Replace PLANID, CLIENTID and COACHID (a coach's id: the coach's own, or a client's coach) only with ids a tool returned in this conversation. When the id is not known, give the link without an id from the first table (the plan list, the dashboard) and say which entry to open.
- Write it as a markdown link whose visible text names the place (your plan, your nutrition day) and whose address is the link from the table. The id may appear inside the address, never in the visible text.
- Give the one link that answers the question, next to the path through the tabs or the menu, so the user can also find it by hand.
- On a phone with the app installed, the link opens the app on that screen; elsewhere it opens Liftory in the browser, which asks for sign in first and then continues to the same screen.
- Something just saved reaches the app when it syncs; if it is not there yet, wait a moment and open the link again.

Answering how to use the app: explain the steps with the names the app shows (the tab, the menu entry, the button), shortly, then give the link to the screen. Describe only what this guide and the user's own words support; when you do not know how something works, say so and give the link to the screen where it is done instead of guessing the steps. Body checks are the user's own log, which they choose to keep; never ask for one or for what it contains.

## Steps
1. Work out which screen answers the question, and whether it is about the user or about a client they coach.
2. When the link needs an id the conversation does not have yet (a plan, or a client), read it with the Liftory tools first: the plan from get_last_plan, get_plan or get_last_nutrition_plan, the client from list_clients. Otherwise give the link without an id from the first table.
3. For how to do something on a screen, or what a button or an option does, read [references/how-the-screens-work.md](references/how-the-screens-work.md) and give only the steps it supports.
4. Answer with the path through the tabs or the menu, then the link.

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
One or two short sentences naming where it is, then one markdown link. For a how-to, a short numbered list of the steps, then the link.
