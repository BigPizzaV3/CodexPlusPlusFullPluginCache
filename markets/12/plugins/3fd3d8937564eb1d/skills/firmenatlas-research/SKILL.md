---
name: firmenatlas-research
description: Recherchiere österreichische Firmen, Kennzahlen, Beteiligungen und benannte Firmenatlas-Listen aus den verbundenen Firmenatlas-Daten.
---

Nutze Firmenatlas für österreichische Firmen, Registerdaten, Finanzkennzahlen, Personen und Beteiligungen. Löse Firmen mit search_companies und Personen mit search_people eindeutig auf; bei mehreren plausiblen Treffern nachfragen.

Wähle die kleinste Darstellung, die die Frage beantwortet. Ein Textwunsch hat Vorrang; ohne UI-Unterstützung antworte nativ. Keine Karten für bloße Firmenerwähnungen oder Zwischenschritte. Grafische Antworten erscheinen inline, ohne automatisch ein separates Panel zu öffnen.

Beantworte die Frage direkt mit den Erkenntnissen und einer kurzen Einordnung der Zahlen samt Geschäftsjahr und Quelle. Keine Ankündigung oder Beschreibung der Darstellung wie „Die interaktive Firmenatlas-Grafik zeigt …“ und keine technischen Hinweise zu UI, Tools oder Renderern, außer der Nutzer fragt danach oder braucht Hilfe bei der Bedienung. Firmenatlas als Datenquelle nennen ist passend.

Wähle eine primäre Grafik für die angefragte Analyse. Nach einer passenden Firmenatlas-Grafik ist die grafische Darstellung erledigt: standardmäßig keine zusätzliche ChatGPT-Grafik für dieselben Firmen, dieselbe Kennzahl und dieselben Geschäftsjahre erzeugen. Ein allgemeiner Chartwunsch, ein anderer Grafikstil oder eine erneute Darstellung desselben Trends rechtfertigt kein zweites Chart. Eine Jahrestabelle mit den Werten unter dem Chart ist erlaubt. Wenn die Firmenatlas-Ansicht nicht zur Auswertung passt, z.B. bei mehreren Kennzahlen, indexierten Wachstumsvergleichen oder Aggregationen, stattdessen eine passende eigene Grafik wählen. Nach einem Firmenatlas-Chart eine weitere Grafik nur für eine eigenständige, darin nicht enthaltene Analyse oder bei ausdrücklich gewünschter zusätzlicher/alternativer Grafik liefern. Bei fehlgeschlagener Anzeige oder ohne UI-Unterstützung ist eine native Grafik passend.

Die uiPresentation im Renderer-Ergebnis beschreibt mit displayDescription die vorbereitete Ansicht, Firmen, ausgewählte Kennzahl und Zeiträume. Vorhandene Daten bedeuten noch nicht, dass eine Grafik angezeigt wird: Ein eingeklappter Firmenüberblick und ein allgemeiner Vergleich ohne metric zeigen zunächst kein Chart. loadedFiscalYears sind die gelieferten Abschlüsse, keine Zusage vollständiger Kennzahlen; fehlende Werte bleiben Lücken. Verfügbare Ansichten in Bedienelementen nicht als bereits dargestellte Grafiken behandeln.

| Frage | Daten und Darstellung |
| --- | --- |
| Allgemeiner Firmenüberblick | get_company_summary mit includeDirectOwners=true, wenn verfügbar; bis zu sechs aktuelle direkte Eigentümer, Quoten und Vollständigkeit. render_company_card presentation=overview, zunächst eingeklappt. Kein zusätzlicher Graphabruf. |
| Einzelne Fakten, Finanzzahlen, gewöhnliche Bilanz-/GuV- oder Jahresvergleichstabellen | ChatGPT-Text/native Tabelle mit Geschäftsjahr und Quelle, kein Renderer. financials nur für ausdrücklich gewünschte interaktive Finanzansichten. |
| Gewinn, Verlust, Profitabilität | get_company_summary und get_company_financials limit=6; render_company_card presentation=profitability mit financialResultId. Danach ein bis zwei Sätze mit Jahr; eine Jahrestabelle unter dem Chart ist erlaubt. |
| Kennzahlenverlauf, auch natürliche Folgefragen ohne ausdrücklichen Chartwunsch | Dieselben Daten, presentation=trend und exakte metric-Feld-ID, z.B. bilanz.bilanzsumme, bilanz.eigenkapital, gewinnUndVerlustrechnung.umsatzerloese oder mitarbeiter.gesamt. Nur die angefragte Kennzahl zeigen. |
| Jahresabschluss | get_company_summary, get_company_financials (years=[Jahr] oder limit=2), list_company_documents limit=100; presentation=annual-report mit financialResultId und documentResultId. year nur bei ausdrücklich angefragtem Jahr, comparePrevious=true nur für gewünschten Vorjahresvergleich. documents nur für Dokumentlisten. |
| Personenfunktionen/-beteiligungen | get_person_profile status=current, dann einmal render_person_card. Tatsächliche Rollen und Beteiligungen trennen; Verbindungen sind keine Geschäftsführerrollen. Historische Daten nur auf Wunsch mit status=all. |

Firmenvergleiche verwenden einmal render_company_comparison mit summary-resultIds und financialResultIds jeder Firma (limit=6 oder angefragte years), wenn diese Ansicht zur Analyse passt; andernfalls eine passende native Grafik wählen. presentation=overview ohne metric/years bleibt der Standard, auch nach Finanzdatenabrufen. Eine konkrete Kennzahl verwendet deren Feld-ID, ein Zeitverlauf trend, ausdrücklich interaktive volle Finanztabellen financials. Standard ist das jüngste gemeinsame Jahr; periodMode=latest nur für ausdrücklich jeweils letzte Abschlüsse. Nettomarge misst relative Profitabilität, currentProfit absolute Ergebnisse. Keine einzelnen Firmenkarten daneben.

Bei Jahresabschluss-Folgefragen eine neue Karte für genau das neue Jahr zeigen; gültige summary-resultId wiederverwenden. Ein PDF-Link allein genügt nicht. Neuester Abschluss nach Stichtag, nicht Einreichungsdatum; neue PDFs ohne Kennzahlen zeigen, ohne ältere Zahlen einzusetzen.

Firmenrecherche: get_filter_metadata, dann list_companies_by_filters. Normaler Text/native Tabelle mit Firmenname, Profil-Link, angefragten Kennzahlen und Jahr. Angewendete Filter und Gesamtzahl getrennt von der Auswahl nennen. Filter, Felder und Pagination beibehalten; weitere Seiten bei Bedarf. Kein interaktives Recherchetabelle-Widget.

Beteiligungen: get_company_ownership_graph depth=2, direction=both, dann render_ownership_graph. Zunächst kompakte direkte Beziehungen auf Desktop/Mobile; weitere Ebenen gezielt öffnen. Großer Graph nur per ausdrücklicher Desktop-Aktion. Für Personen andere tatsächliche Beteiligungen aus get_person_profile holen, keine Organfunktionen als Eigentum behandeln.

Render einmal aus vorhandenen Ergebnis-IDs, ohne erfundene Finanzwerte oder zusätzlichen Verbrauch. Bei RESULT_EXPIRED Daten erneut holen. Fehlende Werte, null Euro, Jahresergebnis und Bilanzgewinn unterscheiden; das Geschäftsjahr nennen. Bei widersprüchlichen Ergebniswerten aus Übersicht/Abschluss keine sichere Profitabilitätsaussage bis zur Klärung.

Listenänderungen nur auf Nutzerwunsch mit gewollter Auswahl und Listennamen; fehlende Angaben klären. Keine künstlichen Folgeprompts für UI-Aktionen und keine blinde Wiederholung unbestätigter Schreibvorgänge nach Verbindungsabbruch.

Zugriffs-/Kontingentfehler neutral erklären; get_usage zeigt den Verbrauch. Einfache Suchen, Metadaten und render_* sind frei; erfolgreiche Detailabfragen, erweiterte Suchen und Listenänderungen zählen. Keine Plan-, Kauf- oder Upgrade-Werbung in ChatGPT; informative Erklärung: https://firmenatlas.com/mcp-access.html. Keinen öffentlichen Eintrag, geprüfte Verfügbarkeit oder Vollständigkeit gekürzter Graphen behaupten.
