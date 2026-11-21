# Search Console tool annotation justifications

These values describe the existing hosted MCP implementation. They are not
manifest overrides: OpenAI must connect to and scan the MCP server to import
the current tool definitions. All four hints below are explicit booleans.

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| `list_metrics_and_breakdowns_search_console` | `true` | `false` | `true` | `false` |
| `list_workspace` | `false` | `false` | `true` | `true` |
| `retrieve_reporting_data` | `false` | `false` | `false` | `true` |
| `preview_and_retrieve_reporting_data` | `false` | `false` | `false` | `true` |
| `set_reporting_mode` (component only) | `false` | `false` | `true` | `false` |

## Why each tool uses these values

- **Metric and breakdown discovery:** Reads Adzviser's fixed Search Console
  field catalog. It changes no user state, deletes nothing, and repeated calls
  have no additional effects. It does not query external Search Console accounts
  or an open-ended collection of resources.
- **Workspace discovery:** Returns the user's connected Search Console
  workspaces. Account resolution can clear a stale saved account preference,
  so it is not strictly read-only. Listing does not delete workspaces or source
  data. Repeating the same stale-preference cleanup has no additional effect.
  External-account interaction is marked open-world under the submission-review
  definition recorded for this integration.
- **Data retrieval:** Reads Search Console reports and persists usage
  counters/flags in Adzviser, so it is not strictly read-only. Repeated retrievals
  can record additional usage, making the operation non-idempotent. It does not
  delete or overwrite source data. It interacts with the connected external
  Search Console account and is marked open-world.
- **Interactive preview:** Opens the report component. Its supported
  compatibility paths can save preferences or execute retrieval and record
  usage; the annotation covers those paths as well as opening a preview.
  It is therefore a non-idempotent write, is non-destructive, and can interact
  with the external Search Console account.
- **Reporting-mode preference:** Saves `ui` or `data` for the authenticated
  private MCP session. This is a non-destructive write; setting the same value
  again is idempotent. It does not interact with external accounts or publish
  data, so it is closed-world. Only the interactive component can invoke it.

## Verification limits

On 2026-09-30, 113 existing Search Console connector tests passed with external
account calls mocked. The public endpoint reported build
`a10c7eac-20260929204856`, matching the repository's 2026-09-29 deployment record.
This package preparation did not access authenticated production `tools/list`,
run reports against the reviewer account, or inspect the portal's saved scan.

## New submission setup

This package declares the Search Console MCP server in `.mcp.json`. Its package
name is `adzviser-search-console`; the user-facing name is Adzviser Search Console.
The MCP-enabled draft has now been created. Upload this updated ZIP to that
existing `adzviser-search-console` draft; its MCP declaration is unchanged.
The earlier skills-only entry cannot accept an added MCP server.

After upload, open MCPs, select Search Console, and complete Connect with OAuth
and the portal's domain-verification challenge. The server endpoint is
`https://search-console.mcp.adzviser.com/widgets/http`. Wait for tool discovery
and compare the imported annotations with the table above.

The manifest includes five positive and three negative review cases using the
Demo workspace. The publisher confirmed that the intended reviewer login has
access to that same workspace. Actual sign-in with those reviewer credentials
has not been exercised here.

On 2026-09-30, live tools on the installed **Adzviser Search Console Test**
connection returned the following results. These were direct tool calls,
not isolated ChatGPT runs of the submitted prompts and not the new portal draft.

| Case | Verification completed | Still unverified |
| --- | --- | --- |
| Monthly totals/rates | Live August 2026 request returned all four requested metrics | Fresh-conversation prompt and answer behavior |
| Month comparison | Live August/July 2026 request returned both periods; August counts matched the totals request | Fresh-conversation prompt and answer behavior |
| Top queries | Live August 2026 request returned 4,815 query rows with numeric clicks, impressions, and position; rows could be ranked | Fresh-conversation prompt and answer behavior |
| Daily trend | Live August 2026 request returned all 31 dates; daily click/impression sums matched monthly totals | Fresh-conversation prompt and answer behavior |
| Interactive landing pages | Underlying live data request returned 1,022 landing-page rows | Preview mounting, visual rendering, and the actual Run-button interaction |
| Three negative prompts | Requested deletion and website editing are outside this tool catalog; source isolation has local test coverage | Actual model refusal/routing behavior in fresh conversations |

The 113 existing Search Console connector/profile and UI integration tests were
rerun and passed. They use mocked authentication, backend report data, and widget
loading; they do not verify the production iframe or reviewer-account sign-in.

A data-quality limitation was found: the backend rounds fractional CTR to two
decimal places before returning it. The monthly case now requires disclosing
that rounding or explicitly calculating a more precise ratio from clicks and
impressions. The backend implementation was not changed during this audit.

Run all eight submitted prompts with the intended reviewer login against the
new MCP-enabled draft before treating the complete review suite as passed.

The supplied demo recording is included as `review.demo_recording_url`:
https://youtu.be/dmRHECWu9c8

An anonymous YouTube metadata check returned HTTP 200 and player status `OK`
for “Adzviser Search Console  ChatGPT Plugin Demo” by Adzviser, with duration
157 seconds and `isPrivate: false`. The recording's visual quality and coverage
of every review case have not been independently watched or verified here.

Before review, run the cases in the intended host using the dedicated reviewer
account and confirm that the recording demonstrates the submitted behavior.
Supply reviewer credentials only through the portal. The publisher selected
all supported countries, recorded as `publication.countries: []`. Subscriptions
are purchased separately on the Adzviser website; the plugin does not provide
checkout or payment processing, recorded as `review.commerce: false` with an
explanation in `review.commerce_description`. Translations are optional.
Check the imported review details, any required UI screenshots, and publisher
verification in the existing draft. The deleted listing's saved reviewer access
details are not included in this package.

References: [submission setup](https://developers.openai.com/plugins/deploy/submission#create-the-draft)
and [MCP connection](https://developers.openai.com/plugins/deploy/submission#connect-and-scan-your-mcp-server).
