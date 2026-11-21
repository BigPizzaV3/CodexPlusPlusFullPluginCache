---
name: overeni-odpovedi
description: "Ověření čísel a tvrzení, která uživateli řekla AI, konzultant nebo dodavatel, proti datům v ES Zone: přepočet každého čísla, verdikt potvrzeno / potvrzeno s výhradou / odchylka / nelze ověřit a správná hodnota s odkazem do portálu. Použij, když chce uživatel něco ověřit, zkontrolovat odpověď, doložit čísla, najít chybu v reportu nebo zjistit, zda tvrzení sedí."
metadata:
  title: Ověření odpovědi
  short-description: Ověření čísel z odpovědi AI, reportu nebo nabídky proti portálu
  version: 1.0.0
  tools: [get_organization_overview, verify_figures, search]
  modules: []
---

# Ověření odpovědi

Nejdřív si přečti `references/pravidla.md` a dodržuj je. Mapování tvrzení na metriky a povinná pole jsou
v `references/kriteria.md`, šablona odpovědi v `assets/vystup.md`.

Cíl: každé číselné tvrzení z textu nechat přepočítat nástrojem `verify_figures` s oprávněními uživatele a vrátit
verdikt se správnou hodnotou. Sám nic nepřepočítávej a nic neodhaduj.

## 1. Zjisti, co je k dispozici

- Zavolej `get_organization_overview()`. Z `data.grantedScopes` zjisti, ke kterým kategoriím dat má spojení přístup
  (spotřeba, náklady, smlouvy). Tvrzení z kategorie mimo přístup označ „nelze ověřit“ s důvodem.

## 2. Vytáhni tvrzení

Z textu, který uživatel vložil (odpověď AI, report, e-mail dodavatele), vypiš každé číselné nebo datové tvrzení:

- hodnota a jednotka (kWh, MWh, m3, kW, Kč, EUR/MWh, %, počet, datum);
- období (`from`, `to` ve formátu `RRRR-MM` nebo `RRRR-MM-DD`, u nákladů kalendářní rok `year`);
- rozsah: všechna OM, konkrétní OM, nebo štítek;
- komodita a metrika podle tabulky v `references/kriteria.md`;
- přibližná čísla („asi“, „kolem“, „přes“, „téměř“) označ zaokrouhlením `roundedTo` (např. „kolem 180 MWh“ →
  `roundedTo: 10`).

Tvrzení bez čísla, názory a doporučení neověřuj; vypiš je zvlášť jako „mimo ověření“.

## 3. Přiřaď figure id nebo popis metriky

- Když číslo pochází z výsledku nástroje ES Zone v této konverzaci, použij jeho `figure_id` (`figureId`). Je to
  nejpřesnější cesta: nástroj přepočítá přesně stejný dotaz nad týmiž daty. Shoda tak potvrdí výpočet, rozsah OM
  a období, ne správnost dat samotných.
- Jinak tvrzení popiš metrikou (`metric`) a poli podle tabulky v `references/kriteria.md`.
- Tvrzení, pro které v tabulce metrika není, neposílej; v odpovědi ho uveď jako „nelze ověřit (mimo katalog)“.

## 4. Najdi odběrná místa

Když tvrzení jmenuje OM názvem, zavolej `search(query=<název OM>, types=["metering_point"], limit=5)`.
Výsledek `id` má tvar `mp:<GUID>`; do `meteringPointIds` dej jen GUID. Při více shodách se uživatele zeptej.
Když OM nenajdeš, tvrzení označ „nelze ověřit“ (OM není dostupné).

## 5. Ověř jedním voláním

- Zavolej `verify_figures(claims=[…])` se všemi tvrzeními, nejvýše 20 v jednom volání; víc rozděl do dalších volání
  po 20.
- Příklad popisu tvrzení: `{"text": "V srpnu jsme spotřebovali 182 MWh", "metric": "consumption_total",
  "commodity": "electricity", "all": true, "from": "2026-08-01", "to": "2026-08-31", "value": 182, "unit": "MWh"}`.
- Výsledek pro každé tvrzení je v `data.claims[]`: `verdict`, `recomputedValue`, `difference`, `differencePct`,
  `tolerance`, `toleranceRule`, `completeness`, `reservations`, `reason`, `reasonText`, `portalUrl`, `figureRef`.
  Souhrn je v `data.summary` (`total`, `confirmed`, `confirmedWithReservation`, `deviation`, `unverifiable`).

## 6. Odpověz

Použij šablonu `assets/vystup.md`:

1. **Shrnutí:** „{x} z {y} tvrzení potvrzeno“ podle `data.summary`, a nejzávažnější odchylka.
2. **Tabulka:** tvrzení | verdikt | správná hodnota | odkaz. U `odchylka` uveď `recomputedValue` jako správnou
   hodnotu, u `potvrzeno_s_vyhradou` výhradu z `reservations`, u `nelze_overit` důvod z `reasonText`.
3. **Hodnocení:** jsou chyby náhodné (zaokrouhlení, jiné období), nebo systematické (jiná jednotka, jiný rozsah OM,
   s DPH proti bez DPH)?
4. **Jak si to ověřit:** `portalUrl` a `figure_id` každého přepočtu.

## Nikdy

- Nehádej hodnotu tvrzení, které nástroj nepřepočítal; „nelze ověřit“ je platný výsledek.
- Nepřeváděj m³ na kWh ani EUR na Kč, abys tvrzení „dostal“ do katalogu.
- Neprozrazuj, proč přesně nelze OM ověřit (cizí, neexistující nebo mimo přístup); stačí „nelze ověřit“.
- Neupravuj tvrzení tak, aby prošlo; ověřuj přesně to, co v textu stojí.
