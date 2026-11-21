# Kritéria: Kvalita dat

Výchozí prahové hodnoty pilotu. Upravují se podle zpětné vazby klientů; hodnocení `rating` počítá nástroj
`get_data_quality` podle stejných prahů (nastavení služby `Mcp:Quality`).

<!-- thresholds: green_min_completeness=0.98 green_max_estimated=0.02 orange_min_completeness=0.90 orange_max_estimated=0.10 stale_after_days=3 -->

## Semafor po odběrném místě

| Hodnocení | Podmínka |
|---|---|
| Zelená (`green`) | úplnost ≥ 98 % **a** odhady TDD ≤ 2 % **a** poslední data nejvýše 3 dny stará |
| Oranžová (`orange`) | úplnost ≥ 90 % **a** odhady TDD ≤ 10 % (nebo podíl odhadů neznámý), ale nesplňuje zelenou; sem patří i úplná data starší 3 dní |
| Červená (`red`) | úplnost pod 90 % **nebo** odhady nad 10 % |
| Neznámé (`null`) | úplnost nelze určit; nikdy ji nevydávej za zelenou |

## Další nálezy

| Nález | Práh | Co s tím |
|---|---|---|
| Mezera v datech | souvislý úsek bez dat delší než 7 dní | ověřit import od distributora nebo dodavatele za dané dny |
| Zastaralá data | poslední data starší než 3 dny | ověřit, zda běží automatický import |
| Chybí přepočet plynu na kWh | mezera s důvodem „chybí přepočet na kWh“ | doplnit spalné teplo (přepočítací koeficient) pro OM |
| Konflikt odečtů | alespoň 1 nevyřešený konflikt | rozhodnout v portálu, který zdroj platí |
| Faktury čekající na zpracování | alespoň 1 faktura čeká na kontrolu nebo potvrzení | potvrdit rozpis, jinak chybí v nákladech |

## Upozornění na začátku odpovědi

Když je celková úplnost pod 95 % nebo podíl odhadů nad 10 %, začni odpověď upozorněním (pravidlo 12).
