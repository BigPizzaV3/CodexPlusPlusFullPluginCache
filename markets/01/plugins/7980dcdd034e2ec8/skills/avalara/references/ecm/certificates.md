# ECM: exemptions and certificates

Navigation in AvaTax: Exemptions > Customer certificates, and Exemptions > Customers.
Administrator access to change; a Viewer sees this read-only.

Exemption certificate management is its own product line, ECM Essentials through ECM Pro
and Premium, and it replaced the older AvaTax Exemptions product. Avalara's products
function independently and have distinct roles and permission structures.

## A certificate is not the only thing that decides exemption

Three account-level settings can override everything a certificate says. Check them
before concluding anything from a certificate record:

- **Exemption certificate handling** decides whether certificates count at all. One
  setting exempts by certificate, one ignores certificates entirely and exempts from
  invoice data, and one requires a certificate and ignores invoice data. In the middle
  setting, a perfect certificate changes nothing.
- **An exempt override code** charges tax on a specific transaction even when the
  customer has a valid certificate on file.
- **The Statement of Taxability exempt reason is informational and does not exempt
  anything.** A certificate carrying it looks complete and still produces tax.

## Statuses

ECM distinguishes more than valid and invalid. Common statuses include the following;
use the labels and validation state shown by the selected product:

| Status | Meaning |
|---|---|
| Valid | ECM validated it and confirmed it has the required information. Usable for exempt transactions. |
| Invalid | ECM found missing or incorrect information, such as a missing business name or signature. |
| Expired | Past its expiration date. No longer exempts. |
| Paused | Someone manually paused it. ECM excludes it from transaction processing. |
| Pending | Not yet validated. In review. |
| Pending-future | Has a future effective date. Becomes Valid on that date. |

Saving a certificate does not validate it. Validation is a separate step ECM performs.

## Turning exemption off, and the four controls that look alike

These are not interchangeable and the intuitive one is usually wrong:

- **Pause** is the deliberate, reversible switch. It stops the certificate exempting the
  customer. Resume restores it, and the valid or invalid status is untouched either way.
- **Invalid** is a validation state describing incomplete or incorrect data. Avalara also
  documents marking a certificate invalid as the correct way to stop one that was applied
  in error. The remedy for a genuinely invalid certificate is to correct it, not to clear
  a flag.
- **Expire** is the wrong tool for a certificate applied in error. Avalara documents that
  expiring one in that situation causes API errors and leaves the exemption record in
  AvaTax unchanged. Mark it invalid instead.
- **Delete** is permanent and is covered below.

## Traps

- **Deleting a certificate is irreversible and does not reliably stop exemption.** The ID
  and all related data go, and the record cannot be recovered. Worse, Avalara documents
  that a deleted certificate that was still valid can remain active and keep applying to
  transactions, which is why their own guidance is to mark it invalid first. For a
  multijurisdictional certificate, deleting the primary deletes the whole group; deleting
  a single one affects only that jurisdiction. Suggest marking invalid before anyone
  reaches for delete.
- **Customer records also delete permanently**, including ones linked to a certificate,
  and cannot be recovered. Nothing in ECM behaves like the transaction rule where records
  are always retained.
- **Making a certificate valid does not fix past invoices.** A certificate exempts
  transactions calculated after it became active. An invoice already calculated keeps its
  tax until someone recalculates it. Never reason backward from an old transaction to a
  certificate's current state.
- **Customer codes must match exactly** between ECM and the business application, or the
  certificate never applies. This is the most common reason a valid certificate appears
  to do nothing.
- **Do not assume address-specific exemption.** Default customer-code matching may cover
  multiple locations in the same state. Verify the selected product's matching rules
  before suggesting separate customer codes or certificates; changes require the user's
  intended treatment and authorization.
- **Exemptions never inherit from a parent company to its children.** Even when a child
  company uses the parent's tax settings, exemptions are managed per company and must be
  added to each one. Advanced company settings behave the opposite way, so an assumption
  carried over from there will be wrong.
- **When several certificates cover the same region, ECM picks which one is active**, by
  a cascade that prefers valid over invalid and unexpired over expired before falling
  back to dates and IDs. Uploading a newer certificate does not reliably supersede an
  older one.
- **A correction to a multijurisdictional certificate is sent in one API call.** One bad
  jurisdiction can prevent the correction from applying. Check visible history and the
  errors report for all affected jurisdictions before reporting success. This is a browser
  verification step, not authorization to call an API.

## Diagnosing "this customer should be exempt"

Rule out the cheap causes before touching a certificate:

1. Does the account's exemption certificate handling setting even use certificates, and
   is there an exempt override code on the transaction?
2. Does a certificate exist for that customer and state, and what is its status? Paused
   and Pending are as common as Invalid and mean different things.
3. If it is Invalid, read the recorded reason. That reason is the finding. Report it. Do
   not clear it.
4. Does the customer code on the transaction match the customer record exactly?
5. Is the exempt reason Statement of Taxability, which never exempts anything?
6. Was the transaction calculated before the certificate became active? Check whether
   recalculation is needed under the approved effective dates. Do not recalculate without
   authorization for the affected records and tax changes.
7. Is nexus even active for that jurisdiction? Missing nexus produces the same zero tax
   as a valid exemption. See [nexus](../avatax/nexus.md).

Match remediation to the visible cause and the user's intended treatment. For stopping
exemption, explain the available pause, invalidation, and deletion effects before a
consequential change. Never mark a certificate invalid or valid merely to change the tax.
