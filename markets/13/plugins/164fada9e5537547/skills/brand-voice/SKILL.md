---
name: brand-voice
description: Answer a question from the Brand Kit or Knowledge Base, e.g. "/writesonic-agents:brand-voice what does our guide say about tone".
disable-model-invocation: true
---
`whoami` first. Answer "$ARGUMENTS" using `get_brand_kit` for voice/tone/positioning questions, falling back to `search_knowledge` across knowledge sources. Quote the relevant passages and name the source.
