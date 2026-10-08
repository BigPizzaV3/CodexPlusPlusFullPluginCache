---
name: manadsgenomgang
description: Gå igenom företagets ekonomiska läge för en månad — nyckeltal, resultat, kostnadsavvikelser och förfallna fakturor — och sammanfatta med en prioriterad åtgärdslista. Använd när användaren ber om en månadsgenomgång, månadsavstämning, "hur går det för företaget" eller en ekonomisk lägesrapport.
---

# Månadsgenomgång

Ge företagaren en komplett bild av ekonomin på någon minut, med konkreta åtgärder i stället för bara siffror.

## Gör så här

1. **Hämta helhetsbilden** med `get_economy_brief`. Den ger nyckeltal, omsättningstrend och prioriterade åtgärder i ett anrop — börja alltid här.
2. **Hämta månadsutvecklingen** med `get_monthly_result`. Jämför den senast avslutade månaden mot de föregående och mot samma månad förra året om den finns i svaret.
3. **Leta avvikelser** med `detect_cost_anomalies`. Verktyget flaggar kostnadskonton som stuckit iväg mot sitt historiska snitt, och helt nya kostnader.
4. **Kolla pengar på väg in** med `list_overdue_invoices`. Notera de största och de mest försenade.
5. **Kolla vad som ligger framför** med `get_upcoming_deadlines` — moms, arbetsgivardeklaration och fakturor som förfaller snart.

Behöver du gräva djupare i en enskild siffra: `get_income_statement` för resultaträkningen, `get_account_ledger` för ett specifikt konto, `get_invoice` för en enskild faktura.

## Sammanfatta så här

Håll det kort och läsbart. Använd den här ordningen:

1. **Läget i en mening.** Går det upp eller ner, och räcker pengarna?
2. **Nyckeltal.** Omsättning, resultat och kassa för månaden, med förändring mot föregående månad.
3. **Det som avviker.** Bara verkliga avvikelser — hoppa över rubriken helt om inget sticker ut.
4. **Att göra nu.** Max fem punkter, mest brådskande först, var och en med belopp och datum.

## Viktigt

- Alla belopp är i SEK om inget annat anges. Skriv dem svenskt: `125 400,50 kr`.
- Siffrorna gäller anslutningens aktiva företag. Om användaren nämner ett annat bolag: kör `list_companies`, bekräfta vilket företag som avses och använd `switch_company` med dess id innan du hämtar siffrorna.
- Saknas ett verktyg i listan har användaren inte behörighet till den modulen. Säg det rakt ut och fortsätt med det du har, i stället för att gissa.
- Denna skill är helt läsande, även när företaget har aktiverat senare etapper. Föreslå gärna åtgärder, men skapa ingenting utan en separat begäran.
