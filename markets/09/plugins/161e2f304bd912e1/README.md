![Public Comment Deadlines icon](./assets/icon.png)

# Public Comment Deadlines

Version 0.1.3. Use this when you want to find federal public-comment notices, inspect observed closing dates and related notices, or export a selected date to a calendar.

[Product homepage](https://commentclock-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://commentclock-mcp.sunrysetech.com/mcp](https://commentclock-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://commentclock-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://commentclock-mcp.sunrysetech.com/support) · [Privacy policy](https://commentclock-mcp.sunrysetech.com/privacy) · [Terms](https://commentclock-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Public Comment Deadlines. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://commentclock-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://commentclock-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `search`: Search public-comment notices. Use this when you want a bounded topic or docket search of Federal Register proposed rules and notices, with observed deadlines and official PDF links where provided.
- `fetch`: Inspect a public-comment notice. Use this when you have a Federal Register document number and want its observed closing date, dates excerpt, official PDF and a bounded related-notice search that may identify extensions or corrections.
- `build_comment_calendar`: Export selected comment planning dates. Use this when you have explicitly selected a notice and date and want date-only ICS text; this does not recheck the notice, install reminders or submit comments.

## Inputs, sources and privacy

Public lookup queries and identifiers are sent only to the fixed public providers described below. In this suite, those provider API hosts are saferproducts.gov (CPSC), api.crossref.org (Crossref) and federalregister.gov (Federal Register); a dedicated workflow uses only its own stated provider. Public providers have their own policies.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

- [Federal Register API documentation and legal-status notice](https://www.federalregister.gov/developers/documentation/api/v1)
- [Official Federal Register editions on GovInfo](https://www.govinfo.gov/app/collection/FR)

## Bounds and limitations

Search returns at most 10 documents per call. Fetch reads one document and, if a docket exists, searches at most 10 related notices for the first docket only. Each source request is limited to 8 seconds and 1 MiB. Calendar output requires a caller-confirmed date and is an export only.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- FederalRegister.gov is an informational rendition; verify the linked official PDF and agency docket before relying on a filing deadline.
- A date-only closing field does not establish a closing time or time zone. Later extensions or corrections may exist.
- Related review is a bounded search of one docket string and is not a legal determination or exhaustive review.
- No accounts, comment submissions, scheduled monitoring, private data storage or installed reminders.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "search",
    "arguments": {
      "query": "File No. R607007",
      "limit": 3
    }
  },
  {
    "name": "fetch",
    "arguments": {
      "documentNumber": "2026-20078"
    }
  },
  {
    "name": "search",
    "arguments": {
      "query": "sunryse-synthetic-no-match-7a952",
      "limit": 2
    }
  },
  {
    "name": "build_comment_calendar",
    "arguments": {
      "documentNumber": "2026-20078",
      "selectedDeadline": "2026-10-30",
      "today": "2026-10-01",
      "title": "Review FTC petition notice",
      "leadDays": 7,
      "selectionConfirmed": true
    }
  }
]
```

## Verification boundary

The dedicated-host builder validates current official portable plugin and MCP schemas, listing bounds, the exact five archive members, updated review cases, preserved endpoint identity and unchanged icons, and source/output hashes. It reads back the completed ZIP. The schema and archive checks do not establish hosted endpoint availability, domain verification, AI-host behavior, submission, approval, or publication. See the accompanying submission-index.json and validation.json outside this individual ZIP for build evidence.

Publisher: Sun Ryse Software LLC.

## Brand assets

This package preserves the original 256 × 256 PNG icon and its SVG source. The manifest references the PNG as both listing logo and composer icon.
