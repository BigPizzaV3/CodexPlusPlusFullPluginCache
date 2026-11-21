# Veriscore ChatGPT plugin 1.0.11 (VER-298)

Public review ZIP, based cumulatively on 1.0.9 and the verified VER-329 MCP capabilities.

MCP endpoint: https://veriscore.se/api/veriscore/mcp

Tools: search_candidates, get_candidate_tests, find_jobs, find_extra_work, advertise_on_veriscore, contact_candidate.

Includes 5 positive and 3 negative review cases under `extensions.com.openai.review.test_cases` and in `tests/prompts.json`.

Retained: OAuth settings, original Veriscore logo/icons, author, support/privacy/terms links.
No Drupal changes. No changed Drupal/composer versions.

WARNING: A ZIP with MCP configuration may be treated as desktop-only on plugin install. Public listing and MCP review eligibility depend on the OpenAI platform workflow and cannot be guaranteed by this ZIP alone. Inspect the MCPs section after upload and confirm server connection; do not submit if `No MCPs connected` is shown.

Three listing prompts cover all six tools. Five positive and three negative review tests remain separate and unchanged.
