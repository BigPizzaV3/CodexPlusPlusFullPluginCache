---
name: obnova-smlouvy
description: "Příprava na obnovu nebo výpověď smlouvy na dodávku elektřiny či plynu: termíny, výpovědní lhůta, automatické prodloužení, checklist obnovy, srovnání fixní ceny a spotu na vlastním odběrovém profilu a tržní ceny. Použij, když se uživatel ptá na konec smlouvy, výpověď, obnovu, nákup energie na další rok, fix nebo spot, nebo na nabídku dodavatele."
metadata:
  title: Obnova smlouvy
  short-description: Termíny, checklist a fix vs spot před obnovou smlouvy
  version: 1.0.0
  tools: [get_organization_overview, get_data_quality, list_contracts, get_consumption, analyze_fix_vs_spot, get_market_prices, verify_figures]
  modules: [contracts]
---

# Obnova smlouvy

Nejdřív si přečti `references/pravidla.md` a dodržuj je. Prahové hodnoty jsou v `references/kriteria.md`,
šablona odpovědi v `assets/vystup.md`.

Cíl: připravit uživatele na rozhodnutí o obnově nebo výpovědi smlouvy: kdy nejpozději jednat, co ještě chybí
a jak by na jeho vlastním odběru dopadla fixní cena proti spotu. Nákupní rozhodnutí je na něm.

## 1. Zjisti, co je k dispozici

- Zavolej `get_organization_overview()`. V `data.capabilities` zkontroluj `list_contracts` (modul smlouvy),
  `analyze_fix_vs_spot` (modul spot-advanced) a `get_market_prices`. Nedostupnou část vynech a napiš proč.

## 2. Najdi smlouvu a termíny

- Pro konkrétní OM: `list_contracts(meteringPointId=<id OM>, includePlaybook=true, includePriceHistory=true)`.
- Přehled smluv, které vyžadují pozornost: `list_contracts(status=needs_action, includePlaybook=true)`; smlouvy
  končící v příštím roce: `list_contracts(status=expiring, expiringWithinDays=365, includePlaybook=true)`.
- Z `data.items[]` vezmi: `supplierName`, `commodity`, `productType`, `validFrom`, `validTo`, `noticePeriodDays`,
  `noticeDeadline`, `daysToNoticeDeadline`, `daysToEnd`, `autoRenewal`, `autoRenewalExtendsMonths`,
  `autoRenewalTrap`, `status`, cenu (`fixPriceCzkMwh`, `fixPriceEurMwh`, `priceCzkMwh`) a `portalUrl`.
- Termíny konce a výpovědní lhůty mají figure (`contract_end`, `notice_deadline`); cituj je [F…].
- `noticeDeadline: null` znamená, že lhůtu nelze určit (chybí konec nebo výpovědní doba); řekni to a doporuč doplnit
  smlouvu v portálu.

## 3. Checklist obnovy

- Stav přípravy je v `data.items[].playbook`: `state`, `noticeGiven` (výpověď podána), `documentsPrepared`
  (podklady připraveny), `internallyApproved` (schváleno interně). Checklist portál vrací pro smlouvy s lhůtou do
  180 dní.
- Vývoj ceny a spotřeby po letech je v `data.items[].priceHistory[]` (`year`, `priceCzkMwh`, `consumptionKwh`,
  `costCzk`).
- Srovnání s trhem podle portálu: `data.items[].savings` (`kind`, `annualSavingsCzk`, `currentPriceCzkMwh`,
  `referencePriceCzkMwh`).

## 4. Objem a profil odběru

- Zavolej `get_data_quality(meteringPointIds=[<id OM>], from=<RRRR-MM-01 před 12 měsíci>)`.
- Zavolej `get_consumption(commodity=<electricity|gas>, meteringPointIds=[<id OM>], from=<RRRR-MM před 12 měsíci>, to=<poslední uzavřený měsíc RRRR-MM>, granularity=month, unit=MWh)`.
  Roční objem je v `data.total`, průběh po měsících v `data.series`.

## 5. Fix proti spotu na vlastním profilu (elektřina)

- Zavolej `analyze_fix_vs_spot(from=<RRRR-MM před 12 měsíci>, to=<poslední uzavřený měsíc RRRR-MM>, contractId=<id smlouvy>)`.
  Když smlouva nemá fixní cenu v EUR a uživatel má nabídku v EUR/MWh, zavolej
  `analyze_fix_vs_spot(from=<RRRR-MM>, to=<RRRR-MM>, meteringPointIds=[<id OM>], fixPriceEurMwh=<cena z nabídky>)`.
  Cenu v Kč na EUR sám nepřeváděj; bez ceny v EUR srovnání neprováděj a řekni proč.
- Výsledek je v EUR a jen za komoditní část (bez distribuce, marže dodavatele a DPH): `data.analysis`
  (`fixCostEur`, `spotCostEur`, `fixMinusSpotEur`, `differencePct`, `cheaper`, `monthly[]`), kumulativně
  `data.cumulative`, potenciál nákupu v levnějších hodinách `data.savingPotential`. Částky v Kč jen tehdy, když je
  `data.fx` vyplněné (jeden kurz ČNB, datum v `rateDate`).
- Pro plyn tento nástroj srovnání neposkytuje; uveď jen tržní kontext z kroku 6.

## 6. Tržní kontext

- Zavolej `get_market_prices(commodity=<electricity|gas>, from=<RRRR-MM-DD před 3 měsíci>, to=<včera RRRR-MM-DD>, granularity=day, includeForwards=true)`.
- Průměr, minimum a maximum spotu jsou v `data.average`, `data.min`, `data.max` (EUR/MWh), forwardy
  v `data.forwards[]` (`productCode`, `deliveryLabel`, `settlementEurMwh`, `settlementDate`, `settlementCzkMwh`).
- Průměrná tržní cena je jen kontext. Rozhodnutí fix nebo spot opírej o výsledek na vlastním profilu (krok 5).

## 7. Ověř termíny a klíčová čísla

Zavolej jednou `verify_figures(claims=[…])`: termíny `{"figureId": "<id figure termínu>", "at": "<RRRR-MM-DD>", "unit": "date"}`,
roční objem a průměrnou spotovou cenu `{"figureId": "fig_…", "value": <číslo>, "unit": "<MWh|EUR/MWh>"}`.

## 8. Odpověz

Použij šablonu `assets/vystup.md`: Termíny (konec, výpovědní lhůta [F], dny do ní) → Checklist → Fix vs spot na
vašem profilu → Tržní kontext → Doporučení k posouzení (s předpoklady) → Jak si to ověřit.

## Nikdy

- Nedávej závazné doporučení k nákupu; jde o podklad k rozhodnutí.
- Neporovnávej produkty na průměrné tržní ceně místo vlastního profilu.
- Nepřeváděj EUR na Kč jiným kurzem, než vrátil nástroj, a nesčítej výsledek fix vs spot s distribucí nebo DPH.
- Nepřehlédni automatické prodloužení (`autoRenewalTrap`), ani když je lhůta daleko.
