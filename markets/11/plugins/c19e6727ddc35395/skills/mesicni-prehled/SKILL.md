---
name: mesicni-prehled
description: "Měsíční přehled energií pro vedení na jednu stranu: spotřeba elektřiny a plynu za poslední uzavřený měsíc, srovnání s předchozím měsícem a s loňskem, největší změny po odběrných místech, náklady, otevřené anomálie a blížící se výpovědní lhůty smluv. Použij pro měsíční report, souhrn za měsíc, přehled pro vedení nebo otázku „jak jsme na tom s energiemi“."
metadata:
  title: Měsíční přehled energií
  short-description: Přehled spotřeby, nákladů, anomálií a smluv za minulý měsíc
  version: 1.0.0
  tools: [get_organization_overview, get_data_quality, get_consumption, get_costs, get_anomalies, list_contracts, verify_figures]
  modules: [dashboard]
---

# Měsíční přehled energií

Nejdřív si přečti `references/pravidla.md` a dodržuj je. Prahové hodnoty jsou v `references/kriteria.md`,
šablona odpovědi v `assets/vystup.md`.

Cíl: jedna strana pro vedení o posledním uzavřeném měsíci. Každé číslo z nástroje, s citací [F…].

## 1. Urči měsíc a dostupná data

- Měsíc = poslední uzavřený kalendářní měsíc (Europe/Prague), pokud uživatel neurčí jiný. Běžící měsíc nikdy
  nehodnoť jako celý; když ho uživatel chce, označ ho jako neuzavřený.
- Zavolej `get_organization_overview()`. Z `data.meteringPoints` zjisti, zda organizace má OM elektřiny a plynu
  (počet větší než 0). Z `data.capabilities` zjisti, které z nástrojů `get_costs`, `get_anomalies` a
  `list_contracts` jsou dostupné; nedostupnou část přehledu vynech a napiš proč.
- Zavolej `get_data_quality(from=<RRRR-MM-01>, to=<poslední den měsíce RRRR-MM-DD>)`. Při úplnosti pod 95 % nebo
  odhadech nad 10 % začni přehled upozorněním (pravidlo 12).

## 2. Spotřeba po komoditách

Pro každou komoditu, kterou organizace má, zavolej dvakrát `get_consumption`:

1. Srovnání s předchozím měsícem:
   `get_consumption(commodity=<electricity|gas>, from=<RRRR-MM>, to=<RRRR-MM>, granularity=month, unit=MWh, compare=previous_period)`.
   Celková spotřeba je v `data.total`, změna v `data.comparison.changePct`; oboje má figure v `figures`.
2. Srovnání s loňskem a změny po OM:
   `get_consumption(commodity=<electricity|gas>, from=<RRRR-MM>, to=<RRRR-MM>, granularity=month, unit=MWh, compare=same_period_last_year, breakdown=meteringPoint)`.
   Meziroční změna je v `data.comparison.changePct`, po OM v `data.byMeteringPoint[]` (`name`, `total`,
   `previousTotal`, `changePct`, `completeness`).

U plynu zkontroluj `data.gasCoverage`: část spotřeby bez přepočtu na kWh (`unconvertedVolumeM3`) uveď zvlášť v m³
a nesčítej ji s MWh.

## 3. Největší změny po odběrných místech

- Z `data.byMeteringPoint[]` meziročního volání vyber nejvýše 3 OM, která splňují kritérium „top změna“
  v `references/kriteria.md`, seřazená podle absolutní hodnoty `changePct`.
- Uveď `total`, `previousTotal` a `changePct` tak, jak je vrátil nástroj. Rozdíl v MWh nepočítej a necituj.
- OM s `changePct: null` (chybí loňská data) nezařazuj a nevydávej za nulovou změnu.

## 4. Náklady

- Náklady portál eviduje po kalendářních rocích z potvrzených faktur; měsíční součet nákladů není k dispozici.
- Zavolej `get_costs(commodity=<electricity|gas>, year=<RRRR>)` pro rok zvoleného měsíce. Uveď celkové náklady od
  začátku roku `data.total.amountCzk` (bez DPH) a průměrnou cenu `data.total.averagePriceCzkPerMwh`.
- Z `data.invoices[]` uveď faktury, jejichž období (`periodFrom`, `periodTo`) spadá do zvoleného měsíce, s částkou
  `totalNetCzk` (bez DPH). Nesčítej je.
- `data.total.amountCzk: null` znamená, že portál nemá potvrzenou fakturu; napiš to, neuváděj 0 Kč.

## 5. Anomálie

- Zavolej `get_anomalies(from=<RRRR-MM-01>, to=<poslední den měsíce RRRR-MM-DD>, status=open)`.
- Počty nevyřízených anomálií jsou v `data.counts` (`electricityPending`, `gasPending`), jednotlivé anomálie
  v `data.items[]` (`meteringPointName`, `date`, `severity`, `excessPct`). Uveď nejvýše 3 se závažností `high`,
  jinak `medium`.

## 6. Smlouvy

- Zavolej `list_contracts(status=expiring, expiringWithinDays=365, includePlaybook=false)`.
- Uveď smlouvy, u kterých je `daysToNoticeDeadline` nebo `daysToEnd` do 90 dní (kritérium v `references/kriteria.md`),
  s `noticeDeadline`, `validTo` a `supplierName`. Smlouvu s `autoRenewalTrap: true` označ jako past
  automatického prodloužení.

## 7. Přepočti klíčová čísla

- Zavolej jednou `verify_figures(claims=[…])` s `figureId` nejvýše 10 klíčových čísel přehledu (spotřeba,
  meziroční změna, náklady od začátku roku, termíny smluv). Každé tvrzení: `{"figureId": "fig_…", "value": <číslo>,
  "unit": "<jednotka>"}`.
- Číslo s verdiktem `odchylka` nahraď správnou hodnotou z výsledku; `nelze_overit` uveď s důvodem.

## 8. Odpověz

Použij šablonu `assets/vystup.md`: Shrnutí (3 věty) → Klíčová čísla [F…] → Top 3 změny po OM → Anomálie →
Smlouvy do 90 dní → Doporučení k posouzení → Jak si to ověřit.

## Nikdy

- Nesčítej elektřinu a plyn do jednoho čísla a nepřeváděj m³ na kWh.
- Nevydávej náklady od začátku roku za náklady měsíce.
- Nepočítej rozdíly ani podíly sám; ber `changePct` a další hodnoty z nástrojů.
- Nehodnoť neuzavřený měsíc jako celý.
