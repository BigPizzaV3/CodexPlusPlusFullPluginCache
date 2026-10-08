# Lenguaje doméstico para España

Read this reference only when technical units, Spanish electricity-market
concepts or appliance examples appear in the answer.

## Start with the consequence

Say first what the person can do or what the evidence means. Put the technical
measurement after it as support.

- Prefer "entre las 12:00 y las 15:00 tus placas suelen cubrir la casa" over
  starting with a threshold or percentile.
- Prefer "hay margen observado, pero aún no suficiente para cambiar el
  contrato con seguridad" over starting with an analytical status.
- Prefer "hoy la hora barata es..." over listing 24 prices before the answer.

## Terms people recognise

Use the everyday phrase first and add the precise term only when useful:

| Everyday Spanish | Precise meaning |
| --- | --- |
| lo que consume tu casa | consumo de la vivienda |
| lo que producen tus placas | producción fotovoltaica |
| lo que compras de la red | importación de red |
| lo que viertes o te sobra | grid export or measured surplus, only when supported |
| potencia contratada | límite de potencia simultánea del contrato |
| horas valle | returned low-price or P2 period; do not assume a schedule |

Do not use "energia gratis". Solar generation has an installation cost and an
exported kWh is not equivalent to an avoided imported kWh unless VaDa returns
that economic comparison.

## Units without a lesson in electricity

- `kWh` responde a "cuánta energía se usó o produjo durante un periodo".
- `kW` responde a "cuánta potencia coincidió a la vez" and is the relevant idea
  for contracted power.
- `EUR/kWh` is the price applied to each unit of energy. State whether it is
  import, export compensation, tax-inclusive or otherwise only when returned.

Explain the distinction in one sentence when two units appear together. Do not
compare an hourly average in kWh with a 15-minute maximum in kW as if they were
the same measurement.

## Household appliances

Name the practical window first. If VaDa uses a typical appliance profile,
call it "un ciclo habitual" or "una referencia orientativa", never the user's
measured appliance. A favourable solar window does not guarantee that the
entire washing-machine, dishwasher, dryer, water-heater or pool-pump cycle is
covered.

## Spanish presentation conventions

- Use the 24-hour clock: `13:30`, not AM/PM.
- In prose use decimal comma: `6,5 kW`, `0,24 EUR/kWh`.
- Use `EUR` when the tool returns it; use the euro sign in natural prose when
  no ambiguity is introduced.
- Keep official contractual labels such as P1 and P2, but explain them in
  ordinary language the first time they affect the conclusion.
- Do not infer the user's distributor, retailer, tariff schedule, taxes or
  export-compensation terms from the country alone.
