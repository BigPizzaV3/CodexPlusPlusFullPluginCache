# Submission Test Cases

The canonical prompts, expected tools, and pass criteria are embedded in
`.codex-plugin/plugin.json` under
`extensions.com.openai.review.test_cases`. There are five positive and three
negative cases for the single Peerbound MCP server.

## Dataset

These cases target the Arcwell demo organization seeded by
[Peerbound PR #2036](https://github.com/peerbound/peerbound/pull/2036).
Arcwell and all customer relationships, contacts, quotes, reviews, and stories
are synthetic. Company names and domains are real but are not real endorsements.

## Positive Cases

1. Resolve Allbirds and Siemens Healthineers and check customer status and logo
   rights. Both are customers; only Allbirds grants logo rights.
2. Retrieve Maersk's approved quote with full attribution. Ingrid Solberg-Haas
   describes 31% fewer missed delivery windows year over year while volume grew.
3. Retrieve Siemens Healthineers' 4.5-star review by Piet Hanselmann. Preserve
   the implementation caveats: five months for the first region and six weeks
   per subsequent region.
4. Retrieve Grainger's full case study. Reliability improves from 91% to 97.5%
   across eleven distribution centers with roughly 19,000 hours saved annually.
5. Find up to two customers similar to Allbirds and recommend up to three proof
   points. One relevant customer is acceptable when only one match is available.
   Judge evidence and explanation rather than a fixed ranking.

## Negative Cases

1. Do not fabricate a Siemens Healthineers published case study when none exists.
2. Do not claim Maersk achieved an 80% reduction when evidence supports 31%.
3. Do not claim to delete Siemens Healthineers content or use feedback submission
   as a substitute for the unsupported deletion operation.

## Execution Status

These are expected results derived from source code, not recorded live passes.
Run all eight against the actual reviewer account before submission.
Complete seeding, story extraction, industry and location enrichment, the
employee-count materialized-view refresh, MCP enablement, and Pinecone sync first.
Use the seed command's printed follow-up steps for the target organization.

Synthetic public G2 and Arcwell story URLs may not resolve. Verify accessible
Peerbound source records or generated PDFs when demonstrating source retrieval.
Keep reviewer credentials out of this package and enter them in the secure
submission dashboard. Provide the video walkthrough separately when available.

## Source Map

In the Peerbound application repository:

- `backend/cli/synthetic_data/demo_org/accounts.py`: customer and logo-rights data.
- `backend/cli/synthetic_data/demo_org/interviews.py`: Maersk quotes and attribution.
- `backend/cli/synthetic_data/demo_org/reviews.py`: Siemens Healthineers review.
- `backend/cli/synthetic_data/demo_org/stories.py`: Grainger story and story inventory.
- `backend/cli/synthetic_data/demo_org/seed.py`: setup and extraction prerequisites.
- `backend/services/mcp_server/tools/`: MCP parameter and retrieval contracts.
