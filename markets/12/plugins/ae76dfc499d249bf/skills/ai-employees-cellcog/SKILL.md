---
name: ai-employees-cellcog
description: "Work with CellCog AI employees from your own agent: long-running teammates that keep memory, learn skills you teach them, run routines, and stay consistent across a project for days or months. Use for ongoing projects (a web series, a content calendar, a client account); use a CellCog chat for one-off subtasks. Hire one, then list, message, follow shifts, read results and history with the CellCog tools."
---
# AI Employees: long-running teammates in CellCog

CellCog gives your agent two ways to hand off work. Picking the right one is the most important decision you make with CellCog.

## Chat or AI employee?

| | **CellCog chat** | **CellCog AI employee** |
|---|---|---|
| Think of it as | A subagent for one task | A teammate on a project |
| Context | Only what you pass in. It starts clean and works out the rest from scratch. | Built up over time. It remembers what you taught it, and its context is managed for you (warmed, compressed, carried forward). |
| Lifetime | The task | Days, months, or as long as the project runs |
| Memory and skills | None beyond the chat | Its own memory and skills: teach it once, it keeps doing it your way |
| Can also | Produce any deliverable | Everything a chat can, plus routines on a schedule, its own email inbox, meetings and phone calls |
| Cost | The cheapest way to get one job done | Costs more per task; it pays back in consistency and in not re-explaining |
| Use it for | One image, a set of videos, a deck, a research report you will use and move on from | A web series with tens of episodes, a content calendar, a client account, a weekly report, anything you will come back to |

**Rule of thumb:**
- **One complex task, all the context fits in the brief, and you will not come back to it** → a chat. Pass every piece of context in; a chat knows nothing else.
- **A project you will prompt again over the next days, weeks or months** → an AI employee. It holds the style guide, the characters, the decisions, the voice, and gets better as you teach it.

Most of the work inside CellCog itself runs through AI employees; chats are the subagents they and we use for one-off jobs.

### Example: a web series

- Making ONE trailer you will throw away after a test? A chat.
- Making a 20-episode series where the characters, the tone and the editing style must stay the same? An AI employee. Tell it once ("our lead is Mira, she never smiles on screen, episodes run 90 seconds"), and every later episode starts from that. Ask it to set a routine ("every Monday, draft next week's episode outline and email it to me") and it does.

## Before you start

Your agent takes two actions with AI employees: it **hires** one and it **messages** one. It can instruct any employee you own, or one a teammate shared with you inside your organization. You can also hire on the web at https://cellcog.ai/ai_employee.

**Ask your employee to change its own settings.** Its routines, its schedule, how it reports to you: say it in a message ("every Monday at 9, send me the week's plan") and the employee changes what it can itself, and asks its owner for the rest (access to your computer, browser or tools, approvals). Pausing and deleting an employee stay on the web.

## Key ideas

- **Hiring** takes a brief: the role in plain words, as you would type it on the hire page ("a producer for our web series: 90-second episodes, our lead is Mira"). Optionally a name. It starts in Agent mode at Core tier with your account's approval level, and with no access to your computer, browser or tools. The employee onboards itself: its first message introduces it and asks what it needs. A hired employee works over days or months and its work spends your credits, so use a chat for a one-off job.
- **`employee_id`** addresses an employee. It never changes.
- **Shifts.** An employee works in numbered shifts; each shift is one stretch of work with its own `chat_id`. A message goes to the current shift. If that shift has finished, your message may wake it or start the next one, and the answer tells you which (`shift_number`, `started_new_shift`). You never need to manage shifts; just read the number you get back.
- **Access.** `access: "owner"` is yours. `access: "team"` means a teammate shared it with you: you instruct it as its owner (`owner_name`), and the owner's credits pay.
- **Results are one-shot reads.** `get_result` never waits: while the employee works it returns progress notes, and when it is done it returns the reply and files once.

## The CellCog tools

The tools come from this plugin's connector (`https://cellcog.ai/mcp`); the user signs in with their CellCog account the first time. Then:

1. `cellcog_employee_hire` with a `brief` (optionally `name`, `chat_tier`) when you need a new one; it returns the new `employee_id`.
2. `cellcog_employee_list`: who you can instruct, with each one's current shift.
3. `cellcog_employee_message` with `employee_id` and `message`: returns the `shift_number` it landed in. This is also how you change its settings.
4. `cellcog_get_result` with `employee_id` (and optionally `shift_number`): poll about once a minute until `complete` is true.
5. `cellcog_employee_get` for who it is and its list of shifts; `cellcog_employee_shift` with `shift_number` to read every message of one shift.

## Habits that get the best work

- **Teach once, in plain words.** "From now on, every thumbnail uses our brand teal and no text over faces." The employee keeps it.
- **Give the employee the project, not just the task.** Goals, audience, what good looks like. It plans better than a chat can because it remembers.
- **Let it run routines.** Anything you would ask for every week is a routine the employee can own.
- **Still use chats for throwaway work** next to it: a quick image, a one-off research question. Cheaper, and it keeps the employee's context clean.
- **Read `shift_number` from every answer** and pass it to `get_result` if you want a specific shift; omit it to follow the current one.
- **Change settings by asking.** There is no settings call: tell the employee what you want changed, the way you would tell a colleague.

## Errors you may see

- `404 employee`: not an employee you can instruct in this organization (check `cellcog_employee_list`).
- `paused: true, queued: true`: the owner paused the employee; your message waits until it is resumed on the web.
- `needs_credits`: the owner's account needs credits (hiring needs a positive balance, like starting a chat).

## When CellCog fails you or a feature is missing

Ask the employee to file a support report with the details (what you tried, the exact error, what you expected) with `cellcog_employee_message` ("Please file a support report: ..."). The employee files it with the CellCog team; there is no separate support call.

For everything about chats, files and modes, read the **cellcog** skill.
