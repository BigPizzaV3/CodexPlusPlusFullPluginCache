# Kritéria: Rezervovaná kapacita a jistič

Výchozí prahové hodnoty pilotu. Upravují se podle zpětné vazby klientů.

| Závěr | Podmínka | Zdroj |
|---|---|---|
| Překročení (nález) | `exceeded: true` v kterémkoli měsíci, tj. `exceedanceCount` ≥ 1 | `get_capacity_analysis` |
| Riziko překročení | `maxUtilizationPct` > 95 % za 12 měsíců | `get_capacity_analysis` |
| Prostor ke snížení | `maxUtilizationPct` < 80 % za 12 měsíců a žádné překročení | `get_capacity_analysis` |
| Nastaveno přiměřeně | `maxUtilizationPct` mezi 80 % a 95 % a žádné překročení | `get_capacity_analysis` |
| Nelze posoudit | `exceedanceCount: null`, `maxUtilizationPct: null` nebo méně než 6 měsíců s daty (`monthsWithData`) | `get_capacity_analysis` |

## Zohlednit vždy

- **Sezónnost:** posuď 24 měsíců; maximum jedné sezóny nesmí rozhodnout o snížení na celý rok.
- **Plánované změny provozu:** nové stroje, rozšíření provozu, elektromobilita, tepelná čerpadla. Zeptej se na ně.
- **Roční a měsíční RK:** měsíční RK může pokrýt sezónní špičku; uveď, který typ platí (`data.capacity.history[].type`).
- **NN (hlavní jistič):** porovnej maxima z faktur (`maxKw`), pokud jsou, s orientačním výkonem jističe
  (`breakerApparentPowerKva`). Bez průběhového měření maxima chybějí a velikost jističe z dat posoudit nelze.
- **Plyn:** porovnej `maxDailyM3` s `bookedDailyM3`; m³/den nepřeváděj na kWh.

## Doporučení

| Závěr | Doporučení k posouzení |
|---|---|
| Překročení | zvážit zvýšení RK nebo řízení špiček (posun spouštění strojů); uvést měsíce a časy špiček |
| Riziko překročení | ponechat nebo mírně zvýšit; hlídat špičky v rizikových měsících |
| Prostor ke snížení | zvážit snížení RK s rezervou nad dosaženým maximem; předpoklad: provoz se nezmění |
| Nastaveno přiměřeně | ponechat |
