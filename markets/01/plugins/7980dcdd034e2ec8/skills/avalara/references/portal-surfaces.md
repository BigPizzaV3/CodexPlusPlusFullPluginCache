# Portal surfaces

Which consoles a user reaches depends on their subscriptions, and the same concept can
appear differently in each one.

## Getting to the right place

Honor an explicit choice of URL, tab, product, account, or environment. Otherwise prefer:

1. **A tab the user already has open,** claimed through the Browser skill's supported
   tab-selection flow. It carries their session, environment, and company selection.
2. **An official URL the user supplied.** Use it as given, subject to Browser site policy.
3. **`https://admin.avalara.com/` for production, or `https://sandbox.admin.avalara.com/`
   for sandbox,** then navigate to the product from within the signed-in session. Which
   of those two you open is which environment you are working in, so choose deliberately
   rather than defaulting to production. These are AvaTax admin-console entry points,
   not universal hosts for every Avalara product.
4. **[Avalara's product sign-in page](https://www.avalara.com/us/en/signin.html)** when
   another product or its entry point is needed. The AvaTax sign-in flow may use
   `https://identity.avalara.com/`; a shared authentication host alone does not establish
   the final account, product, company, or environment.

Do not type a product URL from memory, and do not construct one by editing the host or
path of a URL you are already on. Environment boundaries live in those hosts, and an
edited URL is the most common way to cross one by accident.

If the requested product is unavailable from the official sign-in page or selected
session, report the limitation rather than guessing another address.

## Product families you may encounter

Confirm what the signed-in session actually offers rather than navigating from this list.

- **Core tax calculation and transaction management.** Transactions, companies, items,
  customers, nexus, tax codes, reports. This is where most transaction review happens.
- **Exemption certificate management.** Certificates, exemption requests, customer
  exemption status, certificate validity and expiry. A product line of its own, ECM
  Essentials through Pro and Premium, and it replaced the older AvaTax Exemptions
  product. Account-level settings here can override what a certificate says, so a
  certificate record alone does not tell you whether tax was exempted.
- **Returns and filing.** Liability worksheets, returns, filing calendars, filing status,
  funding and remittance.
- **Registrations, licenses, and other compliance products.** Separate workflows,
  frequently separate consoles.
- **Specialized tax products** for excise, communications, lodging, and beverage alcohol.
  Their subscriptions, setup, and portals can differ; use the official product sign-in
  page and what the session actually offers.

## Do not cross surfaces on your own initiative

A record missing from one console is not a reason to go looking in another. You may end
up reporting a figure from the wrong place.

When the requested data is not where the user expects it:

- Report exactly what you looked at and what you found.
- Name the product where it might live, if you have a visible reason to think so.
- Navigate there only when the user's requested scope already covers that product and
  company; otherwise ask before expanding scope.

The same discipline applies to environments. Never open the sandbox to check something
about production, or the reverse.

## Concepts that do not translate cleanly

Be careful when a task spans products:

- **Exemption status** shown against a transaction reflects what applied at calculation
  time, not the certificate's state today. A certificate corrected afterwards does not
  change an invoice that already calculated.
- **Customer codes must match exactly** between the certificate record and the
  transactions arriving from the user's business application. A mismatch is the most
  common reason a valid certificate appears to do nothing. See [certificates](ecm/certificates.md).
- **Period is not one word.** Reports and returns assign transactions by document date,
  the returns side talks about the filing period, and transaction search filters by date
  range. Confirm which one a screen means before reporting on it.
- **Filing calendar** is what users call it. The control is labeled filing frequency, and
  a filing schedule is the value you pick inside it, not a second control. Search for
  what the screen calls it, and use the user's word back to them.

When reconciling across products, identify each source, company, period, and refresh
time. Compare like-for-like figures rather than merging totals with different scopes.

## When a surface is unavailable

If the product is not subscribed, the role does not permit it, or the console will not
load, name the specific limitation and the supported path. Do not approximate the result
from another product's data and do not present a partial view as if it were the whole.
