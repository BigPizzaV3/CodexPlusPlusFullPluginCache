# Kritéria: Anomálie a základní odběr

Výchozí prahové hodnoty pilotu. Upravují se podle zpětné vazby klientů.

| Ukazatel | Prověřit, když | Zdroj |
|---|---|---|
| Základní odběr | `baseLoadShareOfAveragePct` > 40 % (nejnižší hodinové zatížení přesahuje 40 % průměrného) | `get_load_profile`, `data.indicators` |
| Spotřeba v neprovozní den | `ratioPct` > 30 % (průměrná denní spotřeba neprovozního dne proti provoznímu) | `get_load_profile`, `data.nonOperatingDays` |
| Víkendový odběr | `weekendToWorkdayPct` > 30 % u provozu, který o víkendu nepracuje | `get_load_profile`, `data.indicators` |
| Anomálie | `severity` `medium` nebo `high` (odchylka od očekávání nad 2σ podle modelu portálu) | `get_anomalies` |
| Základní odběr ISO 50001 | `deviationPct` > 10 % (průměr posledních 30 dní nad referenční hodnotou) | `get_load_profile`, `data.baseLoad` |

## Poznámky

- `offHoursStatus`: `OK` = podíl spotřeby mimo provozní dobu (`offHoursSharePctLast30Days`) lze posoudit;
  `NO_SCHEDULE` = chybí provozní rozvrh, podíl mimo provoz nelze posoudit; `CONTINUOUS_OPERATION` = nepřetržitý provoz.
- Hodnota null znamená „nelze posoudit“, nikdy „v normě“.
- Provoz s nepřetržitým chodem (24/7) má přirozeně vysoký základní odběr; na režim provozu se zeptej dřív, než ho
  označíš za plýtvání.
- Anomálie plynu bývají v kWh i m³ (`energyUnit`); nesčítej je.
