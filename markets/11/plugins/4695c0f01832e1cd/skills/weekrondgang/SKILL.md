---
name: weekrondgang
description: Wekelijkse rondgang langs alle gevolgde bol-producten - wat deed elk product vorige week, waar ging het omhoog of omlaag, en wat verdient een blik.
---

Gebruik deze werkwijze als de gebruiker vraagt hoe de week ging, om een weekoverzicht vraagt, of op maandag een rondgang wil.

1. Roep `account_pulse` aan voor de lijst gevolgde producten en de stand van de metingen.
2. Roep voor elk product `week_analyse` aan met `weekOffset` 1 (vorige week). Bij meer dan tien producten: vraag eerst welke producten de gebruiker wil zien.
3. Zet per product in één regel: verkocht en omzet vorige week, het verschil met de week ervoor, de zichtbaarheid, en het weekoordeel uit het antwoord.
4. Noem daarna de drie producten die het meest opvallen (grootste daling, grootste stijging, laagste zichtbaarheid) met de meetdag en de bron.

Houd je aan de bewijsgrenzen in de antwoorden: verschillen tussen verkoop, bezoeken en zoekvraag bewijzen geen oorzaak. Bij kleine aantallen noem je de absolute aantallen. Een ontbrekende waarde is onbekend, niet nul.
