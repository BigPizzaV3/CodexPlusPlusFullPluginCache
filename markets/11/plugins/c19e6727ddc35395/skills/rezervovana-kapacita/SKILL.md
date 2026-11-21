---
name: rezervovana-kapacita
description: "Posouzení rezervované kapacity (RK, rezervovaný příkon), hlavního jističe nebo denní rezervované kapacity plynu: překročení, využití, prostor ke snížení a riziko pokut. Použij, když se uživatel ptá na rezervovanou kapacitu, jistič, čtvrthodinová maxima, překročení kapacity, platby za příkon v distribuci nebo zda má kapacitu správně nastavenou."
metadata:
  title: Rezervovaná kapacita a jistič
  short-description: Využití a překročení rezervované kapacity nebo jističe
  version: 1.0.0
  tools: [get_organization_overview, get_data_quality, list_metering_points, get_metering_point, get_capacity_analysis, get_load_profile, list_distribution_tariffs, verify_figures]
  modules: [map, dashboard]
---

# Rezervovaná kapacita a jistič

Nejdřív si přečti `references/pravidla.md` a dodržuj je. Prahové hodnoty jsou v `references/kriteria.md`,
šablona odpovědi v `assets/vystup.md`.

Cíl: pro každé posuzované odběrné místo říct, zda byla kapacita překročena, jak je využitá a zda je prostor ji
snížit nebo potřeba ji zvýšit. Rozhodnutí je na uživateli.

## 1. Zjisti, co je k dispozici

- Zavolej `get_organization_overview()` a v `data.capabilities` zkontroluj `get_capacity_analysis` a
  `get_load_profile`. Bez `get_capacity_analysis` postup nelze provést; řekni proč.

## 2. Vyber odběrná místa

- Když uživatel OM nejmenuje, zavolej `list_metering_points(commodity=<electricity|gas>)` a vyber OM, u kterých
  se kapacita posuzuje: elektřina VN a VVN s `reservedCapacityKw`, elektřina NN s `breaker`, plyn s denní
  rezervovanou kapacitou. Při více než 5 OM se zeptej, na která se zaměřit.
- Konkrétní OM najdi přes `list_metering_points(query=<název nebo město>)`.
- Zavolej `get_data_quality(meteringPointIds=[<id OM>])`. Maxima pocházejí z faktur distributora, takže úplnost
  průběhových dat se týká jen vysvětlení špiček v kroku 4.

## 3. Vyhodnoť kapacitu

- Zavolej `get_capacity_analysis(meteringPointId=<id OM>, months=12)`. Pro posouzení sezónnosti (topná sezóna,
  sezónní výroba) zavolej `get_capacity_analysis(meteringPointId=<id OM>, months=24)`.
- `data.kind` říká, co se posuzuje: `reserved_capacity` (RK), `main_breaker` (hlavní jistič), `gas_daily_capacity`
  (denní rezervovaná kapacita plynu), `none` (neposuzuje se; řekni to a OM přeskoč).
- Po měsících jsou v `data.months[]`: `month`, `maxKw` a `maxAt` (čtvrthodinové maximum z faktury), `reservedKw`,
  `utilizationPct`, `exceeded`; u plynu `maxDailyM3` a `bookedDailyM3`.
- Souhrn je v `data.summary`: `exceedanceCount` (null = nelze určit, ne 0), `maxKw`, `maxAt`, `maxUtilizationPct`,
  `currentReservedKw`, `monthsWithData`, `monthsInWindow`.
- U jističe je velikost v `data.breaker` (`display`, např. 3×25 A) a orientační výkon v `data.breakerApparentPowerKva`.

## 4. Vysvětli nejvyšší špičku

- Pro měsíc s nejvyšším maximem (`data.summary.maxAt`) zavolej
  `get_load_profile(meteringPointIds=[<id OM>], from=<RRRR-MM>, to=<RRRR-MM>, topPeaks=5)`.
- Z `data.topPeaks[]` (`at`, `kw`) popiš, kdy špičky vznikají (den v týdnu, hodina). Profil zatížení je jen pro
  elektřinu s průběhovým měřením; jinak napiš, že čas špiček nelze z dat určit.
- 15minutová maxima z průběhových dat a maxima z faktur se mohou lišit; pro hodnocení platí faktura.

## 5. Platby za příkon

- Zavolej `get_metering_point(meteringPointId=<id OM>)`. Historie kapacity je v `data.capacity.history[]` (`type`
  roční nebo měsíční, `valueKw`, `billingPeriodFrom`, `billingPeriodTo`, `amountCzk` = zaplaceno za RK, jen
  s kategorií dat náklady). Smlouvy s distributorem jsou v `data.contracts[]`.
- Zavolej `list_distribution_tariffs(commodity=<electricity|gas>, tariff=<kód sazby>)`. Ceny ERÚ za rezervovanou kapacitu
  v této verzi portál neeviduje (`data.priceSourceAvailable: false`), proto úsporu ze snížení RK v Kč nevyčísluj;
  uveď jen, kolik portál eviduje zaplaceno (`amountCzk`).

## 6. Použij kritéria

Podle `references/kriteria.md` urči pro každé OM jeden závěr: překročení (nález), riziko překročení, prostor ke
snížení, nebo nastaveno přiměřeně. Zohledni sezónnost (24 měsíců) a plánované změny provozu, na které se zeptej.

## 7. Přepočti čísla

Zavolej jednou `verify_figures(claims=[…])` s `figureId` počtu překročení a nejvyššího maxima z výsledku
`get_capacity_analysis` (každé tvrzení `{"figureId": "fig_…", "value": <číslo>, "unit": "<count|kW>"}`).

## 8. Odpověz

Použij šablonu `assets/vystup.md`: Shrnutí → Zjištění (tabulka měsíc | maximum [F] | RK | využití | překročení)
→ Hodnocení → Doporučení (snížit / zvýšit / ponechat, s předpoklady a sezónností) → Jak si to ověřit.

## Nikdy

- Nedoporučuj snížení kapacity z dat kratších než 12 měsíců bez výslovné výhrady.
- Nevydávej `exceedanceCount: null` za nulu překročení.
- Nepočítej úsporu ani pokutu v Kč; ceník ERÚ portál zatím neeviduje.
- Nezaměňuj kW a kWh ani m³/den a kWh.
