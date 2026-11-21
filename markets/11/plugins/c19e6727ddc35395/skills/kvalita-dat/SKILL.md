---
name: kvalita-dat
description: "Kontrola kvality a úplnosti energetických dat v ES Zone: chybějící data, mezery, odhady TDD, zastaralá data, konflikty odečtů a faktury čekající na zpracování. Použij, když se uživatel ptá, jestli může číslům věřit, proč něco chybí, jak úplná nebo aktuální jsou data o spotřebě elektřiny či plynu, nebo před jakýmkoli vyhodnocením spotřeby a nákladů."
metadata:
  title: Kvalita dat
  short-description: Semafor úplnosti a aktuálnosti dat po odběrných místech
  version: 1.0.0
  tools: [get_organization_overview, get_data_quality, list_metering_points]
  modules: []
---

# Kvalita dat

Nejdřív si přečti `references/pravidla.md` a dodržuj je. Prahové hodnoty semaforu jsou v `references/kriteria.md`,
pojmy v `references/slovnik.md`, šablona odpovědi v `assets/vystup.md`.

Cíl: říct uživateli, zda může číslům v ES Zone věřit, a pokud ne, kde přesně data chybějí a co s tím.

## 1. Zjisti, co je k dispozici

- Zavolej `get_organization_overview()`.
- Z `data.meteringPoints` zjisti počet OM elektřiny a plynu, z `data.dataCoverage` první a poslední měsíc s daty.
- Když má `get_data_quality` v `data.capabilities` hodnotu `available: false`, řekni uživateli důvod (`reason`)
  a skonči. Kvalitu dat bez tohoto nástroje neodhaduj.

## 2. Urči rozsah a období

- Když uživatel jmenuje konkrétní OM, najdi ho přes `list_metering_points(query=<název, město nebo štítek>)` a vezmi
  jeho `data.items[].id`. Při více shodách se zeptej, které OM myslí.
- Když jmenuje štítek (skupinu OM), použij `list_metering_points(tag=<štítek>)`.
- Období: když ho uživatel neurčí, použij výchozí (poslední tři měsíce do včerejška) a vynech `from` i `to`.
  Kvalitu lze hodnotit nejpozději do včerejška.

## 3. Načti kvalitu dat

- Zavolej `get_data_quality(commodity=<electricity|gas>, meteringPointIds=[<id OM>], from=<RRRR-MM-DD>, to=<RRRR-MM-DD>)`.
  Bez upřesnění vynech `commodity` i `meteringPointIds` (obě komodity, všechna OM).
- Jedna stránka podrobně vyhodnotí nejvýše 8 OM. Když výsledek vrátí `data.nextCursor`, zavolej nástroj znovu se
  stejnými parametry a `cursor=<data.nextCursor>`. Načti nejvýše 3 stránky; u zbytku napiš, kolik OM zůstalo
  nevyhodnoceno, a nabídni pokračování.
- Celkový přehled je v `data.overall` (`completeness`, `estimatedShare`, `rating`, `evaluatedMeteringPoints`,
  `totalMeteringPoints`). Seznam všech OM se stavem je v `data.allMeteringPoints` (jen na první stránce).

## 4. Sestav semafor

- Hodnocení každého OM ber z `data.meteringPoints[].rating` (`green`, `orange`, `red`). Nástroj ho počítá podle
  prahů v `references/kriteria.md`; sám ho nepřepočítávej. `rating: null` znamená, že úplnost nelze určit;
  uveď „neznámé“, ne zelenou.
- Ke každému OM uveď `completeness` a `estimatedShare` v procentech, `lastDataDate` a `daysSinceLastData`.

## 5. Najdi konkrétní problémy

Projdi a vypiš (jen ty, které nastaly):

1. OM bez čerstvých dat: `data.allMeteringPoints[].noRecentData` je `true`, nebo `daysSinceLastData` je větší než
   práh aktuálnosti.
2. Mezery delší než 7 dní: `data.meteringPoints[].gaps[]` s `days` > 7. Uveď `from`, `to` a `reason`
   („chybí data“ nebo „chybí přepočet na kWh“ u plynu).
3. Odhady TDD: OM s `estimatedShare` nad prahem oranžové.
4. Konflikty odečtů: `data.pendingReadingConflicts` větší než 0.
5. Faktury čekající na zpracování: `data.invoiceInbox` (`manualRequired`, `awaitingConfirmation`, `failed`).
   Do nákladů v portálu se nepočítají, dokud je někdo nepotvrdí.
6. Poslední import: `data.lastImport` (`at`, `committed`). Nepotvrzený import znamená, že data ještě nejsou v přehledech.

## 6. Odpověz

Použij šablonu `assets/vystup.md`:

1. **Shrnutí** (3 věty): lze číslům věřit? Kolik OM je zelených, oranžových, červených a neznámých.
2. **Semafor**: tabulka OM | úplnost | odhady | poslední data | hodnocení.
3. **Co s tím**: ke každému problému z kroku 5 konkrétní krok (doplnit import, vyřešit konflikt, potvrdit fakturu,
   ověřit přepočet plynu na kWh). Formuluj jako doporučení k posouzení.
4. **Jak si to ověřit**: `portalUrl` každého problémového OM (`data.meteringPoints[].portalUrl`) a `portalUrl`
   výsledku.

## Nikdy

- Neoznačuj OM za zelené, když nástroj vrátil `rating: null` nebo `completeness: null`.
- Nevydávej chybějící data za nulovou spotřebu.
- Neodhaduj úplnost OM, která nebyla na načtených stránkách vyhodnocena.
- Nepřeváděj m³ na kWh, ani když přepočet chybí.
