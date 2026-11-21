# Roamdesk 2.0.1

Remote-work productivity planning by Karson Bailey.

## Architecture
Hybrid plugin: five planning skills, two support policies, and a remote stateless MCP service at https://roamdesk.karsonbailey.com/mcp. Tools: calculate_trip_budget, find_work_overlap, assess_work_readiness. No login, trip database, booking/payment actions or calendar access. Hosted tools use supplied inputs only. Read the public privacy policy before use. Local Python calculators remain a fallback when the host supports them.

## Deployment status
This package is prepared for the new MCP submission route. The service and four public pages are deployed. Production MCP tool calls and all public page routes passed direct HTTPS checks. Deployment is not OpenAI approval. Use a NEW plugin draft: OpenAI currently does not support adding MCP to an existing skills-only draft.

## Public URLs after deployment
Product: https://roamdesk.karsonbailey.com/
Support: https://roamdesk.karsonbailey.com/support
Privacy: https://roamdesk.karsonbailey.com/privacy
Terms: https://roamdesk.karsonbailey.com/terms
MCP: https://roamdesk.karsonbailey.com/mcp

Reviewer test cases are included in manifest metadata. A 48-second reviewer walkthrough at /reviewer-demo.mp4 replays the actual production test responses using fictional inputs. Domain verification has passed in the new Platform draft. No credentials are required for the public calculation tools.

The new package identifier is roamdesk-mcp so the portal creates a separate MCP-backed plugin rather than matching the old roamdesk skills-only draft. The display name remains Roamdesk.
