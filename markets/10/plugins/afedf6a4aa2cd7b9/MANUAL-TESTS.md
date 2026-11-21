# Ask Shorty — manual tests in ChatGPT

Run these in ChatGPT developer mode before you submit. Check each box and note anything odd.

## Setup

- [ ] **Settings → Security and login → Developer mode** is on.
- [ ] At chatgpt.com/plugins, select **+** and add `https://mcp.askshorty.app/mcp`.
- [ ] The plugin shows 19 tools: `ask`, the 16 calculator tools (`calc_voltage_drop`, `calc_box_fill`, `calc_offset_bend`, and so on), `citations_panel`, and `open_shorty`. ChatGPT may hide `settings_read` and `settings_update` (its settings page calls them) and `exam_questions` and `exam_check` (only the app calls them).
- [ ] If you connected the plugin before, refresh it in the plugin settings so ChatGPT loads the new `answer-v4`, `panel-v4`, `calc-v1`, and `app-v1` widgets.

## Answers (the 5 positive review cases)

Start a new chat for each group so the side panel starts empty.

- [ ] "How far apart do kitchen countertop receptacles need to be?" → the answer card shows a yellow **✓ 210.52(C)(1)** tag right after the sentence it backs.
- [ ] "Do I need GFCI protection for a dwelling unit laundry area receptacle?" → shows a **✓ 210.8(A)** tag.
- [ ] "What size equipment grounding conductor for a 60 A circuit?" → shows a tag for a section in **Article 250** (expect Table 250.122). The card shows only the 60 A row, each value labeled by its column, never the whole table.
- [ ] "Can I put a receptacle face up in a kitchen countertop?" → shows a tag for a section in **Article 406**.
- [ ] Open the **Ask Shorty** tab in the side panel → it lists every section cited in this chat, newest first.

## Calculators

- [ ] "What's the voltage drop on a 12 AWG copper single-phase circuit at 120 V, 16 A, 75 feet one way?" → the calculator card shows the voltage drop in volts and percent, the steps, and an **Informational Note: Voltage Drop** tag.
- [ ] "I need a 6 inch offset with 30 degree bends. Where do I mark?" → the card shows the distance between bends and the shrink, a **Trade math** tag, and "This is trade math, not an NEC rule. Check your bender's marks before you bend."
- [ ] "What size EGC for a 60 amp circuit?" → the card shows only the 60 A row, each value labeled by its column.
- [ ] "Run box fill." → ChatGPT asks you for the missing inputs and doesn't guess.
- [ ] Switch ChatGPT to dark mode → the calculator card is readable.

## Ask Shorty app

- [ ] Open the app from the sidebar entry → it opens full screen with **Calculators** and **Exam prep** tabs.
- [ ] Open the app from the **Ask Shorty** quick action → same result.
- [ ] Fill in and submit each of the 16 calculator forms → each shows a result.
- [ ] The settings line in the app header matches your settings.
- [ ] On the ChatGPT phone app, the app opens and scrolls.

## Exam prep

- [ ] The tab lists all 9 NEC chapters, each with a question count.
- [ ] Answer a practice question and select **Check** → the card shows **Correct** or **Not quite**, the answer, where to look, and why.
- [ ] Start a chapter test → it has 10 questions and ends with your score and the pass mark of 8.
- [ ] Close the app and reopen it on the same device → your progress is still there. This is best effort: progress lives in the browser on that device.

## Settings

- [ ] Open the plugin's settings in ChatGPT. Set occupancy to **Commercial** and units to **Metric**.
- [ ] Reopen the app → the header shows Commercial and Metric.
- [ ] Run a bending calculation → the result shows millimeters first.
- [ ] With units set to **Metric**, open the Ask Shorty app, run a bending calculator, and confirm the result headline shows mm first. This confirms ChatGPT sends the user id on calls the app makes.
- [ ] Ask a question that depends on occupancy → the answer is for commercial occupancies.
- [ ] The code edition shows 2026 and you can't change it.

## No code text

- [ ] Spot-check five exam questions and three calculator cards. None shows quoted code text.

## Refusals (the 3 negative review cases)

- [ ] "Write me a poem about wire." → Shorty says it only answers electrical code questions.
- [ ] "What's the plumbing code for vent stacks?" → same refusal.
- [ ] Paste the over-length question from `TEST-CASES.md` (more than 500 characters) → the tool rejects it and ChatGPT asks you to shorten it.

## Answer card

- [ ] The card shows the Ask Shorty header and the answer, with a section tag after each sentence it backs. Cited sections the answer never placed show as tags below it.
- [ ] The card never shows quoted code text: no quote marks, no quote cards, no section bodies.
- [ ] Verified tags are yellow with a check mark. Any unverified tag is grey and dashed with a warning mark.
- [ ] Select a yellow tag → a box shows the section heading, the sentence it backs, and "Shorty checked this against the 2026 NEC text. Look up {section} in your code book to read it." Select it again → the box closes.
- [ ] Select a grey tag → the box says "Shorty couldn’t match this to the 2026 NEC text. Check {section} in your code book before you rely on it."
- [ ] Switch ChatGPT to dark mode → the card and the panel are readable, including the grey tags.
- [ ] Ask something vague, like "Do I need GFCI here?" → if Shorty needs details, the card shows a details box. Type "Dwelling unit kitchen, 120 V" and select **Get answer** → the button disables while it works, then a new answer appears.
- [ ] ChatGPT's own reply summarizes the card in a sentence or two, names section numbers, doesn't quote code text, and doesn't add uncited code rules.

## Side panel

- [ ] In a brand-new chat, open the Ask Shorty tab before asking anything → it shows "Ask Shorty a code question and every section it cites shows up here."
- [ ] Ask two questions in one chat → the panel lists sections from both, with no duplicates.
- [ ] Each panel item shows the tag, the section heading, the answer sentence it backs, and the look-it-up note. No code text is quoted.
- [ ] Start a second chat → its panel doesn't show the first chat's sections.

## Phone

- [ ] On the ChatGPT iPhone or Android app, ask the kitchen question → the card renders.
- [ ] Open the side panel on the phone → it lists the sections.

## Links and listing

- [ ] askshorty.app, /privacy, /terms, and /support all open.
- [ ] The privacy page names Anthropic Claude and Google Gemini and has the "Ask Shorty in ChatGPT" section.

## Firewall (after you add the rule)

- [ ] ChatGPT still answers normally.
- [ ] From your laptop, this request is blocked (403) or rate-limited (429):
  `curl -s -o /dev/null -w "%{http_code}\n" -X POST https://mcp.askshorty.app/mcp -H 'content-type: application/json' -H 'accept: application/json, text/event-stream' --data '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'`
