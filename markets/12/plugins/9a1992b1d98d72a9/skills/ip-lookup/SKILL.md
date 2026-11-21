---
name: ip-lookup
description: Look up who owns an IP address from the regional internet registries (network, organisation, country, allocation range and dates, abuse contact) and get the reverse DNS name, with the lookup_ip and reverse_dns_lookup tools.
---

# Zovo IP Lookup

Use `lookup_ip` when the user asks who owns an IP address, whois details, the abuse
contact for an address, an IP range, or "which ISP is this IP".

1. Pass every address the user gives in one `ips` string, separated by commas, spaces or
   new lines (up to 20). Accept IPv4, IPv6 and CIDR ranges. Call the tool straight away
   when the request already contains addresses.
2. After the result, give the registry, the network name, the holding organisation, the
   country, the allocation range and dates, the abuse contact (if published) and the
   reverse DNS name. Include both registry and PTR "Source" lines with their URLs and retrieval times. Do not present
   the registry country as the location of a person.
3. Mention the CSV download when the user asked about a range or several addresses.

Use `reverse_dns_lookup` when the user only wants the PTR (reverse DNS) name for one or
more addresses and does not need the registry record.

Private, loopback, link-local, shared (100.64/10), multicast, documentation and reserved
addresses are classified locally and are not sent to a registry or to the DNS resolver.

Do not use these tools for a precise location or a street address, to identify a person,
or to scan, block or otherwise act on an address.
