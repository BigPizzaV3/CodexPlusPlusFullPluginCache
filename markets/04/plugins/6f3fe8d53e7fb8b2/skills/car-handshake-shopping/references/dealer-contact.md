# Dealer contact and reviewer validation

Read this before preparing or sending a dealer-contact request. Use the live tool
schema for required fields; browsing does not require a name, email or phone number.

## Select the action

- `submit_vehicle_inquiry`: send the user's question about one selected listing.
- `schedule_test_drive`: request an appointment for one selected listing; it does not
  book or confirm a time, reserve a vehicle or complete a sale.
- `request_trade_in_appraisal`: request a dealer appraisal related to one selected
  listing; it does not calculate or guarantee a trade-in value.

"Is it available?", "show me the dealer" and "help me draft a question" do not by
themselves authorize sending. Prepare a draft when asked; stop before the contact tool
unless the user explicitly requests delivery or explicitly confirms a reviewer dry-run
under the procedure below. Do not contact additional dealerships.

## Before a normal send

1. Confirm the exact current vehicle and owning dealership using the returned
   `listing_id` and, if details are stale or incomplete, `get_vehicle`. If the listing
   is unavailable or the selection ambiguous, stop before sending.
2. Collect the necessary name, message and chosen contact channel. Ask for email only
   for email contact, and phone only for phone/SMS. Do not request both unnecessarily,
   or collect payment details, government IDs, credentials or a personal street address.
3. For a test drive, clarify the requested date, time and timezone when relevant; do
   not invent `appointment_at`. For a trade-in, collect the required year, make and
   model and only the applicable optional details the user wants to share.
4. Show the recipient, exact vehicle, full outgoing request, contact details and
   allowed channels. Present the consent wording and obtain explicit confirmation of
   this particular send. Neither prior browsing, silence, a checkbox chosen by the
   assistant nor a generic request to find a car supplies consent.
5. Populate `consent_text` with wording actually accepted by the user and
   `allowed_channels` with only the accepted channels. Record the real confirmation
   time as `consent_granted_at` using a trustworthy current timestamp; never fabricate,
   backdate or refresh consent to pass validation. If time or consent cannot be
   established, do not submit. `preferred_contact`, when supplied, must be authorized.
6. Generate one fresh `idempotency_key` for the confirmed payload, then invoke the
   chosen tool. Respect any host confirmation gate as well. A changed recipient,
   listing, message or contact scope needs renewed confirmation and a new key.

## Results and recovery

- `received`: the service received the request for the dealership; do not promise
  delivery, a response time, an appointment, a reservation, a price or an appraisal.
- `duplicate`: the same request was already received; do not create another request.
- `validated`: only input validation completed; no dealer request was created or sent.
- On a timeout or ambiguous response, don't claim success and don't resend with a new
  key. If the error is explicitly retryable and the original consent remains valid,
  at most one retry may use the exact same payload and key. Otherwise stop and explain
  that the outcome is uncertain. Never retry a consent or validation failure unchanged.

If the user cancels before submission, do not send. No recall/cancellation tool is
provided for an already received dealer request; don't promise to retract it. Don't
send follow-up messages, add marketing channels or reuse contact details for another
dealer without separate explicit consent.

## Reviewer dry-run

For an explicitly requested review or test, use `dry_run:true` on every contact call.
Use clearly synthetic reviewer-provided fixture details, never real customer data.
Apply the same listing, required-field, accepted-consent, trustworthy timestamp and
idempotency checks listed above; dry-run does not waive those prerequisites.
The reviewer must explicitly confirm the validation-only request and its test consent
wording. Expect `validated` and say nothing was sent. Do not silently fall through to
normal sending if validation fails. A dry-run is not an appointment or a delivery test,
and does not mean that no technical usage event is recorded.
