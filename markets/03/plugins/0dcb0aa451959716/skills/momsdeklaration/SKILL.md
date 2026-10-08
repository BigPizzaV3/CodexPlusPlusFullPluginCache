---
name: momsdeklaration
description: Ta fram och stäm av momsunderlaget inför en momsdeklaration, med kontroll av momskontonas saldon och när deklarationen ska lämnas. Använd när användaren frågar om moms, momsdeklaration, momsredovisning, "hur mycket moms ska jag betala" eller vill stämma av momsen inför inlämning.
---

# Momsdeklaration

Detta arbetsflöde läser och stämmer av momsunderlaget. Appen lämnar inte in en deklaration till Skatteverket, oavsett aktiverad etapp.

Ge användaren siffrorna som ska in i Skatteverkets momsdeklaration — och kontrollera att bokföringen håller ihop innan de lämnas in.

## Gör så här

1. **Säkerställ rätt företag** om användaren nämner ett bolag: använd `list_companies` och vid behov `switch_company` efter att valet bekräftats.
2. **Hämta underlaget** med `get_vat_summary`. Utan angiven period används innevarande räkenskapsår fram till idag — ange därför alltid `period_start` och `period_end` för den period som ska deklareras.
3. **Ta reda på när det ska in** med `get_upcoming_deadlines`. Den ger deklarationsdag och vilken period den avser, utifrån företagets momsperiod (månad, kvartal eller år).
4. **Stäm av mot bokföringen** med `get_trial_balance` för samma period. Kontrollera momskontona:
   - 2610–2650 utgående moms per sats
   - 2640/2641 ingående moms
   - 2650 momsredovisningskonto
5. **Gräv vidare vid avvikelse** med `get_account_ledger` på det konto som inte stämmer, och `get_journal_entry` för misstänkta verifikationer.

## Presentera så här

Följ ordningen i Skatteverkets blankett så att siffrorna går att föra över direkt:

1. **Försäljning** — momspliktig omsättning per momssats.
2. **Utgående moms** — per sats (25 %, 12 %, 6 %), plus omvänd skattskyldighet och importmoms om beloppen finns i svaret.
3. **Ingående moms** — att dra av.
4. **Att betala eller få tillbaka** — nettot, tydligt utmärkt.
5. **Deklarationsdag** — datumet, och hur många dagar det är kvar.

Avsluta med avstämningen: stämmer momskontonas saldon mot underlaget, eller finns en differens som behöver utredas först?

## Viktigt

- **Detta är ett underlag, inte en inlämnad deklaration.** B2B.nu lämnar inte in momsdeklarationen åt användaren — den fyller hen i hos Skatteverket. Säg det tydligt.
- Hittar du en differens mellan underlaget och momskontona: peka ut den och föreslå vad som kan orsaka den. Bokför ingenting för att "jämna ut" — den här skillen skriver inte.
- Kontantmetod och faktureringsmetod ger olika periodisering. Verktygen räknar utifrån företagets metod; lägg inte till egna antaganden.
- Belopp i SEK, skrivna svenskt: `48 750,00 kr`.
