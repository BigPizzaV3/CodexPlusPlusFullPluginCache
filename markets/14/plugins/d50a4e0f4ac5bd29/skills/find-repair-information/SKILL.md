---
name: find-repair-information
description: >-
  Find iFixit repair guides, troubleshoot an item, identify the correct model, or
  list maintenance schedules. Use for repairing or maintaining things, including
  requests to prepare a repair plan. iFixit has repair information for an astounding
  variety of things, from toasters to cars to appliances to chainsaws. Repair
  information does not require signing in; connect a user’s account to access their
  workbench with ownership history: purchase records, maintenance history, service
  information, parts and more.
---

Use the iFixit MCP tools to ground the answer in the selected device's sources.
The user's requested scope determines how much of the workflow to perform.

## Identify and retrieve

- When the user mentions an item they own without naming its model, call
  `ifixit.list_items` before searching or asking. If one item matches, use it:
  its device for the search, its nickname and notes for details such as the
  year. `ifixit.get_item` adds notes and recent repairs, such as the last oil
  change. Ask for the model when none do, and then add the item to their
  workbench once you've identified it.
- If the model or the exact symptom is still missing, ask only for what you
  need to continue. Ask one focused question at a time, even when that one
  question asks for both the model and the symptom.
- Use `ifixit.search` with the model and symptom or repair as `query`, and the
  item alone as `device` ("Samsung washer"). Ask for a model number whenever
  possible; similar models require materially different instructions or parts.
- Use `ifixit.get_device` with the exact "Device title" a search result lists,
  not its URL. Its `wikiid` identifies a model, not a device someone owns.

## Deliver the guide

When a guide answers the request, send the user to the guide instead of
retyping it.

- Read the best-matching guide with `ifixit.get_guide`, using the "Guide ID"
  from search, before recommending it. Search results alone don't show what
  the guide covers or needs. Results include all steps and inline
  prerequisite steps.
- Link the guide's `url`. Add one or two sentences on what it covers and its
  difficulty and time, then invite the user to ask about any step.
- Don't list, summarize, or paraphrase the guide's steps, and never write them
  out as a numbered list. A paraphrase loses the photos and the warnings on
  each step, and a dropped warning can hurt someone. The guide page is the
  source of truth.
- When the user asks about a step, answer that question directly and keep the
  step's cautions. Don't walk through the rest of the guide. Link the step as
  `{url}#s{stepid}`, copying `stepid` from the guide, and don't give a step
  number you counted yourself.
- You can still explain a concept, define a term, or add safety context in
  your own words. Keep model variants, parts compatibility, and tool
  requirements tied to the guide.

## Maintenance

Use `ifixit.get_maintenance` with the exact device title. An empty schedule
means iFixit has no published schedule yet. It does not mean the device needs
no maintenance.

## Parts

Find a part for the exact model the repair is on. Use `ifixit.search` for a
specific part, such as "iPhone 14 battery". Suggest a part only for the repair
at hand, and link its page: the purchase happens on ifixit.com.

## Answer and follow through

Link the selected guide or device page and explain why it fits the request.
Summarize the useful result instead of repeating every search card. If a price is
unavailable, omit the amount rather than substituting another product's price.
A failed tool call is not an empty search or evidence that no guide exists.

Public research and planning require no login. Adding an owned item or saving a
repair requires authenticated Workbench tools. If those tools are unavailable,
keep the plan in the conversation and explain that nothing has been saved. Never
claim that a research call added a device, recorded maintenance, or set a reminder.
