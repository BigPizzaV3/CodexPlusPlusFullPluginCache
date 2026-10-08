# Proposal request — fields accepted by `request_a_proposal`

Required
- contact.name — full name of the person Kratons should reply to
- contact.email — e-mail address for the reply
- trip.destinations — one or more countries, regions or cities within Spain, Portugal and/or Morocco
- trip.dates — one of: exact start (and end) dates YYYY-MM-DD, a month YYYY-MM, or flexible: true
- trip.travelers.adults — number of adults (children optional, with ages when relevant)

Optional
- contact.phone (with country code), contact.preferredChannel (email | phone | whatsapp | video_call),
  contact.language (en | es)
- trip.nights, trip.budgetTotal + trip.currency (EUR | USD), trip.interests, trip.accommodationStyle,
  trip.occasion, trip.needs (mobility or dietary), trip.notes
- requester.kind (traveller | travel_agent | ai_agent), requester.agentName, requester.agentVendor
- idempotencyKey — reuse the same key to retry safely

Example (two adults, art and gastronomy)
- destinations: ["Madrid", "Seville", "Granada"]; dates: { month: "2027-05" }; nights: 8
- travelers: { adults: 2 }; budgetTotal: 12000; currency: "EUR"; interests: ["art", "gastronomy"]
- contact: { name: "Jane Doe", email: "jane@example.com", language: "en" }

What comes back
- reference (PR-YYYYMMDD-XXXX), duplicate (true when the same request was received in the last 24 h),
  receivedAt, whatHappensNext, contactForChanges
