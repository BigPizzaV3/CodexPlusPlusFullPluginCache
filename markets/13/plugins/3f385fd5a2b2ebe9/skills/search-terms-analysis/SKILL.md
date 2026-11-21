---
name: search-terms-analysis
description: "Analyzes Google Ads search terms through the Pilot MCP server: queries that spend without converting, irrelevant intents, terms already excluded, and new keyword candidates, then proposes negative keywords and keyword additions for a person to apply. Use when the user asks about search terms, search queries, negative keywords or wasted search spend. Triggers: search terms report, negative keywords, wasted queries. Déclencheurs : termes de recherche, requêtes Google Ads, mots clés négatifs, exclusions, requêtes qui gaspillent."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with a Google Ads account attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "google_list_accounts google_list_campaigns google_get_search_terms_report google_get_keyword_performance google_list_shared_sets google_list_shared_criteria google_list_customer_negative_criteria pilot_diagnose_wasted_spend"
  pilot-mcp-read-only: "true"
---

# Search terms analysis

Read the queries that triggered Google Ads search ads, find the ones that waste money or miss intent, and propose exclusions and new keywords. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace that holds the account.
- **Optional MCP servers:** a file storage server to save the proposed lists, a team messaging server to send them for review. None is needed for the analysis.
- **Read-only:** never call a tool that creates, updates, pauses or deletes anything. The proposed negative keywords are a list for a person to add in Google Ads.

## Tools

- `google_list_accounts`: the Google Ads accounts attached to the workspace.
- `google_list_campaigns`: campaigns and their channel type, to keep search campaigns.
- `google_get_search_terms_report`: the actual queries, with their metrics.
- `google_get_keyword_performance`: the keywords that matched them.
- `google_list_shared_sets`: shared negative keyword lists.
- `google_list_shared_criteria`: the terms inside a shared list.
- `google_list_customer_negative_criteria`: account-level exclusions.
- `pilot_diagnose_wasted_spend`: campaigns that spend without converting, to focus the analysis.

## Steps

1. Call `google_list_accounts` and pick the account (ask if several are attached). Use its ID as `customer_id`.
2. Call `pilot_diagnose_wasted_spend` with `platform: "google"` and `days: 30` to know which campaigns leak the most.
3. Call `google_list_campaigns` and keep the search campaigns.
4. Call `google_get_search_terms_report` with `date_range: "LAST_30_DAYS"`, first on the campaigns from step 2, then on the account.
5. Read the existing exclusions: `google_list_customer_negative_criteria`, `google_list_shared_sets`, then `google_list_shared_criteria` for each negative list.
6. Call `google_get_keyword_performance` to see which keywords bring the costly queries.
7. Sort the queries into four groups: wasteful (cost and no conversion, or cost per conversion far above the account), off-intent (wrong product, job seekers, free, competitors when unwanted), already excluded but still showing, and promising (converting queries not yet keywords).

## Output

1. **Summary**: spend analyzed, share of spend on queries without conversion, top three actions.
2. **Negative keywords to add**: a table with the term, the proposed match type, the level (campaign, ad group or shared list), the spend and conversions behind it.
3. **Keywords to add**: converting queries that deserve their own keyword, with their metrics.
4. **Watch list**: queries with too little volume to decide.

## Rules

- Never propose excluding a query that converts at an acceptable cost.
- Check every proposed exclusion against existing negatives first.
- Mind close variants: a negative in exact match only blocks that query.
- Show the period and the currency of every amount.

## Examples

- "Which search terms wasted money last month?"
- "Analyse les termes de recherche de mes campagnes Search et propose des mots clés négatifs."
- "Quelles requêtes convertissent mais ne sont pas encore des mots clés ?"
