# Public Submission Checklist

Do not submit until local testing is complete.

## Package
- [ ] Root `plugin.json` validates against the Agent Plugins schema.
- [ ] Package name is stable and kebab-case.
- [ ] Version is valid semantic versioning.
- [ ] Skill is located under `skills/power-bi-report-builder-copilot/`.
- [ ] All referenced files exist.
- [ ] No secrets, credentials, tenant IDs, private URLs, or proprietary production samples are bundled.

## Listing
- [ ] Display name is 30 characters or fewer.
- [ ] Short description is 30 characters or fewer.
- [ ] Long description is 4,000 characters or fewer.
- [ ] Developer/publisher identity matches the verified OpenAI Platform identity.
- [ ] Final category is supported by the submission portal.
- [ ] Composer icon and logo are square, valid, and production-ready.
- [ ] Website/support/privacy/terms URLs are added if required for the final submission configuration.

## Starter prompts
- [ ] No more than three.
- [ ] Each is unique and 128 characters or fewer.
- [ ] Prompts demonstrate the highest-value workflows.

## Testing
- [ ] Five positive test cases pass.
- [ ] Three negative test cases pass.
- [ ] Test cases are reproducible without private/internal context.
- [ ] Plugin does not claim to execute Power BI/Fabric actions without a real connected tool.
- [ ] Plugin does not request credentials, tokens, or unredacted regulated data.
- [ ] Unrelated requests do not trigger the Power BI workflow.

## Power BI quality
- [ ] Report Builder path/terminology is accurate.
- [ ] Parameter guidance distinguishes report parameters from dataset/query parameters.
- [ ] Expressions use VB syntax and correct scope.
- [ ] PDF/Excel/print guidance is renderer-aware.
- [ ] DAX advice checks grain/filter context before rewriting measures.
- [ ] Architecture advice is requirements-driven, not DirectQuery/Direct Lake by default.
- [ ] Current Microsoft feature claims are verified against official documentation when needed.

## OpenAI submission account
- [ ] Submitter has Apps Management write access.
- [ ] Developer or business identity is verified.
- [ ] Availability regions are selected intentionally.
- [ ] Release notes are current.
- [ ] Policy attestations are reviewed only after final package testing.
