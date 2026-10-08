# Marketplace Submission Draft

## Listing

- Plugin display name: Institutional Equity Analyst
- Short description: Institutional equity research
- Suggested long description: Use a comprehensive institutional equity-research operating system to investigate public companies from primary sources through accounting reconstruction, industry and competitive analysis, driver-based forecasting, valuation, risk, falsification, and investment-memo construction. The plugin includes specialized workflows plus 36 sector playbooks. Deep workflows maintain a concise decision layer and a complete evidence layer so assumptions, calculations, sources, contrary evidence, and completion gates remain reproducible.
- Category: Finance
- Website, support, privacy, and terms URLs: optional for the current skills-only ZIP submission path; add public HTTPS URLs if you want them shown or if portal requirements change.
- Logo: TODO - supply marketplace-compliant original logo asset.
- Developer identity: TODO - submit from the OpenAI organization/project containing the verified publisher identity.

## Architecture submitted

Skills-only V1. No remote MCP server is required. The plugin uses existing model tools plus bundled skills, references, deterministic scripts, and templates. A future MCP version can add controlled market and filing data APIs without changing the research methodology.

## Required reviewer materials included

- Starter prompts: `starter-prompts.json`
- Positive tests: `tests/positive-tests.json`
- Negative tests: `tests/negative-tests.json`
- Release notes: `RELEASE_NOTES.md`
- Use-case inventory: `USE_CASE_INVENTORY.md`
- Package integrity report: `../INTEGRITY_REPORT.md`

## Pre-submission checklist

1. Add an original logo if the live submission form requires or benefits from one.
2. Optionally add public HTTPS website/support/privacy/terms URLs for the skills-only listing.
3. Run `python developer-tools/integrity_check.py` from the plugin root.
4. Run the bundled unit tests.
5. Install the plugin in a local/personal marketplace and test all starter prompts in fresh conversations.
6. Verify every Skill triggers correctly and does not over-trigger on unrelated requests.
7. Submit at least five positive and three negative test cases. This package includes more than the minimum.
8. Confirm publisher identity and desired country/region availability in the portal.
9. Review financial-services disclosures and marketplace policy requirements current on the submission date.
