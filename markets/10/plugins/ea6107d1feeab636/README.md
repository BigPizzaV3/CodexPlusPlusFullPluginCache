# TodayNYC 0.1.13

Mary offers four workflows: arrival, three hours in Manhattan, the available NYC weekend edition and the return journey. Six MCP tools support these workflows, including get_airport_transfer_options for grounded advice before ticket times are known.

Curated airport transfers cover EWR, JFK and LGA to/from the exterior of Penn Station, 8 Av / W 33 St. Modes are car, rail/metro and bus with explicitly labelled connections. LGA has no direct terminal train. Only one flight segment is calculated, using local ticket times and timezones supplied by the traveler. Optional access from another place uses a traveler-selected airport and duration. No nearest-airport search, live tracking, third-party data API, booking or payment.

Critical warnings and the short summary are visible first; stage details and official route sources expand on request. All minute ranges are editorial estimates. Updates recalculate the same journey from reported facts; a delay does not automatically relax the original airport deadline.

Travel state is memory-only with an unguessable capability handle, expires after 24 hours idle or server restart, and is capped at 64 concurrent journeys. Forgetting removes server state, not chat history. Do not provide identity documents, booking references or sensitive personal data.

This directory is a local release draft. No public service or OpenAI listing has been changed.
