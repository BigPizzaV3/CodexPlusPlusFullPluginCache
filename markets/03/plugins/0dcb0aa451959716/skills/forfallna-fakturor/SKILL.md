---
name: forfallna-fakturor
description: Gå igenom obetalda och förfallna kundfakturor, prioritera vilka som ska drivas in först och skriv färdiga påminnelsemejl. Använd när användaren frågar om obetalda fakturor, förfallna fakturor, kundfordringar, "vem är skyldig mig pengar" eller vill skicka betalningspåminnelser.
---

# Förfallna fakturor

Förvandla en lista med förfallna fakturor till en indrivningsplan och färdiga mejl.

## Gör så här

1. **Säkerställ rätt företag** om användaren nämner ett bolag: använd `list_companies` och vid behov `switch_company` efter att valet bekräftats.
2. **Hämta läget** med `list_overdue_invoices`. Svaret innehåller belopp, förfallodatum och antal dagar sena, samt summan per valuta.
3. **Se helheten per kund** med `get_accounts_receivable` när flera fakturor hör till samma kund — driv in per kund, inte per faktura.
4. **Hämta detaljer** med `get_invoice` för de fakturor som ska följas upp. Kontrollera om det redan finns delbetalningar eller tidigare påminnelser innan du föreslår nästa steg.
5. **Hämta kontaktväg** med `get_customer`. Använd kontaktpersonernas namn och e-post i mejlet.

## Prioritera så här

Störst först, med hänsyn till hur sent det är:

1. Fakturor över 30 dagar sena — här är risken för kreditförlust reell.
2. Stora belopp, oavsett antal dagar.
3. Kunder med flera öppna fakturor — samla dem i ett mejl.
4. Nyligen förfallna småbelopp sist; de löser sig ofta av sig själva.

Nämn särskilt om en faktura redan fått påminnelser utan resultat — då är nästa steg inkasso, inte ännu ett vänligt mejl.

## Påminnelsemejl

Skriv på svenska, artigt och kort. Tonen trappas upp med antal dagar:

- **1–14 dagar sent:** vänlig påminnelse, utgå från att det är ett förbiseende.
- **15–30 dagar:** tydligare, be om betaldatum, nämn fakturanummer och belopp.
- **Över 30 dagar:** bestämd, sätt ett sista datum och nämn att ärendet annars går vidare.

Varje mejl ska innehålla fakturanummer, belopp, ursprungligt förfallodatum och OCR-nummer (finns i `get_invoice`).

## Viktigt

- Börja med läsning och ett mejlförslag. Skicka endast om användaren uttryckligen ber om det, etapp 3 är aktiv och `send_invoice_reminder` är tillgängligt med rätt samtycke. Verktyget förbereder granskningen; användaren måste klicka **Godkänn och utför**. Anropa aldrig ett `confirm_`-verktyg från modellen. Behåll samma `request_key` vid återförsök. Vid osäker leverans ska utfallet kontrolleras i B2B innan något nytt skickas. Saknas verktyget ger du användaren texten att skicka själv. Registrera inga betalningar som del av påminnelsen.
- Har en faktura status `partial` — nämn det återstående beloppet, inte totalbeloppet.
- Belopp i SEK om inget annat anges, skrivna svenskt: `12 500,00 kr`.
- Får du inte tillgång till kundverktygen saknar användaren behörighet till kundregistret. Gör då klart fakturadelen och säg vad som fattas.
