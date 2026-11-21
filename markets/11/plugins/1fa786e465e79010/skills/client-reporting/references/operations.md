# Reports: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `google_ads_client_report_data` | reports_read | Wants the raw numbers of one Google Ads account to build their own client report. |
| `google_ads_portfolio_report` | reports_read | An agency user wants one report across all connected or selected Google Ads accounts. |
| `marketing_insights` | reports_read | Wants prioritized cross-channel opportunities from connected Google sources: Search Console quick wins, Google Ads keywords that spend without converting, Analytics pages that do not convert and unanswered reviews. |
| `marketing_overview` | reports_read | Wants one funnel overview across connected Google sources: Google Ads spend and conversions, Search Console, Google Analytics 4 and Business Profile. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `looker_studio_report` | reports_create | Wants a live, editable Looker Studio (Data Studio) dashboard of their marketing data in their own Google account. |
| `marketing_report_pdf` | reports_create | Wants a finished, designed marketing report (monthly, weekly, client or period) across connected platforms, delivered as a PDF download link. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `google_ads_shareable_report_link` | reports_edit | Wants a shareable white-label web page that shows one Google Ads account's performance. |
| `looker_studio_settings` | reports_edit | Wants to read or change the branding and connection settings of their Looker Studio report. |
