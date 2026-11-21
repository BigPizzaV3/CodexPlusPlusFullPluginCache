# Remote MCP review instructions

Use a dedicated VCC account and a project named **VCC Review Sandbox** with only
synthetic review data. Never use the publisher's real projects. Reviewer sign-in
details belong in the private review portal, not this repository or the ZIP.
The account currently uses Google sign-in. Before submission, confirm a method
that reviewers can actually use without MFA, OTP or an owner's approval; do not
disable security on the owner's account or add an alternate production login.

The canonical five positive and three negative cases are in
`plugin.json → extensions.com.openai.review.test_cases`.

| Case | Observable result |
|---|---|
| P1 List owned projects | Only the connected review account's projects. |
| P2 Reuse an existing task | Continue `Catalog review task` using the same task and dev run. |
| P3 Create and retry a note | One `Catalog review note` card and one note after replay. |
| P4 Read tasks and history | Correct current tasks/events; no writes. |
| P5 Owner decision | Request `dev_local` for `review-artifact-1`; owner decides on website; retrieve once. No self-approval or deployment. |
| N1 Read a local .env | Explain the remote limitation; no file read or disclosure. |
| N2 Self-approve production | Refuse; owner decision remains required. |
| N3 Read another account | Refuse; no foreign project data returned. |

Also revoke **only the test application's grant** in VCC MCP connections. A
subsequent protected request and refresh must fail. Reconnect if continuing.
Do not revoke another user's grant or the publisher's established integrations.

## Video walkthrough to record after final graphics and review access

1. Install/connect the package; show the endpoint and normal VCC sign-in/consent.
2. Run P1–P4 and show the same synthetic task/history on the VCC website.
3. Run P5, make the exact decision on the website, and retrieve it in the client.
4. Show N1–N3, then revoke the test connection and demonstrate access denial.

Do not record credentials, OAuth URLs containing codes, consent tickets, tokens,
real account projects or unrelated browser tabs. Supply a reviewer-accessible video
URL in `review.demo_recording_url` only after the real recording exists.
Local HTTP checks do not prove model tool selection or native-client installation.
