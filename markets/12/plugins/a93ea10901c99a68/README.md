# Delpha for ChatGPT and Codex

This folder is the plugin package, as uploaded to the OpenAI plugin directory and as installed by
Codex: `plugin.json` and `mcp.json` in the portable Agent Plugins 1.0.0 format (OpenAI listing,
review and publication settings under `extensions.com.openai`), the `.codex-plugin/plugin.json` +
`.mcp.json` overlay for older Codex clients, two skills, the logo and three demo screenshots.

`skills/` and `assets/logo.svg` are **generated** from the repository's canonical `/skills` and
`/images/delpha-mark.svg` by `scripts/sync-skills.sh`; `scripts/build-openai-plugin.sh` zips this
folder (no enclosing directory, no `.DS_Store`) into `dist/delpha-<version>.zip`.

## Connection

The server is `https://mcp.delpha.ai/mcp` (streamable HTTP). Authentication is OAuth 2.1 + PKCE
with dynamic client registration: the client discovers everything from the server's `.well-known`
documents and you sign in with your Delpha account. The team must have **MCP access** enabled
(console → **Developer → MCP setup**). The package carries no credential.

## Included skills

- `delpha` — routes a request to the right tool, handles the asynchronous submit-then-read
  pattern, reads the scores, and documents only the inputs each MCP tool accepts (REST-only fields
  are marked as such).
- `delpha-gtm-account-routing` — turns an ultimate-parent result into a new-logo or routing
  decision, without inferring CRM state.

## Upload to the plugin directory

1. [platform.openai.com/plugins](https://platform.openai.com/plugins) → **Upload new or existing
   plugin** → the ZIP from `scripts/build-openai-plugin.sh`. The upload creates a draft version.
2. **MCPs → Connect** (With MCP): the domain-verification token is already served at
   `https://mcp.delpha.ai/.well-known/openai-apps-challenge`; connect with a Delpha account, then
   **Scan Tools**.
3. **Review details**: a justification per tool and per annotation (the ZIP cannot carry them),
   a reviewer test account that signs in with a password only, a demo recording URL, and —
   because the scan reports UI templates — one 706 px-wide PNG screenshot per starter prompt.
   The five positive and three negative test cases and the release notes travel in `plugin.json`.

## Use without the directory

- **ChatGPT**: Plugins → **+** → **Add custom MCP server** → `https://mcp.delpha.ai/mcp` → OAuth →
  **Create as a plugin**. This connects the tools; it does not install the bundled skills.
- **Codex, Claude Code, Cursor**: install from the repository marketplace — see
  [`providers/README.md`](../../README.md).

## Smoke test after sign-in

1. The connected server lists 16 tools, including `validateAndNormalizePhone` and
   `validateAndNormalizeName`.
2. Ask to validate a website you own: the agent submits once, then reads the result once
   (`findAndValidateWebsite` → `getWebsiteResult`). This spends credits.
3. Ask for the commercial parent of a company with a known website. Without CRM evidence the
   routing skill must leave the new-logo decision undetermined.
4. Where a result widget renders, the card and the structured result agree.

## Review examples and screenshots

The manifest contains five positive cases (Sephora Brazil commercial parent, Starbucks Chile commercial parent,
supplied Schneider website validation, supplied Delpha SIREN validation, and Germain Bourgeois
LinkedIn discovery) and three negative cases
(private home contact details, flight booking, and Salesforce writes). LinkedIn cases use the
current `findAndValidateLinkedInProfile` / `getLinkedInProfileResult` names.

The three bundled screenshots are supplied historical demo captures, in starter-prompt order.
They were downloaded unchanged from:

- https://mcp.delpha.ai/delpha_sephora_706x800.png
- https://mcp.delpha.ai/delpha_starbucks_706x800.png
- https://mcp.delpha.ai/delpha_contact_verification_706x800.png

Starter prompts are shortened to the directory limit. The Starbucks prompt explicitly supplies
an existing CRM account, as required to assess whether the lead is a new logo. Screenshots
illustrate prior outputs; they do not establish that the current server or reviewer account passes.
Run the formal cases with the reviewer account before submission and provide the demo video
URL and reviewer credentials in the portal.

Supplementary manual checks (outside the required five positive cases):

- Validate `germain.bourgeois@delpha.io` using `findAndValidateEmail` / `getEmailResult`, reporting
  deliverability and personal/company domain classification as returned.
- Resolve Sephora Brazil’s commercial parent and distinguish passive financial holdings.
  The supplied historical screenshot shows LVMH; use current evidence when retesting.
- Resolve Starbucks Coffee Chile (`starbucks.cl`) against an existing Starbucks Corporation
  account, reporting commercial relationship, confidence and the supported routing decision.
- Find Germain Bourgeois at Delpha: LinkedIn profile, current title and business email. Use
  LinkedIn profile and email submit/result pairs; state when current employment is unconfirmed.
- Find Delpha’s SIRET in Paris, France as a separate registry check from the formal SIREN case.

## Review test evaluation protocol

Evaluate each prompt independently. Keep expected answers out of fresh-chat routing tests.
Record two separate outcomes: **handling** (tool selection, polling, faithful interpretation)
and **functional completion** (the requested result is actually supported). Successful tool
selection or an honest failure explanation alone does not establish functional success.

- A completed unconfirmed result fails a case requiring a service-validated SIREN. Website
  validation must distinguish URL reachability from legal-entity identity consistency.
- An upstream terminal error or unfinished job blocks functional completion. Record the error;
  do not infer an entity comparison from only one successful result.
- Discovery can return a supported candidate (P5). Label unconfirmed URL validation explicitly.
  Discovery success does not establish successful validation.
- Recommendation scores, match scores and validation status are different fields. Preserve
  inconsistencies in the report instead of choosing the most favorable field.
- Submit once, retrieve the result, and poll again only after 202 and a wait. Extra result reads
  after 202 are valid. Do not resubmit a billable lookup solely to obtain a preferred answer.
- Report exact tools and relevant response fields, without credentials. Record credits only
  when the service reports them. Distinguish upstream errors from authentication failures.
- Negative cases test whether Delpha is invoked outside its scope. Use isolated fresh chats
  with only Delpha available for routing checks. Record any evaluation-only constraints;
  those runs do not establish behavior when an independent CRM write tool is available.

User-reported October 14 run (not independently rerun during this metadata edit): P1 and P5
passed, P2 was blocked, P3/P4 failed, and N1–N3 passed the constrained routing check. P2 returned
a terminal 400 for bolt.com. P3 recommended se.com without confirming it. P4 returned SIRET
suggestions for a SIREN request. P5 supported profile discovery but did not confirm URL validity.
These unresolved findings are retained; revised criteria are not a claim that the server is fixed.


## Revised positive fixtures after live checks

The blocked bolt.com comparison is removed from the positive submission suite and retained
as an unresolved regression in the ticket findings. Website discovery is replaced by validation
of a supplied URL; SIREN discovery is replaced by validation of a supplied identifier. These are
explicitly different tasks, not reclassified passes for the original failures.

Use exactly the prompt in each manifest case. The tested submission inputs are:

- P1: company_name `Sephora Brazil`, website `https://www.sephora.com.br`, country `Brazil`.
  The user reported a successful run: LVMH commercial parent, Wholly Owned, confidence 0.95;
  Agache SCA financial holding. The raw response and job ID were not supplied for this run.
- P2: company_name `Starbucks Coffee Chile`, website `https://starbucks.cl`, country `Chile`.
- P3: name `Schneider Electric Industries SAS`, website `https://www.se.com`, country `France`.
- P4: name `Delpha`, legal_id `880524400`, legal_id_type `FRA - SIREN`,
  address `{ "city": "Paris", "country": "France" }`.
- P5: first_name `Germain`, last_name `Bourgeois`, company_name `Delpha`, website `https://delpha.io`.

Live checks used the connected DELPHA MCP tools. They verify server behavior for these inputs;
they are not an independent fresh-chat test of the installed Delpha plugin's skill routing.
The three negative cases retain the earlier user-reported constrained routing results.


P1 now uses the user-tested Sephora Brazil scenario, matching the first carousel image.
The independent Bolt example remains a supplementary regression check; it is no longer one
of the five formal positive cases. The Sephora result is user-reported, not an independently
rerun direct MCP check in this edit. The other four positive cases retain their prior evidence.
