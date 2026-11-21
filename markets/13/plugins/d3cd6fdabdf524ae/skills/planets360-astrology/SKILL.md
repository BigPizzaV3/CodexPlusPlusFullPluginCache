---
name: planets360-astrology
description: Use when a user requests Planets360 Vedic astrology calculations, Panchang/Kundli reports, transits, Dasa/Bhukti, Chandrashtama, Panchapakshi, compatibility, Moon-sign predictions, or Planets360 editorial content.
homepage: https://planets360.in/
author: Planets360
version: 1.1.1
license: Proprietary
privacy-policy: https://planets360.in/privacy-policy
terms-of-service: https://planets360.in/terms-and-conditions
support: support@planets360.in
---

# Planets360 astrology workflow

- Use the matching Planets360 API tool for personalized calculations. Never fabricate API values or infer missing calculation results.
- Collect all required fields before calling a tool. Birth-time/location tools require latitude, longitude, IANA time zone, year, month, day, hour, and minute exactly as described by the tool schema.
- Do not guess a person's coordinates or timezone. Ask for a birthplace or coordinates and clarify the timezone when needed.
- For detailed Kundli reports, use `planets360_planet_position_details`, `planets360_upagraha_position_details`, `planets360_ashtakavarga`, `planets360_shadbala`, `planets360_bhava_bala`, or `planets360_kundali_yoga` rather than substituting the fast Panchang report.
- For a single divisional chart use `planets360_divisional_chart_d1` through `planets360_divisional_chart_d60` (for example, D9 is Navamsa). Use `planets360_divisional_charts_d1_to_d60` only when all divisions are needed. Dasa/Bhukti remains available as `planets360_dasa_bhukti`.
- Only send optional settings supported by the selected tool. Seconds, ayanamsha correction and Bala conventions are not shared by every endpoint. When omitted, backend defaults apply; Upagraha and Kundali Yoga use minute precision. Do not request or send elevation: it does not affect these position/chart calculations.
- Preserve provisional-calculation notes, unverified divisional mappings and convention/precision warnings. For Kundali Yoga, distinguish formation, cancellation and mitigation; null means not evaluated, not absent.
- Use `planets360_read_public_article` only for public pages on `planets360.in`; give the source URL when using article material.
- Keep raw API output faithful. Explain fields in plain language, and clearly distinguish API data from interpretation or general background.
- For errors, explain the returned error and ask the user to correct missing/invalid inputs or retry later. Never expose API credentials.
- Astrology is a cultural/spiritual interpretation, not a substitute for professional medical, legal, financial, or safety advice.

## Privacy

- Birth details (date, time, place, coordinates, names, Moon sign, Nakshatra) are used only to compute the requested astrology report via the Planets360 API (`https://ephemeris.gopim.dev`) and to fetch supporting editorial text from public `planets360.in` pages.
- No account, email address, or phone number is required. The plugin stores no personal data beyond the current conversation.
- Website analytics and advertising (Google Analytics, Google Ads) apply only when browsing `planets360.in` directly; see the [Privacy Policy](https://planets360.in/privacy-policy) and [Contact Us](https://planets360.in/contact-us) page.
- For full details see the [Privacy Policy](https://planets360.in/privacy-policy) and [Terms and Conditions](https://planets360.in/terms-and-conditions).
