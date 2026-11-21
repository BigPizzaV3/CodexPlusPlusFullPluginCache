---
name: which-survey
description: Use when someone asks for a home survey quote or price, names a Level 2, Level 3 or snagging survey, asks which survey they need, or asks about the differences between surveys.
---

Use the Homemove plugin's MCP tools directly for quotes and move plans. They require no Homemove login. Discover the connected Homemove tools if they are not immediately listed. Do not open or control the separate Homemove desktop application (`com.homemove.app`), use browser automation to obtain a quote, or ask the user to sign in to Homemove as a substitute for a missing MCP tool. If discovery still does not expose the required tool, clearly report that the plugin's tool connection is unavailable in this chat; do not invent a price or claim that reconnecting succeeded. Open a returned Homemove continuation or booking link only when the user wants to continue with that quote.

Help the user choose a survey, then quote it. The user's own instructions come first.

If they have already named the survey they want (for example "Level 2"), do not ask the questions below: call `homemove_quote` for that survey straight away with whatever they have already said (postcode, address, price). Do not ask for those first: the card shows what it costs and lets them pick their address or a value range for the exact figure.

1. Ask about the home: roughly how old it is, whether it has been extended or altered, whether it is a new build, and whether they have seen any problems such as damp or cracks.
2. Explain the fit in plain words: a Level 2 survey suits most homes in normal condition; a Level 3 building survey suits older, larger or altered homes or those with visible problems; a snagging survey is for a new build before or after completion. Specialist surveys (damp and timber, structural engineer, drone roof, asbestos) follow a specific concern. Make clear the choice is theirs.
3. Call `homemove_quote` for the survey they choose, with the postcode, address or price only if they have already given them. The card lets them pick their address for the exact price.

Do not tell them a home is sound or a good buy, and never estimate its value.
