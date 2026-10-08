---
name: empire-cost-policy
description: Resolve and enforce Empire LLM economic boundaries before external-model routing. Use when a user asks for free-only or Absolute Zero models, prefers free or value routing, requests frontier models, sets a spending ceiling or target language, previews a route, asks why a model was chosen, or wants to prevent paid fallback.
---

# Empire Cost Policy

Keep Codex as lead. Resolve the user's economic boundary before invoking
`$empire-review`, `$empire-handoff`, `$empire-image`, or `$empire-video`; treat
the result as enforcement data, not as a model-ranking hint.

Resolve the Empire Review root as the sibling `../empire-review` directory and
run its `scripts/empire_router.py` commands.

## Interpret user intent

Map language precisely:

- `only` means `hard_lock`; never cross the selected lane.
- `prefer` means `prefer`; use that lane when eligible and allow disclosed fallback.
- `try first` means `try_first`; make one governed attempt before another lane.
- `free` or `Absolute Zero` means `free` / `absolute_zero`.
- `mid-tier` or `best value` means `value` / `value_paid`.
- `premium`, `best`, or `frontier` means `frontier` / `frontier_quality`.
- No explicit boundary means `auto` / `adaptive`.

OpenAI models remain excluded because Codex is already the OpenAI lead. Never
weaken privacy, evidence, modality, language, context, or budget gates to obtain
a route.

## Set or inspect policy

Save a default:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" mode set free \
  --selection-strength hard_lock
```

Inspect or reset it:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" mode status
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" mode reset
```

Treat a policy stated in the current conversation as request/session scope by
passing `--cost-mode`, `--selection-strength`, and `--language` to every Empire
operation in that session. Do not silently persist it as a user default unless
the user asks to save it.

Set a saved target locale only when requested:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" language set es-PR
```

If current catalog or benchmark data lacks language evidence, report it as
`unverified`; never invent a proficiency score.

## Inspect and preview

List a live lane:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" models \
  --cost-mode free --task review --language es-PR --refresh
```

Preview without dispatch or reservation:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" route \
  --repo "$PWD" --task "Review the current diff" \
  --cost-mode free --selection-strength hard_lock
```

Use `explain` with the same arguments for score dimensions, provider policy,
and alternatives. A preview must return `dispatch_performed: false` and must
not reserve budget.

## Enforce cost

- Free hard-lock requires a zero projected total and disables paid fallback.
- Count prompt, completion, fixed request, and every planned billable tool unit.
- Fail closed when a planned tool's price is unavailable.
- Distinguish explicit `:free` routes from `openrouter/free`; disclose that the
  generic router does not guarantee a served model.
- Show expected cost and reserved maximum separately.
- Use project budget commands for accumulated local enforcement:

```bash
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" budget set \
  --repo "$PWD" --limit-usd 1.00
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" budget status --repo "$PWD"
python3 "$EMPIRE_REVIEW_ROOT/scripts/empire_router.py" budget history --repo "$PWD"
```

When no model satisfies a hard lock, return Codex-only. Do not reinterpret a
decline as permission to spend.

For image and video generation, `free` remains the same Absolute Zero hard
lock. Paid media routes currently use `auto` plus approval of the exact route
and maximum cost. Do not translate `value` or `frontier` into an unsupported
media-quality ranking; explain that the media catalog does not yet provide the
evidence needed for those lanes. Pass the resolved free/auto mode to both media
preview and generation so the approval token cannot cross an economic lane.
