# Coach setup: the rules that catch people out

## Getting paid
- Two gates, both needed before a client can pay for a priced service: the Coach Agreement accepted, and Stripe finished (card payments on). The client sees the same message whichever one is missing.
- Liftory's fee is a share of each card payment with a monthly cap; quote the figures get_coach_setup returns, never a remembered rate. Cash payments a coach records carry no fee.
- Free services and invite-code arrangements need neither gate: a coach with no Stripe account can still publish a free intro call.

## Profile
- Discovery, open requests and the price display are on by default, so a new coach is listed publicly from the start, with a name taken from the email address until they change it.
- The availability line is free text that only people read; the bookable hours are set separately, and nothing keeps the two in step.

## Services
- A new service starts as not for sale and cannot be booked until it is Free or Priced.
- A Free service is always billed per session; the app does not let a free service be monthly or a plan.
- A per-plan service needs the number of sessions it includes; the app refuses to save one without it.
- A client holds one monthly subscription per coach; a second one is refused.
- A window reserved for some services is hidden from clients who picked another, which the booking preview shows.
- A price change applies to new purchases only.
- Where it happens defaults to the profile; set it only where a service differs. In person and online lets the client choose when booking, and online sessions get a video room by themselves.

## Hours
- Times are local and follow daylight-saving changes; the week starts on Monday.
- Offer one or two free hours, not a whole day; a person can hold one free hour ahead at a time.
- A blocked day removes everything that day, and clients see the coach as not working rather than fully booked.
- Until a window exists, the coach and clients see that nobody can book yet.
