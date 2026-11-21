---
name: email-deliverability
description: Audit Reteno email deliverability technical setup using live MCP configuration, public DNS and TLS. Use for SPF, DKIM/CNAME, DMARC, sender and Reply-To domains, required custom link domains or setup audits. Reports unavailable evidence separately from confirmed failures and applies the current Reteno customer checklist.
---

# Email deliverability

This is read-only. Call `get_email_deliverability_setup` for the selected account and save the
fresh response locally. Resolve `<skill-dir>` from the installed plugin, not the working directory.
The helper uses Python 3.11+ and `dnspython` from the plugin's pinned requirements.

```sh
python3 <skill-dir>/scripts/audit_technical_setup.py --input <setup.json> \
  --organization-id <authenticated-org-id> --output-dir output/email-deliverability
```

Read the JSON and Markdown results before answering. Lead with confirmed failures, followed
by unavailable evidence and its practical effect. Never describe an incomplete audit as passed.
DNS timeout, SERVFAIL, DNSSEC/network or query-budget failures are unavailable evidence.
Only confirmed absence/mismatch against an applicable requirement is a failure.

The October 6 checklist requires an effective DMARC `quarantine`/`reject` policy; `p=none` and
`t=y` do not satisfy enforcement. SPF must be evaluated at the exact envelope/Return-Path domain
with actual Reteno sending IPs, including mechanism order, qualifiers, includes, redirects and
lookup limits. It does not inherit from the From domain or a parent. Preserve other authorized
senders; `~all` and `-all` are both allowed. Do not recommend flattening solely from a theoretical
maximum lookup count. The bounded evaluator reports unsupported macro/PTR evidence as unavailable.

DKIM follows CNAMEs and uses the Reteno `esputnik` selector as discovery fallback. Missing
fallback evidence alone does not fail the customer. Validate active/in-flight selectors against
account-specific expected names, record types and keys/targets; retired selectors are excluded.
A customer-controlled custom link domain is mandatory for every Reteno organization. Confirm
its selection, activation, CNAME target and TLS, including retained domains still used in old emails.
`shortLinks.settings.enabled` controls UTM tagging; `destinationDomains` are redirect destinations,
not expected DNS CNAME targets. `oneClickUnsubscribe.enabled` (configuration 371) does not prove
unsubscribe headers; do not generate a header finding from it. BIMI/MTA-STS/TLS-RPT are optional.

If MCP exposes insufficient account reference details, report unavailable evidence and explain
what is missing. Where those details are supplied by live settings or the user, prepare the
[reference evidence file](references/checklist-evidence.md) and pass `--references <file>`.
Do not guess an envelope hostname, sending IP, DKIM key, custom link CNAME or technical MX target.
Technical MX documentation disagreements are not customer failures. Never refresh verification,
change DNS/configuration or send test mail as part of an audit.
