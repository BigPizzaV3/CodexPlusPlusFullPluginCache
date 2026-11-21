---
name: cubrik-skill-author
description: Help the user write, improve, import or organise their own cubrik skills — the SKILL.md playbooks cubrik's chat and agents follow. Use when the user says "make a skill for…", "save these rules as a skill", "teach my agents my risk rules", "turn this into a playbook", asks what their skills are, or wants to edit or delete one. Drafts a skill with a precise trigger line and clear instructions, shows it, and saves it with save_skill only when the user agrees.
---

A cubrik skill is a playbook: a name, one line saying what it is for, and instructions. cubrik's
trading chat and agents see each skill's name and line, and open the instructions only when a
request is that kind of work — so **the line decides when the skill is used**, and the instructions
decide what happens then.

## Calls

- `list_skills` — the user's skills, where each is used (the chat, every agent or chosen ones), and
  whether it is on.
- `get_skill` (`name`) — one skill's full instructions.
- `save_skill` — creates the skill, or replaces the one with the same name: `name`, `description`,
  `instructions`, and where it applies (`chat`, `agents`: "all" or a list of agent ids from
  `list_agents`).
- `delete_skill` (`name`).

## Writing a good skill

**Name** — lowercase words with hyphens, e.g. `risk-rules`, `london-breakout`, `hyperliquid-orders`.

**Line (description)** — what it is for AND when to use it, in one or two sentences, up to 1,024
characters. Name the situations and the words a request would use: "My position-sizing and stop
rules. Use before opening any trade, and when the user asks how much to buy or where to put a stop."
A vague line ("trading tips") is never opened.

**Instructions** — written to the AI, as steps it can follow on its own:
1. What to check first (the account, the open positions, the calendar).
2. The rules, exactly, with numbers ("risk at most 1% of the balance per trade; stop at 1.5× ATR(14)
   on the entry timeframe").
3. What to do when a rule is not met (skip, warn, ask).
4. What to report.

Keep it to what is the user's own: cubrik's own rules (confirmations, limits) already apply and a
skill cannot switch them off. Up to 20,000 characters; shorter is better.

## Flow

1. Ask what the skill should achieve and where it should apply (the chat, all agents, some agents).
2. Draft name, line and instructions; show them.
3. Save with `save_skill` only after the user agrees. Saving an existing name replaces that skill —
   say so before overwriting one.
4. Tell the user where to see it: cubrik → Skills, where it can be switched off, exported as a
   `SKILL.md` (which Claude can also load), or edited.

## Rules

- Never put keys, passwords or account numbers in a skill.
- Do not delete or overwrite a skill without the user's explicit yes.
