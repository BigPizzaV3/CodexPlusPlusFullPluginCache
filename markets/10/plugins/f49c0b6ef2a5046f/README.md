# AdsGPT for AI clients

Create, review and optimize ad campaigns from your AI client on the ad platforms your organization
connected to [AdsGPT](https://adsgpt.dev), such as Google Ads. This package adds two things
to Claude, Codex and Grok:

- **The AdsGPT MCP server**, which reads and changes your ad accounts with your AdsGPT account.
- **The AdsGPT skills**, the instructions that guide the model through each task: how to create a
  campaign with the platform's creation tool, how to write ads within each format's limits, how to
  review and optimize spend, and the rules of each platform and campaign type.

The MCP server works without the skills; the skills make the model ask the right questions and get
each campaign right at the first attempt.

You need an AdsGPT account with an ad account connected. A new campaign is created paused unless
you ask otherwise, and every tool that changes something says so, so your client can ask for your
approval before it runs.

## Install

### Claude Code

```text
/plugin marketplace add adsgpt-dev/agent-plugins
/plugin install adsgpt@adsgpt
```

Then run `/mcp`, choose `plugin:adsgpt:adsgpt` and sign in with your AdsGPT account.

### Claude (web and desktop)

In **Customize > Plugins**, add the marketplace `adsgpt-dev/agent-plugins` and install **AdsGPT**. Then
connect the AdsGPT server from the plugin's **Connectors** tab and sign in.

### Codex and the ChatGPT desktop app

```bash
codex plugin marketplace add adsgpt-dev/agent-plugins
```

Then open `/plugins` in Codex, or the plugins of the ChatGPT desktop app, install **AdsGPT** from
`adsgpt` and start a new session. Sign in with your AdsGPT account when the client
asks.

### Grok

Add the marketplace `adsgpt-dev/agent-plugins` and install `adsgpt` from `adsgpt`. Grok
signs in with your AdsGPT account on first use.

## What it runs, sends and reads

- **On your machine, nothing.** The package has no scripts, hooks, commands or binaries: only the
  skills, which are Markdown the model reads, the manifest of each client and the address of the
  MCP server. The skills bring no instructions from anywhere else.
- **One remote server,** `https://mcp.adsgpt.dev`, over HTTPS (`.mcp.json`). Your client
  signs in with OAuth 2.1 and keeps the token; it asks for `ads:read` and, the first time a tool
  changes something, for `ads:write`.
- **What reaches the server:** the calls your client's model makes to its tools, with their inputs,
  such as an account id, the report and period you ask for, a new campaign with its budget,
  targeting and ads, ad texts, image URLs, YouTube links or a landing page URL. Never your
  conversation.
- **What the server does with them:** it reads and changes the ad accounts your organization
  connected to AdsGPT, through each platform's API, and keeps a log of every change in your AdsGPT
  organization. It downloads the images you give by URL to check them and uploads to the ad account
  those it lacks, and opens each landing page a change sends, to check that it works.

The [privacy policy](https://adsgpt.dev/privacy) says what AdsGPT stores and shares.

### Tools

| Tool                                        | What it does                                                                                        | Changes something |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------- |
| `list_accounts`                             | Lists the connected ad accounts and the platforms you can connect.                                  | No                |
| `google_ads_report`                         | Reports an account's performance, budgets, recommendations, policy issues and changes.              | No                |
| `google_ads_compare_periods`                | Compares a period with the one before, with what moved the most and the changes made.               | No                |
| `google_ads_get_campaign`                   | Reads a campaign with the sections a change needs, from its structure to its targeting.             | No                |
| `google_ads_get_ads`                        | Reads ads with their texts, images and Google's approval.                                           | No                |
| `google_ads_list_assets`                    | Lists the images and videos of an account.                                                          | No                |
| `google_ads_list_negative_keyword_lists`    | Lists the shared negative keyword lists of an account.                                              | No                |
| `google_ads_research_keywords`              | Finds keyword ideas with their monthly searches and bids, from words or a page.                     | No                |
| `google_ads_forecast_keywords`              | Forecasts the clicks, cost and conversions of keywords for a bid and a budget.                      | No                |
| `google_ads_search_targeting`               | Finds locations, languages, interests, audiences and topics by name.                                | No                |
| `google_ads_create_campaign`                | Creates a campaign of any type with its budget, targeting and ads, paused unless you ask otherwise. | Yes               |
| `google_ads_create_ad_group`                | Creates an ad group with its first ad and, on Search, its keywords.                                 | Yes               |
| `google_ads_create_ad`                      | Creates an ad in an ad group.                                                                       | Yes               |
| `google_ads_create_asset_group`             | Creates a Performance Max asset group.                                                              | Yes               |
| `google_ads_create_conversion_action`       | Creates a conversion action.                                                                        | Yes               |
| `google_ads_create_negative_keyword_list`   | Creates a shared negative keyword list, optionally applied to campaigns.                            | Yes               |
| `google_ads_upload_images`                  | Uploads images to an account's library.                                                             | Yes               |
| `google_ads_add_keywords`                   | Adds keywords to an ad group.                                                                       | Yes               |
| `google_ads_add_negative_keywords`          | Adds negative keywords to a campaign or a shared list.                                              | Yes               |
| `google_ads_attach_negative_keyword_list`   | Applies a shared negative keyword list to campaigns.                                                | Yes               |
| `google_ads_add_extensions`                 | Adds sitelinks, callouts, snippets, a phone, the business name or a logo.                           | Yes               |
| `google_ads_add_targeting`                  | Adds locations, languages, audiences and other targeting.                                           | Yes               |
| `google_ads_set_targeting`                  | Replaces a campaign's ad schedule or device bid adjustments, or an ad group's demographics.         | Yes               |
| `google_ads_add_labels`                     | Adds labels to campaigns, ad groups or ads.                                                         | Yes               |
| `google_ads_update_budget`                  | Changes a campaign's budget.                                                                        | Yes               |
| `google_ads_update_status`                  | Pauses or enables campaigns, ad groups, asset groups, ads, keywords or extensions.                  | Yes               |
| `google_ads_update_bid_strategy`            | Changes a campaign's bid strategy and its target.                                                   | Yes               |
| `google_ads_update_campaign_settings`       | Changes a campaign's name, dates, networks, tracking, conversion goals and other settings.          | Yes               |
| `google_ads_update_ad_group`                | Changes an ad group's name, bid, rotation, tracking or audience.                                    | Yes               |
| `google_ads_update_ad`                      | Changes a search ad's texts or landing page.                                                        | Yes               |
| `google_ads_update_asset_group`             | Changes a Performance Max asset group's assets, landing page or audience signal.                    | Yes               |
| `google_ads_update_keywords`                | Changes keywords' bids or landing pages.                                                            | Yes               |
| `google_ads_update_conversion_action`       | Changes a conversion action's name, category, counting, value or status.                            | Yes               |
| `google_ads_apply_recommendations`          | Applies Google's recommendations.                                                                   | Yes               |
| `google_ads_dismiss_recommendations`        | Dismisses Google's recommendations.                                                                 | Yes               |
| `google_ads_remove_keywords`                | Removes keywords.                                                                                   | Yes               |
| `google_ads_remove_negative_keywords`       | Removes negative keywords.                                                                          | Yes               |
| `google_ads_remove_extensions`              | Unlinks extensions; their assets stay in the library.                                               | Yes               |
| `google_ads_remove_targeting`               | Removes locations, audiences and other targeting.                                                   | Yes               |
| `google_ads_remove_labels`                  | Removes labels.                                                                                     | Yes               |
| `google_ads_remove_campaigns_groups_or_ads` | Removes campaigns, ad groups, asset groups or ads for good.                                         | Yes               |

The `google_ads_*` tools appear only when your organization connected Google Ads.

## Skills

| Skill                    | What it covers                                                       |
| ------------------------ | -------------------------------------------------------------------- |
| `adsgpt-agent`           | The rules of any request about your ad accounts.                     |
| `adsgpt-create-campaign` | Creating a campaign, from the objective to the campaign created.     |
| `adsgpt-google-ads`      | Google Ads: its tools, reports, objectives and campaign types.       |
| `adsgpt-write-ads`       | Writing ad copy from the brand's facts, within each format's limits. |
| `adsgpt-optimize`        | Reviewing performance and improving spend.                           |

## About this folder

AdsGPT publishes this plugin from its own repository: the skills here are a copy, replaced on
each release. Report problems in the issues of `adsgpt-dev/agent-plugins`.

## License

MIT (`LICENSE`).
