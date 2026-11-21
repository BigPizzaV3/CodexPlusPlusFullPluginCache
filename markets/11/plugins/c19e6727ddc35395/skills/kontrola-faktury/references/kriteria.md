# Kritéria: Kontrola faktury

Výchozí prahové hodnoty pilotu. Upravují se podle zpětné vazby klientů (hlášení „číslo nesedí“).

| Položka | Sedí, když | Zdroj rozdílu | Poznámka |
|---|---|---|---|
| Množství | \|`differencePct`\| ≤ 1 % | `verify_figures` (figure spotřeby) | kontrolu neprováděj při úplnosti dat pod 95 %; m³ a kWh zvlášť |
| Silová cena (fix) | ceny se liší nejvýše o 0,5 % | smlouva (`list_contracts`) proti ceně z faktury nebo z `data.supplyPrices[]` | procento nepočítej v hlavě; když se ceny na uvedenou přesnost neshodují a rozdíl nedá žádný nástroj, verdikt „k ověření u dodavatele“ |
| Silová cena (spot) | nelze ověřit | spotové ceny jen v EUR bez ověřeného kurzu | uveď produkt a marži ze smlouvy, pokud jsou známé |
| Regulované složky | nelze ověřit proti ceníku | portál zatím neeviduje ceník ERÚ | ověř jen sazbu, rezervovanou kapacitu nebo jistič a shodu s potvrzeným rozpisem téhož období |
| Celkem bez DPH | \|`difference`\| ≤ 1 Kč **nebo** \|`differencePct`\| ≤ 0,5 % | `verify_figures` (figure řádku faktury) | |
| Celkem s DPH | \|`difference`\| ≤ 1 Kč **nebo** \|`differencePct`\| ≤ 0,5 % | `verify_figures` (`cost_total`, `vat: gross`, `invoiceId`) | sazbu DPH ani DPH nepočítej; porovnej s `totalWithVatCzk` potvrzeného rozpisu |

## Verdikty položek

| Verdikt | Kdy |
|---|---|
| sedí | rozdíl v toleranci a data úplná |
| sedí s výhradou | rozdíl v toleranci, ale data neúplná nebo s odhady (`potvrzeno_s_vyhradou`) |
| nesedí | rozdíl mimo toleranci při úplných datech (`odchylka`) |
| nelze ověřit | chybí data, ceník, přístup nebo převod jednotek (`nelze_overit`), nebo položku portál neeviduje |

Fakturu jako celek označ „nesedí“ jen tehdy, když aspoň jedna položka nesedí a data za celé období jsou úplná
(úplnost ≥ 95 %).
