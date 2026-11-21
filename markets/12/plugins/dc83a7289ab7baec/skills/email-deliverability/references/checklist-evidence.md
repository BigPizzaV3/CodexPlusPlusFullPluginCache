# Account reference evidence

Pass `--references <json>` only for facts established by the selected account's live settings,
provided instructions or delivered-message headers. Include `orgId` to bind the evidence.
These are local audit inputs, not additional Reteno MCP fields. Omit unknown entries. Record
where facts came from in the user-facing report. The helper does not derive private configuration
from domain names. The standard include is `spf2.esputnik.com`; the standard full DKIM CNAME
is `esputnik._domainkey.<domain>` → `dkim.esputnik.com`. Account-specific instructions take precedence.

```json
{
  "orgId": 123,
  "spf": [{"domain": "bounce.example.com", "ips": ["<actual-public-sending-IP>"], "expectedInclude": "spf2.esputnik.com"}],
  "dkim": [{"name": "esputnik._domainkey.example.com", "type": "CNAME", "value": "dkim.esputnik.com", "lifecycle": "active"}],
  "links": [{"domain": "click.example.com", "expectedCname": "<account-specific-host>", "selected": true, "customerControlled": true}],
  "technical": [{"domain": "bounce.example.com", "mxTarget": "<account-specific-MX-host>"}]
}
```

The sample contains placeholders; it must not be run as account evidence. DKIM lifecycle is
`active`, `in_flight`, or `retired`. Add retained custom link domains to `links` with
`selected:false`; they still need CNAME/TLS validity. `expectedInclude` is optional when
account-specific instructions authorize sending IPs without that include. DNS failures remain
unavailable even when a reference exists. SPF is checked only for supplied IPs, not every possible
sender. See [RFC 7208](https://www.rfc-editor.org/rfc/rfc7208) for SPF and
[RFC 9989](https://www.rfc-editor.org/rfc/rfc9989) for DMARC tree walk and testing policy.
