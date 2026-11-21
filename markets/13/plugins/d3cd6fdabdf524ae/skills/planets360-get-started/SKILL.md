---
name: planets360-get-started
description: Onboard users to Planets360 Vedic Astrology - explain what birth details are needed and guide the first Kundli, Panchang, or compatibility request.
homepage: https://planets360.in/
author: Planets360
version: 1.1.1
license: Proprietary
privacy-policy: https://planets360.in/privacy-policy
terms-of-service: https://planets360.in/terms-and-conditions
support: support@planets360.in
---

# Getting started with Planets360 Astrology

Welcome to Planets360 Vedic Astrology. This skill runs once after installation
to help the user make their first request.

## What this plugin does

- Janam Kundli and planetary positions from birth date, time, and place.
- Detailed graha and Upagraha positions, Ashtakavarga, Shadbala, Bhava Bala,
  Kundali Yoga, and individual or combined divisional charts D1-D60.
- Daily Panchang, planetary transits, Vimshottari Dasa/Bhukti timelines,
  Chandrashtama dates, Panchapakshi analysis, Moon-sign predictions,
  and compatibility.
- Supporting explanations from public Planets360 articles
  (cite the source URL when used).

## What to ask the user

1. What do they want first: Kundli, today's Panchang, or compatibility?
2. For Kundli, Panchang, transits, Dasa/Bhukti, or Moon-sign predictions,
   collect: birth date, birth time, birthplace (or latitude, longitude,
   and IANA time zone). Never guess coordinates or time zones - ask.
3. For compatibility, collect either two birth dates plus time zone,
   two Moon signs, or two names.

## Rules

- Never fabricate calculation results; always call the matching tool.
- For a birth chart, use `planets360_divisional_chart_d1`; for detailed
  planetary positions, use `planets360_planet_position_details`. Keep
  `planets360_panchang_kundli` for Panchang requests. Request other Kundli
  reports only when needed, and prefer a single chart over all D1-D60 charts.
- Preserve calculation warnings and endpoint-specific optional settings;
  never describe provisional or unverified calculations as validated.
- Astrology is cultural/spiritual guidance only - not professional
  medical, legal, financial, or safety advice.
- Birth details are used only for the requested calculation; see the
  [Privacy Policy](https://planets360.in/privacy-policy).
