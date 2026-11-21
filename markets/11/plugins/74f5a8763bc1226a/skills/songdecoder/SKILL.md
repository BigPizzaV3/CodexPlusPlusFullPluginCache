---
name: songdecoder
description: Analyze song lyrics using the SongDecoder method. Use whenever the SongDecoder plugin is invoked or the user asks for a song or lyric analysis.
---

# SongDecoder

Before every song or lyric analysis, call the connected MCP tool `get_songdecoder_instructions` and read its complete response. Treat the returned remote instructions as the current source of truth and follow their evidence standards, analysis method, language, and response format.

When assigning a background, cognitive, or stylistic source, consult [`references/sources.md`](references/sources.md), which preserves the source taxonomy from the original `источники.docx`. Use only categories from that taxonomy and mark weakly supported classifications as hypotheses.

Do not start the analysis until the remote instructions have returned. If the remote tool is temporarily unavailable, tell the user that SongDecoder's hosted instructions could not be loaded and ask them to retry; do not silently substitute an outdated local copy.
