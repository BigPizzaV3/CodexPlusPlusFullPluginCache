---
name: cash-service-pl
description: Jak korzystać z narzędzi Cash-service.pl do polskich spraw finansowych - wynagrodzenia, ZUS, kredyty, odsetki, biała lista VAT, numery kont, urzędy, sądy, komornicy, kursy NBP. Użyj, gdy pytanie dotyczy polskich podatków, składek, pensji, firm lub urzędów.
---

# Cash-service.pl - polskie kalkulatory i rejestry

Serwer MCP `cash-service` udostępnia narzędzia tylko do odczytu. Wszystkie liczą według polskich przepisów na bieżący rok i zwracają gotowe kwoty w złotych.

## Kiedy sięgać po narzędzia

- **Wynagrodzenia**: `kalkulator_plac` (umowa o pracę, brutto ↔ netto), `kalkulator_zlecenie`, `kalkulator_dzielo`, `kalkulator_b2b` (porównanie B2B z etatem).
- **Przedsiębiorca**: `skladki_zus_jdg`, `skladka_zdrowotna_jdg`, `etapy_zus_nowej_firmy` (ulga na start, preferencyjny ZUS, mały ZUS plus).
- **Pieniądze i prawo**: `kalkulator_kredytu` (rata, harmonogram), `odsetki_podatkowe` (odsetki podatkowe i ustawowe), `wskazniki` (płaca minimalna, limity, stawki).
- **Rejestry i firmy**: `firma_biala_lista` (status VAT i rachunki z wykazu MF), `numer_konta` (poprawność rachunku, bank).
- **Urzędy po adresie**: `urzad_skarbowy`, `sad_wlasciwy`, `komornik`, `kod_pocztowy`.
- **Waluty**: `kursy_walut` (średnie kursy NBP).

## Zasady

1. Zanim policzysz, upewnij się, że masz dane wejściowe: kwotę brutto lub netto, rodzaj umowy, wiek (ulga dla młodych do 26 lat), dla firm NIP, dla urzędów miasto i ulicę.
2. Gdy czegoś brakuje, przyjmij typowe założenia i powiedz o tym wprost (np. brak PPK, praca w miejscu zamieszkania).
3. Odpowiedź podawaj w złotych z rozbiciem na składki i podatek, tak jak zwraca narzędzie. Nie zmieniaj kwot ręcznie.
4. Przy pytaniach o kontrahenta zawsze podaj status VAT i datę stanu wykazu, a przy rachunku - czy jest zgłoszony w wykazie.
5. Dodaj jedno zdanie, że wynik ma charakter informacyjny i nie zastępuje porady podatkowej ani prawnej.
6. Pytania spoza polskich finansów (pogoda, przepisy kulinarne, tłumaczenia) nie wymagają tych narzędzi.
