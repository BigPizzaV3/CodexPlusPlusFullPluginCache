---
name: mybeatz-get-started
description: Help a user get started with MyBeatz or choose from its available instrumental beat styles and BPM options, without starting a generation.
---

# Get started with MyBeatz

Use the bundled `mybeatz` MCP server. Respect the user's requested language and goal. MyBeatz primarily creates original instrumental beats and type beats; its music catalogue is an optional information feature, not a prerequisite for creation.

- For onboarding or style discovery, call `list_beat_styles` with `{}`. Show a useful selection of the returned styles, or the whole list if requested. Use only returned BPM options and current costs, not a hard-coded catalogue or price.
- If the user has no direction, ask which available style they want. A request such as “un type beat Jul à 130 BPM” selects an existing instrumental style, not a voice or an existing song.
- Explain that private account access and creation need the normal MyBeatz OAuth connection. Do not ask for a password or token in chat, claim the account is linked before success, or switch accounts without authorization. For a requested balance check, use `get_my_account`; do not infer a balance from a subscription label.
- For an actual creation request, follow [the creation workflow](../mybeatz-create-beat/SKILL.md). For a library or existing-generation request, follow [the library workflow](../mybeatz-my-beats/SKILL.md).

Onboarding and installation do not authorize preparation, generation, credit use, purchases or plan changes. If OAuth fails, report the blocker once and stop repeated linking attempts until there is a relevant change. A permissions grant is not confirmation to create a beat.

Keep the answer practical: the available choices, any account requirement, and one clear next question. Do not promise unsupported styles, copied recordings, voice cloning, artist endorsement or a guaranteed measured output BPM.
