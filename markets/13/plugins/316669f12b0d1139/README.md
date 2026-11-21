# Taption plugin

Version: **1.1.0**  
Display name: **Taption**  
Subtitle: **AI Transcription & Subtitles**  
Category: **Productivity**

## Description

Taption uses AI to quickly turn recordings and videos into accurate, editable transcripts, subtitles and translations in 50+ languages, with optimized handling for Chinese, Japanese and Korean.

In ChatGPT, Taption can transcribe a file uploaded in the chat, or a pasted link; produce a plain transcript, a speaker-labeled transcript or captions/subtitles; translate a recording into up to five languages as part of its transcription, or translate an existing transcript; report progress and return the finished transcript or a translation as text, SRT or VTT; and find transcripts by name or list the user's recent transcripts. The full listing copy, including limitations, is `longDescription` in `plugin.json`.

## What's new in 1.1.0

Translation: `translate_to` on `transcribe` and the new `translate_transcript` tool; translations listed and readable through `get_transcript` and `list_transcripts`; name search (`query`) on `list_transcripts`; short recordings can finish within one `get_transcript` reply; completion emails follow the user's Taption email setting. The MCP server reports version 1.1.0.

## Listing links

| Link | URL |
| --- | --- |
| Website | https://www.taption.com/ |
| Support | https://www.taption.com/faq (contact: help@taption.com) |
| Privacy policy | https://www.taption.com/privacy |
| Terms of service | https://www.taption.com/terms |

## Connection

| Setting | Value |
| --- | --- |
| MCP endpoint | `https://api.taption.com/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth 2.1 with PKCE (S256), dynamic client registration |
| Scopes | `transcripts:read`, `transcripts:write` |

The package contains no credentials or OAuth client secrets. Users sign in with their Taption account on Taption's consent page and can disconnect at any time in Taption under Account > Connected apps.

## Tools

| Tool | Scope | What it does |
| --- | --- | --- |
| `transcribe` | `transcripts:write` | Starts a transcription from an uploaded file or a link. Requires the spoken language and the output type (plain transcript, speaker labels or captions). Optional `translate_to` (up to 5 languages) translates the transcript automatically once it is done. Uses minutes from the user's Taption account, and each translation uses minutes too. |
| `translate_transcript` | `transcripts:write` | Translates an existing, complete transcript into up to 5 languages. Never replaces a translation that already exists, since it may contain the user's edits; those can be translated again in the Taption editor. Uses minutes per language. |
| `get_transcript` | `transcripts:read` | Returns a transcript's status and its translations, or the transcript (or, with `language`, a translation) as text, SRT or VTT in pages, with download and edit links. Read-only. |
| `list_transcripts` | `transcripts:read` | Lists the user's most recent transcripts with their translations; `query` finds transcripts by name. Read-only. |

## Package contents

| File | Purpose |
| --- | --- |
| `plugin.json` | Agent Plugins 1.0 manifest: listing metadata, review test cases and release notes |
| `mcp.json` | Remote MCP connection and OAuth configuration |
| `assets/taption-icon.svg` | Square icon containing the official Taption logo |
| `README.md` | This file |

## Sources and branding

- [Taption website](https://www.taption.com/)
- [MCP protected-resource metadata](https://api.taption.com/.well-known/oauth-protected-resource/mcp)
- [OAuth authorization-server metadata](https://api.taption.com/.well-known/oauth-authorization-server)
- [Official Taption logo](https://www.taption.com/img/logo.4621b7ea.png)

The icon embeds the original 188 × 174 PNG logo centered in a transparent 256 × 256 SVG viewport, with no external asset requests.
