> Submission preparation copy, 30 October 2026. Publisher: Codemore PLT. Availability: all available countries. Commerce: ShipPDF subscriptions and document credits, with Stripe checkout outside ChatGPT/Codex. Light and dark PNG branding and the supplied YouTube demo URL are included. Reviewer account/workspace and recording exist; the publisher confirms all eight review cases passed. Independent portal verification and publication of the updated privacy page remain pending. This ZIP has not been uploaded or submitted.

# ShipPDF for Codex and ChatGPT

Create reusable PDF templates, edit drafts, publish revisions, and generate PDFs
in your ShipPDF workspace. This portable Agent Plugins package includes three
skills and ShipPDF's hosted OAuth-enabled MCP connection.

## Install locally in Codex

From this plugin directory:

```sh
codex plugin marketplace add .
codex plugin add shippdf@shippdf
```

Restart your session, enable the plugin if needed, and authenticate ShipPDF using
the client's MCP connection controls. Sign in to ShipPDF and select a workspace.
No API keys belong in the plugin or in chat.

In supported ChatGPT desktop sessions, the marketplace can also appear as a
local source in the Plugins Directory. The catalog is
`.agents/plugins/marketplace.json`, with its plugin source pointing at this
directory. Local-source availability varies by client.

## ChatGPT connection and testing

Register `https://mcp.shippdf.com/` in ChatGPT developer mode as an OAuth-enabled
MCP connection, then install and authenticate it through the Plugins Directory.
Use a new Work chat to test the connection. The package's `mcp.json` declares the
same server for portable distribution.

For local testing that combines these skills with an already registered ChatGPT
connection, supply its assigned `plugin_asdk_app...` technical ID to Plugin
Creator. That workflow maps the assigned ID through `.app.json` and the OpenAI
manifest extension. This package does not invent or embed a registered ID.
Keep registered-app mappings in a separate local testing copy: ZIPs with
`apps`/`.app.json` references cannot currently be submitted publicly.

## Skills

| Skill | Example |
| --- | --- |
| `$shippdf-create-template` | Create an A4 invoice template with line items and a calculated total. |
| `$shippdf-edit-template` | Update template tmpl_… with our branding and leave it as a draft. |
| `$shippdf-generate-document` | Generate a PDF using template tmpl_… and this data. |

You can also ask naturally. The skills follow the server's live authoring guide,
preserve concurrent draft edits and reviewed publishes through lock versions,
and reuse idempotency keys when recovering uncertain generation requests. Each
generated PDF costs one ShipPDF credit; draft browser previews are free and do
not verify PDF pagination.

The selected workspace and OAuth scopes control tool access. Discovery uses
`projects:read` and `templates:read`; authoring uses `templates:write`; generation
and polling use `documents:create` and `documents:read`. Supported workflows
include public-URL image import, image-byte upload into an existing template
(base64 content, up to 5 MB decoded), and individual generation. Image uploads
require the client to access the bytes; passing a local path does not upload it.
Batch generation and webhook setup are not exposed by these MCP tools.

Global preset management is operator-only and requires an explicit
`presets:manage` permission in addition to current operator status. A `*` key
grants workspace permissions and does not include global presets. Operators can
create a separate API key with the global preset permission selected, or use an
OAuth client that explicitly requests it. Existing keys and OAuth connections
without that scope cannot manage presets. The public plugin requests only the
five workspace scopes above by default.

## Package

```sh
python3 scripts/package_plugin.py
```

The ZIP is written to `dist/shippdf-openai-plugin-0.1.1.zip`. It includes root
`plugin.json`, `mcp.json`, assets, and skills with their UI metadata. Marketplace
configuration and developer scripts stay outside the upload archive.

For public distribution, upload the ZIP through OpenAI's plugin submission
portal, configure OAuth, and complete review. The listing links the published
[support](https://shippdf.com/support/), [privacy](https://shippdf.com/privacy/),
and [terms](https://shippdf.com/terms/) pages. Before submission, complete the
review cases, demo recording, reviewer access, and publication details. Building
this package does not publish it or establish a ChatGPT connection.

## Review cases

The five positive and three negative cases are in `plugin.json` under
`extensions.com.openai.review.test_cases`. They are written reviewer scenarios;
the publisher previously confirmed all eight passed. Setup has since been aligned to the supplied My Project / Start here fixtures; the revised discovery case and pending onboarding have not been independently verified by this agent. Package validation and automated server tests are separate evidence.

The publisher has prepared a dedicated non-operator review account and workspace,
a project named **My Project**, and a starter template named **Start here**.
Complete pending onboarding before review; discovery lists the starter only if published. Connect with the five workspace scopes listed above and
provide generation entitlement and enough credits for repeated review runs.
Keep passwords and sign-in instructions in the portal's secure reviewer fields.
The publisher confirms this reviewer setup exists, with onboarding pending. Credentials and access instructions belong only in secure portal fields.

Run P1–P5 in order in one ChatGPT conversation. P2 creates **Review Invoice**;
retain its actual `template_id` and subsequent lock versions in that conversation.
Keep the returned `document_ref` from P5 for the email boundary case. Before
repeating the sequence, reset the test workspace through the app so existing
templates with the same name do not make discovery ambiguous.

| Case | Scenario | Live result |
| --- | --- | --- |
| P1 | Discover projects and published templates | Publisher-reported; updated setup unverified |
| P2 | Create a sample invoice draft with calculated totals | Publisher-reported; updated setup unverified |
| P3 | Edit heading/color, preview, and leave unpublished | Publisher-reported; updated setup unverified |
| P4 | Publish the reviewed draft version | Publisher-reported; updated setup unverified |
| P5 | Generate one PDF and retrieve another link to the same document | Publisher-reported; updated setup unverified |
| N1 | Refuse access to another company's unauthorized private workspace | Publisher-reported; updated setup unverified |
| N2 | Explain unsupported email delivery without sending or regenerating | Publisher-reported; updated setup unverified |
| N3 | Explain unsupported webhook setup without making requests | Publisher-reported; updated setup unverified |

For a recording, show the development connection and run the same sequence in
ChatGPT with readable prompts, actual tool results, draft previews, publication,
and the completed PDF. Open the PDF to check the heading, sample values, and
USD 100.00 total. Then show the three negative responses. One walkthrough can
cover all eight cases. Keep credentials and unrelated content out of the video.
The supplied [recorded certificate workflow](https://www.youtube.com/watch?v=MN0aSLCBSNc) plays without sign-in. It demonstrates connection, authoring, an image edit, publishing, and generation. It does not establish results for the exact invoice cases, link refresh, or negative scenarios above. The publisher confirms reviewer access and all eight cases have passed. The saved submission version still needs portal checks; the existing recording does not show the negative cases or link refresh.

## Verify

Use Codex's marketplace listing to confirm it discovers the plugin, and run the
skill-creator `quick_validate.py` validator for each skill. Packaging verifies
that distributable files stay inside the plugin and creates a standard ZIP.
Manifest and skill checks do not complete live OAuth or test paid generation.

Test in a ShipPDF test workspace: discover a project, create a template, edit its
draft, validate it, publish when authorized, generate one requested PDF, poll its
status, and refresh the completed download link without generating again.

Official references: [Package your plugin](https://developers.openai.com/plugins/build/plugins),
[ChatGPT connection quickstart](https://developers.openai.com/plugins/quickstart),
and [submission requirements](https://developers.openai.com/plugins/deploy/submission).
