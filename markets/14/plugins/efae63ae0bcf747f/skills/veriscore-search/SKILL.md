---
name: veriscore-search
description: Use Veriscore MCP to search candidates, candidate tests, jobs and extra work, and guide users through advertising and candidate contact.
---

Use the Veriscore MCP server when the user asks about Veriscore.

Supported, production-tested VER-329 tools:
- `search_candidates`: Search publicly discoverable candidates by skill or other supported filters.
- `get_candidate_tests`: Retrieve eligible candidate's publicly visible completed tests.
- `find_jobs`: Search available job listings.
- `find_extra_work`: Search available extra/direct work.
- `advertise_on_veriscore`: Explain or initiate the advertising workflow according to the server's actual capabilities.
- `contact_candidate`: Follow the existing candidate-contact handoff/authorization flow.

Use only parameters exposed by the current server tool schemas; never invent parameter names or extra MCP tools. Public searches may work without login. For protected features, use the server's OAuth authentication and enforce the current user's Veriscore account permissions. Never expose private contact details, bypass an access check, fabricate results, or claim an advertisement or contact was submitted unless the server confirms that action. Ask for confirmation before any consequential write. Follow returned URLs where appropriate. Respond in the user's language.

Competency test catalogue search may be described as a Veriscore site feature; do not claim it is a dedicated MCP tool unless the connected server exposes one.
