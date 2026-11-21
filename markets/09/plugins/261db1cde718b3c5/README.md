![Scope Change Checker icon](./assets/icon.png)

# Scope Change Checker

Version 0.1.3. Use this when client requests need comparison with agreed line-item allowances and explicitly approved rates.

[Product homepage](https://scopeguard-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://scopeguard-mcp.sunrysetech.com/mcp](https://scopeguard-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://scopeguard-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://scopeguard-mcp.sunrysetech.com/support) · [Privacy policy](https://scopeguard-mcp.sunrysetech.com/privacy) · [Terms](https://scopeguard-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Scope Change Checker. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://scopeguard-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://scopeguard-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `compare_scope`: Compare requests with remaining agreed scope. Use this when new requests have explicit scope line IDs and units. Shows extra units, unmapped requests and unit mismatches without interpreting contract language.
- `estimate_change_cost`: Estimate mapped scope changes in exact cents. Use this when identified scope changes reference explicitly user-approved quoted rates. Computes exact cents with matching IDs and units; never issues a binding quote or approves the work.

## Inputs, sources and privacy

This workflow performs no outbound data lookup. RFC or documentation links below are reference material, not a connected dataset.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

This workflow reads no external dataset. All examples are synthetic, and all calculations use only explicitly supplied inputs.

## Bounds and limitations

Up to 30 scope lines and 50 requests or changes. Quantities are whole units up to 1,000,000; rates use USD integer cents with explicit approval declarations. No contract interpretation or independently verified approval is implied.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- Caller-supplied line IDs, units, quantities and approval declarations only; no semantic contract interpretation.
- Whole units and USD integer cents; no hidden rounding, authentication, storage or outbound messages.
- Synthetic examples do not imply a real contract or independently verified approval.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "compare_scope",
    "arguments": {
      "agreedScope": [
        {
          "lineId": "DESIGN-01",
          "label": "Included design revisions (synthetic)",
          "unit": "revision",
          "agreedQuantity": 2,
          "alreadyUsedQuantity": 1
        }
      ],
      "requests": [
        {
          "requestId": "CHANGE-01",
          "scopeLineId": "DESIGN-01",
          "unit": "revision",
          "requestedQuantity": 3,
          "description": "Three new revision rounds"
        },
        {
          "requestId": "CHANGE-02",
          "scopeLineId": "COPY-NEW",
          "unit": "page",
          "requestedQuantity": 2
        }
      ]
    }
  },
  {
    "name": "estimate_change_cost",
    "arguments": {
      "changes": [
        {
          "changeLineId": "EXTRA-01",
          "scopeLineId": "DESIGN-01",
          "unit": "revision",
          "quantity": 2,
          "approvedRateId": "RATE-01"
        }
      ],
      "approvedQuotedRates": [
        {
          "rateId": "RATE-01",
          "scopeLineId": "DESIGN-01",
          "unit": "revision",
          "rateCents": 7500,
          "currency": "USD",
          "explicitlyApproved": true
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
