# 2hongo for Claude

Learn Japanese step by step in Claude, from your first words onward, with [2hongo](https://www.2hongo.com).

The plugin has two halves. A **skill** helps Claude explain, correct, and practice Japanese
at your pace — it needs no 2hongo account and works entirely from the conversation. An
**MCP connector** adds 2hongo's stored dictionary data, so readings, meanings, curated examples,
JLPT level, and frequency come from a source rather than from recall.

## Install

```bash
claude plugin marketplace add 2hongo/plugins
claude plugin install 2hongo@twolexis
```

Prefer no plugin? The same tools are available as a custom remote connector — add
`https://www.2hongo.com/api/mcp` as a custom connector in Claude and skip the package entirely.

## Account and authentication

The teaching skill works immediately, with no account.

Every 2hongo tool, the dictionary included, requires a **free** 2hongo account; until the server
is connected, Claude sees no 2hongo tools at all. Connect it from `/plugin` (or the connector
settings in Claude): the 2hongo authorization page opens, you sign in or create an account and
approve the connection. There is no subscription step and no upgrade prompt in that flow — an
existing paid subscription is simply recognized. A connection lasts 30 days, after which you
connect again.

The connection uses OAuth 2.1 with PKCE. Access tokens are short-lived and limited to the
permissions you approved. To end the connection, revoke it on 2hongo under Account Settings >
Sessions > Connected AI assistants; access stops on the next request. 2hongo never receives
your Claude conversation — only the specific word or query a tool call carries.

## Try it

```
Help me learn Japanese step by step. Start with what I already know and guide me from there.
```

```
Break down 「昨日は友達と映画を見に行った」 for me. I'm around N4.
```

```
Look up 込む in 2hongo and show me the readings and a couple of real examples.
```

```
I wrote 「私は日本語を勉強しました三年間」. Correct it and explain what moved and why.
```

## Tools

| Tool                      | What it returns                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `search_words`            | Dictionary matches for a spelling or reading, as stable slugs                                                                                 |
| `search_by_meaning`       | Entries found from a description of the meaning, in any supported language                                                                    |
| `get_word`                | One entry: readings, localized meanings, curated examples, relationships, JLPT and frequency data, and a link to hear its recording on 2hongo |
| `search_grammar`          | Grammar patterns matching a pattern form or a meaning                                                                                         |
| `get_grammar`             | One pattern's authored explanation, formation, register, and worked examples                                                                  |
| `get_review_summary`      | Words due today, reviews done today, and the current streak                                                                                   |
| `get_study_plan`          | The current 2hongo study plan and which items are done                                                                                        |
| `get_learner_profile`     | Your editable learning profile, settings, pacing stage, and progress                                                                          |
| `get_practice_set`        | Due, weak, and recently started items from your record, with authored questions where available                                               |
| `get_content_brief`       | Words and grammar you are learning for Claude to write into new Japanese, and the level to use                                                |
| `get_progress_insights`   | Recent activity, vocabulary accuracy trends, learning signals, and a concrete next step                                                       |
| `get_jlpt_readiness`      | Coverage of a JLPT level across 2hongo grammar, kanji, vocabulary, basics, and prerequisites                                                  |
| `record_usage_evidence`   | A structured correct-use or error signal for a word or grammar sense the learner produced                                                     |
| `update_learning_state`   | Saves a word, grammar sense, kanji, or kana to your reviews, or marks it known                                                                |
| `update_learner_settings` | Updates your declared level, goal, or daily study time after you confirm the values                                                           |
| `update_learning_profile` | Replaces the learning profile after you approve the complete proposed text                                                                    |
| `submit_practice_results` | Grades authored answers and records due-item results, including misses                                                                        |
| `report_content`          | Sends an error you agree to report in a 2hongo question or word entry to the 2hongo team; changes nothing in your record                      |

The account tools read or change your 2hongo account, so Claude asks for those permissions separately
when you connect — a connection that only searches the dictionary never gets them.

`get_content_brief` is told only whether Claude is writing a story, a dialogue,
examples, or an explanation — never what it is about. Claude writes the text; 2hongo supplies what
to weave in.

The tools follow the same plans as the website. Every account reads the dictionary and the full
grammar reference at every JLPT level. Word audio, and recording study progress on grammar and kanji,
cover N5 and kana on a free account and every level from Standard. Meaning search has a daily
allowance that grows with the plan. `get_learner_profile` returns your own settings and editable
learning profile on any account; the stage and progress it derives from your study record come with
Plus and Max. Personalized practice selection, reading checks, and writing briefs follow the same
boundary. Progress insights follow it too, and explicitly leave accuracy unavailable where 2hongo
does not yet keep per-review history. JLPT readiness follows the same boundary and reports only
coverage of 2hongo's inventory — never a test score or pass prediction. Submitting practice results
is available on every plan. `record_usage_evidence` follows the personalization boundary. It
stores only the word or grammar sense, result, optional issue category, day, and calling client —
never the learner's sentence — after the learner is told. Every entry appears under Account Settings
→ Learning Profile → AI assistant activity and can be deleted there. Repeated mapped grammar evidence
can update a checked Basics chapter and refresh an existing Sensei plan; it never moves an SRS schedule.
The tools say when you have hit one of those boundaries;
they never offer to sell you anything.

Word recordings play on 2hongo: `get_word` links to the word's page when your plan includes its
recording, and leaves the link out otherwise.

## Troubleshooting

- **"Connect a free 2hongo account", or Claude says it can't reach 2hongo** — the server isn't
  connected, the 30-day connection lapsed, or it was revoked. Re-authorize the plugin from
  `/plugin`, or reconnect the connector. Setup steps for each app:
  [2hongo.com/en/help/ai-assistants](https://www.2hongo.com/en/help/ai-assistants#connect).
- **A word isn't found** — Claude resolves conjugated forms to the dictionary form before looking
  a word up, but it can miss. Ask it to search the dictionary form directly — 見に行った → 行く.
- **Claude answers without consulting 2hongo** — that is the skill working as designed for generic
  explanation. Ask it to look the word up in 2hongo when you want sourced data.

Anything else: [2hongo.com/en/contact](https://www.2hongo.com/en/contact).

## Links

[Help](https://www.2hongo.com/en/help) · [Privacy](https://www.2hongo.com/en/privacy) ·
[Terms](https://www.2hongo.com/en/terms) · [About](https://www.2hongo.com/en/about)

## License

MIT — see [LICENSE](./LICENSE).

---

This repository is **generated**. It is projected from 2hongo's application repository by a sync
script, so pull requests opened here are overwritten by the next sync. Please report issues through
[2hongo.com/en/contact](https://www.2hongo.com/en/contact).
