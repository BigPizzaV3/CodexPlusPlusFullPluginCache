# Owner-only submission steps — DUE Brand Deal Commercials

Draft app id (portal): recorded in the portal only.

1. Verify developer identity for the DUE business (once, shared with the DUE account plugin).
2. On the existing draft select **Upload new version** and upload `due-brand-deal-commercials-0.2.3.zip` (https://brieftopaid.app/downloads/due-brand-deal-commercials-0.2.3.zip).
3. Authentication is read from `mcp.json` (`extensions.com.openai.auth` = `{ "type": "none" }`). Under **MCPs**, confirm the saved settings show no authentication; the panel only displays them.
4. Domain verification: open **MCPs → Connect**, copy the challenge token, and give it to the developer to serve at `https://brieftopaid.app/.well-known/openai-apps-challenge`; publish, then select **Connect**.
5. Wait for the tool scan; confirm only `check_brand_deal_commercials` with readOnlyHint true, destructiveHint false, openWorldHint false.
6. Review information: the five positive and three negative cases are imported from `plugin.json` (`extensions.com.openai.review.test_cases`) and are read-only in the dashboard. No reviewer credentials are needed.
7. The demo recording URL (https://brieftopaid.app/review/due-public-review-walkthrough-20261016.mp4) is imported from `plugin.json`; confirm it, then submit for review. Publish the listing after approval.
