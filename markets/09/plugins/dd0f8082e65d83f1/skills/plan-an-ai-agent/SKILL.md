---
name: plan-an-ai-agent
description: Answer questions about CRM Connector AI Agents before anything is set up. Use it when a person asks whether ChatGPT can work with the customers, deals, invoices or quotes in their own CRM or accounting system, what an AI agent can do in a particular system, which systems have an AI agent, or what the difference between AI Analyst and AI Agent is.
---

# Explore what an AI agent can do

This belongs to part 1 of the plugin, **AI Agents inside one system**. An AI agent works with the records of one of the person's own systems, right here in the chat: it reads their customers, deals, invoices and quotes, and when they allow it, it changes records and keeps automations running in that system. None of these questions needs a CRM Connector account. Answer from the tools, then offer the next step.

## What AI Agents is

- "Can ChatGPT work with my CRM?", "Can you update my deals for me?", "Can you read my invoices?"
- Call `get_ai_agent_options` without a system. It returns the systems that have an AI agent as one plain list.
- Keep it short: say in a sentence what an agent does and give that list. When they want one, ask which system.
- Explain the two packages in plain words:
  - **AI Analyst** reads: it searches and reads records, counts and adds them up, and finds the same customer in the person's other connected systems.
  - **AI Agent** also changes records when the person asks: fields, stages, notes, tasks, activities, line items and links. Every change is shown first and only written after a yes; risky ones the person approves in CRM Connector. It can also keep automations running: fixed rules inside that system, approved once.
- Say what it never does and what waits for the customer: it never deletes a record, it records a payment only where the system allows it and after the customer approves it, and it does not sync between two systems. Syncing between two systems is an integration, part 2 of the plugin.
- Do not call `search_records` or other record tools for this: they work on an agent that is already set up.

## What an agent can do in one system

- "What can an AI agent do in my CRM?", "Can it move deals between stages?", "Can it add tasks?"
- Call `get_ai_agent_options` with the system. It says whether there is an agent there, its record types and its groups of actions. Lead with what it can do instead of reading out a list of what it cannot. When the person asks about something it cannot do, say so plainly and offer to request it with `send_request`.
- Available: plan it right away with `plan_ai_agent`, without asking the person to choose first. Not available: offer to request it with `send_request`, which is free.
- Answer only from that answer, in a few sentences, without reading out every action.

## Several accounts

- One AI agent works in one account of a system: one GoHighLevel sub-account, one HubSpot portal, one QuickBooks Online company. Someone with several accounts, such as an agency with many sub-accounts, sets up one agent per account, each with its own place.
- In the chat they then name the account they mean, and the assistant can answer across accounts one agent at a time.

## Ideas to try

- When the person is unsure what to use it for, give a few examples that fit what the tool returned for their system, such as:
  - "Which deals did not move in the last two weeks?"
  - "Add a follow-up task to every open quote older than a week."
  - "Whenever a deal is won, add a kick-off task due in two days." (an automation, see the `automate-workflows` skill)
- If the tool answer carries automation ideas for that system, pass those on.

## Next step

- **Plan it**: as soon as the person names their system, call `plan_ai_agent` and share the link it returns in the same answer. Pass what they already said it should read, change or do; when they said nothing, call it with the system alone and it plans the defaults every new agent gets: it reads every record type and adds notes and tasks where the system has them. Do not ask them to choose first. In one or two lines, say what the agent will be able to do and that they can narrow or widen it any time, here in the chat with `update_ai_agent` once it is saved or in its settings in CRM Connector. The link opens the setup in CRM Connector filled in, where the person signs in to their system. The plan is saved under AI Agents; nothing works until they finish it. With AI Agent, the plan also names an automation that fits what it may do. A plan never switches on what sends messages, records payments or changes the setup; the person switches that on later in its settings.
- **Back from the setup**: the setup page sends the person back here and asks them to say "done" (or ask them to, once the setup is saved). Then call `get_ai_agent_options` with the system to check that the agent is saved.
- **Test it**: before the agent is switched on, it can be tried here in the chat: it reads up to 100 records of that system with every read tool, filters, counting, reports and lists included, and makes up to 25 changes the person agrees to. Offer a first question that shows its value, such as their open deals by stage or five newest contacts, then a small change. Sending messages, recording payments and voiding wait until it is switched on. Answers say how much of the test is left.
- **A first automation**: offer one of the automations the plan named. `propose_automation` writes it right away, also before the agent is switched on; the person's yes approves it with `set_automation_status`, and it starts the moment the agent is switched on (see the `automate-workflows` skill).
- **Switch it on**: when the person wants the agent to work for real, share the Switch it on link the tool answer gives. One step there switches on every agent that waits.
- **No key or token**: when a tool answer names an app that connects the system without a key or token, offer that way in.
- **Already set up**: when the person has an agent, continue with the `manage-business-records` skill.
- **Another system**: when their system has no AI agent yet, offer `send_request` with kind `ai_access`, the system, `read` or `read_write`, and in the details what the agent should do there. Show what will be sent and send it only after the person confirms.

## Rules

- Only describe what the tools return. Never name a system as having an AI agent unless a tool answer names it.
- Keep AI Agents and integrations apart, and ask which one the person needs when it is not clear.
- Do not discuss prices, fees, plans, trials or discounts.
- Never ask for passwords, API keys or tokens. Systems are connected inside the CRM Connector app, never in the conversation.
