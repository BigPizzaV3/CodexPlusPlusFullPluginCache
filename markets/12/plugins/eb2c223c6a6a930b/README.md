# Junocal — booking setup and account handoff

Junocal helps independent instructors and studios teaching dance, music,
coaching, fitness and other disciplines prepare a bookable business. It supports
online and in-person teaching. A website is optional.

## Submitted production tools

The public MCP endpoint is https://junocal.com/api/plugins/junocal/mcp.
Both tools work without a Junocal account or MCP authentication:

1. `prepare_booking_setup` validates the owner's supplied offering details and
   displays an unpublished review of the prices, capacity and local schedule.
2. `save_booking_setup` saves that exact reviewed draft only after an explicit
   request or click. Repeating the same save returns the same continuation.
3. **Continue in Junocal** opens Junocal signup, preserving the draft. An existing
   signed-in owner can explicitly attach it to their business. A new owner signs
   in, confirms business details and chooses Free or the separate Studio trial.
4. The owner reviews and publishes the offering on Junocal, then shares the
   hosted booking page. Customers book there; the owner sees bookings in Sales.

These tools do not read customer records, publish offerings, charge customers or
start subscriptions. Those actions are performed separately on Junocal. The
website's normal signup uses email or its available social sign-in options.

## Costs and supported services

Junocal Free has no monthly subscription. It includes multiple offerings, three
instructor/team members, one location/room, unlimited bookings paid through
Junocal, and 50 free or externally paid bookings per month. Payments on Free
carry a 4% Junocal fee plus Stripe processing. Paid Junocal plans remove the
Junocal transaction fee. The website discloses these terms before plan choice;
the plugin has no subscription checkout or upgrade prompt.

Offerings can be in person or online. This downstream account-acquisition and
commerce journey is disclosed for formal review, including online coaching and
lessons. OpenAI support case 17391229 acknowledged the complete proposal but did
not issue a policy determination. No approval is claimed.

## Testing without live payments

The five positive and three negative MCP cases are in the review metadata. Run
these against the submitted production endpoint; no credentials are required.
The production continuation leads to the normal Junocal signup flow.

Separately, dedicated synthetic accounts and a private sandbox MCP URL are
provided in the confidential Review details field for reproducing the full
account, publication and payment journey without real charges. This sandbox is
an additional downstream test environment, not the submitted public endpoint.
Production draft links are not interchangeable with sandbox draft links: start
that complete check with the supplied sandbox connection and save a fresh draft.

Sandbox sign-in:
https://junocal-journey-staging.curly-sun-ae21.workers.dev/auth/reviewer

The unused music, coaching, fitness and reserve identities require no email
code, magic link or MFA. They have authentication identities but no business,
so the business is created through actual onboarding. Use synthetic customer
details only. Credentials and the private sandbox URL are excluded from this
archive and supplied separately to the review team.

For a full fresh-business check, prepare a future in-person dance class, 60
minutes, 12 places and a £0 introductory price. Review and save, continue, sign in
with an unused identity, choose Free, confirm the business, review the saved
offering and publish. Open the hosted page, make a free customer booking, and
confirm it in both My bookings and the owner's Sales screen.

For repeatable payment testing, sign in with the supplied payment identity,
which owns **Junocal Review Bookings** and has a synthetic Stripe merchant.
Open `/junocal-review-bookings` on the sandbox origin. The £20 dance class is on
14 November 2026 at 10:00 Europe/London. Use Stripe test card 4242 4242 4242 4242,
a future expiry and any three-digit CVC. Confirm the booking and the 80p platform
fee. After that class date, publish another future session in the same business.
New accounts do not automatically receive this payment fixture. This avoids
requiring a reviewer to complete live Stripe merchant verification.

The sandbox uses existing free Cloudflare, Netlify, Render and Neon services.
It stays available when the developer's computer is off. Render may sleep;
a measured cold save took 29 seconds, and the card waits up to 60 seconds.

## Recording and verified evidence

https://junocal-review-materials.curly-sun-ae21.workers.dev/

The 4:47 recording shows actual earlier local browser actions from a ChatGPT
card through account onboarding, publication, Stripe TEST checkout and confirmed
sale. Idle time was removed and playback accelerated. The same page includes
dated evidence from the subsequent hosted free and paid booking checks.
The recording is not represented as footage of the later production deployment.

Hosted verification covered a fresh ChatGPT card without retry, an explicit
save, account handoff, new business, publication, free booking, £20 test payment,
an 80p fee receipt and signed webhook processing. External receipt-email delivery,
Google sign-in, CAPTCHA and live merchant verification are not certified by this
sandbox walkthrough.

Support: https://junocal.com/contact
Privacy: https://junocal.com/privacy
Terms: https://junocal.com/terms
