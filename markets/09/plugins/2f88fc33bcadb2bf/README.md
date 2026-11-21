# Urantia Papers plugin

Search and read the Urantia Papers, in English and Spanish, with the Bible and 21 other texts, from Claude Code, Cursor, Gemini CLI, ChatGPT, or Codex. The plugin connects the hosted [urantia.dev](https://urantia.dev) MCP server and adds a research skill for well-cited answers. No key, no account, no local process.

## Install

Claude Code, as a plugin (the MCP server and the research skill):

```
/plugin marketplace add urantia-hub/urantia-papers-claude-code-plugin
/plugin install urantia-papers@urantia-papers
```

Claude Code, the MCP server only:

```
claude mcp add --transport http urantia-papers https://api.urantia.dev/mcp
```

Cursor: the repo is also a Cursor plugin (`.cursor-plugin/plugin.json`), listed at [cursor.directory/plugins/urantia-papers](https://cursor.directory/plugins/urantia-papers). Or add the server by hand, in Cursor or any client that reads an `mcpServers` config:

```json
{ "mcpServers": { "urantia-papers": { "type": "http", "url": "https://api.urantia.dev/mcp" } } }
```

Gemini CLI: the repo is also a Gemini CLI extension (`gemini-extension.json`):

```
gemini extensions install https://github.com/urantia-hub/urantia-papers-claude-code-plugin
```

ChatGPT: install the [Urantia Papers plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ac15926d5388191a941565bfaaa2a9a).

The repo root is also a portable plugin package (`plugin.json`, `mcp.json`, `skills/`, `assets/`). Build the ZIP for the OpenAI plugin directory with `scripts/build-openai-zip.sh`.

Setup for other clients: [docs.urantia.dev/mcp-servers](https://docs.urantia.dev/mcp-servers).

## What's included

- **MCP server:** `https://api.urantia.dev/mcp` (Streamable HTTP). 28 read-only tools.
- **Research skill:** `skills/urantia-research`, which tells the model which tool to use and how to cite.

## Tools

| Tool | What it does |
|------|-------------|
| `toc.get` | Table of contents: the Foreword, 4 parts, 197 papers |
| `papers.list` | All 197 papers with metadata |
| `papers.get` | One whole paper, as reference, section, and plain text |
| `papers.sections` | Sections within a paper |
| `paragraphs.get` | A paragraph by reference, for example `2:5.10` |
| `paragraphs.context` | A paragraph with the paragraphs around it |
| `paragraphs.random` | A random paragraph |
| `search.fulltext` | Keyword search (`and`, `or`, `phrase`) |
| `search.semantic` | Search by meaning |
| `entities.list` | Browse more than 4,400 named beings, places, and concepts |
| `entities.get` | One entity's details |
| `entities.paragraphs` | Every paragraph that names an entity |
| `audio.get` | Narration audio links for a paragraph |
| `bible.books`, `bible.book`, `bible.chapter`, `bible.verse` | The World English Bible |
| `bible.search.semantic` | Search the Bible by meaning, with related Urantia paragraphs |
| `bible.verse.urantia_parallels` | The nearest Urantia paragraphs for a Bible verse |
| `works.list` | The Bible and the 21 other texts, with tradition and edition |
| `works.search`, `works.search.semantic` | Search the works by reference, keyword, or meaning |
| `works.read` | A passage, range, or chapter of a work by reference, for example `BG 2.47` |
| `works.urantia_parallels` | The nearest Urantia paragraphs for a passage of a work |
| `quotes.verify` | Check a quotation against the text of the Papers |
| `cite.get` | A citation of a paragraph in APA, MLA, Chicago, or BibTeX |
| `editions.list` | The editions of the text, from the 1955 first printing to the Standard Reference Text of 2024 |
| `editions.variants` | Each change to the text since 1955, by paper, paragraph, edition, or between two editions |

## Example prompts

- "What do the Urantia Papers say about what happens after death? Quote the paragraphs and give the references."
- "Read Paper 1 about the Universal Father."
- "Who is Machiventa Melchizedek?"
- "Show me paragraph 2:5.10 with the paragraphs around it."
- "Which Urantia paragraphs are closest in meaning to Matthew 5:3?"
- "What does the Dhammapada say about anger? Show the nearest Urantia paragraphs."
- "How did paragraph 98:3.8 read in the 1955 first printing, and what changed since?"

## Links

- [urantia.dev](https://urantia.dev)
- [Docs](https://docs.urantia.dev)
- [API reference](https://docs.urantia.dev/api-reference/introduction)

## License

[MIT](./LICENSE).

## Disclaimer

This is an independent community project operated by Adams Technologies LLC. It is not affiliated with, endorsed by, or connected with Urantia Foundation. The original English text of *The Urantia Book* is in the public domain (*Michael Foundation v. Urantia Foundation*, 10th Cir. 2003). All use of "Urantia" is nominative fair use to identify the subject matter.
