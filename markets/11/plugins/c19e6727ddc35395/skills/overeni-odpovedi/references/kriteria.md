# Kritéria: Ověření odpovědi

Tolerance a verdikty počítá nástroj `verify_figures`; tady je, jak tvrzení popsat a jak výsledek číst.

## Mapování tvrzení na metriku

| Tvrzení (typická slova) | `metric` | Povinná pole popisu | Jednotky |
|---|---|---|---|
| „spotřeba…“, „spotřebovali jsme…“, „odebrali“ | `consumption_total` | `commodity`, rozsah (`all`, `meteringPointIds` nebo `tag`), `from`, `to` | kWh, MWh, m3 |
| „meziročně…“, „proti loňsku…“ | `yoy_change` | jako spotřeba + `compare: "same_period_last_year"` | % |
| „proti minulému měsíci…“, „oproti předchozímu období…“ | `period_change` | jako spotřeba + `compare: "previous_period"` | % |
| „náklady…“, „zaplatili jsme…“, „faktura za…“ | `cost_total` | `commodity`, `year` (celý kalendářní rok) a rozsah, nebo `invoiceId`; `vat` (`net` / `gross`) | Kč, tis. Kč, mil. Kč |
| „průměrná cena…“, „cena za MWh…“ | `avg_unit_price` | `commodity`, `year` (u elektřiny i `voltageLevel`), nebo `invoiceId` | Kč/MWh, Kč/kWh |
| „podíl složky…“ (např. distribuce na nákladech) | `share` | `commodity`, `year`, `componentKey` | % |
| „špička…“, „maximum…“, „nejvyšší příkon…“, „nejvyšší výkon…“ | `peak_power` | `commodity: "electricity"`, `meteringPointIds`, `from`, `to`; čas v `at` | kW, MW |
| „překročení…“ (rezervované kapacity) | `capacity_exceedances` | jedno OM v `meteringPointIds`, `from`, `to` (celé měsíce) | count |
| „konec smlouvy…“, „smlouva končí…“ | `contract_end` | `contractId`; datum v `at` | date |
| „výpovědní lhůta…“, „vypovědět do…“ | `notice_deadline` | `contractId`; datum v `at` | date |
| „spot…“, „průměrná spotová cena…“ | `spot_avg_price` | `commodity`, `from`, `to` | EUR/MWh |

Tvrzení, které do tabulky nepatří (např. emise CO₂, počet zaměstnanců, cena konkurence, předpověď), je „nelze
ověřit (mimo katalog)“. Nikdy ho neověřuj odhadem.

## Verdikty

| Verdikt | Význam | Co uvést |
|---|---|---|
| `potvrzeno` | rozdíl v toleranci, data úplná | přepočtenou hodnotu a odkaz |
| `potvrzeno_s_vyhradou` | rozdíl v toleranci, ale data neúplná nebo s odhady | výhradu z `reservations` |
| `odchylka` | rozdíl mimo toleranci | správnou hodnotu `recomputedValue` a rozdíl |
| `nelze_overit` | mimo katalog, chybí data nebo přístup, nejde převést jednotku | důvod z `reasonText` |

## Tolerance (výchozí, počítá nástroj)

| Metrika | Tolerance |
|---|---|
| `consumption_total` | 0,5 % nebo zaokrouhlení tvrzení (větší z obou) |
| `cost_total` | 1 Kč nebo 0,5 % (větší z obou) |
| `avg_unit_price`, `spot_avg_price`, `peak_power` | 0,5 %; u špičky navíc přesná čtvrthodina |
| `yoy_change`, `period_change`, `share` | 0,5 procentního bodu |
| `capacity_exceedances`, `contract_end`, `notice_deadline` | přesně |

Souhrn „{x} z {y} potvrzeno“ počítej z `data.summary.confirmed` a `data.summary.total`; tvrzení
s výhradou uveď zvlášť.
