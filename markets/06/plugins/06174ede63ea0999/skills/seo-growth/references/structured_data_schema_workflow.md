# Structured Data and Schema Workflow

## Two different questions

1. Does Schema.org define a vocabulary/type?
2. Does a search engine currently support a search feature for that type?

These are not the same.

## Workflow

1. Identify the visible page content/entity.
2. Select the most accurate Schema.org type.
3. Check current Google Search supported structured-data features if Google visibility is the goal.
4. Add required properties.
5. Add recommended properties only when true.
6. Ensure markup matches visible content.
7. Validate JSON-LD/schema syntax.
8. Test with the relevant Rich Results Test where supported.
9. Use URL Inspection after deployment when useful.
10. Monitor Search Console enhancement/search-appearance reports.

## Never fabricate

Do not invent:
- ratings;
- review counts;
- prices;
- availability;
- dates;
- authors;
- FAQ answers;
- product identifiers;
- event details.

## Common useful types

Depending on actual page content:
- Organization;
- WebSite;
- Article;
- BreadcrumbList;
- Product;
- SoftwareApplication;
- LocalBusiness;
- VideoObject;
- ProfilePage;
- Dataset;
- Event.

Eligibility and requirements change; verify current search documentation.

## FAQ change

Google removed the FAQ rich-result feature from Search in May 2026.

Therefore:
- do not add `FAQPage` only to chase a Google FAQ rich result;
- FAQ content can still be useful to users;
- Schema.org semantics and other consumers are a separate question.

## Deployment

Roll out on a small representative page set first.

Monitor:
- parse errors;
- invalid items;
- valid item count;
- live URL output;
- template regressions.

A valid Rich Results Test does not guarantee a rich result will be shown.
