# Public Submission Checklist

## Package
- [x] Portable root `plugin.json`
- [x] Package name uses stable kebab-case: `job-outreach-copilot`
- [x] Semantic version: `0.1.0`
- [x] At least one valid skill under `skills/<name>/SKILL.md`
- [x] Skills-only architecture; no MCP server required
- [x] Square branding assets included
- [x] Starter prompts: 3 or fewer, each under current final-directory length limit
- [x] Display name and short description fit current final-directory limits

## Behavior
- [x] Generic across candidates
- [x] No hardcoded personal resume/rate/authorization/contact data
- [x] Evidence-first fit analysis
- [x] Strong / Partial / Weak fit
- [x] Proceed / Qualify first / Skip action
- [x] Recruiter-thread continuity
- [x] Platform-specific limits must be verified when relevant
- [x] No false claim that messages/applications were sent
- [x] Privacy/scam safeguards

## Testing
- [x] Five positive test cases prepared
- [x] Three negative test cases prepared
- [ ] Run all tests against the installed private plugin
- [ ] Confirm no unintended activation on unrelated prompts
- [ ] Confirm missing facts stay unknown rather than being invented

## Public submission account requirements
- [ ] Submitter has Apps Management write access in the publishing OpenAI Platform organization
- [ ] Developer or business identity is verified
- [ ] Publisher name matches the verified identity
- [ ] Final availability/regions selected
- [ ] Policy attestations completed
- [ ] Safety/security scan passes for the bundled skill

## Listing / URLs
For a skills-only ZIP, listing URLs can be optional in package validation, but confirm the portal's final requirements at submission time.

- [ ] Website URL, if used
- [ ] Support URL, if used/required
- [ ] Privacy policy URL, if used/required
- [ ] Terms URL, if used/required

Do not invent placeholder URLs in a public submission.

## Release
- [x] Initial release notes prepared
- [ ] Upload through **Create plugin → Skills only**
- [ ] Review imported metadata and skill files
- [ ] Submit for review
- [ ] After approval, choose Publish
