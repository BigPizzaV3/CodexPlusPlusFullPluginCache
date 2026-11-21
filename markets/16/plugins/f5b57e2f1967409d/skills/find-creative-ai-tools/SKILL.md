---
name: find-creative-ai-tools
description: Help someone pick a creative AI tool (pictures, video, voice, music, talking presenters, 3D) using Plainly Guide's sourced catalogue, in plain English.
---
When someone wants to make something with AI (an image, a video, a voiceover, a song, a talking presenter or a 3D model), or asks which tool to use, what a tool costs, whether it is open source, or whether they can sell what they make:

1. Ask at most one short question if the task, budget or need for commercial use is unclear. Otherwise go straight to step 2.
2. Call find_tool with the task in plain words. Add budget (US dollars per month, 0 for free only), open_source or commercial_use only when the person said so.
3. Offer 3 to 5 options in plain English: what each is good for, free option, cheapest paid plan, open or closed. Use get_entry for one tool's full detail, and compare_tools when the person is choosing between 2 to 5.
4. Prices and terms change. Say when facts were last checked (last_checked) and link the Plainly page (page) for each tool you mention.
5. Plainly does not rank by payment and does not benchmark quality. Do not invent prices, licences or features that are not in the results.
