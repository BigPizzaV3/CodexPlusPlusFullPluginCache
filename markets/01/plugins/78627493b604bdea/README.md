# Oracle BI

Explore dashboards, investigate changes, export reports, and build analyses in your organization's Oracle BI workspace. The plugin supports the Oracle BI Enterprise Edition (OBIEE), Oracle Analytics Server or Cloud, and BI Publisher features available to your signed-in account.

This plugin is built and maintained by OpenAI. It is powered by computer use, and is not an Oracle-provided API or MCP integration.

## Try It

- Summarize my Oracle BI dashboard and explain what changed.
- Compare this quarter with last quarter by region and export the results.
- Create a revenue-by-region analysis and save it in My Folders.
- Add a region filter to my sales dashboard.
- Open this BI Publisher report for last month and download a PDF.
- Check why my scheduled report failed and summarize the visible error.
- Find the saved output when my report succeeded but the email attachment is missing.
- Reconcile this financial summary with its drill-to-detail report.
- Turn the selected report into an executive brief with its filters and source date.
- Schedule this report for Mondays at 9 a.m. in my time zone, with the recipients and format I specify.

## Connect Your Workspace

This plugin requires local browser access in ChatGPT Desktop or desktop Codex. Use desktop-local Work; web, mobile, and cloud-backed tasks are not supported for live account access. A Work handoff is usable only when it leads to a supported desktop-local session. Explanations and analysis of files you supply can stay in Chat.

Provide your organization's BI URL or select an existing signed-in local browser tab. There is no universal Oracle BI sign-in address. The assistant uses the supported local browser, such as the in-app browser (IAB). It must be available and permitted by your organization's SSO, VPN, device, and site policies; an unavailable local browser is not replaced with a cloud browser.

Sign in through the browser when prompted, then ask the assistant to continue. Keep passwords and verification codes in the sign-in page. Your account's catalog access, subject areas, authoring privileges, and export permissions determine what is available.

## Working With Reports

The assistant keeps track of the dashboard or report, selected filters, date range, currency, and available refresh information. Comparisons distinguish visible results from calculated differences and identify incomplete exports or missing data.

If a report ran successfully but delivery failed, the assistant can inspect the matching job history and help retrieve existing output. A brief or spreadsheet created from an export is a snapshot; it does not automatically refresh or inherit Oracle's access controls when shared elsewhere.

You can request creation or editing of BI content. New analyses and dashboards default to your personal folder when you do not specify a destination. Changes to shared content, overwrites, deliveries, and schedules require a clear request identifying the affected object and destination. A request to review or draft does not send a report or save changes.

This plugin operates the BI web interface. It does not administer databases or connections, change security or semantic models, perform transactional write-back, or operate other Oracle business applications. It includes no API or MCP connection and does not grant additional access to your organization.

## Brand Asset

The icon uses the official Oracle "O" mark from [Oracle's repository](https://github.com/oracle/apex/blob/bbb9d59b505308030cc491d7ab24461d3d53c392/docs/img/icons/pinned-icon.svg), with its original vector path and the `#C74634` color specified by [Oracle's page](https://github.com/oracle/apex/blob/bbb9d59b505308030cc491d7ab24461d3d53c392/docs/index.html#L13). It is the corporate Oracle mark, not a separate Oracle BI product logo. Oracle's trademarks belong to Oracle and/or its affiliates; this plugin is maintained by OpenAI.
