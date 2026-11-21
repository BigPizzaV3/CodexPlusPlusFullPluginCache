# EN Training

Private plugin for the existing English-learning MCP server at
`https://en.ruslan.pro/mcp/training` (without a trailing period).

## Contents

- `plugin.json`: portable Agent Plugins 1.0 manifest and OpenAI presentation.
- `mcp.json`: Streamable HTTP connection to the existing server.
- `skills/english-practice/SKILL.md`: personal training and learning-material workflows.
- `assets/logo.svg`: existing EN website logo.

## Connect and verify

Install the private plugin from its Plugin Creator link, then connect your
en.ruslan.pro account through the host's OAuth flow. The server advertises
scope `mcp:use`, authorization code with PKCE S256, refresh tokens, and dynamic
client registration. Authentication remains on the server; this package has
no credentials or static authorization headers.

In a new chat, try:

1. “Show my grammar rules and progress.” Verify personal titles and colors.
2. “Start grammar practice.” Verify the widget appears and accepts an answer.
3. “Find an article about English articles.” Verify search, fetch, and a canonical citation.

Native and target languages come from the website profile. The current MCP
uses native language for rule titles; exercise question text is returned as
stored, without native-language translation.

## Publication and review

Package version 1.0.2 declares `publication.countries: []`, which removes
country targeting restrictions. No language targeting restriction is declared.
Listing translations are optional and do not determine who can use the plugin.

Five positive and three negative review cases are included in
`extensions.com.openai.review.test_cases`. They cover personal rule listing,
automatic practice and widget clicks, selected-rule practice, article search,
and article reading with a Ukrainian explanation; negative cases cover profile
changes, another learner's private progress, and automatic answers on behalf
of the user. These are drafted expectations, not a record of successful host
tests. Run them in order with a dedicated review account containing English
rules, at least one weak rule, approved exercises and a published article about
English articles. Keep the account details outside the ZIP, in the portal's
secure reviewer access fields.

The supplied walkthrough URL is https://en.ruslan.pro/demo-mcp_2.mp4.
The URL returns HTTP 200 with video/mp4; playback and coverage of all review
cases have not been independently verified. An authenticated host run is
still required. Reviewer credentials remain outside the package. Country
availability remains subject to the host platform's own availability.

Live anonymous endpoint and OAuth metadata checks do not establish that an
authenticated session or the widget works in the host. Those require the
user's OAuth consent and installation.

Packaging reference: https://developers.openai.com/plugins/build/plugins

To rebuild the archive from the repository root:

```sh
python3 - <<'PY'
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path('plugins/en-training')
with ZipFile('plugins/en-training.zip', 'w', ZIP_DEFLATED) as archive:
    for path in sorted(root.rglob('*')):
        if path.is_file():
            archive.write(path, Path('app-6ab844d06f30819195150a5edbdef909') / path.relative_to(root))
PY
```
