---
name: get-started
description: Set up Google Ads by Loopthink, work out why it returns no data, or make a change safely. Use when the user has just added the app, asks what it can do, gets a "connect it at …" or "changes are not allowed" message, cannot find one of their ad accounts, or asks to change a campaign, budget or keyword.
---

# Get started with Google Ads by Loopthink

The app reads the Google Ads accounts the user connected in Loopthink, and only
the ones their member group was granted. The tools are always the same:

- `connection_status`: whether Google Ads is connected, and the link to connect it
- `google_ads_list_accounts`: the accounts the user can report on
- `google_ads_report`: a report on one account
- `google_ads_mutate`: changes to one account, where the workspace allows them

## 1. Find out what is connected

Call `connection_status`.

- **`connected: true`.** Call `google_ads_list_accounts` and pass the
  `customerId` exactly as returned to `google_ads_report`.
- **`connected: false`.** Give the user the `connectUrl` and continue with step 2.

## 2. Connect Google Ads

Send the user to the link. Do not try to do it for them: it needs a Google
sign-in in their browser.

1. Sign in to Loopthink and add Google Ads.
2. Sign in with the Google account that has access to the ad accounts.
3. Pick the accounts the app may read. Client accounts under a manager
   account work too.

Then ask the question again. The tools do not change, so nothing needs
refreshing or reconnecting in ChatGPT.

## 3. An account is missing

- It was not picked when Google Ads was connected: an admin adds it on the
  server in the Loopthink web app.
- The person's member group was not granted it: an admin grants it.
- The Google account behind the connection cannot see it.

## Notes for answering

- Cost comes as `cost_micros`: divide by 1,000,000 for the account's currency.
- Pick `resource` by question: `campaign`, `ad_group`, `ad_group_ad`,
  `keyword_view` for keywords, `search_term_view` for search terms.
- Use `dateRange` (for example `LAST_7_DAYS`, `LAST_30_DAYS`, `THIS_MONTH`) or
  `startDate`/`endDate`.
## Making changes

- Before any change, say exactly what will change and ask the user. Run
  `google_ads_mutate` with `dryRun: true` first when the change is more than
  one field, and show the result.
- Get resource names from `google_ads_report` (for example the dimension
  `campaign.resource_name` or `campaign.campaign_budget`). Amounts are micros:
  30 euros is `30000000`.
- The app never starts a campaign and never removes anything. New campaigns
  are created paused, and a paused campaign cannot be set to enabled here: the
  user does that in Google Ads. Ad groups, ads and keywords inside a campaign
  can be enabled.
- If the answer says changes are not allowed, pass it on: a workspace admin
  turns on "Allow changes" on the Google Ads server in Loopthink and grants the
  member group the change tool. Reports keep working meanwhile.
