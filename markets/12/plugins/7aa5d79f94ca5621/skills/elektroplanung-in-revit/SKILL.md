---
name: elektroplanung-in-revit
description: Elektroplanung in Revit nach deutschen Normen (DIN 18015, DIN VDE 0100, VDE-AR-N 4100): Stromkreise aufteilen, Verteilerplan und Stromlaufplan normgerecht, VDE-Regelprüfung, Leistungsbilanz nach DIN 18015-1 rechnen, Revit-Familienbibliothek für TGA aufbauen. Nutze diesen Skill bei Fragen zu Stromkreisen, Verteilerplänen, RCD-Pflicht, Querschnitten, Anschlussleistung, Wallbox und Wärmepumpe in der Leistungsbilanz, Revit-Familien und Familienbibliotheken. Use for German electrical design in Revit: circuits, panel schedules vs. Verteilerplan, VDE checks, DIN 18015-1 load calculation, TGA family libraries.
---

# Elektroplanung in Revit

Fachwissen und Werkzeuge für die Elektroplanung mit Revit nach deutschen Normen. Die Texte stammen aus der Planungspraxis von Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired; die Werkzeuge sind der öffentliche MCP-Server von BimWired (https://mcp.bimwired.com/mcp), der dieselben Kataloge und Prüfungen bereitstellt wie das Produkt, lesend und ohne Konto.

## Wann dieser Skill greift

- Fragen zu Stromkreisen in Revit, Verteiler- und Stromlaufplänen, RCD-Pflicht, Mindestquerschnitten, Sicherungswahl, Panel Schedule gegen deutschen Verteilerplan.
- Anschlussleistung und Leistungsbilanz nach DIN 18015-1, auch mit Wärmepumpe, Wallbox, PV, Gewerbeflächen.
- Aufbau und Pflege einer Revit-Familienbibliothek für TGA (IFC, DIN 276, Parameter, Typenkataloge, Freigabe).
- Englische Anfragen zu denselben Themen (German electrical design in Revit, DIN 18015 load calculation, VDE checks).

## So arbeitest du

1. **Erst lesen, dann antworten.** Öffne `references/INDEX.md` und lade die ein bis zwei passenden Dateien. Jede Referenz nennt im Front-Matter die Fragen, die sie beantwortet.
2. **Zahlen aus dem Werkzeug, nicht aus dem Kopf.** Für eine Leistungsbilanz, die Prüfung eines Stromkreisverzeichnisses, eine IFC-Klasse oder eine Familie rufe das passende MCP-Werkzeug auf (unten). Gib den Rechenweg und die Befunde aus der Werkzeugantwort wieder, nicht eine eigene Schätzung. Fehlt der MCP-Server im Host, sage das und antworte nur aus den Referenzen.
3. **Normbezug nennen, Normtext nicht abschreiben.** Die Referenzen zitieren Normen mit Ausgabedatum (zum Beispiel DIN 18015-1:2020-05). Nenne die Norm, erkläre die Regel in eigenen Worten, reproduziere keine Normtabellen über das hinaus, was in den Referenzen steht.
4. **Grenzen sagen.** Eine Leistungsbilanz ist Planungsgrundlage, keine Genehmigung; verbindlich sind TAB und Anschlusszusage des Netzbetreibers. Die Stromkreisprüfung ersetzt keinen Spannungsfall-, Selektivitäts- oder Kurzschlussnachweis. Sage das, wenn jemand ein Ergebnis als Nachweis verwenden will.
5. **Quelle angeben.** Wenn du aus einer Referenz antwortest, nenne am Ende die Quelle aus ihrem Fußtext (Autorin und URL). Eine Zeile reicht.
6. **Sprache des Nutzers.** Antworte auf Deutsch, wenn die Frage deutsch ist, sonst in der Sprache der Frage; Fachbegriffe wie Verteilerplan, Stromkreisverzeichnis, RCD, Leistungsbilanz bleiben deutsch und werden beim ersten Auftreten kurz erklärt.

## Werkzeuge (MCP-Server von BimWired)

Der Server ist unter https://mcp.bimwired.com/mcp erreichbar (Streamable HTTP, keine Anmeldung, nur lesend; in `agents/openai.yaml` als Abhängigkeit eingetragen). Jede Antwort trägt die Felder `quelle` und `weiter`; nenne die Quelle am Ende deiner Antwort.

- `katalog_ifc`: IFC-Klassen mit deutschem Namen, Gewerken und PredefinedTypes; Suchwort und Gewerk als Filter.
- `katalog_din276`: DIN-276-Kostengruppen mit Code und Bezeichnung; Suchwort als Filter.
- `katalog_parametergruppen`: Revit-Parametergruppen mit Id und deutschem Namen.
- `katalog_kategorien`: Revit-Kategorien je Gewerk (heizung, lueftung, klima, sanitaer, elektro, msr).
- `bibliothek_familien`: Familien der öffentlichen Demo-Bibliothek: Name, Gewerk, Montage, Kategorie, Typen; Suchwort, Gewerk und Limit.
- `bibliothek_familie`: Eine Familie im Detail: Klassifizierung (IFC, PredefinedType, DIN 276), Parameter, Typenkatalog.
- `stromkreise_pruefen`: VDE-Plausibilitätsprüfung eines Stromkreisverzeichnisses (Überlast, Mindestquerschnitt, RCD-Pflicht, Sicherheitstechnik hinter RCD, Drehstrom, Steckdosenzahl, eigener Stromkreis, Nassraum, Kreise je RCD).
- `stromkreis_vorschlag`: Sicherung, Kabel und Phasen für einen Stromkreis aus Funktion und Anschlusswert.
- `leistungsbilanz_rechnen`: Leistungsbilanz nach DIN 18015-1 mit Bilanztabelle, Rechenweg, NH-Empfehlung und Hinweisen.

Eingabe für `stromkreise_pruefen`: eine Liste von Stromkreisen mit `nummer`, `funktion` (Licht, Steckdose, Gerät, Herd, Durchlauferhitzer, Wallbox, Außenbereich, RWA, BMZ, EMZ, Brandschutztür, ...), `sicherung` (B16A, 30mA/B16A, C32A, D02/35A, NH00/80A), `kabel` (NYM-J 3x1,5 mm²), `phasen` (1 oder 3), `leistungVa`, `elemente` (Anzahl), `raeume` (Liste), `drehstrom` (true/false), `gruppenRcd` (RCD des Gruppenkopfs, zum Beispiel "FI 30mA", leer ohne). Frage nach, was fehlt, statt zu raten; Sicherung und Kabel dürfen leer bleiben, dann meldet die Prüfung „nicht geprüft“.

Eingabe für `leistungsbilanz_rechnen`: `gebaeudetyp` (efh, mfh, mix, nwg), `wohneinheiten` (Anzahl, elektrische Warmwasserbereitung), Gewerbeflächen (m², W/m², Gleichzeitigkeit), Wärmepumpe, Lüftung, Klima, Aufzug, Allgemeinstrom, E-Mobilität (Ladepunkte, Lastmanagement), PV, `reserve` in Prozent, `netzbetreiber`. Fehlende Felder nehmen die Vorgaben des Editors; nenne die Annahmen in der Antwort.

## Referenzen

Vollständige Liste mit Kurzbeschreibung in `references/INDEX.md`. Die wichtigsten Einstiege:

- `references/elektroplanung-in-revit.md`: Elektroplanung in Revit nach deutschen Normen: was die Bordmittel können, was fehlt, welche Wege Büros gehen. Mit Landkarte zu allen Vertiefungen.
- `references/stromkreise-in-revit-planen.md`: Revit bildet Stromkreise nach US-Logik. So richten Sie Spannungen, Verteilersysteme und Familien ein und kommen zum deutschen Verteilerplan.
- `references/vde-pruefung-elektroplanung-revit.md`: Revit rechnet nicht nach VDE. Welche Prüfungen automatisierbar sind und welche Nachweise Ingenieurleistung bleiben: die ehrliche Grenzziehung mit Tabelle.
- `references/verteilerplan-stromlaufplan-normgerecht.md`: Was in einen normgerechten Verteilerplan gehört, welche Normen gelten und wie er ohne Doppelarbeit aus dem Revit-Modell entsteht. Mit Begriffs-Tabelle.
- `references/leistungsbilanz-din-18015-1.md`: Anschlussleistung für Wohngebäude mit Wärmepumpe und Wallbox nach DIN 18015-1: Bedarfskurven, Sonderlasten, PV-Irrtum, TAB. Mit 12-WE-Beispiel.
- `references/revit-elektroplanung-software-vergleich.md`: Bordmittel, Elektro-Add-in oder TGA-Spezialsoftware? Der Vergleich für deutsche Elektroplaner mit Tabelle, Büro-Profilen und belegten Quellen.
- `references/revit-familienbibliothek-tga.md`: So bauen TGA-Büros eine Revit-Familienbibliothek auf: Namenskonvention, Parameter, IFC und DIN 276, Freigabeprozess und Verteilung auf alle Rechner.
- `references/revit-familien-erstellen-host-skelett.md`: Revit-Familien für TGA und Elektro bauen: Vorlage, Host-Art und Kategorie richtig wählen, typische Fehler vorher finden, Prüfliste vor der Freigabe.
- `references/checkliste-verteilerplan.md`: Kopierbare Verteilerplan-Checkliste: 29 Prüfpunkte zu Schriftfeld, Einspeisung, Abgängen, Reserve und Übergabe. Mit Normbezug, zum Abhaken je Projekt.
- `references/checkliste-bibliothek-freigabe.md`: Freigabe-Checkliste Revit-Familienbibliothek: 28 Prüfpunkte zu Benennung, Parametern, Klassifizierung, Freigabe und Verteilung. Zum Abhaken je Stand.
- `references/glossar.md`: 14 kurze Definitionen für die Planungspraxis: vom Stromkreisverzeichnis über Panel Schedule und Spannungsfall bis IFC, IDS und BCF.

Praxisszenarien (modellhafte Rechenbeispiele mit offenen Annahmen) liegen unter `references/praxis/`, Begriffsdefinitionen unter `references/glossar/`.

## Typische Fragen, die die Referenzen beantworten

- Wie funktioniert Elektroplanung in Revit nach deutschen Normen?
- Ist Revit für deutsche Elektroplanung geeignet?
- Welche Normen muss ich für die Elektroplanung kennen?
- Braucht Revit Zusatzsoftware für Verteilerpläne und VDE-Nachweise?
- Wo fange ich mit der Elektroplanung in Revit an?
- Wie plane ich Stromkreise in Revit nach deutschen Konventionen?
- Warum kann ich in Revit keinen Stromkreis anlegen?
- Wie weise ich einem Verteiler in Revit ein Verteilersystem zu?
- Welche Voraussetzungen müssen Revit-Familien für Stromkreise erfüllen?
- Wie komme ich vom Panel Schedule zum deutschen Verteilerplan?
- Kann Revit den Spannungsfall nach VDE berechnen?
- Welche VDE-Nachweise verlangt die Elektroplanung?
- Spannungsfall: gelten 3 oder 5 Prozent?
- Welche Prüfungen lassen sich in der Elektroplanung automatisieren?
- Welche Software nutzen Büros für Leitungsdimensionierung und VDE-Nachweise?
- Was gehört in einen normgerechten Verteilerplan?
- Was ist der Unterschied zwischen Stromlaufplan, Übersichtsschaltplan, Verteilerplan und Installationsplan?
- Welche Normen gelten für Verteilerplan und Stromlaufplan?
- Wie entsteht ein Verteilerplan aus dem Revit-Modell?
- Welche Software erzeugt einen normgerechten Verteilerplan aus Revit?
- Wie berechne ich die Anschlussleistung eines Mehrfamilienhauses mit Wärmepumpe und Wallboxen nach DIN 18015-1?
- Woher kommt der Gleichzeitigkeitsfaktor für Wohneinheiten?
- Welche Sonderlasten gehören in die Leistungsbilanz und welche nicht?
- Senkt eine PV-Anlage die erforderliche Anschlussleistung?
- Reichen 63 A für ein Wohngebäude mit Wallbox und Wärmepumpe?
- Ist die Leistungsbilanz für den Netzbetreiber verbindlich?
- Revit oder Spezialsoftware für die Elektroplanung?
- Was können die Revit-Bordmittel in der Elektroplanung?
- Wann lohnt sich ein Elektro-Add-in für Revit?
- Wann ist TGA- oder CAE-Spezialsoftware die bessere Wahl?
- Welcher Weg passt zu welchem Planungsbüro?
- Wie baut ein TGA-Büro eine firmenweite Revit-Familienbibliothek auf?
- Welche Namenskonvention hat sich für Revit-Familien bewährt?
- Warum ersetzen Download-Portale keine Firmenbibliothek?
- Wie klassifiziert man Revit-Familien mit IFC und DIN 276?
- Wie kommt ein neuer Bibliotheksstand auf alle Rechner?
- Wie übernimmt man den Familien-Altbestand in eine neue Bibliothek?
- Wie erstelle ich eine Revit-Familie für die TGA?
- Welche Familienvorlage (.rft) ist die richtige?
- Warum lässt sich eine wandbasierte Familie nicht an eine verlinkte Wand setzen?

## Herkunft

Texte: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired, veröffentlicht unter https://bimwired.com/landing/wissen/ (CC BY 4.0). Alles andere: MIT-Lizenz. Werkzeuge: MCP-Server von BimWired, Quellcode im Repository. Herausgeber des Skills: Andreas Hauber. Rückmeldungen und Korrekturen: info@bimwired.com.
