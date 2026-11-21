---
name: get-started
description: Use when a user starts Appier Ad Cloud reporting or needs help selecting an authorized report account.
---

# Get Started with Appier Ad Cloud Portal

1. Call `list_report_accounts` to find the report accounts that the user can access.
2. Ask the user to select an account when more than one account matches the request.
3. Ask for a date range when the request does not contain one.
4. Call `list_metrics` when the user asks for available metrics or names a metric that is not clear.
5. Use the report tool that matches the request.
6. State when the account has no available data or does not support the requested report.

Do not infer account access or report values. Use only data from the connected Appier Ad Cloud tools.
