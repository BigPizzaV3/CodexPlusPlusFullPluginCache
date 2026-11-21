![Document Change Checker icon](./assets/icon.png)

# Document Change Checker

Version 0.1.3. Use this when a public RFP addendum changes and you need line evidence plus an explicit requirement coverage checklist.

[Product homepage](https://bidpatch-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://bidpatch-mcp.sunrysetech.com/mcp](https://bidpatch-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://bidpatch-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://bidpatch-mcp.sunrysetech.com/support) · [Privacy policy](https://bidpatch-mcp.sunrysetech.com/privacy) · [Terms](https://bidpatch-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Document Change Checker. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://bidpatch-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://bidpatch-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `diff_public_documents`: Compare public bid document versions. Use this when you have before/after public bid text and need exact added, removed and changed lines with date, money and obligation review flags. Never determines legal compliance.
- `check_requirement_coverage`: Map bid evidence to requirement IDs. Use this when explicit requirement IDs and supplied excerpts need a coverage checklist. Distinguishes missing evidence, unknown status and unverified user assertions; never certifies satisfaction.

## Inputs, sources and privacy

This workflow performs no outbound data lookup. RFC or documentation links below are reference material, not a connected dataset.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

This workflow reads no external dataset. All examples are synthetic, and all calculations use only explicitly supplied inputs.

## Bounds and limitations

Each supplied document is limited to 12,000 characters and 200 lines. Coverage accepts at most 30 requirements and 60 evidence entries. No documents or procurement accounts are fetched; requirement mapping uses caller-provided IDs.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- Operates only on caller-supplied text and IDs; it does not access procurement accounts or retrieve documents.
- Maximum 12,000 characters and 200 lines per version; no semantic or legal compliance decision.
- Synthetic examples demonstrate behavior, not a real bid award or verified customer result.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "diff_public_documents",
    "arguments": {
      "beforeLabel": "RFP original (synthetic)",
      "afterLabel": "Addendum 1 (synthetic)",
      "beforeText": "RFP 24-A\nProposals must arrive by October 12, 2026.\nBudget: $25,000\nSubmit one PDF.",
      "afterText": "RFP 24-A\nProposals must arrive by October 19, 2026.\nBudget: $30,000\nSubmit one PDF.\nA security questionnaire is required."
    }
  },
  {
    "name": "check_requirement_coverage",
    "arguments": {
      "requirements": [
        {
          "id": "R-01",
          "text": "Include two references.",
          "mandatory": true
        },
        {
          "id": "R-02",
          "text": "Include delivery schedule.",
          "mandatory": true
        }
      ],
      "evidence": [
        {
          "evidenceId": "E-01",
          "requirementId": "R-01",
          "sourceLabel": "Synthetic proposal",
          "sourceLineStart": 4,
          "sourceLineEnd": 5,
          "excerpt": "Reference A; Reference B.",
          "userAssessment": "addresses_requirement"
        }
      ]
    }
  }
]
```

## Verification boundary

The dedicated-host builder validates current official portable plugin and MCP schemas, listing bounds, the exact five archive members, updated review cases, preserved endpoint identity and unchanged icons, and source/output hashes. It reads back the completed ZIP. The schema and archive checks do not establish hosted endpoint availability, domain verification, AI-host behavior, submission, approval, or publication. See the accompanying submission-index.json and validation.json outside this individual ZIP for build evidence.

Publisher: Sun Ryse Software LLC.

## Brand assets

This package preserves the original 256 × 256 PNG icon and its SVG source. The manifest references the PNG as both listing logo and composer icon.
