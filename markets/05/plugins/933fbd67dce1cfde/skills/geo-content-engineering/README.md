# GEO Content Engineering (Agent Skill)

An open Agent Skill (SKILL.md format) for creating and rebuilding web content so
generative engines (ChatGPT, Gemini, Perplexity, Google AI Overviews) extract,
cite, and mention it. This is the discipline called GEO (Generative Engine
Optimization), also known as AI visibility, LLM SEO, or answer engine
optimization.

## What it does

The skill turns a general agent into a GEO content specialist. It walks the agent
through the retrieval mechanic (chunk, embed, retrieve, ground, cite) and applies
it as a repeatable workflow: gate crawler access, structure text into extractable
blocks, force citations with concrete data, cover query fan-out, keep content
fresh, add verifiable authorship, apply correct semantic markup and JSON-LD, strip
machine-tell language, publish with an input register, and measure Share of
Mentions against a competitor benchmark.

It covers two modes: creating new content, and rebuilding existing pages
(baseline first).

## Structure

```
geo-content-engineering/
├── SKILL.md                  # workflow core + reference map
├── references/               # deep concept files, loaded on demand
├── assets/                   # paste-ready templates and JSON-LD
└── LICENSE.md                # CC BY 4.0
```

## Install

Place the folder in your agent's skills directory (for example
`~/.claude/skills/` for Claude Code, or upload in claude.ai settings). The agent
loads the full instructions only when a task matches the description.

## License

CC BY 4.0. Based on the OKF bundle "LLM-Content-Erstellung" by Eugen Ullrich
(eullrich.com). Attribution required: Eugen Ullrich, eullrich.com.
