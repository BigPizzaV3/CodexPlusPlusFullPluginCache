# Infrastructure assessment

Require Screenata sign-in for plugin assessments. Call `screenata_whoami` and
name the connected workspace. If disconnected, guide the user through the
connector's sign-in flow and wait; new users create their account in the
browser. Do not collect signup details in chat or run CLI assessment signup.

When a terminal is available, confirm the CLI is authenticated with
`screenata auth whoami --json` before using it for assessment. If needed, run
`screenata auth login` and let the user complete browser sign-in. Check that
the CLI and connector refer to the same workspace; if they differ, ask which
workspace to use and reconnect the other before scanning or uploading.

Then run `screenata assess discover --json`, which lists identifiers, not
tokens. Ask which accounts support the product being assessed and which local
repository to use;
do not assume the active cloud account, first GitHub organization, or current
directory is the right scope. Use the user's choices as explicit flags:
`--providers=aws,azure,m365,gcp,github` (include only selected providers),
`--aws-profile=`, `--azure-subscription=`, `--m365-tenant=`,
`--gcp-account=` plus `--gcp-project=`, and `--org=` for GitHub.
GCP discovery first lists accounts; after selection run
`screenata assess discover gcp --gcp-account=<email> --json` for projects.
AWS profiles are configured choices, not proof that their sign-ins still work.
AWS connection checks verify the selected identity and `iam:GetAccountSummary`
before upload. Static keys need an SSO/assumed-role profile or an existing
MFA-authenticated temporary session; the CLI does not mint a non-MFA session.
If this preflight is skipped, present its recovery choice before trying another
account; do not report the provider as connected or repeat the same upload.
GitHub choices use the active gh user; Microsoft 365 uses tenants visible to az.
Ask for a local repository path or offer to skip it. Pass `--path=<local-repo>`
or `--skip-repo` so agent-driven runs never wait for a terminal prompt.

Signing in authorizes neither provider credential uploads nor repository
uploads. Obtain consent for the selected accounts and repository separately.

Explain that cloud execution remains on the server before requesting upload
consent. Then run `screenata assess run` with the explicit selections and, only
after consent, `--allow-server-scan --json`. Report coverage, inconclusive checks,
and repository findings separately from the cloud baseline percentage. If no
applicable cloud checks produced a pass/fail result, say the score is unavailable
and explain the inconclusive results instead of showing a percentage. Offer
one next gap to investigate. Ask factual questions when they affect the finding
(for example, whether an account is human or automation); those answers do not
authorize a fix. Show the proposed change, get approval, and verify it before
submitting evidence. Never infer audit readiness from a baseline pass rate.

If a provider cannot be assessed, ask how the user wants to recover; reporting
the error alone does not finish the interaction. Use the host's question UI
when available, with one recovery choice for the affected provider:

- **Missing or expired sign-in:** offer to sign in and retry, choose another
  account, or skip that provider. Use discovery's returned `signIn` instructions
  for the selected account. Keep authentication in the provider's own UI or
  terminal; do not ask for passwords, access keys, or MFA codes in chat.
- **Missing permission:** name the account and the exact denied action from
  the provider response. Ask whether to use another authorized read-only
  account/role, get instructions for an administrator to grant the missing
  access, or skip the provider. Do not grant permissions automatically or
  recommend administrator access as the default.
  If the user chooses administrator instructions, provide the confirmed denied
  action and selected identity. Distinguish a grant for that action from a
  complete scanner policy; passing this preflight does not prove every baseline
  check is accessible. Wait for the permission change before retrying.
- **Confirmed AWS temporary-session limitation:** explain that a non-MFA
  `GetSessionToken` session cannot call IAM. Offer an existing SSO/assumed-role
  profile or a locally established MFA-authenticated session; do not describe
  a successful local sign-in as logged out. Missing IAM permissions still need
  to be resolved even with a suitable session.

Wait for the recovery choice and any required sign-in or permission change,
then retry only that provider. Preserve the workspace, other successful
providers and selected repository; use `--skip-repo` if its upload already
succeeded. When switching accounts, verify the new identity and obtain upload
consent for that scope. Skipped or inaccessible checks remain unassessed, not
passed or failed. If the user skips cloud providers, offer the repository-only
assessment and keep its findings separate from the cloud score.

In a chat without a terminal, send the user to connect providers in the
Screenata portal. Never request or pass provider credentials in chat or MCP
arguments, and never run token-export commands whose output enters the
conversation. With a terminal, the signed-in CLI handles the approved upload
directly without printing credentials. Before connecting, explain that provider
baseline checks run on Screenata servers. Tokens retain their existing
permissions; the scanner only reads provider data. Explain the server access
deadline and vault cleanup; a GitHub token may remain valid at GitHub afterward.
Offer `screenata assess run --repo-only` to scan locally and upload repository
findings without provider credentials. Never pass `--allow-server-scan` on the
user's behalf without this approval; `--yes` does not authorize uploads.
