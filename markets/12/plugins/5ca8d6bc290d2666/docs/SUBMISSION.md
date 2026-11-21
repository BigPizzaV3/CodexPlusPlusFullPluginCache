# Public OpenAI submission

## Current status

This repository contains an OpenAI plugin package with 21 skills, one Global
MCP connection, publisher assets and five positive plus three negative review
cases. The available documented operations are listed in [TOOLS.md](TOOLS.md).
The package uses the available block-height operation and has 66 verified tool
bindings.

This does not establish a submitted or approved public listing. Review cases
have been drafted, but their execution on a dedicated reviewer account has
not been verified. A real demo recording URL, publication countries and the
publisher's commerce declaration still need to be supplied or confirmed.

## Demo recording: required for this plugin

As checked on **2026-10-14**, OpenAI marks `review.demo_recording_url` as
optional when uploading a ZIP and required for MCP review. A skills-only
plugin has different requirements; this package includes a remote MCP server.
See [OpenAI's submission documentation](https://developers.openai.com/plugins/deploy/submission#configure-onboarding-review-and-publication).

Provide a real recording URL accessible to reviewers. A written script,
screenshots or an invented URL do not complete this requirement. The current
package does not claim to contain a completed recording.

## What to record

Use the version being submitted in ChatGPT or Codex, with an authorized
dedicated test account. Rehearse the review prompts before recording.

1. Show the plugin name, the working Global connection and successful sign-in.
   Keep credentials and tokens outside the recording.
2. Ask to resolve BTC and ETH and retrieve their latest available USD prices.
   Show canonical assets, sources and data timestamps.
3. Ask for a Bitcoin reference-data profile and available classifications.
4. For the approved review address, show a balance, a small transaction preview
   and a light AML scoring report.
5. Show a news digest and prediction-market results with their venues.
6. Show a boundary example, such as an unsupported transfer request, and the
   explanation that the plugin cannot perform it.

Capture real prompts, tool interactions and results, with enough time to read
them. Check the saved video's playback, readability and access permissions.
Then supply the verified URL through `review.demo_recording_url` in
[plugin.json](../plugin.json), or the review-information form when that field
is managed there. Do not overwrite a dashboard value with a placeholder.

## Review cases and account

The five positive and three negative cases are under
`extensions.com.openai.review.test_cases` in [plugin.json](../plugin.json).
Run each case and record the actual tool calls, results and outcome.
Live prices and scores must agree with returned data; no fixed price or block
height is assumed.

Prepare a reviewer account with the entitlements and sample data needed for
all cases. Reviewers must be able to sign in without access to your private
network, mailbox or phone. Supply credentials and login instructions only
through the secure submission dashboard, outside GitHub and the public ZIP.

## Publisher and publication details

Confirm the intended verified Lukka publisher identity, supported countries,
commerce behavior and policy coverage. Existing listing values are:

| Field | Value |
|---|---|
| Display name | Lukka Digital Assets Intel |
| Category | Finance |
| Website | [lukka.tech/plugin](https://lukka.tech/plugin/) |
| Support | [Contact Lukka](https://lukka.tech/contact-us/) |
| Support email | [plugin-support@lukka.global](mailto:plugin-support@lukka.global) |
| Privacy | [Privacy policy](https://lukka.tech/privacy-policy/) |
| Terms | [Terms of use](https://lukka.tech/terms-of-use/) |

The website currently describes the Claude edition. Its owner should include
the OpenAI edition and confirm that the published policies cover this use.

## ZIP and final portal setup

A public upload ZIP has [plugin.json](../plugin.json) and [mcp.json](../mcp.json)
at the archive root, alongside `skills/`, `assets/` and documentation. Do not
wrap the upload contents in an extra repository directory. Exclude `.git`,
private catalogs, local authentication settings, credentials and build caches.

Once preparation is complete, use the verified organization in OpenAI Platform
to upload the package, connect Global, verify the domain, run the required
scans and test the saved version. Complete the dashboard's required declarations
before selecting **Submit for review**. Uploading a draft and publishing an
approved plugin are separate actions.

The portal supplies the domain challenge value for
`https://global.mcp.lukka.tech/.well-known/openai-apps-challenge`. The service
owner must expose that exact value. Local package preparation does not perform
domain verification or change the hosted server.

Follow the [current official submission guide](https://developers.openai.com/plugins/deploy/submission)
and any additional requirements shown for the saved submission. Package
validation cannot guarantee acceptance.
