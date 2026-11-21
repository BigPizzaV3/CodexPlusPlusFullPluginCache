# Keys Locksmith

Keys Locksmith by Keys Inc. helps customers find local locksmiths, compare service quotes, book appointments and track service requests for vehicles, homes and businesses.

Listing category: **Other**. The plugin provides local locksmith service discovery,
quote comparison, booking and tracking for automotive, residential and commercial needs.

## For the reviewer

**No sign-in is required.** Keys is guest-first by design: somebody locked out of their
car at night should not meet an account-creation wall. A first name, a mobile number and
a service location are enough to get help, and that guest record can be claimed into a
full account later.

**Confirming a booking dispatches a real locksmith.** Please use a phone number you can
answer. Cancel the job with the cancel tool once you have seen what you need.

**Availability depends on real coverage.** Keys answers honestly when no locksmith is
available near an address, and never invents one. For a test that reaches real providers,
use an address in Tucson AZ, Dallas TX or Virginia Beach VA.

## What the tools do

Ten are read-only: service types, service and vehicle identification, price quotes,
availability, provider quotes, job status, the customer's tracking link and any extra
work proposed.

Eight change state: preparing a booking for review, confirming and dispatching it,
requesting quotes from nearby locksmiths, recording the customer's key type, messaging
the assigned locksmith, approving or declining extra work, issuing a payment link, and
cancelling a job.

Booking is deliberately two-phase. `keys_prepare_booking` shows the customer the service,
vehicle, full address, price basis and timing; only `keys_confirm_booking` dispatches,
and repeating it returns the same job rather than sending a second locksmith.

## Payment

Payment never happens in the conversation. `keys_get_payment_link` returns a link to a
secure Keys-hosted page. No card details are ever collected in chat.

The card is authorized when the job is booked and charged only after the locksmith
completes the work and submits proof. Cancelling releases the hold.

## Data

Keys collects a first name, a mobile number, the service address, and optionally the
vehicle year, make and model -- a locksmith cannot be sent without them. No payment card
details, health data, government identifiers or credentials pass through the connector.

Privacy policy: https://keys.app/privacy
Terms: https://keys.app/terms
Support: https://keys.app/support