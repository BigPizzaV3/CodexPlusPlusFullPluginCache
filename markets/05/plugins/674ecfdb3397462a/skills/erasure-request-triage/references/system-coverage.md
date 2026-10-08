# Source Coverage Model

## Purpose

Show what evidence or connected sources were and were not reviewed without implying organisation-wide coverage.

## Statuses

Use one status for each source actually identified:

- `REVIEWED` - authorised read-only material was reviewed;
- `SEARCHED` - an authorised connected-source search was performed;
- `NOT_SEARCHED` - source identified but not reviewed;
- `AWAITING_ACCESS` - requested source is unavailable or partially authorised;
- `OUT_OF_SCOPE_WITH_REASON` - operator explicitly excludes the source;
- `NO_MATCHES_IN_SEARCHED_SCOPE` - no match found in the searched scope; or
- `REVIEW_COMPLETE` - read-only review entry is complete.

Emit the applicable source value exactly in a dedicated `source_status` field. Source coverage values are separate from `case_status` and must not be combined with trust or record-recommendation values. When an authorised completed search returns no matches, use `source_status: NO_MATCHES_IN_SEARCHED_SCOPE`; when it is the overall case outcome, also emit `case_status: NO_MATCHES_IN_SEARCHED_SCOPE`. Do not replace the token with a prose synonym.

## Portable V1 rule

The Skill must remain useful with pasted or uploaded authorised evidence and must not require Gmail or Google Drive.

When a connector is available and used, record its actual scope and limitations. When it is unavailable, do not imply it was searched.

Do not invoke a connector until verification, applicable authority, request-validity, and operator-authorised source-scope gates pass. Do not use a connector to reconstruct a case from a destructive-action request without case context.

## Coverage limitations

Always make clear that reviewed records or a single connected source do not establish organisation-wide completion and do not cover unreviewed systems, processors, recipients, copies, versions, or backups.

`CASE_PLAN_READY`, `RECORD_REVIEW_COMPLETE`, `REVIEW_COMPLETE`, and `NO_MATCHES_IN_SEARCHED_SCOPE` never certify erasure completion and never instruct the operator to mark the organisation-wide case complete.
