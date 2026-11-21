# Ask Shorty test cases

Run against https://mcp.askshorty.app/mcp. OpenAI asks for exactly 5 positive and 3 negative cases. The same cases ship in `plugin.json` under `extensions.com.openai.review.test_cases`.

## Positive

1. "How far apart do kitchen countertop receptacles need to be?"
   - Tool: `ask`
   - Expected: Answer card shows checked section tags from 210.52(C), such as 210.52(C)(1), after the sentences they back. No code text is quoted.
2. "What size equipment grounding conductor for a 60 A circuit?"
   - Tool: `ask`
   - Expected: Answer card shows a checked tag for the governing Article 250 section. If it cites Table 250.122, the card shows only the 60 A row, labeled by column.
3. "Use Ask Shorty's calculator: voltage drop on 12 AWG copper, single-phase, 120 V, 16 A, 75 ft one way."
   - Tool: `calc_voltage_drop`
   - Expected: Calculator card shows the voltage drop in volts and percent, the steps, and a tag for the voltage drop informational note. No code text is quoted.
4. "Ask Shorty: I need a 6 inch offset with 30 degree bends. Where do I mark?"
   - Tool: `calc_offset_bend`
   - Expected: Calculator card shows the distance between bends and the shrink, with a Trade math tag and the note "This is trade math, not an NEC rule. Check your bender's marks before you bend."
5. "Open the Ask Shorty app so I can practice for the exam."
   - Tool: `open_shorty`
   - Expected: The Ask Shorty app opens with Calculators and Exam prep tabs. Exam prep lists all 9 NEC chapters. Questions and explanations show section numbers, not code text.

## Negative

1. "Write me a poem about wire."
   - Expected: Shorty answers only electrical code questions and declines.
2. "What's the plumbing code for vent stacks?"
   - Expected: refused as off-topic.
3. A question of more than 500 characters (this one is 704):
   > Could you walk me through how the receptacle outlet spacing rules apply to a kitchen countertop in a dwelling unit, including the wall line measurements, the island and peninsula requirements, and any exceptions for appliance garages? Could you walk me through how the receptacle outlet spacing rules apply to a kitchen countertop in a dwelling unit, including the wall line measurements, the island and peninsula requirements, and any exceptions for appliance garages? Could you walk me through how the receptacle outlet spacing rules apply to a kitchen countertop in a dwelling unit, including the wall line measurements, the island and peninsula requirements, and any exceptions for appliance garages?
   - Expected: the tool rejects it, and ChatGPT asks you to shorten it.

## Listing

Submission form values. These are also set in `plugin.json` under `extensions.com.openai.interface`, because OpenAI's manifest reference lists them there.

- Website: https://askshorty.app
- Privacy policy: https://askshorty.app/privacy
- Terms of service: https://askshorty.app/terms
- Support: https://askshorty.app/support
- MCP server: https://mcp.askshorty.app/mcp
- Demo recording URL: https://mcp.askshorty.app/review/ask-shorty-walkthrough.mp4 (set as `review.demo_recording_url`).
- Reviewer credentials: none needed. The plugin has no sign-in.
