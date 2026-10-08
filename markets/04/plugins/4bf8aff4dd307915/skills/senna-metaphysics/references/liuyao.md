# LiuYao workflow

## Lock one question

Before calling `senna_liuyao_analyze`, reduce the request to one observable endpoint. Do not combine success, timing, price, health, motives, and multiple people into one reading.

Collect these five required context fields separately:

- `caster`: an alias or role for who cast or requested the reading, never a real name;
- `actual_subject`: an alias, role, or non-identifying object for who or what is actually being asked about, never a real person's name;
- `target`: the single concrete outcome or object;
- `stage`: the exact stage being judged;
- `time_range`: the bounded period.

Also collect a prospective `success_criterion` when the outcome can later be checked. It must state what counts as full success; progress alone must not be substituted for the stated endpoint.

Do not ask for or pass contact details, account credentials, government identifiers, payment data, medical records, exact addresses, or other sensitive personal data. Use only the minimum context needed to distinguish the question and stage.

## Casting

Pass exactly one supported method:

- six coin values in bottom-to-top order, each 6, 7, 8, or 9;
- exactly three user-provided numbers; or
- one Chinese character plus a user-confirmed positive stroke count.

Pass the actual casting time with its UTC offset. Do not generate random values, choose a character, or count disputed strokes without telling the user. Never alter casting data to obtain a different result.

## Interpretation rules

- Preserve the returned calendar, original/changed hexagram, lines, six relations, six spirits, shi/ying, yongshen, resolution status, and verdict.
- If yongshen is unresolved or confidence is low, say so directly. Do not promote a mechanical auspicious label to a reliable final conclusion.
- Keep stage judgments distinct. Report full success, partial success, failure, or not-comparable against the predeclared success criterion.
- Timing candidates are traditional windows, not appointments or guaranteed event dates.
- The Zhouyi text is an interpretive reference and must not overwrite the engine's primary rule layer.
- The anonymous public tool fixes `freeze_prediction=false`: do not claim that the prediction was stored, frozen, or submitted for engine training. Future outcome feedback belongs in the separate authenticated contribution workflow.

## Minimum answer shape

State the locked question and context, chart facts, selected yongshen and resolution status, traditional conclusion, counter-signals or uncertainty, timing only if returned, and the factual boundary.
