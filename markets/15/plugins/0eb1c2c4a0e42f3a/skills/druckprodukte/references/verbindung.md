# Verbindung und Grenzen

Öffentlicher Endpunkt: https://mcp.online-druck.biz/
Verifizierter Transport: Streamable HTTP ohne Authentifizierungsheader, Zugangsdaten oder Tool-Filter.

Am 04.11.2026 gegen Server-Version 1.0.0+0c154a8f geprüft: search_catalog, lookup_catalog, list_categories, get_product, configure_product, price_scale, get_print_specifications und configure_product_app. Kein bisheriges Tool wurde entfernt.

configure_product_app bleibt ausschließlich für die Konfigurator-Ansicht sichtbar. Die sieben anderen Tools sind für das Modell sichtbar. get_product liefert die serverseitig gehostete Konfigurator-Ressource; ihre URI wird zur Laufzeit ermittelt und nicht im Paket festgeschrieben. Die Ressource wurde erfolgreich gelesen; ihre Darstellung im Zielhost ist separat zu prüfen.

Alle acht Tools liefern boolean readOnlyHint=true, destructiveHint=false, openWorldHint=false und idempotentHint=true. Sie lesen den begrenzten ODB-Katalog beziehungsweise Konfigurator. Bestellungen und Zahlungen erfolgen im Shop. Über MCP wird nur Lieferung nach Deutschland konfiguriert. Laut aktueller Serveranweisung sind andere Lieferländer im Shop-Warenkorb auswählbar, der Versand bleibt inklusive. Keine Länderabdeckung erfinden; der Shop bestimmt Verfügbarkeit und verbindlichen Endpreis. Dies ist unabhängig von der weltweiten Plugin-Sichtbarkeit.

Aktuelle Preise: netto in Cent EUR, zuzüglich MwSt., inklusive Versand laut Serveranweisungen und verifizierten shipping_included=true-Antworten. Die jeweilige Antwort bleibt maßgeblich. Ab-Preise sind keine endgültigen Konfigurationspreise.

get_print_specifications liefert geprüfte Druckdaten-Maßvorgaben und Download-Links, keinen Preis und keinen konfigurierten Produktlink. Bei unklarer Konfiguration wurden needs_clarification und leere specifications verifiziert. Eine fehlende Rückenbreite darf nicht als 0 mm ausgegeben werden.


## Offizielle Anbieterquellen

- Anbieter: Online-Druck GmbH & Co. KG (offizielles ODB-Plugin, vom Nutzer bestätigt).
- Impressum: https://www.online-druck.biz/impressum/
- Dokumentation und Plugin-Webseite: https://www.online-druck.biz/mcp/
- Datenschutz einschließlich eigenem MCP-Abschnitt: https://www.online-druck.biz/datenschutz/
- Hilfe: https://www.online-druck.biz/kontakt/
- AGB: https://www.online-druck.biz/allgemeine-geschaeftsbedingungen/

Impressum, Dokumentationsseite und aktuelle Datenschutzerklärung wurden am 28.10.2026 öffentlich gelesen. Die Datenschutzerklärung enthält spezifische Angaben zu Anfrageinhalten, technischen Angaben, Sitzungs-/Linkkennungen, temporärer IP-Verarbeitung, Suchauswertung und Aufbewahrung; für Details auf die aktuelle Originalseite verweisen. Keine unbelegte Zusage einer vollständig protokollfreien Nutzung machen.


## Änderungen bei der Prüfung am 04.11.2026

Weiterhin acht Tools; keine hinzugefügt oder entfernt. Die Eingabe- und Ausgabestrukturen bestehen unverändert, abgesehen von ergänzten Parameterbeschreibungen der App-Konfiguration. Die Ressource der Konfigurator-Ansicht wurde ersetzt und erfolgreich gelesen; ihr Name wird zur Laufzeit ermittelt. Acht anonyme Direktaufrufe, fehlende Auflagen und Klärungsbedarf bei unbekanntem Format wurden erneut geprüft. Die Webseitenprüfung der Anbieterquellen stammt weiterhin vom 28.10.2026.
