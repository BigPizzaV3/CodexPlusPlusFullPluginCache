# SupMarTech Meta Ads Interest — submission notes

## Directory package

- Requested listing name: **SupMarTech Meta Ads Interest**
- MCP endpoint: `https://supmartech.com/meta-interest-finder/mcp`
- OAuth: Authorization Code + PKCE (S256), Dynamic Client Registration, scopes `interest:read offline_access`.
- MCP tools: `search_meta_interests`, `score_interest_relevance`, `plan_interest_test_sets`, `estimate_interest_test_budget`, `build_saved_audience_prompt`.
- Tool actions: read-only. The server does not connect to Ads Manager and cannot create or modify ads or audiences.
- Listing icon: original SupMarTech MCP icon, copied without editing to `assets/mcp_icon.png`.
- No bearer token, Meta token, password, Plesk credential, reviewer credential, or OAuth client secret is included in this package.

## OpenAI dashboard steps still required

1. Select the verified Supmartech developer identity and upload this ZIP.
2. Connect the MCP server using OAuth, complete the domain challenge, sign in through SupMartech, and run **Scan Tools**.
3. For each scanned tool, enter annotation justifications. The advertised values are read-only=true, destructive=false, and open-world=true only for `search_meta_interests` because it queries Meta’s external targeting search; the other four tools operate on supplied inputs and advertise open-world=false.
4. Enter a dedicated reviewer account through the secure review form. Never place test credentials in this package. The reviewer account must be usable without a private network, MFA handoff, SMS, or email verification.
5. Add an accessible video walkthrough URL and verify all five positive and three negative test cases with the reviewer account.
6. Submit for review. After approval, publishing is a separate action in the portal.

## Items that block final submission

- Privacy and terms pages have been uploaded and verified publicly: `https://supmartech.com/meta-interest-finder/privacy.php` and `https://supmartech.com/meta-interest-finder/terms.php` both return HTTP 200.
- An accessible review video and a dedicated reviewer account still need to be supplied in the OpenAI dashboard.

## Annotation justifications for the portal

- `search_meta_interests`: Read-only because it sends search terms to Meta Targeting Search and returns results; it does not change Meta state. `openWorldHint=true` because it queries an external Meta service. `destructiveHint=false` because it performs no write action.
- `score_interest_relevance`: Read-only calculation on caller-supplied data; no external lookup or state change. `openWorldHint=false`; `destructiveHint=false`.
- `plan_interest_test_sets`: Read-only grouping/calculation on caller-supplied data; no audience is created. `openWorldHint=false`; `destructiveHint=false`.
- `estimate_interest_test_budget`: Read-only arithmetic from caller-supplied assumptions. `openWorldHint=false`; `destructiveHint=false`.
- `build_saved_audience_prompt`: Read-only text generation from caller-supplied data; it does not operate Ads Manager. `openWorldHint=false`; `destructiveHint=false`.

## Live checks performed for this draft

- The production MCP endpoint returns HTTP 405 to a browser GET, as expected for a POST-only Streamable HTTP endpoint.
- The production protected-resource and authorization-server discovery documents return HTTP 200.
- The connected SupMartech MCP was called successfully for all five tools. A live English `Coffee` search returned Meta data; scoring, grouping, budget calculation, and prompt generation returned structured results.
- The test case expecting a Thai search for `ลูกสุนัข` to find results is deliberately not used: Meta returned zero direct and related results during this check.

The current local `meta-interest-finder/mcp.php` source now includes per-tool OAuth security schemes and a tool-level OAuth challenge, but that source change has not been deployed to production yet.
