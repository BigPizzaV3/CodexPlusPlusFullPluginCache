![Renewal Deadline Planner icon](./assets/icon.png)

# Renewal Deadline Planner

Version 0.1.3. Use this when you know a renewal date and calendar-day notice period and want planning dates or a calendar file.

[Product homepage](https://renewalclock-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://renewalclock-mcp.sunrysetech.com/mcp](https://renewalclock-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://renewalclock-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://renewalclock-mcp.sunrysetech.com/support) · [Privacy policy](https://renewalclock-mcp.sunrysetech.com/privacy) · [Terms](https://renewalclock-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Renewal Deadline Planner. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://renewalclock-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://renewalclock-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `calculate_notice_dates`: Calculate renewal notice dates. Use this when you want to subtract an explicit calendar-day notice period and preparation lead time from a renewal date, with weekends flagged without shifting.
- `build_notice_calendar`: Build a renewal planning calendar. Use this when you want date-only ICS text for a renewal notice plan using dates and day counts you supplied. Supply a stable unique planId per contract and renewal cycle; this does not install reminders or cancel anything.

## Inputs, sources and privacy

This workflow performs no outbound data lookup. RFC or documentation links below are reference material, not a connected dataset.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

- [iCalendar date and text format (RFC 5545)](https://www.rfc-editor.org/rfc/rfc5545)

## Bounds and limitations

One supplied renewal date per call; notice periods are 0–3,660 calendar days and preparation lead is 0–365 days. Calendar export requires a stable unique planId for each contract and renewal cycle. Reuse that ID for an update and use a new ID for another contract or cycle. No business-day adjustment, cancellation or installed reminder.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- Uses explicit calendar-day counts only; does not interpret contracts, business days, holidays, time zones, or cancellation requirements.
- All-day ICS text is an export, not an installed reminder or a cancelled renewal.
- Inputs are processed without storage or network access.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "calculate_notice_dates",
    "arguments": {
      "renewalOn": "2027-01-01",
      "today": "2026-10-01",
      "noticeDays": 60,
      "leadDays": 14,
      "title": "Review annual software renewal"
    }
  },
  {
    "name": "calculate_notice_dates",
    "arguments": {
      "renewalOn": "2026-10-01",
      "today": "2026-10-02",
      "noticeDays": 30,
      "leadDays": 7,
      "title": "Past planning date example"
    }
  },
  {
    "name": "build_notice_calendar",
    "arguments": {
      "planId": "sample-software-2027",
      "renewalOn": "2027-01-01",
      "today": "2026-10-01",
      "noticeDays": 60,
      "leadDays": 14,
      "title": "Review annual software renewal"
    }
  }
]
```

## Verification boundary

The dedicated-host builder validates current official portable plugin and MCP schemas, listing bounds, the exact five archive members, updated review cases, preserved endpoint identity and unchanged icons, and source/output hashes. It reads back the completed ZIP. The schema and archive checks do not establish hosted endpoint availability, domain verification, AI-host behavior, submission, approval, or publication. See the accompanying submission-index.json and validation.json outside this individual ZIP for build evidence.

Publisher: Sun Ryse Software LLC.

## Brand assets

This package preserves the original 256 × 256 PNG icon and its SVG source. The manifest references the PNG as both listing logo and composer icon.
