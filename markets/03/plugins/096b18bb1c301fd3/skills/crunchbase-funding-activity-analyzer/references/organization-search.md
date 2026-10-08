# Organization Search

Use organization searches for thesis landscapes, company screens, canonical profile links, and current-state monitoring.

## Structured screen

Resolve every predicate and order field through `cb_reference` on the current session. Candidate fields commonly include:

- `identifier`, `website_url`, `short_description`, `description`
- `categories`, `category_groups`, `location_identifiers`
- `funding_total`, `last_funding_at`, `last_funding_type`, `last_funding_total`
- `last_equity_funding_type`, `funding_stage`, `founded_on`
- `num_employees_enum`, `investor_identifiers`, `founder_identifiers`
- `status`, `operating_status`, `ipo_status`, `facet_ids`
- `last_key_employee_change_date`, `last_layoff_date`
- `rank_org`, `rank_delta_d30`, `rank_delta_d90`

For the demonstration mandate, use live-confirmed enum values corresponding to pre-seed, seed, and Series A; United States headquarters; total funding under $15M; operating status; private IPO status; and the company facet. Do not omit pre-seed from the stage predicate.

## Categories and text

Resolve every category on the current run. If no category matches the thesis precisely, use a broader resolved category plus a distinctive text predicate. Resolve the text field and operator before use.

When refining text:

1. Apply all structured mandate filters first.
2. Test one distinctive phrase per query so each phrase's effect is observable.
3. Union and deduplicate useful result sets.
4. Read descriptions before excluding a candidate.
5. Treat semantic relevance as analyst interpretation, not a hard automatic exclusion.

Record the resolved identifiers, filter values, broad count, refinements, and exclusions in the query audit.

## Current-state fields

Current status, employee band, and rank movement describe the returned record at query time. Do not describe an undated field as having changed unless a prior snapshot supplied in the task proves the difference.
