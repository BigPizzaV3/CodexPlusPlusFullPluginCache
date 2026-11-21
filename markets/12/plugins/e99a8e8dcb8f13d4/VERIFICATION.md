# Distribution verification — October 14, 2026 (America/Los_Angeles)

**Update, package 0.1.2 (October 14, 2026, evening PDT):** the publisher approved the
Vibe Coding Control brand. The package now includes `assets/logo.png` (1024×1024,
opaque) and `assets/icon.png` (128×128) referenced as `logo` / `composerIcon`, with
`brandColor` `#3B82F6`. The service was released as VCC **0.1.7** (Production
release `20261015T044604Z`), including the `annotations.title` metadata patch and
MCP `serverInfo.icons`. The Registry entry `io.github.OMNOM-111/vcc-remote` **0.1.2**
(with icons) is active/latest. Schemas and the 12 targeted cases were re-run: PASS.
Rows below are the original 0.1.1 verification against VCC 0.1.6.

The public service reported VCC **0.1.6**. This package is **0.1.1**; these are
separate version numbers. No Production deployment was performed in this work.

| Check | Result and boundary |
|---|---|
| Agent Plugins plugin/MCP and official Registry JSON schemas | PASS against the downloaded official versioned schemas. |
| Five positive and three negative service cases, OAuth/revocation/hints | PASS, 12 targeted HTTP tests on isolated fixtures. Includes real two-user isolation. This is not a native client or model prompt-selection test. |
| Public OAuth and scenarios P1–P5 | PASS over Production HTTPS using a dedicated synthetic account: projects, task/run reuse, note retry, history and a website decision delivered once. |
| Public negative boundaries | File/shell tools absent, protected push denied, nonexistent foreign project denied. Actual second-account foreign-project isolation was exercised on fixtures; the publisher's real projects were not probed. |
| Claude custom connector | PASS: real DCR/PKCE OAuth, nine tools, synthetic task/run/step/note, website owner decision, one acknowledgment, run completion. Three negative prompts were refused or explained without attempting them. |
| Codex CLI | PASS: real tools over public HTTPS, own task/run reuse, same note retry returns the same event ID. Cross-agent run resume was correctly denied; own-run resume passed. OAuth bearer was supplied from the dedicated test consent, not from the publisher's account. Directory package installation and CLI-managed OAuth storage were not tested. |
| Public test-grant revocation | PASS: website revoke, subsequent protected MCP request 401 and refresh 400; ephemeral test token file removed. Claude's separate test connection remains available for its draft. |
| Official MCP Registry | Published `io.github.OMNOM-111/vcc-remote` 0.1.1; API readback reports active/latest. This does not prove inclusion in the separately curated GitHub/VS Code gallery. |
| VS Code, Cursor, Windsurf native client installation | NOT RUN for this package. Official connection examples and install-link payloads are prepared; no user's existing editor settings were changed. |
| ChatGPT private plugin / common directory install | NOT RUN in this work. OpenAI publisher identity verification blocks even draft upload. |

One initial Claude consent attempt returned HTTP 501; the retry connected
successfully. This transient result is retained as a limitation, not hidden by
the later successful calls.

Claude's live tool scan suggested `annotations.title` on all nine tools. A narrow
metadata patch is prepared and locally verified, but has not been deployed.
The `vcc_step` API-doc suggestion appears to treat its evidence URL as an external
API input; the server stores that URL and does not fetch it.

The common OpenAI submission still needs verified publisher identity, approved
graphics, the portal's exact domain challenge, independent reviewer access and
an accessible real demonstration video. The current Google test identity has not
been supplied to reviewers and is not a reviewer-ready credential solution.
No private account credentials, application source or runtime data are in this
repository. GitHub Actions remain disabled, including this distribution repo.
