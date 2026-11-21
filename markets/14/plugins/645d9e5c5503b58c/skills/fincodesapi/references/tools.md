# Fin Codes API tools

This guide reflects `plugins/Mcp/src/Service/McpService.php` in the supplied
Fin Codes API source. Discover the current tools and schemas after connecting;
these names are not a substitute for live discovery.

| Tool | Required string arguments | Purpose |
| --- | --- | --- |
| `lookup_iban` | `iban` | Validate an IBAN and return bank details and BIC/SWIFT. |
| `verify_iban_payee` | `iban`, `payee_name` | Check the account-holder name and return the same bank details. |
| `lookup_bic` | `bic` | Look up an 8- or 11-character BIC/SWIFT code. |
| `lookup_us_routing_number` | `rtn` | Look up a nine-digit US ABA routing number for ACH and Fedwire. |
| `lookup_canada_routing_number` | `crn` | Look up `0YYYXXXXX` electronic or `XXXXX-YYY` paper format. |
| `lookup_australia_bsb` | `bsb` | Look up a six-digit BSB, with or without a hyphen. |
| `lookup_new_zealand_bank_code` | `ncc` | Look up the six-digit bank and branch prefix of an NZ account. |
| `lookup_india_ifsc` | `ifsc` | Look up an 11-character IFSC. |
| `lookup_mexico_clabe` | `clabe` | Validate an 18-digit CLABE and look up its bank. |
| `lookup_argentina_cbu` | `cbu` | Validate a 22-digit CBU and look up its bank. |
| `screen_sanctions` | `name` | Return similar names on sanctions lists. |

`screen_sanctions` optionally accepts `type` (`INDIVIDUAL`, `ENTITY`, `VESSEL`,
or `AIRCRAFT`), `sources` (an array of source IDs from the current schema), and
`min_score` (an integer within the current schema's bounds). Omit filters unless
the user requests them. The source covers EU, UK, UN, OFAC, Swiss, Australian,
and Canadian sanctions lists.

The supplied source supports Verification of Payee for IBANs beginning with:
AD, AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IS, IE, IT, LV, LT, LU,
MT, MC, ME, NL, NO, PL, PT, RO, SM, SK, SI, ES, SE, CH, GB, VA.
Use the live tool description for current coverage. For unsupported countries
or non-IBAN accounts, explain that only bank details can be looked up with these
tools, and that the holder's name remains unverified.
