# Measurement and tracking

## The standard stack

1. **Enhanced conversions**: first-party data, hashed, sent with conversions. Recovers conversions lost to cookies and devices.
2. **Consent**: Google's EU user consent policy applies to EEA traffic since March 2024. Consent Mode v2, with a certified consent platform, is how sites pass consent signals. Without them, audience and measurement features stop working for EEA users.
3. **Server-side tagging**: improves signal durability. It does not replace consent.
4. **Offline conversion import** for lead generation: send the real business outcome (qualified lead, sale, value), not only the form fill. Check `platform-facts.md` for the current API route.

## Reading conversions

- Primary conversions (the "Conversions" column) are what bidding optimizes and what most reports show.
- "All conversions" adds secondary actions, view-through and cross-device. It matters for upper-funnel campaigns, but it mixes units.
- The business source of truth is usually outside Google Ads: CRM, shop, app analytics, finance. Reconcile against it before judging a campaign.
- Google Ads and GA4 have separate attribution settings. Say which one a number comes from.

## Attribution

- Google Ads offers data-driven attribution (default) and last click. See `platform-facts.md`.
- Attribution assigns credit for conversions that happened. It does not say which conversions the ads caused. For that, run an incrementality test (the Fiera Incrementality plugin covers this).

## Common tracking failures

| Symptom | Likely cause |
|---|---|
| Conversions drop to near zero overnight, clicks normal | Tag removed or broken, consent banner change, site release |
| Conversions double | Tag firing twice, two conversion actions both primary for the same event |
| CVR jumps on one campaign only | That campaign's goal includes a micro-conversion |
| Conversion value constant | Value hard-coded, value-based bidding has nothing to learn |
| Recent days always look worse | Conversion lag: compare at the same age |
| GA4 and Google Ads disagree | Different attribution, counting (every vs one), or time zone |

## Counting

- Lead generation: count one conversion per click for leads; every conversion for purchases.
- Check which actions are primary. Primary actions in the goal feed bidding; a micro-conversion set as primary pulls bidding toward cheap, low-value actions.
