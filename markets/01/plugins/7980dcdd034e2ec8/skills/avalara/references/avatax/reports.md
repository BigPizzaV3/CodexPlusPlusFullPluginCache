# AvaTax: reports

Navigation: Reports, then a category. Liability and tax return reports are their own
category. Choose category, choose report name, complete the required fields, generate.

Account Viewers can run reports.

## Traps

- **Report refresh and data freshness differ.** Changes can take longer to appear than
  the refresh interval suggests. Use visible generation/data timestamps and current help
  for timing; for the current transaction state use the Transactions page. Do not describe
  a generated report as live or change records simply to force its totals to match.
- **Liability worksheet reports are available only to Managed Returns subscribers, and
  must be exported.** If the user is not on Managed Returns, the report is genuinely
  unavailable rather than hidden by role.
- **"Dirty" in an approval status indicates processing.** Report the visible state and
  check any filing deadline rather than retrying or assuming a completion time.
- **Reports present by document date** while tax calculates on tax date. A transaction can
  appear in an unexpected period, or appear as a no-nexus exemption, purely because of
  this. See [nexus](nexus.md).

## Scope of a report request

Generating, filtering, and downloading a report the user asked for is a read. What that
does not authorize is in [data handling](../data-handling.md).

Always report row limits, truncation, and the generation timestamp. A report that
silently stopped at a limit is worse than no report, because it looks complete.
