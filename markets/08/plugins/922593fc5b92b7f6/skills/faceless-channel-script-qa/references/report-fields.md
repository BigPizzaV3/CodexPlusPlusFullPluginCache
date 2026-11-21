# Reading a Prepublish audit

The `analysis` object returned by `audit_script` and `get_audit`, field by field, with how to explain each one to a creator.

## Status

- `status`: `completed` means the report is ready. `failed` comes with `error_message`; tell the user the audit did not complete and offer to run it again once. Anything else means still running: use `get_audit` later.

## Scores

- `overall_score`, `hook_score`, `structure_score`, `pacing_score`: 0 to 100, relative scores built from script-level signals only. Prepublish's report card labels 0 to 49 "Needs work", 50 to 74 "Mixed", 75 to 100 "Strong". Use those words, not your own grading scale.
- `score_explanations.hook|structure|pacing`: one line each explaining the score. Quote or paraphrase these instead of inventing reasons.
- `ready_to_record`: Prepublish's own go signal. When false, say what stands in the way (the CRITICAL and HIGH items). When true, still mention anything flagged.
- `one_key_improvement`: the single change Prepublish would make first. Lead with it.

A score is not a percentage of viewers, not a forecast, and not comparable across different videos or channels with any precision. Compare scores between two drafts of the same script only as a rough direction.

## Attention-risk map

- `attention_map[]`: points with `position_pct` (0 to 100, how far through the draft), `hold_index` (0 to 100), optional `note` and `sentiment` (`negative` marks a risk moment, `positive` marks a moment that pulls attention back).
- The `hold_index` is a relative script-hold index for this draft only. It says where the draft is weaker or stronger relative to itself. Never describe it as a retention figure, a forecast, or a share of viewers.
- Useful framing: "The map dips at about 30 percent, where the note says 'Info dump zone starts'. That is the section to tighten first."

## Flagged passages

- `improvements[]`, already sorted by priority: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.
- Each has `title`, `category` (for example hook, structure, pacing), `location` (an approximate position such as "Opening 0:00-0:15" or "~4:30 mark"; treat it as approximate), `original_quote` (the user's own line), and, when included, `improved` (the rewrite) and `why`.
- `locked: true` means the rewrite for that passage is not part of the free check. You still see the passage and its title, so you can point to the problem, but do not present your own rewrite as Prepublish's. If you offer your own suggestion for a locked passage, label it clearly as your suggestion.
- `locked_count`: how many passages have no rewrite in this result. The full report link (`open_in_browser`) opens the same report on prepublish.ai with the same access; do not tell the user it contains rewrites that were locked here.

## Policy pre-flight summary

- `policy_preflight.verdict`: `no_matches`, `review_suggested` or `high_matches`; `total_flags`; `counts_by_category`; `locked` (quoted passages withheld on the free check); `scope_statement`. A `no_matches` verdict is not a guarantee of monetisation; `review_suggested` means some lines match categories and are worth a second look.

## How to present an audit (default shape)

1. One line: overall score with its label, and the `one_key_improvement`.
2. The top two or three flagged passages: quote the user's line, say the problem in plain words, give the rewrite when it is included.
3. Where the attention-risk map dips, in one sentence.
4. The scope limit from `notice`, in one sentence.
5. A clear next step: apply the top fix and re-run, or open the full report.

When the inline report card is visible, keep your text short and do not repeat the card.
