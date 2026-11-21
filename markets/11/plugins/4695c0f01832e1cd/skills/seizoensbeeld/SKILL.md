---
name: seizoensbeeld
description: Het seizoenspatroon van een bol-product - zoekvraag per week over twee jaar, jaar-op-jaar, en de eigen zoekpositie over de laatste maanden.
---

Gebruik deze werkwijze als de gebruiker vraagt wanneer de vraag piekt, hoe dit jaar zich verhoudt tot vorig jaar, of hoeveel hij rond een seizoen kan verwachten.

1. Roep `search_volume_index` aan met de EAN voor de weekreeks van het totale zoekvolume over twee jaar; voor één zoekwoord geef je het `keyword`-argument mee.
2. Roep `ranking_history` aan met `days` 90 voor de eigen zoekpositie over de laatste maanden.
3. Beschrijf het patroon: in welke weken het volume piekt, hoe de piek van dit jaar zich verhoudt tot vorig jaar, en of de eigen positie in aanloop naar de piek stijgt of daalt.
4. Geef aan welke weken de gebruiker in de gaten kan houden en welke gegevens nog ontbreken voor een inkoop- of voorraadbesluit (verkoopsnelheid, voorraad, kostprijs).

Zoekvolume is bol's geschatte zoekvraag (NL en BE samen), geen aantal kopers en geen omzet. Volledige dekking per week is niet bewezen; zeg dat als weken ontbreken.
