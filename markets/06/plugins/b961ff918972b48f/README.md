# SRT Subtitle Translator – Arabic & English

Version 1.1.0. A ChatGPT plugin for Arabic, English, and other subtitle translation workflows.

Select the plugin in ChatGPT, attach an SRT file or paste its contents, and specify the target language. Example: **ترجم هذا الملف إلى العربية مع الحفاظ على التوقيت وأعطني ملف SRT للتنزيل.**

The model translates dialogue. The bundled standard-library Python helper preserves numbering and timestamps, verifies completeness and formatting, and exports UTF-8 SRT. Bilingual output is optional.

Included: `skills/translate-srt/SKILL.md`, `scripts/srt_tool.py`, and `references/usage.md` (scripts and references are inside that skill).

Requires a session that can read files and run Python. No API keys, external translation services, network calls, or connected accounts are required. Structural validation does not guarantee linguistic accuracy. Incomplete translations and malformed source files are rejected. Cue separators are normalized. The plugin does not extract audio/video, synchronize timing, or parse VTT/ASS as SRT.

Creating the plugin in an account does not publish it publicly or establish search-engine indexing.


Version 1.1.0 adds a subtitle translation icon and clearer English/Arabic listing copy. Translation and validation behavior is unchanged. Public distribution requires submission and approval through the OpenAI plugin portal.
