![Job Status Checker icon](./assets/icon.png)

# Job Status Checker

Version 0.1.3. Use this when two structured job-status snapshots disagree and you want an exact-ID reconciliation and a follow-up checklist.

[Product homepage](https://jobcheck-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://jobcheck-mcp.sunrysetech.com/mcp](https://jobcheck-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://jobcheck-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://jobcheck-mcp.sunrysetech.com/support) · [Privacy policy](https://jobcheck-mcp.sunrysetech.com/privacy) · [Terms](https://jobcheck-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Job Status Checker. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://jobcheck-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://jobcheck-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `reconcile_job_snapshots`: Compare job status snapshots. Use this when you want exact job-ID conflicts, missing entries, stale updates and overdue work identified across two snapshots without assuming which one is correct.
- `build_followup_checklist`: Build a job review checklist. Use this when you want review action types for differences between two job snapshots; this does not send messages, modify jobs or verify completion.

## Inputs, sources and privacy

This workflow performs no outbound data lookup. RFC or documentation links below are reference material, not a connected dataset.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

This workflow reads no external dataset. All examples are synthetic, and all calculations use only explicitly supplied inputs.

## Bounds and limitations

Up to 100 rows in each supplied snapshot, matched only by exact job ID. Staleness uses an explicit threshold of 0–3,650 days and the caller's date. No job-system connection, outbound follow-up message or verified real-world completion.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- Works only on supplied structured snapshots and exact IDs; does not connect to job systems or infer semantic matches.
- Reported status and actual real-world completion remain separate.
- Inputs are processed without storage or network access.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "reconcile_job_snapshots",
    "arguments": {
      "today": "2026-10-01",
      "staleAfterDays": 14,
      "left": [
        {
          "jobId": "JOB-1",
          "status": "open",
          "updatedAt": "2026-09-01T12:00:00Z",
          "dueDate": "2026-09-30"
        }
      ],
      "right": [
        {
          "jobId": "JOB-1",
          "status": "completed",
          "updatedAt": "2026-09-30T14:00:00Z",
          "dueDate": "2026-09-30"
        }
      ]
    }
  },
  {
    "name": "reconcile_job_snapshots",
    "arguments": {
      "today": "2026-10-01",
      "left": [
        {
          "jobId": "JOB-2",
          "status": "in_progress",
          "updatedAt": "2026-10-01T10:00:00Z",
          "dueDate": "2026-10-15"
        }
      ],
      "right": [
        {
          "jobId": "JOB-2",
          "status": "in_progress",
          "updatedAt": "2026-10-01T11:00:00Z",
          "dueDate": "2026-10-15"
        }
      ]
    }
  },
  {
    "name": "build_followup_checklist",
    "arguments": {
      "today": "2026-10-01",
      "left": [
        {
          "jobId": "JOB-3",
          "status": "blocked",
          "updatedAt": "2026-09-01T12:00:00Z"
        }
      ],
      "right": []
    }
  }
]
```

## Verification boundary

The dedicated-host builder validates current official portable plugin and MCP schemas, listing bounds, the exact five archive members, updated review cases, preserved endpoint identity and unchanged icons, and source/output hashes. It reads back the completed ZIP. The schema and archive checks do not establish hosted endpoint availability, domain verification, AI-host behavior, submission, approval, or publication. See the accompanying submission-index.json and validation.json outside this individual ZIP for build evidence.

Publisher: Sun Ryse Software LLC.

## Brand assets

This package preserves the original 256 × 256 PNG icon and its SVG source. The manifest references the PNG as both listing logo and composer icon.
