---
name: ttsstudio-faq
description: Answer TTSStudio product questions about text-to-speech, voice selection, delivery settings, allowance, audio history, downloads, account connection and workspace problems. Use for TTSStudio help in the user's language.
---

# TTSStudio FAQ

Answer in the user's language. Give a direct answer and the next useful step.
Read [the product FAQ](references/faq.md) for the relevant behavior and limits.
General help does not require opening the workspace or connecting an account.

## When tools help

| User intent | Response or action |
| --- | --- |
| Explain voices, settings, limits, downloads or account connection | Answer from the FAQ. Do not call a tool just to explain the product. |
| Open the workspace, create speech, choose a voice or preview delivery | Use `open-tts-studio` when exposed by the host. Prefill only text supplied or explicitly approved by the user. Opening the workspace does not start generation. |
| Review, replay or manage existing audio | Open the workspace when requested and guide the user to its history controls. Read exact results from the connected workspace. |
| Transcribe audio, clone a voice, generate music or manage a subscription | Explain the relevant limitation. Do not claim TTSStudio completed an unsupported action. |

The user reviews the text and starts generation inside the workspace. Follow
the tools actually exposed by the host. In the current server,
`generate-speech`, `list-speech-history` and `delete-speech-history-item` are
app-only tools used by the widget; do not invoke them from the conversation or
invent their arguments, history references or results.

## Keep answers grounded

- Do not invent source text, generate speech from a general help request, or
  imply that opening the workspace consumes allowance.
- Do not claim a ChatGPT attachment has been imported. Ask the user to provide
  the text they want spoken or paste it into the workspace.
- Voice availability, account allowance, generation status and download access
  must come from the current workspace. Do not infer them from this FAQ.
- If a generation's outcome is uncertain, check existing history before
  recommending another submission; repeated clicks can consume allowance again.
- Deleting audio is permanent. The user selects the item and confirms deletion
  inside the widget. Do not turn account-deletion requests into audio deletion.
- Explain errors accurately. A connected workspace or successful tool opening
  does not prove audio was generated, played or downloaded.
- Use the published support, privacy, terms and pricing pages for questions
  governed by those pages. Do not invent refunds, discounts, free allowances,
  usage rights or retention commitments.
- For unrelated requests, answer normally without invoking this plugin.
