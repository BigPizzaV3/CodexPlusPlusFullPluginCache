---
name: estimar-ahorro-solar
description: Take a home or business in Mexico from its CFE bill (kWh, tariff, state) to a solar system size and a 25-year savings estimate with the Zenit Solar tools. Use it when someone asks whether solar panels are worth it for them, how many panels they need or how fast a system pays for itself.
---

Use this skill when a user in Mexico wants to know whether solar panels are
worth it, how many panels they need, or how long a system takes to pay for
itself. Every figure comes from the Zenit Solar tools; never estimate by hand.

## Inputs to gather (ask only for what is missing)

1. **Consumption in kWh.** A CFE residential bill is usually bimonthly and a
   commercial bill monthly. Pass a bimonthly figure as `bimonthlyKwh` when
   sizing, and half of it as `monthlyKwh` when estimating a bill. If the user
   only knows the amount in pesos, ask for the kWh printed on the bill; do not
   guess it.
2. **The CFE tariff** printed on the bill (1, 1A–1F, DAC, PDBT, GDBT, GDMTO,
   GDMTH…). A residential user who does not know it can proceed with the
   default (tariff 1); say that the tariff was assumed.
3. **The state** where the service is located. It sets the tariff region, the
   summer season and the solar yield. If it is missing, the tools fall back to
   the Central region and report it in `region.fuente`; tell the user which
   region was assumed.

## Steps

1. `calculate_system_size` with the consumption and state: panels, installed
   kW and expected annual production. When the user only asked how many
   panels they need, stop here and offer the savings estimate as a next step.
2. When the user asked about savings, payback or whether solar is worth it:
   `estimate_solar_savings` with the same consumption, tariff and state gives
   the annual and 25-year savings. Include `systemPriceMxn` only when the user
   gave a price; the tool then also returns payback, IRR and NPV.
3. Optionally `calculate_cfe_bill` to show what the current bill looks like
   month by month, including the summer season.

## Output

- Report the number of panels, installed kW, annual production, first-year
  savings and 25-year savings in Mexican pesos, plus payback, IRR and NPV when
  a price was given.
- Label everything as an estimate based on CFE's published tables and typical
  solar yields, not a quotation.
- Repeat the assumptions the tools made: region, tariff, the 4 % annual rate
  escalation and VAT at the general 16 % rate.

## Do not

- Do not invent consumption, prices or production figures; use only tool
  results.
- Do not recommend specific installers or products, and do not quote prices
  the user did not provide.
- Do not use these tools for utilities outside Mexico; explain that they only
  cover CFE tariffs.
