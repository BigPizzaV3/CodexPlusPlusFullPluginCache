---
name: concurrentiescan
description: De concurrenten van één bol-product naast elkaar - wie staat beter in de zoekresultaten, wie adverteert waar, en hoe verhouden prijs en reviews zich.
---

Gebruik deze werkwijze als de gebruiker vraagt wie zijn concurrenten zijn, wie er wint op een zoekwoord, of wie er adverteert.

1. Roep `gevolgde_set` aan met de EAN van het eigen product voor de bevestigde concurrenten en hun EAN's.
2. Roep voor de drie belangrijkste concurrenten `compare_with_competitor` aan (eigen EAN plus `competitorEan`).
3. Roep `ads_adverteerders` aan, met de EAN van het eigen product als dat kan, om te zien wie in deze markt adverteert en hoe zwaar.
4. Roep voor de zwaarste adverteerder `ad_profile` aan met zijn EAN voor de zoekwoorden waarop hij adverteert.
5. Geef een tabel met per concurrent: zoekpositie tegenover de eigen positie, prijs, reviews en advertentiedruk. Sluit af met wat opvalt en met de meetdag.

Ontbrekende advertentiewaarnemingen bewijzen niet dat een concurrent niet adverteert. Prijzen en reviews zijn alleen beschikbaar voor bevestigde concurrenten.
