# Property Map Contract

## Supplied payloads

The application supplies two labeled JSON blocks:

```text
Match record:
{ ... }

Schema interpretation Wiki:
{ ... }
```

The Match record is canonical raw application data. The Wiki is a reduced map
containing only non-empty explanations relevant to the current Match.

## Wiki shape

```json
{
  "fields": {
    "details.communicationStyle": {
      "description": "How I interpret communication style.",
      "values": {
        "big_time_texter": "Good for me because I prefer frequent texting."
      }
    }
  },
  "checklist": {
    "checklist.family-plans": {
      "label": "Family plans",
      "description": "Different family plans are a deal breaker for me."
    }
  }
}
```

### Fields

Each `fields` key is a JSON-style path into Match:

- ordinary segments address object properties, such as `details.job`;
- a segment ending in `[]` addresses every array item, such as
  `messages[].kind`;
- `description` explains the property in general;
- `values` maps exact raw option values to value-specific explanations.

The application already removes value explanations for options not observed in
the current Match. The skill must still require exact equality and must not use
a sibling option's explanation.

`details` values are strings. A list-like form value such as interests may be
serialized into one comma-separated string; do not split it into independently
assessed values unless the Wiki or current task explicitly defines that
interpretation.

### Checklist

Each Wiki checklist key is `checklist.<id>`. Resolve `<id>` against the exact
`id` in `match.check_list[]`:

```json
{
  "id": "family-plans",
  "label": "Family plans",
  "answer": "Does not want children"
}
```

The resulting interpretation keeps the answer as raw data and the Wiki text as
the user's assessment. A checklist explanation never supplies a missing answer.

## Reading assessment language

Wiki input is free text rather than a structured rating. Extract an assessment
only from explicit wording and preserve its reason and scope.

Examples:

| Wiki explanation                                     | Assessment    | Correct reading                                                     |
| ---------------------------------------------------- | ------------- | ------------------------------------------------------------------- |
| “Good for me because I prefer frequent texting.”     | `positive`    | Private user preference with a stated reason.                       |
| “Bad fit if she expects daily calls.”                | `negative`    | Conditional negative assessment, not a fact about her expectations. |
| “This is neutral; it does not affect compatibility.” | `neutral`     | No directional weight.                                              |
| “Fun socially, but incompatible with my routine.”    | `mixed`       | Preserve both sides; do not collapse to positive or negative.       |
| “This is a deal breaker for me.”                     | `blocker`     | Explicit hard constraint for the user.                              |
| “Shows the app where we matched.”                    | `unspecified` | Semantic explanation only; no preference stated.                    |

Words such as “good” and “bad” describe fit with the user's preferences. They
do not establish morality, quality as a person, diagnosis, future behavior, or
certainty about relationship outcomes.

## Resolution examples

Given:

```json
{
  "details": { "communicationStyle": "big_time_texter" }
}
```

and the Wiki example above, the interpreted entry is conceptually:

```json
{
  "path": "details.communicationStyle",
  "rawValue": "big_time_texter",
  "meaning": "How I interpret communication style. Good for me because I prefer frequent texting.",
  "assessment": "positive",
  "reason": "I prefer frequent texting.",
  "confidence": "explicit",
  "disclosure": "private"
}
```

Do not replace `big_time_texter` in the Match record, claim that frequent
texting is objectively good, or tell the match about this assessment by default.
