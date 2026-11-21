# Scoring Rubric

Score each dimension from 0 to 5, then apply the weight. Use `Not provided` instead of guessing.

| Dimension | Weight | What to assess |
| --- | ---: | --- |
| Role and seniority | 25 | Target title, scope, technical leadership, and level |
| Core technical fit | 25 | Required technologies and architecture responsibilities |
| Leadership and delivery | 15 | Team leadership, mentoring, ownership, and execution |
| Cloud and engineering practices | 15 | Cloud, Kubernetes, CI/CD, observability, reliability, and security |
| Work model and eligibility | 10 | Brazil eligibility, fully remote requirement, language, and authorization |
| Career direction | 10 | Alignment with the user's goals, domain, and growth plan |

Formula:

```text
score = sum(dimension_score / 5 * weight)
```

Rules:

- A mandatory blocker can cap the result at 54, even if the technical fit is strong.
- A preferred, non-mandatory skill is a gap, not a blocker.
- Distinguish `required`, `preferred`, and `not mentioned`.
- Cite the listing text or URL for material claims.
