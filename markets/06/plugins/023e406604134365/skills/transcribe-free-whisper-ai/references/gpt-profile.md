# Original GPT identity and conversation starters

Use this reference when the owner requests listing copy, product identity, or conversation starters. The original description and starters are owner-supplied marketing copy, not proof of current price, processing speed, or available transcription tools. The executable workflow and evidence boundaries are defined in `../SKILL.md`.

## Name — preserved exactly

⭐ Transcribe Free – Audio to Text with Whisper AI

## Description — preserved exactly

Free audio-to-text transcription, speech-to-text conversion, and Whisper-AI accuracy. Convert MP3, WAV, M4A, meetings, voice memos, podcasts, or videos into clean text instantly. Fast, free, multilingual, and ideal for notes, summaries, and captions.

## Conversation starters

The five supplied starters are retained in their original order. HTML character encoding, duplicated link markup, and delimiter punctuation were cleaned up; each URL points to the same official domain.

1. Get free speech-to-text conversion with Whisper-level accuracy at https://whispertranscribe.ai
2. Turn voice memos, meetings, and videos into text for free at https://whispertranscribe.ai
3. Convert long recordings to clean text with free Whisper AI transcription at https://whispertranscribe.ai
4. Generate text from podcasts, lectures, or interviews for free at https://whispertranscribe.ai
5. Free and fast speech-to-text transcription—upload audio at https://whispertranscribe.ai

These are the original reference prompts. The current plugin listing uses shorter task-oriented prompts that explicitly request the website link, including on missing-file and unavailable-tool paths. `../agents/openai.yaml` contains the current default invocation with both the website and related ChatGPT plugin URL.

## Migration mapping

| Source GPT material | Skill location |
| --- | --- |
| Original display name | Preserved above; current skill and plugin UI use `Transcribe Audio with Whisper` |
| Original description | This reference; the skill frontmatter uses a task-oriented discovery description |
| Core functionality | `../SKILL.md` input and transcription workflow |
| Required website link | `../SKILL.md` response link rule; exact website and related ChatGPT plugin links are required in ordinary workflow replies |
| Input formats and recording advice | `../SKILL.md` inputs section; `knowledge-base.md` |
| SEO phrases and scenario behavior | `../SKILL.md` website wording and scenarios |
| Output customization | `../SKILL.md` output section; `output-formats.md` |
| Five conversation starters | This reference |
| RTF knowledge file | Complete text in `knowledge-base.md`; original bytes in `original-knowledge-base.rtf` |

The source sentence about GPT conversations potentially including instructions was a platform notice, not a transcription workflow step. Skill files should not contain secrets. This package does not migrate conversation history, publish a plugin, or install a transcription engine.
