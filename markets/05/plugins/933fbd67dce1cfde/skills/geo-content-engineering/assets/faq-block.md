# FAQ block template

Structure for covering sub-queries at the end of a page, with a schema note.

## Frame

```markdown
## Frequently asked questions about [core entity]

### [Question in the exact phrasing a user would prompt]?
[Answer in at most three sentences. The first sentence answers fully.
Name the entity.]

### [Question about price or cost]?
[Concrete number or range with a date marker.]

### [Question about risks or common mistakes]?
[Concrete risk plus countermeasure.]
```

## Usage rules

- At least three, at most eight pairs; each pair covers a real sub-query of the
  cluster, no alibi questions.
- Derive the questions from the tracked prompt pool, do not invent them. See
  `../references/measurement.md`.
- Mark the block up as `FAQPage` in JSON-LD. See
  `../references/semantic-html.md` and `json-ld-snippets.md`.
