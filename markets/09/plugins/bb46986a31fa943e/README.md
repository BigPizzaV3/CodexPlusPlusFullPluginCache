![Report Numbers Checker icon](./assets/icon.png)

# Report Numbers Checker

Version 0.1.3. Use this when you need to check report totals, ratios and growth claims against a supplied table, with traceable references and unresolved-data handling.

[Product homepage](https://reportcheck-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://reportcheck-mcp.sunrysetech.com/mcp](https://reportcheck-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://reportcheck-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://reportcheck-mcp.sunrysetech.com/support) · [Privacy policy](https://reportcheck-mcp.sunrysetech.com/privacy) · [Terms](https://reportcheck-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Report Numbers Checker. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://reportcheck-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://reportcheck-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `audit_report`: Check report arithmetic against supplied data. Use this when checking up to twenty claimed totals, ratios or percentage changes against explicit metric/period cells. Require source and claim references plus an absolute rounding tolerance. Missing, null, zero-denominator and negative-baseline cases stay unresolved. Only supplied data is checked; send aggregate nonpersonal data, never confidential or personal records. Inputs are not retained.
- `compare_periods`: Compare two supplied periods. Use this when comparing absolute and relative changes for aggregate metrics in two supplied periods. Requires distinct periods and unique IDs. Relative change is undefined for zero or negative prior values. No source verification, connected analytics or causal explanation is inferred. Inputs are not retained.

## Inputs, sources and privacy

This workflow performs no outbound data lookup. RFC or documentation links below are reference material, not a connected dataset.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

This workflow reads no external dataset. All examples are synthetic, and all calculations use only explicitly supplied inputs.

## Bounds and limitations

Up to 12 metrics, 12 periods, 144 supplied cells and 20 claims. Absolute tolerance must be explicitly set from 0 through 1. Missing/null inputs and zero or negative growth baselines remain unresolved. No analytics account or source verification is performed.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- Checks only caller-provided numbers and source references; it does not connect to analytics, verify the source, or infer causation.
- Missing cells and explicit nulls remain unresolved. Relative percentage change requires a positive baseline; zero and negative baselines are reported separately.
- Tolerance is an explicit absolute amount from 0 through 1 in the claim result's units. Totals use compensated summation; other arithmetic uses finite JavaScript numbers with an operation- and magnitude-scaled representation allowance. Unrepresentable overflow or underflow remains unresolved.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "audit_report",
    "arguments": {
      "table": {
        "metrics": [
          {
            "id": "orders",
            "label": "Synthetic order count",
            "unit": "count"
          }
        ],
        "periods": [
          {
            "id": "before",
            "label": "Example prior period"
          },
          {
            "id": "after",
            "label": "Example current period"
          }
        ],
        "cells": [
          {
            "metricId": "orders",
            "periodId": "before",
            "value": 100,
            "sourceRef": "Synthetic table row 1"
          },
          {
            "metricId": "orders",
            "periodId": "after",
            "value": 120,
            "sourceRef": "Synthetic table row 2"
          }
        ]
      },
      "claims": [
        {
          "id": "growth",
          "lineRef": "Synthetic report sentence 1",
          "kind": "percentage_change",
          "metricId": "orders",
          "fromPeriodId": "before",
          "toPeriodId": "after",
          "claimedValue": 25,
          "absoluteTolerance": 0.05
        }
      ]
    }
  },
  {
    "name": "compare_periods",
    "arguments": {
      "table": {
        "metrics": [
          {
            "id": "orders",
            "label": "Synthetic order count",
            "unit": "count"
          }
        ],
        "periods": [
          {
            "id": "before",
            "label": "Example prior period"
          },
          {
            "id": "after",
            "label": "Example current period"
          }
        ],
        "cells": [
          {
            "metricId": "orders",
            "periodId": "before",
            "value": 100,
            "sourceRef": "Synthetic table row 1"
          },
          {
            "metricId": "orders",
            "periodId": "after",
            "value": 120,
            "sourceRef": "Synthetic table row 2"
          }
        ]
      },
      "metricIds": [
        "orders"
      ],
      "fromPeriodId": "before",
      "toPeriodId": "after"
    }
  }
]
```

## Verification boundary

The dedicated-host builder validates current official portable plugin and MCP schemas, listing bounds, the exact five archive members, updated review cases, preserved endpoint identity and unchanged icons, and source/output hashes. It reads back the completed ZIP. The schema and archive checks do not establish hosted endpoint availability, domain verification, AI-host behavior, submission, approval, or publication. See the accompanying submission-index.json and validation.json outside this individual ZIP for build evidence.

Publisher: Sun Ryse Software LLC.

## Brand assets

This package preserves the original 256 × 256 PNG icon and its SVG source. The manifest references the PNG as both listing logo and composer icon.
