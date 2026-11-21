# ReMCP review submission — v0.2.170

The official translations are **in `.codex-plugin/plugin.json`** at `extensions.com.openai.publication.translations`; the `locales/` directory is supplementary only.

## Country availability

`publication.countries: []` requests unrestricted country targeting. Final availability still depends on OpenAI regional eligibility and the ReMCP service.

## Locales

English is the default listing language; localized subtitles and descriptions are supplied for ru-RU, uk-UA, pl-PL, de-DE, fr-FR, es-ES, pt-BR, it-IT, nl-NL, tr-TR, ja-JP, ko-KR, zh-CN, hi-IN, ar-SA, id-ID, sv-SE, cs-CZ (18 locales).

## Reviewer credentials (dashboard only)

Provide a dedicated reviewer login, account URL, an authorized paired test computer, and sign-in steps in the secure dashboard Review details. Never package passwords, OAuth secrets or private account information.

## Tests

Five positive and three negative draft test cases are embedded in the manifest. Before submitting, **run each test against the provisioned reviewer account**, including its desktop and browser capabilities; edit mismatches and upload a new ZIP.

## Supporting content

A reviewer-accessible walkthrough recording URL is required in Review details (or `review.demo_recording_url` in the manifest). None is fabricated here.

## Existing MCP preserved

The correct manifest key `mcpServers: "./.mcp.json"` remains unchanged. The MCP endpoint remains `https://remcp.site/mcp` and uses OAuth.
