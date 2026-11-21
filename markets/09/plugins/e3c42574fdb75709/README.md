![Study Plan Builder icon](./assets/icon.png)

# Study Plan Builder

Version 0.1.3. Use this when scoring authorized practice answers or dividing a study session among weak, unseen and older topics using supplied results.

[Product homepage](https://studysprint-mcp.sunrysetech.com/)

## Install and public review

This is a dedicated-host public-review package, not an approved public-directory listing. This build prepares files only; it does not submit, approve, publish, deploy, or verify domain ownership.

Remote MCP URL: [https://studysprint-mcp.sunrysetech.com/mcp](https://studysprint-mcp.sunrysetech.com/mcp)

Authentication: none. Use Streamable HTTP. The host must connect to the deployed endpoint; this ZIP does not run a server. Host plan and administrator settings may control access.

The portable Agent Plugins 1.0.0 archive contains exactly five files: root `plugin.json`, `mcp.json`, `README.md`, `assets/icon.png`, and `assets/icon.svg`. It retains five positive and three negative review cases using public or synthetic inputs. Reviewer walkthrough: [Watch the recorded demo](https://studysprint-mcp.sunrysetech.com/review-demo.mp4).

[Support](https://studysprint-mcp.sunrysetech.com/support) · [Privacy policy](https://studysprint-mcp.sunrysetech.com/privacy) · [Terms](https://studysprint-mcp.sunrysetech.com/terms)

Follow the [OpenAI packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission requirements](https://developers.openai.com/plugins/deploy/submission). Domain verification, endpoint availability, current tool scans, developer identity, actual host conversations, and review materials are separate submission gates. Serve only this plugin's portal-issued token at the challenge URL shown in its draft; do not replace another plugin's token.

## Interactive workspace and usage guide

In a compatible ChatGPT surface, ask to open Study Plan Builder. The `open_app` tool opens a task selector and input form. Review the inputs before running a task; examples are synthetic scenarios or public samples, not saved customer records. The interface adds no account access, persistence or background automation.

The [public usage guide](https://studysprint-mcp.sunrysetech.com/) contains a labeled example, usage steps and sample prompts in the current navy/blue design. No public ZIP download is required.

The retained recording at https://studysprint-mcp.sunrysetech.com/review-demo.mp4 demonstrates the earlier tool workflow and predates the interactive workspace. Current direct MCP checks verify `open_app`, the deployed UI resource and the functional data-tool cases. These checks do not establish ChatGPT rendering, user interaction or model refusals.

## What it does

- `score_practice`: Score supplied practice answers. Use this when scoring your authorized original or public practice answer key and selected options. Exact option sets receive credit; missing and invalid responses are excluded by default unless a count_wrong policy is explicitly chosen. Duplicate IDs and invalid keys fail validation. Supply question IDs and option labels only, not personal details. No question bank is supplied and no progress is stored.
- `plan_review`: Allocate a study session. Use this when turning supplied topic attempt/correct counts, review ages and a 1–240 minute budget into a whole-minute review plan. Gives unseen, weak and older topics explicit priority weights; all allocated minutes fit the budget. This is a planning heuristic, not an official exam-readiness assessment or scheduled reminder. No progress is stored.

## Inputs, sources and privacy

This workflow performs no outbound data lookup. RFC or documentation links below are reference material, not a connected dataset.

The service has no customer-account access, OAuth credentials, receipt access, private-system integration, database, persisted progress or stored user session. Inputs and outputs are processed temporarily in memory. The supplied Worker configuration disables application request logs and traces; this statement does not describe retention by your AI host, network provider or public data provider. Send public or nonsensitive aggregate inputs only. Do not send passwords, account records, receipts, personal identifiers or confidential documents.

This workflow reads no external dataset. All examples are synthetic, and all calculations use only explicitly supplied inputs.

## Bounds and limitations

Up to 60 questions with 2–8 option labels each. Missing and invalid answers are excluded unless count_wrong is explicitly chosen. Review plans accept up to 20 topic summaries and a 1–240 minute budget. No licensed question bank, learner account or saved progress is supplied.

The shared HTTP service caps each request at 48 KiB, data-tool response at 128 KiB (native UI resources have a separate 1 MiB ceiling) and execution at 20 seconds; those transport bounds also apply when an individual schema permits a larger combination of fields. Source failure, incomplete coverage and unresolved inputs must remain visible.

- Use only an answer key and options you are authorized to provide. No question bank, private exam content or official exam integration is supplied.
- Scores reflect only the supplied key and explicit grading policies. They do not establish official exam readiness or validate the key.
- Review allocations are a transparent planning heuristic based on supplied aggregate counts and review age, not a validated learning prediction. No progress is stored.

## Public or synthetic examples

These are input examples, not customer outcomes. Replace only with public or authorized nonsensitive inputs. They do not create accounts, send messages, submit comments, change contracts, cancel renewals, install calendar reminders or store study progress.

```json
[
  {
    "name": "score_practice",
    "arguments": {
      "answerKey": [
        {
          "id": "q1",
          "topicId": "fractions",
          "selection": "single",
          "options": [
            "A",
            "B",
            "C"
          ],
          "correctAnswers": [
            "B"
          ]
        },
        {
          "id": "q2",
          "topicId": "fractions",
          "selection": "multiple",
          "options": [
            "A",
            "B",
            "C"
          ],
          "correctAnswers": [
            "A",
            "C"
          ]
        }
      ],
      "answers": [
        {
          "questionId": "q1",
          "selectedOptions": [
            "B"
          ]
        },
        {
          "questionId": "q2",
          "selectedOptions": [
            "A"
          ]
        }
      ],
      "missingAnswerPolicy": "exclude",
      "invalidAnswerPolicy": "exclude"
    }
  },
  {
    "name": "plan_review",
    "arguments": {
      "minutes": 30,
      "topics": [
        {
          "id": "fractions",
          "label": "Synthetic fractions practice",
          "attempted": 8,
          "correct": 3,
          "lastReviewedDaysAgo": 7
        },
        {
          "id": "geometry",
          "label": "Synthetic geometry practice",
          "attempted": 0,
          "correct": 0,
          "lastReviewedDaysAgo": null
        },
        {
          "id": "algebra",
          "label": "Synthetic algebra practice",
          "attempted": 10,
          "correct": 9,
          "lastReviewedDaysAgo": 1
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
