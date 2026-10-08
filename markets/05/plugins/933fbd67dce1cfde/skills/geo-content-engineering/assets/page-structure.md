# Page structure template

Skeleton for an LLM-optimized guide or pillar page with autonomous chunk blocks.

## Frame

```markdown
# [Core entity + core benefit as H1]

[Direct-answer paragraph: the page's core statement in two or three sentences,
with a date marker "As of MM/YYYY" and at least one concrete number.]

## What changed?
[Update box, see update-box.md]

## [Sub-question 1 as H2, in user language]
[Autonomous block: answer in the first sentence, then evidence.
Name the entity, no pronouns across block boundaries.]

## [Sub-question 2: comparison "X or Y?"]
[Real HTML table with named criteria.]

## [Sub-question 3: "When is each worth it?"]
[Condition block: if A, then X; if B, then Y. Criteria explicit.]

## Frequently asked questions about [core entity]
[FAQ block, see faq-block.md]

[Author box: name, credentials, role, profile link.]
```

## Usage rules

- Every H2 block must pass the self-containment test: pulled out of context, it
  still makes sense. See `../references/chunking.md`.
- Order the sub-questions by prompt demand of the cluster, not by the author's
  internal logic. See `../references/query-fan-out.md`.
- Technical sign-off (semantic tags, JSON-LD) before publishing. Criteria in
  `../references/semantic-html.md`.
