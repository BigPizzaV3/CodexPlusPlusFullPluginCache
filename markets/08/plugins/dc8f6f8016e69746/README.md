# Dentovio Exam Prep

Dentovio Exam Prep brings original dental exam practice and published educational
references into ChatGPT and compatible MCP clients. The existing public listing
is [Dentovio Exam Sources](https://chatgpt.com/plugins/plugin_asdk_app_6a98665d4cd8819190df181676ec6ac5).
Version 1.1.0 expands that same integration; package metadata publication follows
OpenAI review separately from deployment of the hosted endpoint.

## Capabilities

The anonymous, read-only server at `https://dentovio.com/mcp` exposes:

- `search` and `fetch`: source-backed public education, including complete
  publication-eligible guides and source links.
- `list_practice_exams`: available free tests and topic quizzes with actual counts.
- `get_practice_test`: questions and required case context without answer keys,
  plus an optional interactive MCP Apps practice view.
- `grade_practice_test`: deterministic answer feedback for the exact content
  version and submitted choices. Unanswered questions reveal no keys.

Practice covers California dentist, RDH and RDA; Florida dentist and hygienist;
North Carolina dentist; INBDE; NBDHE; and ADAT. It reuses the existing public
selection and topic quizzes rather than exposing the paid banks. The INBDE short
sample and existing longer public practice are both available. Clinical case
fields, approved figures, and essential shared tables remain attached.

No account, email, payment, paid entitlement, external model call, or persistent
attempt record is required. The MCP Apps interface works on mobile and desktop;
clients without UI can use the same structured tools conversationally.

## Content and privacy boundaries

Only already-published education that passes the applicable source or review
checks is served. Reserved assessment forms, unpublished CE, recalled questions,
patient data, personalized advice, commerce, and checkout remain excluded.
Florida practice uses its current publication-gated question selection; Florida
reference summaries remain excluded until their separate exact-body gate clears.
Practice results are educational feedback, not official scores, predictions,
credentials, or CE credit.

The server does not log tool arguments or emit application analytics. The
[privacy policy](https://dentovio.com/privacy) describes request handling and
hosting telemetry. See also the [terms](https://dentovio.com/terms) and
[methodology](https://dentovio.com/methodology).

## Verification

From `apps/web`:

```sh
npm run test:mcp
npm run test:mcp-ui
npm run verify:mcp
```

The runtime content flags must match the environment being checked. The
production verifier requires all nine currently public practice products.
The hosted contract is monitored by `.github/workflows/mcp-health.yml`.

The original launch record remains in `review/submission.md`; the version 1.1.0
update packet is `review/release-v1.1.0.md`.
