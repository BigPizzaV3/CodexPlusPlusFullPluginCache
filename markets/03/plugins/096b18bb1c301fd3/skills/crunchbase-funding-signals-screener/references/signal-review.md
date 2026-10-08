# Workflow: Funding Signals Screening

Goal: identify recently announced rounds in the user's thesis areas, screen them against the stated mandate, and produce a review queue without turning screening signals into investment decisions.

## Procedure

1. Fix the as-of date and review window; when the user does not specify one, use the default defined in `SKILL.md`.
2. Record the user's screening mandate or the demonstration defaults from `SKILL.md`.
3. Resolve funding type, announcement date, organization location, category or text, total funding, and ordering fields through `cb_reference`.
4. Resolve the location and no more than three representative category identifiers per thesis area to current permalinks. Combine related identifiers or text terms in one live-supported predicate; do not fan out across category synonyms.
5. Run one `funding_rounds` query per thesis area so counts and refinements remain attributable. If it returns no records, allow at most one audited relaxation for that area.
6. Request round identifier, date, type, amount, funded organization identifier, organization description, organization total funding, and lead investors. Paginate when the user requests a complete review.
7. Screen rows against the mandate and record the reason for every exclusion.
8. Batch-search surviving organizations to obtain organization profile URLs and any additional screen fields.
9. Enrich only high-priority review candidates. Retrieve the organization with explicit fields and the `founders_lookup` card, then retrieve one or two relevant people with explicit job and education cards. One company call alone does not establish founder background.
10. Classify each survivor as `review now`, `watch`, or `outside stated screen`, using only the supplied mandate. If check size, ownership, or another decisive criterion is absent, state that the classification is a screening priority rather than an investment recommendation.

## Output

Group by thesis area:

| Company | Round (type, date) | Amount | Lead | What it does | Total raised | Review priority | Rationale |
|---|---|---:|---|---|---:|---|---|

Then include:

- **Review-now queue:** concise next steps tied to the mandate
- **Exclusions:** company and explicit screen criterion
- **Query audit:** as-of date, window, resolved identifiers, filters, and returned denominator
- **Source notes:** use `—` conventions from `output-contract.md`

Repeated lead investors are an observation to investigate, not proof of thesis momentum.
