---
name: threat-investigation
description: Look up an IP, domain, network, malware family, exposed file or leaked secret in Etugen and explain what was found.
---

# Investigating with Etugen

## Indicators and infrastructure

For an IP address, start with `get_ip_context`. It returns the threat record, risk score with its reasons, related hosts and any exposed files in one call.

If you're not sure what kind of indicator the user gave you, use `search`. It figures out the type by itself.

Use `get_threats` for a malware family, country, port or network range, `get_asn` for a network, `get_whois` for domain ownership (and reverse WHOIS to find domains sharing a registrant), and `get_techniques` when the user asks about tactics or techniques.

Related hosts are linked by a shared certificate, JARM fingerprint, malware family or network. Follow a link when it helps answer the question. One or two hops is usually enough.

## Files left open on attacker hosts

Many hosts serve open directories: tools, scripts, configs, logs and stolen data.

- `lookup_host` lists what one IP exposes. `get_host_flagged` gives only the high-signal files on it (web shells, malware, credentials, C2), so read those first.
- `search_files` finds files across all hosts by name, extension, content, category, country or network.
- `get_file` returns a file's details and a preview. Use `read_file` when the preview is not enough to tell what the file does.

Explain what a file is for and what it reveals about the operator. Don't paste whole files back unless the user asks for them.

## Operator activity and leaked secrets

- `search_sessions` finds AI coding-assistant sessions left on a host, and `get_transcript` returns one as a conversation. These often show what the operator was building or targeting.
- `search_loot` finds indicators pulled out of file contents: exfiltration endpoints (Telegram, Discord), RAT C2 configs, exposed API keys, private keys and database connection strings. It helps an organisation find its own leaked secrets. When you report a secret, show its type, where it was found and only its first few characters, never the full value.

## Anything else

When no tool above answers the question (counts, trends, grouping, joins), use `sql_query` with a single read-only SELECT. It needs the Business plan; if the account doesn't have it, answer with the other tools and say what could not be computed.

## Reporting

Keep IPs, hashes and technique IDs exactly as returned. If Etugen has no record of something, say so instead of calling it clean. When a result is capped by the account's plan, say that the list is partial.
