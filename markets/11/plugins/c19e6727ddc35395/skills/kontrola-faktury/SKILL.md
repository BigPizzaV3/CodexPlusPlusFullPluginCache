---
name: kontrola-faktury
description: "Kontrola faktury nebo vyúčtování za elektřinu či plyn proti naměřeným datům, smluvní ceně a cenovým složkám v ES Zone. Použij, když uživatel chce zkontrolovat, ověřit nebo rozporovat fakturu, vyúčtování, zálohy, fakturované množství, jednotkovou cenu nebo cenu od dodavatele energie, i když fakturu nahrál jako PDF."
metadata:
  title: Kontrola faktury
  short-description: Kontrola faktury za energii proti měření a smlouvě
  version: 1.0.0
  tools: [get_organization_overview, get_data_quality, list_supplier_invoices, list_metering_points, get_consumption, list_contracts, get_costs, list_distribution_tariffs, get_metering_point, verify_figures]
  modules: [dashboard, price, contracts]
---

# Kontrola faktury za energii

Nejdřív si přečti `references/pravidla.md` a dodržuj je. Prahové hodnoty jsou v `references/kriteria.md`,
šablona odpovědi v `assets/vystup.md`.

Cíl: po položkách říct, co na faktuře sedí s daty v ES Zone, co nesedí a co v této verzi portálu ověřit nelze.

## 1. Urči fakturu

- Pokud uživatel nahrál PDF faktury, vytáhni z něj: dodavatele, období, odběrné místo (název nebo EAN),
  množství (kWh nebo MWh, u plynu i m³), jednotkovou cenu silové části, položky distribuce, poplatky, daně,
  DPH, částku bez DPH a celkovou částku s DPH. Hodnoty z PDF v odpovědi označ „podle faktury“.
- Jinak zavolej `list_supplier_invoices(commodity=<electricity|gas>, year=<RRRR>, from=<RRRR-MM-DD>, to=<RRRR-MM-DD>)`
  a nech uživatele vybrat řádek z `data.items[]`. Čísla faktur portál neeviduje (`invoiceNumber` je vždy null);
  fakturu urči podle období (`periodFrom`, `periodTo`) a odběrného místa (`meteringPointName`).
- Odběrné místo najdi přes `list_metering_points(query=<název, město nebo EAN>)`. Když si nejsi jistý, zeptej se.
- Řádek s `possibleDuplicate: true` uživateli ukaž jako možný duplikát; nekontroluj ho, dokud to nepotvrdí.

## 2. Ověř, že máme data

- Zavolej `get_organization_overview()` a zkontroluj v `data.capabilities` dostupnost nástrojů z tabulky níže.
- Zavolej `get_data_quality(meteringPointIds=[<id OM>], from=<začátek období faktury>, to=<konec období faktury>)`.
- Úplnost pod 95 % (`data.overall.completeness` < 0,95): kontrolu množství neprováděj, řekni proč, a pokračuj jen
  cenami a součty.
- Když `data.invoiceInbox` hlásí faktury čekající na zpracování, upozorni, že kontrolovaná faktura možná v portálu
  ještě není potvrzená.

## 3. Porovnej po položkách

| Položka | Nástroj | Pravidlo |
|---|---|---|
| Množství | `get_consumption` | shoda ±1 % podle `differencePct` z `verify_figures`; když `provenance.sources[].type` obsahuje `invoice`, nelze nezávisle ověřit |
| Silová cena | `list_contracts` a `get_metering_point` | shoda ±0,5 %; u spotu nelze ověřit |
| Distribuce a poplatky | `list_distribution_tariffs` a `get_metering_point` | ceník ERÚ v portálu zatím není; ověř jen sazbu, RK nebo jistič a shodu s potvrzeným rozpisem |
| Celkem bez DPH | řádek z `list_supplier_invoices` (figure „Faktura … bez DPH“) | ±1 Kč nebo 0,5 % |
| Celkem s DPH | `totalWithVatCzk` potvrzeného rozpisu | ±1 Kč nebo 0,5 %; DPH nepočítej |

Podrobnosti k položkám:

- **Množství.** Zavolej `get_consumption(commodity=<electricity|gas>, meteringPointIds=[<id OM>], from=<RRRR-MM-DD>, to=<RRRR-MM-DD>, granularity=day, unit=<kWh|MWh|m3>)`.
  Období zadej přesně podle faktury, granularita den. Jednotku zvol podle faktury: plyn fakturovaný
  v m³ porovnávej s `unit=m3`, fakturovaný v kWh nebo MWh s kWh nebo MWh. Nikdy nepřeváděj m³ na kWh. Když
  `data.gasCoverage.unconvertedVolumeM3` není null, část spotřeby nemá přepočet na kWh a kontrola kWh je neúplná.
  Když `provenance.sources[].type` obsahuje `invoice`, spotřeba v portálu pochází (aspoň zčásti) z faktur
  a porovnání s fakturou je kruhové. Napiš doslova: „Množství v portálu pochází z faktury, nelze ho nezávisle
  ověřit.“ Verdikt množství je pak „nelze ověřit“, i když `verify_figures` vrátí shodu.
- **Silová cena.** Zavolej `list_contracts(meteringPointId=<id OM>, includePriceHistory=true)` a
  `get_metering_point(meteringPointId=<id OM>)`. Z `list_contracts` vezmi `productType`, `fixPriceCzkMwh` (u smlouvy v EUR `fixPriceEurMwh`),
  `priceCzkMwh` a `priceHistory`. Cenu silové části z potvrzených faktur najdeš v `data.supplyPrices[]` výsledku
  `get_metering_point` (`periodFrom`, `periodTo`, `rateCzkPerMwh`). U spotového produktu je cena spot + marže;
  spotové ceny portál vede jen v EUR bez ověřeného kurzu, proto silovou cenu spotové faktury označ „nelze ověřit“.
- **Regulované složky.** Zavolej `list_distribution_tariffs(commodity=<electricity|gas>, year=<RRRR>, tariff=<kód sazby>)`.
  V této verzi vrací jen katalog distribučních sazeb:
  `data.priceSourceAvailable` je `false` a `data.prices` je null. Napiš doslova:
  „Regulované složky nelze ověřit — portál zatím neeviduje ceník ERÚ.“ Ověřit lze jen: (a) že sazba na faktuře je v katalogu (`data.tariffs[].code`)
  a odpovídá sazbě OM (`data.meteringPoint.tariff` z `get_metering_point`), (b) že fakturovaná rezervovaná
  kapacita nebo jistič odpovídá `data.meteringPoint.reservedCapacityKw` nebo `data.meteringPoint.breaker`,
  (c) u PDF faktury, která má v portálu potvrzený rozpis za stejné období a OM, že částky položek
  (`amounts.distributionCzk`, `amounts.ozeCzk`, `amounts.systemServicesCzk`, `amounts.networkFeesCzk`,
  `amounts.taxesCzk`) jsou stejné jako na PDF.
- **Kontext nákladů.** Pro srovnání s ročním průměrem můžeš zavolat `get_costs(commodity=<electricity|gas>, year=<RRRR>, meteringPointIds=[<id OM>])`
  a uvést `data.total.averagePriceCzkPerMwh`. Je to roční průměr bez DPH, ne cena této faktury.

## 4. Přepočti čísla jedním voláním

Zavolej jednou `verify_figures(claims=[…])` se všemi čísly, která porovnáváš. Nástroj přepočte čísla portálu ze
stejných dat; rozdíl proti faktuře je porovnání faktury s portálem, ne nezávislé ověření portálu:

- množství z faktury proti figure spotřeby: `{"text": "Množství podle faktury", "figureId": "<id figure spotřeby>", "value": <množství z faktury>, "unit": "<kWh|MWh|m3>"}`;
- částka bez DPH z faktury proti figure řádku faktury: `{"figureId": "<id figure řádku>", "value": <částka bez DPH>, "unit": "CZK"}`;
- částka s DPH z faktury: `{"metric": "cost_total", "invoiceId": "<id řádku>", "commodity": "<electricity|gas>", "vat": "gross", "value": <částka s DPH>, "unit": "CZK"}`.

Rozdíl ber z `difference` a `differencePct` výsledku, kritéria z `references/kriteria.md`. Verdikt
`potvrzeno_s_vyhradou` znamená neúplná data nebo odhady; uveď výhradu z `reservations`.

## 5. Odpověz

Použij šablonu `assets/vystup.md`:

1. **Shrnutí:** sedí / nesedí / nelze rozhodnout, a u rozporu částka rozporu z `verify_figures` (`difference`).
2. **Tabulka:** položka | na faktuře | podle portálu [F…] | rozdíl | verdikt. Rozdíl jen z `verify_figures`,
   jinak „—“.
3. **Hodnocení:** co je pravděpodobná chyba dodavatele a co je rozdíl v datech (odhady TDD, chybějící dny,
   nepotvrzený rozpis).
4. **Doporučení k posouzení:** co rozporovat u dodavatele a s jakými podklady (odkazy, období, čísla [F…]).
5. **Jak si to ověřit:** `portalUrl` spotřeby, řádku faktury a OM; `figure_id` každé citace.

## Nikdy

- Neoznačuj fakturu za chybnou, když portál nemá úplná data za celé období.
- Nepřepočítávej m³ na kWh. Nepočítej DPH ani součty v hlavě.
- Netvrď, že regulované složky sedí s ceníkem ERÚ; portál ceník zatím neeviduje.
- Nevydávej roční průměrnou cenu z `get_costs` za cenu kontrolované faktury.
