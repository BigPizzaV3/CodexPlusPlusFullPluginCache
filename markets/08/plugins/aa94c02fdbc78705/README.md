# AISEO Plagiarism Checker

This package connects to AISEO's dedicated plagiarism checker.

- MCP URL: https://mcp.aiseo.ai/plagiarism-checker/mcp
- Tool: `check_plagiarism`
- Input: a passage containing 40 to 10,000 words.
- Access: sign in to an AISEO account through OAuth.
- Output: plagiarism and uniqueness scores, matching sources, and matched sentences.

The public server documentation describes these capabilities.
An unauthenticated initialization returned HTTP 401 on October 1, 2026.
Authenticated tool execution and the included review cases still need testing.

## Upload

Update the existing Plagiarism Checker listing through https://platform.openai.com/plugins.
Upload `aiseo-plagiarism-checker-1.0.1.zip` with the verified AE-Intelligence developer identity.
Complete OAuth and the tool scan.

This package uses the existing listing identity: `app-6aa9659970e48191af4c270fe06832c4`.
Its source folder matches that identity.
Do not upload this archive as a new AISEO AI Visibility version.

The existing listing shows a verified domain.
Keep the existing domain challenge token intact.

Enter dedicated reviewer credentials through the secure portal.
Keep credentials outside this archive.
The manifest includes five positive and three negative proposed review cases.
Run them through an authenticated client before submission.
The existing draft contains a video URL.
Verify that reviewers can open it and that it demonstrates the submitted cases.

The public privacy policy must describe text processing, recipients, retention timelines, and user controls.
Privacy-policy PR #346 still needs confirmed retention timelines before publication.

## Interpreting results

Treat scores as similarity indicators.
Review matched passages and sources before drawing conclusions.
A missing or failed result does not mean zero plagiarism.
Do not promise exhaustive source coverage or guaranteed originality.

## Sources

- https://mcp.aiseo.ai/docs
- https://developers.openai.com/plugins/deploy/app-review
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/plugin-guidelines
