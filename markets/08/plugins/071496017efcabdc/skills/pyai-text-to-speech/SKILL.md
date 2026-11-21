---
name: pyai-text-to-speech
description: "Generate natural speech, voiceovers or spoken prompts from text using PyAI Speak text-to-speech (TTS)."
---

# Text To Speech

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `list_voices`, `synthesize_speech`

Use `list_voices` to choose a current voice matching the requested language and delivery. Pass the user's text to `synthesize_speech` using its live schema. Check capability details rather than assuming a stock voice supports a language.

Generation consumes usage; a request for working code alone is not a request to synthesize audio. On the hosted MCP connection, present the returned audio or download link. Do not supply a local `output_path` to the hosted server; file paths are only relevant to local integrations that support them.

Do not automatically repeat synthesis after an uncertain timeout. State what is known about the result and avoid duplicate charges. For speech playback, provide the actual returned media, not a fabricated file or URL.
