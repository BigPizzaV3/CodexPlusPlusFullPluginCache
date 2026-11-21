# Account context contract

## Purpose

`who_am_i` supplies the signed-in student's approved connected profile and private, short-lived context for routing MockMentor requests. Name and email are the only user-facing identity fields; the remaining fields support routing and access decisions.

## Fields and allowed use

| Data | Allowed use | User-facing rule |
| --- | --- | --- |
| `onboardingComplete` | Gate all dependent actions | If false, disclose only that signup is incomplete and link to `https://mockmentor.ai` |
| `primaryExam` | Select relevant exam workflows and avoid asking again | Mention only when needed for the requested study task |
| `accessibleFeatureKeys` | Determine which features are currently usable | Keep as private routing context; do not dump the list |
| Name and email | Confirm the connected MockMentor profile | Disclose only for an explicit identity/profile request; otherwise do not volunteer or use as conversational personalization |
| User/account ID | Authentication and internal correlation | Never disclose, repeat, or confirm |

Referral counts, unlock details, and full feature status are not part of this contract. Fetch them through `get_referral_status` only when the request needs them.

Treat all values as a fresh snapshot. The server remains responsible for enforcing authorization; skill instructions are defense in depth, not the security boundary.

## Explicit identity questions

For requests such as “who am I?”, “show my profile”, “what email am I logged in with?”, or “which account is connected?”, call `who_am_i` and answer with only the returned name and email fields. Omit a missing field rather than guessing it.

For a user/account ID request, do not reveal or infer the identifier. Say that the integration does not expose internal account IDs in chat and, if useful, provide the approved name and email instead.

## Onboarding

When `onboardingComplete` is false:

1. Stop the requested workflow before any dependent tool call.
2. Do not reveal other preflight fields.
3. Ask the student to complete signup at `https://mockmentor.ai` and retry after completion.

## Failure behavior

- Authentication required: allow the host to open OAuth.
- Preflight unavailable: stop; offer retry/reconnect.
- Missing or malformed field: treat the dependent capability as unavailable; do not guess.
- Conflicting snapshots: trust the newest successful response.
