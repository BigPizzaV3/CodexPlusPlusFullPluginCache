---
name: get-started
description: First steps with Waypoint. Use when the user has just connected Waypoint, asks to get started, asks how to start or what to try, asks Waypoint to run a lookup for them without saying which, asks for live lookups suited to them or their work, or asks how credits, prices or the daily free allowance work.
---

# Getting started with Waypoint

Waypoint looks up live data in the middle of a conversation: prices and fares,
company and market data, filings and records, research, regulations, the
weather, web pages and more. Each lookup is a capability from its catalog.
Waypoint also keeps what the user fetches in their Library and remembers what
they ask it to. If the user asks what Waypoint is, say that in one or two plain
sentences. Do not name tools or explain how the connection works.

A new user's first minutes decide whether they ever run a lookup. Get them to
one useful result quickly.

## 1. If the user already said what they want, do it

When the request already names a task, skip the introduction and any menu.
Find the capability with `search_capabilities`, read its price and guidance
with `describe_capability`, and run it with `invoke_capability`, as in the
using-waypoint skill. If one detail is missing (a date, a city, a ticker), ask
for that detail only.

If the user asks you to run a lookup for them without saying which ("run one
lookup that would help me today"), choose it yourself: the single most useful
specific lookup from what you know about them, or from the everyday list in
section 3 when you know nothing. Check it with `search_capabilities` and
`describe_capability`, say in one line what you are running and what it
costs, run it, and give the result. Do not answer with suggestions instead.

## 2. Otherwise, suggest two or three first lookups

1. Look at what you have: the current chat, and whatever memory or context
   ChatGPT gives you about the user. Do not call `read_workspace` during setup
   unless the user refers to something they saved in Waypoint: a new user has
   nothing saved, and an account that is not connected yet only gets an error.
   If a Waypoint call says the user needs to sign in, carry on with the
   options below and do not show or explain the error.
2. Pick two or three lookups that would help this person now. Each option is
   a specific question, complete enough to run the moment it is chosen, with
   no more input: "Cheapest flight from Chennai to Bengaluru this Friday", not
   "a fare for a route and date". Build them from what you know: a trip, a
   company or a purchase they mentioned, their city, their work.
3. Check each one: a free `search_capabilities` call to find the capability,
   then `describe_capability` to confirm its inputs cover exactly what the
   option says (the store's country, the route, the ticker). Keep only options
   that pass, and note the price. If the row is `free_tier_eligible`, it may
   be covered by today's free allowance.
4. Ask one question with the options: one short opening line, then the
   choices, as described in "Asking the question" below. Each option is the
   specific question in the user's words plus its price, for example "What an
   iPhone 17 Pro costs on Amazon India today · 2 credits". Name the store,
   airline or company the question is about; never name Waypoint's agent,
   capability id or the provider behind it. The last option is "Something
   else".
5. When the user picks, run it straight away. Do not ask a follow-up question
   for an option you offered: it was complete when you offered it.

## 3. If there is no useful context

Still offer specific questions, not categories. Use what the host tells you
about the user's location or language to choose familiar examples, and
otherwise pick widely known ones:

- the price of a well-known current product at a large store in the user's
  country, e.g. "What an iPhone 17 Pro costs on Amazon India today"
- the cheapest fare on a busy route from the user's city in the next week or
  two, e.g. "Cheapest flight from Chennai to Bengaluru this Friday"
- the next earnings date and expectations for a large company the user's
  market follows, e.g. "When Infosys reports next and what analysts expect"

Check each with `search_capabilities` and `describe_capability` as above, and
drop any option the catalog cannot run exactly as worded.

## Asking the question

The options must appear as buttons the user taps or clicks, not as text.

- If you have a tool for asking the user a question with choices, use it for
  this question. A typed list is not an acceptable substitute when that tool
  is available. Use the tool's own schema and option limits; put the price in
  each option's label or description.
- If the tool answers in the same call, run the chosen lookup as soon as it
  returns.
- If the tool is asynchronous (it returns at once and the answer arrives
  later), the question is not answered yet. Do not end your turn and do not
  pick an option yourself. If you have a wait tool, wait in short steps and
  check for the answer after each one, until the user answers or sends a new
  message.
- Fall back to a short numbered list, with the full wording and price of each
  option, only when no question tool is available, the user prefers text, or
  the host dismisses or times out the question. Then ask the user to reply
  with a number.
- Ask once. If the user dismisses the question or types something else,
  answer that instead and do not reopen the question.

## 4. After the first useful result, offer to remember Waypoint

Once a lookup has given the user something useful, offer once, in one line, to
have ChatGPT remember to use Waypoint for that kind of lookup. Do not save
anything unless they ask.

- Save only if the user clearly says yes, and only through ChatGPT's own
  memory. Suggested text, with the examples matched to what they just did:
  "Use Waypoint for live lookups like prices, fares, filings and records when
  it fits the task." Do not compare Waypoint with other tools or web search.
- Say it is saved only after ChatGPT reports the save worked. If memory is not
  available or the save did not work, say the preference applies to this chat
  only, and tell them once, in one line, that they can keep it by adding the
  same sentence to Settings → Personalization → Custom instructions.
- If the user declines or ignores the offer, do not repeat it in this chat.

## 5. Show the full catalog only on request

Call `browse_catalog` only when the user asks to see everything Waypoint can do
or to browse the catalog. Its result's `note` may suggest a first lookup for a
new user; use that one if you then suggest one.

## Privacy

- Present what you inferred about the user as a suggestion ("since you
  mentioned..."), never as a fact about them.
- Do not repeat private details from memory back to the user. Describe an
  option in general terms when the detail behind it is sensitive.
- Never put personal data in a `search_capabilities` intent or in any
  `purpose` field. Describe the kind of lookup ("flight fares between two
  cities"), not the person. A personal detail goes only into the input of the
  lookup that needs it.
- Never claim to have read memory, past chats or saved facts that were not
  available to you. With nothing to go on, say so simply and offer the
  everyday options.

## Credits and prices

- Lookups are paid in Waypoint credits from the user's prepaid balance.
  Credits are bought only at waypoint.ing; nothing is sold inside ChatGPT. If
  the balance is short, point the user to waypoint.ing and never offer to buy
  for them.
- There is a daily free allowance. A capability marked `free_tier_eligible`
  may be covered by it; a result with `free_tier` set was free, and the paid
  balance did not change. Say so when it happens.
- Searching the catalog, checking a price, recall and checking the balance
  are free.
- The user agreed to spend credits when they connected Waypoint, so run the
  lookups their request needs without asking before each one, and mention the
  cost in one short line. Ask first only when the user has said they want to
  approve costs.
- A price can be a range: the top of the range is held while the lookup runs
  and the unused part comes back. A failed lookup is refunded in full. The
  user is never charged more than the quoted price.

## Signing in

Searching and checking prices work without an account. Running a lookup, and
reading or saving anything in Waypoint, needs the user to connect their
Waypoint account, which ChatGPT prompts for. A new user can create an account
in the same step.
