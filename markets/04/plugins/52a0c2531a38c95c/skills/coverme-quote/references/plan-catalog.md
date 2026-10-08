# Plan catalog

Compliance-locked names, bullets, and policy PDF links. Load at Stage 2c when rendering the priced table. Use the EN section in EN flow, FR section in FR flow. Render every bullet verbatim, `<br>`-separated with `• ` prefix, in the "What it covers" column. Catalog labels have `\|` pre-escaped — copy as-is.

**Never leak the code.** In each entry below, the `### CODE → Name` heading is INTERNAL. Only the text after the arrow (the plan name) is user-facing. NEVER emit `SAIH`, `SNMIH`, `STCIH`, `SEMH`, `SYDELH`, or `SYAIH` in any message shown to the user.

## STCIH coverage amount

**STCIH is always sent with `coverageAmount: 30000` (Unlimited) — in Stage 2 `getQuotes` and in Stage 3 `saveQuotes`, for every trip cost, in every quote.** There is no tier selection anywhere in this workflow. Do not look up a tier, do not compare the trip cost to a cap, do not ask the user.

`coverageAmount` is **mandatory** for STCIH. Sent without it, `getQuotes` returns `No Rates Error` and the plan disappears from the Stage 2 table.

Rules:

- Always exactly one `plans[]` entry: `{ code: "STCIH", tripPreference: { tripCost, coverageAmount: 30000, deductible: 0 }, adjustments: [] }`.
- Never send `800` or `1500`. Those tiers exist on CoverMe.com and are offered to the customer there via the Edit button — see the **STCIH single-tier success block** in `references/verbatim-messages.md`. They are never quoted in chat.
- **Only exception:** if `tripCost > 30000`, drop STCIH entirely from the `getQuotes` request — the server returns `Trip cost can not exceed 30,000`. Do not surface that limit to the user.
- Never emit the integer `30000` in any user-facing message. The user-facing label is always `Unlimited coverage`.

## EN plan catalog

### SAIH → Single-trip All-inclusive plan
- Up to $10 million in emergency medical benefits
- Trip cancellation and trip interruption insurance
- Baggage loss, damage, or delay insurance
- Flight accident and travel accident insurance

[All-inclusive travel insurance for travelling Canadians \| Manulife](https://www.coverme.com/travel-insurance/content/dam/consumer-portal/documents/en/travel/single-trip-all-inclusive-policye.pdf)

### SNMIH → Non-medical Inclusive plan
- Trip cancellation and trip interruption insurance
- Baggage loss, damage, or delay insurance
- Flight accident and travel accident insurance

[Non-medical inclusive travel insurance \| Manulife Canada](https://www.coverme.com/travel-insurance/content/dam/consumer-portal/documents/en/travel/non-medical-inclusive-policye.pdf)

### STCIH → Trip Cancellation and Trip Interruption plan
- Trip cancellation and trip interruption insurance

[Trip cancellation and trip interruption travel insurance \| Manulife](https://www.coverme.com/travel-insurance/content/dam/consumer-portal/documents/en/travel/trip-cancellation-and-interruption-policye.pdf)

### SEMH → Single-Trip Emergency Medical Plan
- Coverage outside of Canada and within Canada, outside your province or territory of residence
- Up to $10 million in emergency medical benefits
- Premium savings of 50% compared to the standard Single-trip Emergency Medical plan when your entire trip is within Canada.

[Emergency medical travel insurance \| Manulife Canada](https://www.coverme.com/travel-insurance/content/dam/consumer-portal/documents/en/travel/single-trip-emergency-medical-policye.pdf)

### SYDELH → Youth Deluxe All-inclusive plan
- Comprehensive travel coverage for people under 30 years of age and trips less than 30 days.
- Up to $5 million in emergency medical benefits
- Trip cancellation and trip interruption insurance
- Baggage loss, damage, and delay insurance
- Flight accident and travel accident insurance

[Youth deluxe all-inclusive travel insurance \| Manulife Canada](https://www.coverme.com/travel-insurance/content/dam/consumer-portal/documents/en/travel/youth-deluxe-policye.pdf)

### SYAIH → Youth All-inclusive plan
- Comprehensive travel coverage for people under 30 years of age
- Up to $1 million in emergency medical benefits
- Trip cancellation and trip interruption insurance
- Baggage loss, damage, and delay insurance
- Flight accident and travel accident insurance

[Youth all-inclusive travel insurance \| Manulife Canada](https://www.coverme.com/travel-insurance/content/dam/consumer-portal/documents/en/travel/youth-all-inclusive-policye.pdf)

## FR plan catalog (use in FR flow)

### SAIH → Régime Voyage unique Tous risques
- Jusqu'à concurrence de 10 millions de dollars pour la garantie soins médicaux d'urgence
- Annulation et interruption de voyage
- Bagages perdus, endommagés ou retardés
- Accident de vol et Accident de voyage

[Assurance voyage tous risques pour les voyageurs canadiens \| Manuvie](https://www.pourmeproteger.com/travel-insurance/content/dam/consumer-portal/documents/fr/travel/single-trip-all-inclusive-policyf.pdf)

### SNMIH → Régime Forfait sans soins médicaux
- Annulation de voyage et Interruption de voyage
- Bagages perdus, endommagés ou retardés
- Accident de vol et Accident de voyage

[Assurance voyage sans soins médicaux \| Manuvie Canada](https://www.pourmeproteger.com/travel-insurance/content/dam/consumer-portal/documents/fr/travel/non-medical-inclusive-policyf.pdf)

### STCIH → Régime Annulation de voyage et Interruption de voyage
- Annulation de voyage et Interruption de voyage

[Garantie Annulation et interruption de voyage \| Manuvie](https://www.pourmeproteger.com/travel-insurance/content/dam/consumer-portal/documents/fr/travel/trip-cancellation-and-interruption-policyf.pdf)

### SEMH → Régime Soins médicaux d'urgence – Voyage unique
- Couverture à l'extérieur du Canada et au Canada, à l'extérieur de votre province ou territoire de résidence
- Jusqu'à concurrence de 10 millions de dollars pour la garantie soins médicaux d'urgence
- Économies de primes de 50 % par rapport au régime standard Soins médicaux d'urgence – Voyage unique lorsque votre voyage se déroule au complet au Canada

[Assurance voyage pour soins médicaux d'urgence \| Manuvie Canada](https://www.pourmeproteger.com/travel-insurance/content/dam/consumer-portal/documents/fr/travel/single-trip-emergency-medical-policyf.pdf)

### SYDELH → Régime de luxe Tous risques pour les jeunes
- Assurance voyage complète pour les personnes de moins de 30 ans et les voyages de moins de 30 jours Jusqu'à concurrence de cinq millions de dollars pour une couverture médicale d'urgence
- Annulation et interruption de voyage
- Bagages perdus, endommagés ou retardés
- Accident de vol et Accident de voyage

[Assurance voyage tous risques de luxe pour les jeunes \| Manuvie Canada](https://www.pourmeproteger.com/travel-insurance/content/dam/consumer-portal/documents/fr/travel/youth-deluxe-policyf.pdf)

### SYAIH → Régime Tous risques pour les jeunes
- Assurance voyage complète pour les personnes de moins de 30 ans
- Jusqu'à concurrence d'un million de dollars pour la garantie soins médicaux d'urgence
- Assurance annulation et interruption de voyage
- Bagages perdus, endommagés ou retardés
- Accident de vol et Accident de voyage

[Assurance voyage tous risques pour les jeunes \| Manuvie Canada](https://www.pourmeproteger.com/travel-insurance/content/dam/consumer-portal/documents/fr/travel/youth-all-inclusive-policyf.pdf)
