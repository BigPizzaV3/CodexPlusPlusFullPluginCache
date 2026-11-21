# Kritéria: Měsíční přehled energií

Výchozí prahové hodnoty pilotu. Upravují se podle zpětné vazby klientů.

| Oblast | Kritérium | Poznámka |
|---|---|---|
| Top změna po OM | \|`changePct`\| > 10 % **a** `total` a `previousTotal` se liší o více než 1 MWh | meziroční srovnání (`compare=same_period_last_year`); nejvýše 3 OM, seřazená podle \|`changePct`\| |
| Neúplné OM | `completeness` OM pod 95 % | změnu takového OM uveď s výhradou |
| Anomálie | nevyřízené (`status=open`) ve zvoleném měsíci | do přehledu nejvýše 3, nejdřív `high`, potom `medium` |
| Smlouvy | `daysToNoticeDeadline` ≤ 90 **nebo** `daysToEnd` ≤ 90 | výpovědní lhůta pod 30 dní = urgentní |
| Past prodloužení | `autoRenewalTrap: true` | vždy uvést, i když lhůta není do 90 dní |
| Kvalita dat | úplnost < 95 % nebo odhady > 10 % | přehled začíná upozorněním |

Rozdíl v MWh slouží jen k výběru OM; v odpovědi ho necituj jako číslo, protože ho nespočítal nástroj.
