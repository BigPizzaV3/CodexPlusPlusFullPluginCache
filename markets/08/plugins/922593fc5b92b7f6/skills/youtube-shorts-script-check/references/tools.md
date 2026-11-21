# Prepublish MCP tools: exact reference

Server: `https://prepublish.ai/mcp` (Streamable HTTP, stateless, anonymous use allowed). Six tools. Every AI-backed result carries a `notice` field; repeat its meaning to the user and never drop it.

## audit_script

Full audit of a finished or near-finished YouTube script draft.

Inputs:

| Field | Required | Rules |
| --- | --- | --- |
| `video_title` | yes | 1 to 255 characters. The title the creator plans to publish under. The audit checks whether the script delivers the title's promise, so ask for it if missing. |
| `script_text` | yes | 50 to 250,000 characters. Paste the user's script verbatim. Do not rewrite, summarise, clean or translate it first. |
| `email` | anonymous users only | Where the free result is sent. Prepublish stores the address with the audit, emails the result link to it, and may send a short series of follow-up emails about the audit that include an unsubscribe link. Ask the user for it. Never invent one, never reuse an address from elsewhere in the conversation without asking. |
| `video_duration_seconds` | no | Only if the user stated an intended runtime. Never assume one. |
| `category` | no | Only if the user said it (for example "finance", "history documentary"). |
| `audience` | no | Only if the user said it. |

Output (`structuredContent`):

- `notice`: the scope limit. Always pass its meaning on.
- `analysis_id`: keep it; `get_audit` needs it.
- `open_in_browser`: the same report on prepublish.ai.
- `analysis`: present once the audit settles. See `report-fields.md`.
- `status: "running"` and `next_step`: present only when the audit had not settled inside the call. Then call `get_audit` with the id about a minute later.

In ChatGPT the result renders as an inline report card. When the card is shown, do not reprint the whole report as text: summarise the top issue in one or two sentences and add what the user asked for.

## get_audit

Collects an audit started earlier. Input: `analysis_id`. Free, performs no new analysis. Use it when `audit_script` returned `status: "running"`, or when the user refers back to an earlier audit.

## audit_hook

Scores only the opening lines.

Inputs: `hook_text` (10 to 5,000 characters, ideally the first 15 to 30 seconds of speech, verbatim), optional `niche` (only if stated), `email` (only after the daily free anonymous hook check is used; same disclosure and rules as above).

Output `hook`: `overall_score` (0 to 100), `grade` (a letter), `one_sentence_verdict`, `sentences[]` (each: `quote`, `attention_pull` 0 to 10, `curiosity_gap` 0 to 10, `payoff_distance` near, mid or far, `note`), `top_issues[]` (each: `headline`, `quote`, `why`), `rewrites[]` (each: `style`, `hook`, `why_works`).

## check_authenticity

Checks a script for reused, templated or mass-produced content signals, the kind YouTube's inauthentic-content expectations target.

Inputs: `video_title`, `script_text` (verbatim).

Output `authenticity`: `score` (0 to 100, a risk score: higher means more risk), `risk_level` (`low` 0 to 33, `medium` 34 to 66, `high` 67 to 100), `verdict`, `signals[]` (each: `name`, `severity` low/medium/high, `reason`, `quote`), `remediation[]` (each: `title`, `current`, `fix`, `why`), optional `override_note`.

Signal names you may see include `listicle_title`, `clickbait_phrases`, `transition_overuse`, `em_dash_density`, `sentence_burstiness`, `cliche_density`, `lexical_diversity`, `first_person_ratio`, `vague_attribution`, `forced_conflict`, `template_story_narration`, `listicle_no_insight`, `translated_dub_pattern`, `ai_voiceover_stock_assumption`, `generic_hook`, `faceless_no_expertise`. Explain them in plain words; do not print raw ids unless asked.

It reports text-level signals only. It is not a monetisation decision and does not speak for YouTube.

## policy_preflight

Checks a script against the categories in YouTube's published advertiser-friendly guidelines and Community Guidelines.

Inputs: `script` (at least 200 characters, verbatim), optional `title` (titles are checked too).

Output: `policy_preflight.preflight` with `verdict` (`no_matches`, `review_suggested`, `high_matches`), `flags`, `counts_by_category`, `total_flags`, `locked`, the category rubric with a YouTube source URL per category, and `scope_statement`; plus a top-level `note`. On the free check, quoted passages and their rewrites can be locked while the counts are real: a locked result is not a clean pass. See `policy-categories.md` in the pre-flight skill.

## script_runtime

Pure arithmetic, free, no network. Inputs: one of `script_text`, `word_count`, or `target_minutes`. Uses Prepublish's measured speaking rates across 349 YouTube videos: 160 words per minute (25th percentile), 181 (median), 201 (75th percentile). Excludes pauses, B-roll and demonstrations, so a finished edit usually runs longer.

## Limits and errors

- Anonymous users: 3 free full audits per day, plus a daily free hook check; per-caller burst limits apply. A user with a Prepublish account connected through an API key is bounded by their plan instead.
- The tool error text tells you what to do. Follow it:
  - Email needed: ask the user for the address, explain what it is used for, then call again with the same input.
  - Allowance spent (429): do not retry. Tell the user they can run it at https://prepublish.ai/upload or try again tomorrow.
  - Could not be reached (502, 504, unreachable): usually a release rolling out. Wait about a minute and retry once with the same input.
  - Temporarily unavailable (503): tell the user and offer to try again shortly.
  - Needs a signed-in account (401, 403): explain the limit plainly. Do not retry.
- Never retry an AI-backed call in a loop. Never split one script into many calls to get around a limit.
