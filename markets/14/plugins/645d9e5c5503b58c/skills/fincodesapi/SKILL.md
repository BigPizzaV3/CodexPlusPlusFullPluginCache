---
name: fincodesapi
description: Use Fin Codes API to validate IBANs, look up BIC/SWIFT and national bank codes, verify IBAN payee names, or screen people and organizations against sanctions lists.
---

Use the connected Fin Codes API MCP tools for bank-code validation and lookup,
Verification of Payee, and sanctions screening. Prefer the server's maintained
reference data and national validation rules to locally calculated checksums.

Choose the tool from [the tool guide](references/tools.md). Treat the connected
server's current schemas as authoritative for supported arguments and coverage.
Keep identifiers as strings so leading zeroes survive. Ask for missing bank
codes, countries, or payee names when needed; do not guess them.

For IBAN bank details, use `lookup_iban`. If the user requests account-holder
verification and supplies both a supported IBAN and a payee name, use
`verify_iban_payee` directly: it also returns the bank details, so a preliminary
lookup is unnecessary. Each lookup uses the user's account quota; payee checks
also use the VoP balance. Avoid redundant calls and unrequested batch screening.

Report the tool's verdict first, followed by relevant bank, branch, address,
country, and routing details. A valid bank code or checksum does not establish
that an account exists, who owns it, or whether a payment is safe.

For payee verification, preserve the exact status:

- `MATCH`: the supplied name matched the account holder.
- `CLOSE MATCH`: show the bank's returned name and ask the user to confirm it
  before paying.
- `NO MATCH`: explain the mismatch and ask the user to confirm details with the
  payee before paying.
- `NOT APPLICABLE`: explain that verification could not be completed; do not
  present the account as verified.
- `BANK UNAVAILABLE`: the bank does not offer verification; the name remains
  unverified. Repeating the request will not resolve that coverage limitation.
- Missing or unknown status: report that the name could not be verified.

For sanctions screening, report returned candidates, match scores, sources,
and identifying details that help the user review them. Name similarity alone
does not establish identity or sanctioned status. No matches means no similar
listed names were returned under the selected filters and threshold, rather
than a guarantee of clearance. Do not turn a name match into a definitive
compliance decision.

If tools are unavailable or authentication fails, explain that the connection
needs setup and direct the user to the host's secure connection flow. Never ask
for API keys or passwords in chat, read unrelated credential files, or include
secrets in generated files. Do not fabricate a result when a lookup fails.
Respect quota, balance, and service errors; do not repeatedly retry them.


The public test IBAN `DE75512108001245126199` is a service test fixture.
Its result demonstrates the Verification of Payee flow; do not present it as
evidence of a real person's account ownership. Use fictional or published test
data for demos and respect the service's terms for personal data.

These tools cannot initiate payments, reverse-search an account number by a
person's name, reveal balances or transaction history, or determine a person's
creditworthiness. Explain these limits without invoking unrelated lookups.
