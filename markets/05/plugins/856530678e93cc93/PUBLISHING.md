# Publishing checklist

This repository is a local, validation-ready draft. It is not yet submitted or published.

## Before submission

1. Choose the verified individual or business identity that will publish the plugin.
2. Provide public website, support, privacy-policy, and terms URLs that match that identity.
3. Add a production-ready logo in the submission portal. This plugin has no UI, so screenshots are not needed.
4. Review the bundled skill and test cases for current policy and privacy requirements.
5. Decide the countries or regions where the publisher, support process, and legal terms are ready.
6. Prepare release notes describing this initial skills-only submission.

## OpenAI submission flow

Use the OpenAI Platform plugin submission portal, choose **Skills only**, upload the final skill bundle, add the listing metadata, and provide five positive and three negative test cases. Submit for review only after the publisher identity and legal URLs are ready. Approval starts a separate publication step; submission itself does not publish the plugin.

Official references:

- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/app-guidelines

## Local validation

From the plugin-creator skill directory:

```bash
python3 scripts/validate_plugin.py /Users/sheshnarayaniyer/plugins/visa-submission-flow
```

The local Codex marketplace entry is for testing only; it is not public publication.

