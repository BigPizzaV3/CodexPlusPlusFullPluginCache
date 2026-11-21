# uListen plugin package

Great ideas stay with you.

Public display name: **uListen AI**. The stable package identifier remains
`ulisten`. **uListen Activation Fixture** is a deliberately separate synthetic-test
label, never the public name. The brand tagline above is unchanged.

Publisher metadata uses **uListen, Inc.**, the operator the website's privacy and terms
pages name, because OpenAI requires the listing's links to identify the same publisher.

The listing copy uses the uListen Claude connector's directory listing wording, with
ChatGPT as the host. Change both together.

Version `1.0.3` is the candidate for the first public directory listing. Each upload
takes a new version: `1.0.0` to `1.0.2` went up as OpenAI drafts on 2026-10-22. A
passing check doesn't make it ready: the steps under "Required before release" still
apply, and upload and publication each need their own approval.

This portable package contains one remote MCP connection, the existing uListen
icon and one skill. The connection declares no authentication. It uses uListen's
public, read-only catalog tools, the same four that the uListen Claude connector
offers: `search_podcasts`, `list_channels`, `get_episode_analysis` and
`get_transcript_excerpt`. They read uListen's curated catalog and change nothing.
No hooks, local marketplace registration, developer-connection mapping, fixture,
credentials or user data are included.

The skill covers content questions about supplied YouTube links without requiring
a uListen mention. Selection is host- and model-controlled, not a guaranteed URL
hook. Recognizing a link does not establish that uListen has the episode. Supplied
links use the read-only `video_url` argument without rewriting the URL; the server
validates the ID and time without fetching it. Invalid or ambiguous links must not
be retried as salvaged IDs.

## Local validation and archive

From the repository root, using Node 24 and the system zip/unzip tools:

```sh
node scripts/package-chatgpt-plugin.mjs --check
node --test scripts/tests/test-chatgpt-plugin-package.mjs
node scripts/package-chatgpt-plugin.mjs --zip
```

The checker accepts the deliberate subset of Agent Plugins 1.0.0 used here, plus
the applicable OpenAI listing limits. It requires the review details OpenAI reads
only from the ZIP: exactly five positive and three negative cases, with the positive
ones naming only the four public tools and covering all of them, an HTTPS
walkthrough link and release notes, plus an optional `commerce: false`. Unknown
files/fields, links outside this package, symlinks, credential configuration, any
authentication declaration and a changed MCP endpoint fail closed. This is not a
general-purpose schema validator or a substitute for host review. The archive
contains only the six reviewed package files, including the skill's declaration of
that same MCP dependency. Its verified ZIP digest and source-content digest are
printed; timestamps can make ZIP digests differ across fresh checkouts. Build
output stays under the repository's ignored `build/` directory. These commands do
not contact the MCP server or upload or register anything.

The square SVG is an unchanged copy of `website-ulisten/public/favicon.svg`.
Preserve the existing logo and exact tagline; there is no alternate plugin brand.
The website/support/privacy/terms locations come from the existing website. Their
disclosures still need release review, including how requests from ChatGPT reach
uListen. No new license grant is inferred for the repository/assets.

## Required before release

- Follow the current launch document linked from
  `docs/development/chatgpt-documentation.md`. The four tools reach the production
  endpoint with the uListen Claude connector's release; check the live tool list
  before installing.
- Verify the canonical HTTPS endpoint. The exact trailing slash in
  `https://mcp.ulisten.ai/` is deliberate.
- Test the installed package in the ChatGPT desktop app against production: no
  credential prompt, four read-only tools, a topic search, the channel list,
  analysis for catalog links, a clear answer for a non-catalog link and quotes with
  working timestamp links. Local fixtures do not establish those results.
- Run the acceptance cases against the exact installed package and scanned tool
  list, using fresh ordinary requests that do not preselect uListen. Record misses
  rather than claiming that every link triggers the plugin.
- Recheck rights, privacy and provider policies. The privacy page must describe
  requests that arrive from ChatGPT.
- Add the five positive and three negative review cases under
  `extensions["com.openai"].review` only after running each against production,
  with the release notes and the walkthrough link. OpenAI's review form reads them
  only from the ZIP. No fabricated passing result belongs in the ZIP.
- Bind the final package version and digest to the reviewed source and the scanned
  tool list. Push, review, merge, upload, submission and publication each need their
  own approval; a passing checker grants none of them.

References: [portable packaging](https://developers.openai.com/plugins/build/plugins),
[skill dependencies](https://developers.openai.com/plugins/build/skills),
[submission fields](https://developers.openai.com/plugins/deploy/submission),
[manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json),
[MCP schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json).
