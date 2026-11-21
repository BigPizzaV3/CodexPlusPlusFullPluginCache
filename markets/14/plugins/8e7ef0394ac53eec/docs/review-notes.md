# BigCommerce submission preparation

## Package and access

- Internal name: `app-6aa60723ea5c8191bcb02999112fb72a`; version: **1.0.0**.
- Display name: **Adzviser BigCommerce**. Publisher: Adzviser LLC.
- Confirmed existing unpublished/rejected submission and registered endpoint:
  `https://bigcommerce.mcp.adzviser.com/widgets/http`.
- Confirmed reviewer workspace: **BigCommerce Demo**, containing the **Demo** store.
- All supported countries. Subscriptions are purchased on Adzviser's website;
  this plugin does not provide purchases or checkout.
- Supply reviewer credentials through secure portal fields, never this ZIP.

The package preserves the original identity, version and short description.
It includes the Adzviser icon, concrete MCP configuration, source-specific skills,
five positive Data Mode cases, three negative cases, the supplied demo link and
user-facing release notes. The listing describes order totals accurately:
all-status, tax-inclusive order value is not automatically paid or net revenue.
The original downloaded ZIP is intact.

## Five positive cases

1. Order count, total order value and average order value over 30 days.
2. Order counts and values by status over the same 30 days.
3. Recorded refund amounts, shipping and tax on orders created in those 30 days.
4. Top five products by units ordered over seven days, including SKUs and total units.
5. Order count, value and average order value compared with the preceding 30 days.

Use a fresh Data Mode conversation for each. Let D be today's date in the user's
timezone. Recent 30 days are [D-31,D-2], preceding 30 days are [D-61,D-32], and
recent seven days are [D-8,D-2], inclusive. Recalculate dates when reviewing.
The store timezone determines order-creation-day boundaries. No numerical
answer is hardcoded in the test cases; all answers must come from returned rows.

All cases include returned order statuses, including incomplete and cancelled
orders. Refund amounts are the current recorded amounts on the selected orders,
not necessarily refunds processed during the selected dates. Product quantities
represent units ordered, not net units sold. Keep currencies and the Orders and
Products segments separate. No customer-identifying fields are needed.

Three negative cases cover cancelling/refunding orders, changing stock/prices,
and accessing an unconnected competitor's private store. Explain these limits
without invoking reporting tools to simulate changes or inventing private data.
No UI-widget review case is included.

## Direct-query evidence

Checked on **October 26, 2026, America/Los_Angeles**. Workspace and field-catalog
discovery succeeded. The five direct report calls returned model-visible
BigCommerce data with `directData=true`, `reportingMode=data` and no field
assumptions. Recent 30 days were **September 25–October 24**, preceding 30 days
were **August 26–September 24**, and recent seven days were **October 18–24, 2026**.

| Case | Observed response and consistency check | Result |
| --- | --- | --- |
| Order totals | 859 orders, USD 603,993.21 total, USD 703.14 average. Total divided by count rounds to the reported average. | Passed direct-query checks |
| Status breakdown | Eight statuses; counts and values sum to 859 orders and USD 603,993.21. | Passed direct-query checks |
| Refund, shipping and tax | USD 11,430.43 refunded amount, USD 634.03 shipping, USD 29,811.62 tax; separate, supported fields returned. | Passed direct-query checks |
| Product quantities | 90 product rows; their quantities sum to 383, matching the separate order-level items total. A top-five ranking can be derived from the full result. | Passed direct-query checks |
| Period comparison | Recent totals match case 1. Earlier period: 1,509 orders, USD 1,478,511.38 total, USD 979.80 average; both averages reconcile. | Passed direct-query checks |

These are dated preparation observations, not fixed review answers. They verify
tool execution and internal consistency; they are not an independent audit
against the store administration console. Fresh conversations against the
uploaded plugin, including the negative cases, have **not been run**.
No BigCommerce backend change was needed for these five report requests.

## MCP annotations and deployment

The shared local MCP correction prepared during the preceding connector work
sets `openWorldHint=false` for account-bound reporting and workspace discovery.
BigCommerce uses that shared profile. Public-source reporting retains true.
See [tool annotations](tool-annotations.md) for all five tools' explicit flags
and behavior-based explanations.

The shared correction has **not been deployed as part of this preparation**.
The ZIP does not deploy the MCP server, and packaged explanations do not override
the server's tool definitions. Deploy the shared annotation correction and
rescan the existing MCP connection before review. Compare the scanned flags
with the documented values and supply any required portal justifications.

## Listing links, demo and remaining review steps

The package reuses the four Adzviser listing destinations inspected anonymously
earlier on October 26: the service website, support contact form, privacy policy
and terms. Those checks confirmed the intended destinations, not a legal audit.
The supplied 256×256 PNG logo is included.

Demo: https://youtu.be/zfZN1PsXXxc

YouTube identifies this as **Adzviser BigCommerce ChatGPT Plugin Demo** by
Adzviser, approximately 176 seconds long, with a non-private playable listing.
An isolated signed-out browser played sampled segments through the end. The
inspected frames show the source-specific MCP connection and a Data Mode report
workflow. Playback in one uninterrupted session hit a player error, so continuous
full playback and coverage of every packaged case remain unverified.

**Redact the browser address bar in the OAuth callback portion of the demo.**
An inspected frame around 92 seconds visibly contains OAuth callback parameters.
Their current validity was not tested. No values are reproduced here. Replace
the video or update the supplied link after redaction; check the entire recording
for other sensitive material before submitting.

The confirmed endpoint challenges anonymous requests with OAuth, and report
calls through the existing authenticated connection succeeded. This does not
verify a new reviewer's sign-in, consent or callback flow. Test the complete
flow with the exact reviewer credentials entered in the portal and confirm
access to BigCommerce Demo without extra setup or verification.

Fresh reviewer OAuth, saved-version positive/negative conversations, imported
review metadata, final MCP scan and required attestations: **Not run / incomplete**.
No portal upload, submission, publication, account mutation or deletion was performed.
