---
name: anomalie-spotreby
description: "Rozbor anomálií a neobvyklé spotřeby elektřiny a plynu: noční a víkendový základní odběr, spotřeba v neprovozní dny, čtvrthodinové špičky a odchylky od očekávání. Použij, když uživatel hledá plýtvání, neobvyklou nebo podezřelou spotřebu, vysoký základní odběr, spotřebu mimo provoz nebo příčinu nárůstu spotřeby."
metadata:
  title: Anomálie a základní odběr
  short-description: Anomálie, základní odběr a spotřeba mimo provoz
  version: 1.0.0
  tools: [get_organization_overview, get_data_quality, get_anomalies, get_load_profile, get_consumption, verify_figures]
  modules: [dashboard]
---

# Anomálie a základní odběr

Nejdřív si přečti `references/pravidla.md` a dodržuj je. Prahové hodnoty jsou v `references/kriteria.md`,
šablona odpovědi v `assets/vystup.md`.

Cíl: najít, kde a kdy se spotřebovává víc, než by měla (anomálie, vysoký základní odběr, spotřeba v neprovozní
dny), a navrhnout, co prověřit v provozu.

## 1. Zjisti, co je k dispozici

- Zavolej `get_organization_overview()`. `get_anomalies` vyžaduje modul ISO 50001; když má v `data.capabilities`
  `available: false`, řekni to a pokračuj krokem 3 (profil zatížení je v modulu dashboard).
- Zavolej `get_data_quality(from=<RRRR-MM-DD před 90 dny>, to=<včera RRRR-MM-DD>)`. Anomálie ani základní odběr
  nehodnoť u OM s červeným hodnocením; napiš proč.

## 2. Anomálie

- Zavolej `get_anomalies(status=open)` (výchozí období 90 dní, obě komodity). Uživatelem jmenované OM:
  `get_anomalies(status=open, meteringPointId=<id OM>)`.
- Z `data.items[]` vyber anomálie se `severity` `high` a `medium` (kritérium v `references/kriteria.md`).
  Ke každé uveď `meteringPointName`, `date`, `dayType`, `consumption` proti `expected` v `energyUnit`,
  `excessPct`, `excessEnergy`, u elektřiny `peakKw` proti `expectedPeakKw` a `peakAt`, případně `excessCostCzk`.
- Počty jsou v `data.counts` (`electricityPending`, `gasPending`). Řádky v m³ a v kWh nikdy nesčítej.
- Při `data.nextCursor` načti další stránku se stejnými parametry a `cursor=<data.nextCursor>`, jen když uživatel
  chce úplný seznam.

## 3. Základní odběr a spotřeba mimo provoz (elektřina)

- Pro každé posuzované OM elektřiny (nejvýše 5) zavolej
  `get_load_profile(meteringPointIds=[<id OM>], includeBaseLoad=true, includeCalendar=true)`. Výchozí období je
  poslední celý měsíc; ukazatele základního odběru vyžadují právě jedno OM.
- Ukazatele: `data.indicators.averageLoadKw`, `data.indicators.minHourlyLoadKw` a
  `data.indicators.baseLoadShareOfAveragePct` (nejnižší hodinové zatížení v % průměrného),
  `data.indicators.weekendToWorkdayPct`.
- Základní odběr podle ISO 50001: `data.baseLoad` (`avg30Kw`, `referenceKw`, `deviationPct`, `excessKwhPerYear`,
  `excessCostCzkPerYear`, `offHoursStatus`, `offHoursSharePctLast30Days`). Když `data.baseLoad.resultStatus` není
  `complete`, uveď u čísla, že vychází z neúplných dat (`completenessPct`).
- Neprovozní dny: `data.nonOperatingDays` (`days`, `averageKwhPerDay`, `operatingAverageKwhPerDay`, `ratioPct`)
  podle provozního kalendáře v `data.calendar`. Když kalendář chybí, napiš, že neprovozní dny nelze určit.
- Hodinový a týdenní profil (`data.hourly`, `data.weekly`) použij k popisu, kdy odběr neklesá (noc, víkend).

## 4. Detail kolem nejvýznamnějších anomálií

Pro nejvýše 3 nejvýznamnější anomálie zavolej
`get_consumption(commodity=<electricity|gas>, meteringPointIds=[<id OM>], from=<datum − 7 dní>, to=<datum + 7 dní>, granularity=day)`
a popiš, zda jde o jednorázovou špičku, nebo o trvalou změnu úrovně spotřeby (`data.series`).

## 5. Použij kritéria

Podle `references/kriteria.md` označ každé OM a anomálii „prověřit“ nebo „v normě“. Ukazatel s hodnotou null
označ „nelze posoudit“.

## 6. Přepočti čísla

Zavolej jednou `verify_figures(claims=[…])` s `figureId` čísel, na kterých stojí závěr (spotřeba kolem anomálie,
nejvyšší špička z profilu zatížení). Ukazatele bez figure (podíly základního odběru, poměr neprovozních dnů) uveď
se zdrojem a odkazem `portalUrl`.

## 7. Odpověz

Použij šablonu `assets/vystup.md`: Shrnutí → Zjištění (anomálie, základní odběr, neprovozní dny) → Hodnocení podle
kritérií → Doporučení k posouzení (co prověřit v provozu: osvětlení, vzduchotechnika, kompresory, chlazení,
standby technologie; s předpoklady) → Jak si to ověřit.

## Nikdy

- Netvrď příčinu anomálie jako fakt; data ukazují kdy a kolik, ne proč.
- Nesčítej kWh a m³ ani anomálie elektřiny a plynu do jednoho čísla.
- Nevydávej `excessCostCzk` nebo `excessCostCzkPerYear` za ověřenou úsporu; je to odhad portálu.
- Nehodnoť neprovozní dny bez provozního kalendáře.
