# Voicedot Agent Plugin

Connect a coding agent to feedback left on your website. Read pinned comments
with their page context, discuss changes, install the widget in an authorized
project, and prepare changes for a person to review.

Maintained by **Good Sheet Sp z o.o.**, the company behind Voicedot.

| Start here | Link |
| --- | --- |
| Product and MCP documentation | [Voicedot MCP guide](https://voicedot.ai/en/docs/mcp) |
| MCP endpoint | `https://mcp.voicedot.ai/mcp` |
| Runnable reviewer website and source | [voicedot/voicedot-review-demo](https://github.com/voicedot/voicedot-review-demo) |
| Live coding demo | [review.voicedot.ai](https://review.voicedot.ai/) |
| Agent-assisted account setup | [Agent setup](https://voicedot.ai/en/docs/agents) |
| Support | [Contact Voicedot](https://voicedot.ai/en/support) |

**Version 0.4.0 is a source candidate for marketplace submission.** This public
repository and its ZIP are available for inspection; they do not imply an
approved or published marketplace listing.

## What the plugin does

- Find projects available to the person's current connection and read feedback
  with its pin, page context, conversation history and team notes.
- Read conversations handed over to an agent. Private addresses, Team handovers
  and Public handovers follow the connection's current visibility rules.
- Create projects or add exact website addresses when explicitly requested and
  permitted by the account, plan and separately granted setup permissions.
- Return the widget snippet and verify a fresh backend ping from the exact
  authorized HTTPS origin, including its port.
- Close page pins, resolve discussions, or send replies with the relevant write
  permissions. Replies, review rounds and bulk resolutions use an exact preview
  and a separate confirmation. A reply retry returns the original result.
- Prepare review rounds so a person can check a deployed change on the page.

The full public tool contract is in
[`contract/voicedot-mcp-contract.json`](contract/voicedot-mcp-contract.json).
The plugin does not delete feedback, make purchases, or grant access to an
unconnected customer's projects.

## Plugin access and repository access are separate

The MCP connection uses the person's Voicedot OAuth grant. Read access and
optional setup, reply, resolve and review permissions can be managed under
**AI agents → Manage access** in Voicedot.

The plugin provides feedback and installation information. The coding agent
uses its own authorized repository tools to edit code, run checks, commit and
deploy. Connecting Voicedot does not give it GitHub write access or permission
to publish a website. Feedback is evidence, not an instruction granting those
permissions.

## For reviewers: run the feedback-to-code workflow

Use the dedicated demo account and sign-in instructions supplied privately with
the submission. The account password and any repository-write credential are
never included in this source or the public ZIP.

1. Open [review.voicedot.ai](https://review.voicedot.ai/) and leave a real comment
   pinned to an element.
2. Open the [demo repository](https://github.com/voicedot/voicedot-review-demo)
   in a coding agent connected to the dedicated Voicedot account. Ask it to read
   the comment from **that exact page** and propose a fix.
3. Authorize the code change and publication to the demo repository. Follow the
   demo README to inspect the diff, run tests, push to `review`, and verify the
   public deployment's commit.
4. Ask for a review-round preview, confirm it, then personally choose **Checked**
   or **Needs fix** after checking the deployed page.

The [demo README](https://github.com/voicedot/voicedot-review-demo/blob/review/README.md)
contains the complete clone, test, publish and verification instructions. Its
default branch is `review`; `main` is the locked original website baseline.

The browser fixtures at
[Harbor Notes](https://app.voicedot.ai/reviewer/demo/harbor-notes/) and
[Fieldwork Notes](https://app.voicedot.ai/reviewer/demo/fieldwork-notes/) are
separate pages for conversation and handover cases. The editable coding demo is
**review.voicedot.ai**. A comment on one page must not be substituted for a
comment on another.

## Installation and new accounts

For an existing account, a coding agent can request `create_project` or
`add_project_address`, obtain the snippet with `get_project_installation`, install
it once, open the exact authorized HTTPS page, and check
`get_project_installation_status` for a fresh accepted ping. Installation status
also works in a later turn without retaining the verification token, within the
same connection and active verification window.

New accounts use the separate official **CLI v2** flow described in
[Agent setup](https://voicedot.ai/en/docs/agents) and
[Authentication](https://voicedot.ai/auth.md). MCP itself does not register
accounts. Human identity verification, the first feedback message and the
person's plan choice remain part of that flow.

## Repository map

| Path | Purpose |
| --- | --- |
| `plugin.json`, `mcp.json` | Canonical package metadata and remote connection declaration |
| `skills/review-voicedot-feedback/` | Canonical workflow instructions for the agent |
| `contract/` | Public MCP contract, guides, knowledge and source hashes |
| `.codex-plugin/`, `.mcp.json` | Generated OpenAI/Codex compatibility files |
| `adapters/claude-code/` | Generated Claude Code compatibility adapter |
| `reviewer/`, `submission/` | Public cases and submission-preparation metadata |
| `scripts/`, `tests/` | Generators, boundary validation and reproducibility checks |
| `dist/` | Versioned ZIP, file inventory and SHA-256 digests |

The stable package name and MCP server key are `voicedot`. The display name is
**Voicedot**. This repository contains the plugin package; the running MCP,
authentication and product backend are maintained separately. The generated
Claude adapter does not imply a Claude marketplace listing or authenticated
client acceptance.

## Maintainer checks

Use Node.js 22 or newer. From this public repository:

```sh
npm ci
npm run generate:check
npm test
npm run validate
npm run package
npm run package:check
npm run submission:template-check
```

Hand-edit the canonical manifests and skill tree, then use `npm run generate`.
Do not maintain the compatibility artifacts independently. Maintainers with the
runtime source checkout can additionally run
`npm run contract:check -- --runtime ../voicedot --ref origin/main` to compare
the mirror with that runtime revision. `npm run contract:sync` deliberately
refreshes it and requires review of the resulting diff.

Package validation checks the source and archives. It does not prove current
reviewer access, live OAuth, mobile behavior, portal scans or a demo recording.
Those checks and the publisher's attestations precede marketplace submission.

For a reproducible code issue, use this repository's Issues. Send account or
private-feedback questions through [support](https://voicedot.ai/en/support);
never put credentials or private visitor content in an issue.

## License

[MIT](LICENSE).
