# Standout plugin for ChatGPT

Lets people search Standout's startup job board from ChatGPT (and Codex) and
get introduced to founders. The plugin packages:

- **MCP server:** `https://standout.work/api/talent/mcp/public`, the same
  server as `https://standout.work/api/talent/mcp`
  (`app/api/talent/mcp/route.ts`), except that only `/public` serves
  anonymous callers; the main URL requires sign-in on connect. The app was registered at `/public` when it
  served job search alone, and the portal does not let an app change its MCP
  URL ("MCP URL must match the existing app"). Mixed auth:
  - `search_jobs` and `get_job` read the public job board and need no
    account.
  - The account tools need OAuth: `get_my_profile`, `list_my_matches` and
    `get_match_details` (scope `talent:read`), and the write tools (scope
    `talent:write`, approved on the consent screen): `approve_job_match`,
    `reject_job_match`, `update_my_preferences`, `update_my_background`,
    the talent agent's own tools listed in `lib/talent-mcp/agent-tools.ts`,
    and `reply_to_standout` as the last resort. Calling one anonymously
    answers 401 with the resource metadata, which starts ChatGPT's OAuth flow.
- **Skill:** `skills/find-startup-jobs/SKILL.md`.
- **Listing metadata:** `.codex-plugin/plugin.json` and `agents/openai.yaml`.

OpenAI's docs: https://developers.openai.com/plugins/

## Data minimization (OpenAI's "Minimal and purpose-driven inputs")

Rejected once, for inputs that were overly broad. The rules now enforced:

- A tool asks only for what its stated purpose needs. Preferences are search
  criteria matching reads; background is what matching and the sponsorship guard
  read. Nothing is collected "just in case".
- No field or instruction asks for chat history, transcripts, summaries of the
  conversation, or facts remembered from earlier conversations.
- No home location, current pay, citizenship or visa type. Preferred locations
  are where the job may be, at city level at most.
- Every string has a length limit and every list a size limit.
  `tests/talent-mcp/anonymous-protocol.test.ts` fails otherwise.

## Test in ChatGPT developer mode

1. ChatGPT → Settings → Security and login → enable **Developer mode**.
2. ChatGPT → Plugins → **+** and register the MCP server URL above.
3. To test the packaged skill too, copy the app id (`asdk_app_…`) from the
   browser URL into a local `.app.json` next to `.mcp.json`:
   ```json
   { "apps": { "standout": { "id": "asdk_app_…" } } }
   ```
   Add `"apps": "./.app.json"` to `.codex-plugin/plugin.json`, add the plugin
   to a local marketplace (`~/.agents/plugins/marketplace.json`), restart the
   desktop app and install it from the Plugins directory. **Do not commit or
   upload `.app.json`:** the portal rejects packages with app references.

## Submit

The review material lives in `.codex-plugin/plugin.json`
(`extensions.com.openai.review` holds the 5 positive and 3 negative test cases;
`publication.release_notes`). The portal imports it from the ZIP.

The portal asks for exactly 5 positive test cases. They use only the read
tools, which the test account can show every time; the write tools appear in
the demo video instead.

1. **Organization.** On platform.openai.com, complete business verification
   for the organization that will publish. The submitter must be an owner or
   hold **Apps Management Write**.
2. **ZIP.** From the repo root:
   ```bash
   (cd plugins/standout && zip -r ../../.context/standout-plugin.zip . -x '.app.json')
   ```
3. **Upload.** Plugins dashboard → Upload new or existing plugin → choose the
   developer identity → upload the ZIP. Fix anything the Issues panel flags.
   Only one review can run per plugin: cancel a pending one before uploading.
4. **Connect the MCP server.** MCPs → Connect → URL
   `https://standout.work/api/talent/mcp/public`, authentication **OAuth**. ChatGPT
   discovers the endpoints from the resource metadata and registers itself
   (dynamic client registration or a client ID metadata document), so there
   is no client id or secret to enter. Sign in with the reviewer test account
   (below) when the portal opens the consent screen.
5. **Domain verification.** Copy the challenge token into the Vercel env var
   `OPENAI_APPS_CHALLENGE_TOKEN` (Production), redeploy, check that
   `curl https://standout.work/.well-known/openai-apps-challenge` prints the
   token exactly, then confirm in the portal. Wait for the tool scan.
6. **Review details.** In Metadata & Skills → Review information → Review
   details, enter the reviewer access (below). Tick the policy attestations
   and submit. Review takes several business days.
7. **Publish** the approved version. Later MCP server changes need only a
   **Rescan**; skill or metadata changes need a new version and ZIP.

### Demo video (record against production)

OpenAI requires a reviewer-accessible recording URL for any plugin with an MCP
server ([submission docs](https://developers.openai.com/plugins/deploy/submission)):
"Demonstrate the test cases and plugin functionality." It has to be a real
screen recording of the plugin running in ChatGPT, not a mock-up, and it should
cover every surface the plugin supports. Recordings that only show the web app
are reported to be bounced, so include iOS and Android.

- **Where it goes.** `review.demo_recording_url` in `plugin.json`, since the
  ZIP manages review information. Don't also paste it in the dashboard. Host it as an unlisted YouTube video or a direct MP4
  link. Avoid Drive and Dropbox: permission-gated links get sent back.
- **Length.** OpenAI sets no limit; about two minutes once the waiting is cut
  out is plenty.
- **How.** Use a clean ChatGPT account with the plugin added and nothing else
  on screen. Expand each "Called tool" box so the tool name and arguments are
  visible. Keep the MCP URL (`https://standout.work/api/talent/mcp/public`)
  visible once, on the plugin's settings page. Record the account tools with
  the reviewer test account, including the connect flow: the sign-in screen,
  "App reviewer? Sign in with a test account", the consent screen and the
  return to ChatGPT.

Shot list, using the test cases in `plugin.json` (P = positive, N = negative;
unlabelled rows show the write tools, which have no test case):

| Surface             | Prompt                                                                                  | What has to be on screen                                                                   |
| ------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Web                 | Plugin settings                                                                         | The MCP URL and every tool                                                                 |
| Web                 | P1 Find remote backend engineering jobs at startups                                     | `search_jobs` with `query: "backend"` and `remote_only: true`, no sign-in asked            |
| Web                 | P3 …then tell me more about the first one                                               | `get_job` with the first result's id                                                       |
| Web                 | P2 Which startups sponsor visas for data roles?                                         | `search_jobs` with `query: "data"` and `sponsors_visa: true`                               |
| Web                 | P4 What does Standout know about what I'm looking for?                                  | The connect flow: sign-in screen, test-account link, consent screen; then `get_my_profile` |
| Web                 | P5 Show me my Standout matches                                                          | `list_my_matches`; the four pending demo matches                                           |
| Web                 | I'm now open to fully remote roles, and my base salary floor is $200k                   | `update_my_preferences` with only those fields; the saved preferences                      |
| Web                 | Find product roles in San Francisco, then ask Standout to introduce me to the first one | `approve_job_match` with the first id as `job_id`; the sandbox reply, no claim of an intro |
| Web                 | Tell Standout I just got an offer from another company                                  | `report_offer_received`; the offer recorded on the demo profile                            |
| Web                 | N1 Find me a job as an astronaut on Mars                                                | No results, nothing invented                                                               |
| Web (after search)  | N2 Apply to all of these jobs for me and send them my CV                                | Nothing applied or sent; an offer to ask for an intro to a role the user picks             |
| Web                 | N3 Show me Sarah Chen's Standout job matches                                            | No tool call for her; explains it only sees the connected account                          |
| iOS ChatGPT app     | P1, then P5                                                                             | The tool calls and results on a phone                                                      |
| Android ChatGPT app | Find product roles in San Francisco, then ask Standout to introduce me to the first one | The result on a phone                                                                      |

### Reviewer access

Standout sign-in is LinkedIn only, which reviewers cannot use (no MFA, email
codes or magic links allowed). They use a separate test-account door instead,
`/connect/test-account`, linked from the sign-in screen on the consent page
as "App reviewer? Sign in with a test account". It is described in
`lib/talent-mcp/reviewer.ts`:

- It can only ever authorize one seeded demo candidate, created by
  `npm run script -- scripts/seed-talent-mcp-reviewer.ts --apply`. That row
  is `name_only`, so it stays out of talent search, matching and every
  outbound path.
- The write tools answer the demo candidate without running a talent-agent
  turn, so a reviewer never reaches Standout's team or a company.
  `update_my_preferences` and `update_my_background` do save, to the demo
  candidate's own profile.
- It is off unless `TALENT_MCP_REVIEWER_LOGIN`,
  `TALENT_MCP_REVIEWER_PASSWORD` (20+ characters) and
  `TALENT_MCP_REVIEWER_USER_ID` are all set in Production.

Enter in the portal's review details, never in the ZIP:

```
Login: <TALENT_MCP_REVIEWER_LOGIN>
Password: <TALENT_MCP_REVIEWER_PASSWORD>
When ChatGPT opens Standout's sign-in screen, click "App reviewer? Sign in
with a test account" under the LinkedIn button, enter the login and password,
and press Connect. The test account is a sandbox: actions report that
nothing was sent to Standout's team or any company.
```

Rotate the password after the review.

### Privacy policy

The listing points at https://standout.work/privacy/ai-assistants, a page
dedicated to the plugin. It covers what OpenAI's guidelines require: the
categories of data, purposes, recipients, retention and user controls. Keep it
in step with what the tools in `lib/talent-mcp/` return; a new field returned
to the assistant means a new line on that page.

### Field limits

The portal enforces these on upload: `displayName` and `shortDescription`
(shown as the subtitle) at most 30 characters, `longDescription` at most 4000,
and each `defaultPrompt` at most 128 and unique.

### Category

The portal accepts only: Productivity, Creativity, Developer Tools, Business &
Operations, Data & Analytics, Communication, Education & Research, Security,
Finance, Healthcare, Travel, Entertainment, Other. None of them is job search,
so the listing uses `Business & Operations`, the closest fit for hiring and
recruiting. Both `Productivity` and `Other` came back as "couldn't confirm the
selected category".

## Open items

- **UI widget.** A job-card carousel served as an MCP resource
  (`text/html;profile=mcp-app`), linked from `search_jobs` through
  `_meta.ui.resourceUri`.
