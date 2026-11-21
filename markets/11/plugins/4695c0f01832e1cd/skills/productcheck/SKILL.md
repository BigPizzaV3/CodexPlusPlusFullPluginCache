---
name: productcheck
description: Eén bol-product in kaart - zoekpositie, zichtbaarheid, prijs tegenover concurrenten, zwakke zoekwoorden en wat de laatste meting wel en niet bewijst.
---

Gebruik deze werkwijze als de gebruiker vraagt hoe één product ervoor staat, of het goed geprijsd is, of waarom het minder verkoopt.

1. Vraag of bepaal de EAN. Noemt de gebruiker een productnaam, roep dan `markt_vraag` aan met `vraag` "zoekposities" en de naam; bij meerdere treffers laat je de gebruiker kiezen.
2. Roep `product_overview` aan voor de drie kernblokken (rang, prestatie, prijs) met trend.
3. Roep `price_position` en `ranking_scores_today` aan voor de prijsbandbreedte en de zoekpositie van vandaag.
4. Roep `weakest_keywords` aan voor de zoekwoorden waar het product niet of laag staat.
5. Vat samen in vier korte alinea's: positie, prijs, zwakke plekken, en wat de gebruiker als volgende stap kan onderzoeken. Noem bij elk cijfer de meetdag.

Geef geen prijsadvies zonder kostprijs en btw-basis; zeg dan dat die ontbreken. Zichtbaarheid en zoekpositie zijn berekende maten, geen omzet of marktaandeel.
