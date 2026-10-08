# Public Submission Checklist

## Build and local test
- [ ] Validate `plugin.json` syntax and package paths.
- [ ] Confirm `skills/technical-interview-copilot/SKILL.md` is discovered.
- [ ] Test direct activation and indirect activation.
- [ ] Test incomplete inputs that should trigger at most a small number of clarifying questions.
- [ ] Test unrelated requests that should not trigger the skill.
- [ ] Test evidence-first behavior so candidate experience and company interview details are never fabricated.

## OpenAI Platform prerequisites
- [ ] Use the OpenAI organization that will own the public plugin.
- [ ] Ensure the submitter has Apps Management write access.
- [ ] Complete individual or business identity verification for the publisher name.

## Submission portal
- [ ] Create plugin → choose **Skills only**.
- [ ] Add plugin name, descriptions, category, logo, and publisher information.
- [ ] Upload the final skill bundle.
- [ ] Add the three starter prompts.
- [ ] Add exactly five positive and three negative test cases.
- [ ] Select countries/regions where the plugin will be available.
- [ ] Add release notes for v0.1.0.
- [ ] Complete policy attestations.
- [ ] Submit for review.

## Before publishing after approval
- [ ] Re-test the approved build in a clean chat.
- [ ] Verify the public listing and publisher identity.
- [ ] Publish from the portal.

## Future v0.2+ ideas (only if actually needed)
- Persistent interview profiles or prep history through a purpose-built service.
- Custom question bank or assessment-provider integration.
- Controlled coding execution/evaluation service.
- Interview scheduling or job-tracker actions.

These future features would be candidates for MCP or connected apps; they are intentionally excluded from v0.1.0.
