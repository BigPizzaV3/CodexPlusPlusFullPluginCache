# Kritéria: Obnova smlouvy

Výchozí prahové hodnoty pilotu. Upravují se podle zpětné vazby klientů.

| Stav | Podmínka | Co dělat |
|---|---|---|
| Urgentní | `daysToNoticeDeadline` < 60 | rozhodnout o výpovědi nebo obnově hned; ověřit, zda výpověď už nebyla podána (`playbook.noticeGiven`) |
| Připravit | 60 ≤ `daysToNoticeDeadline` < 120 | poptat nabídky, připravit podklady, interní schválení |
| Sledovat | `daysToNoticeDeadline` ≥ 120 | připomenout termín |
| Past | `autoRenewalTrap: true` | vždy upozornit: bez včasné výpovědi se smlouva automaticky prodlouží |
| Neznámý termín | `noticeDeadline: null` | doplnit do portálu konec smlouvy a výpovědní dobu |
| Po lhůtě | `daysToNoticeDeadline` < 0 a smlouva běží | výpovědní lhůta uplynula; ověřit smluvní podmínky prodloužení |

## Srovnání produktů

- Fix a spot porovnávej na skutečném profilu odběru (`analyze_fix_vs_spot`), ne na průměrné tržní ceně.
- Srovnání je za komoditní část v EUR, bez distribuce, marže dodavatele a DPH; uveď to u výsledku.
- Srovnání za méně než 12 měsíců nebo při úplnosti dat pod 95 % uveď s výhradou.
- Minulý vývoj spotu nezaručuje budoucí; forwardy (`data.forwards[]`) ukazují aktuální očekávání trhu.
