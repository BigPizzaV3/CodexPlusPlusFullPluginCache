---
name: setup
description: Richtet die Nutzung des SemBan-Studienassistenten nach der Installation ein: bestehendes Konto verbinden, Cloudstand prüfen und eine passende erste Studienübersicht öffnen.
---

# SemBan einrichten

Hilf dem Studenten, SemBan in wenigen Schritten sinnvoll zu nutzen. Dieser
Skill beschreibt die Einrichtung; er registriert keine Tools und führt keine
Anmeldung stellvertretend durch.

1. Prüfe, ob die SemBan-MCP-Tools im Host bereits verfügbar sind. Falls die
   Verbindung fehlt oder eine Freigabe abgelaufen ist, erkläre den normalen
   Verbindungsweg des Hosts. Die Anmeldung und Zustimmung erfolgen auf SemBan.
   Frage keine Telefonnummern, Passwörter, SMS-Codes oder Tokens im Chat ab.
2. Die Verbindung benötigt ein bestehendes SemBan-Konto mit Cloud-Sync.
   Für den vollständigen Funktionsumfang gelten die bestehenden Freigaben
   `study:read`, `planner:read` und `tasks:propose`. Fehlende Freigaben erklären,
   statt sie selbst zu erweitern. Bestehende begrenzte Verbindungen funktionieren
   weiter mit den jeweils erlaubten Lesefunktionen.
3. Verwende ein bereits bekanntes Datum und eine bekannte IANA-Zeitzone.
   Frage kurz nach, wenn die Zeitzone für die gewünschte Ansicht fehlt.
   Öffne mit `get_daily_dashboard` die vorhandene Tageskarte, wenn der Student
   einen Überblick möchte und die erforderlichen Tools verfügbar sind.
   Ist zunächst nur Lernstatistik freigegeben, verwende bei bekanntem Zeitraum
   stattdessen `get_study_summary`.
4. Erkläre den letzten synchronisierten Stand. Bei fehlenden Kursen oder Aufgaben
   leite zum regulären Anlegen beziehungsweise Synchronisieren in SemBan an.
   Erzeuge keine Beispieldaten im Konto und behaupte keinen aktuellen Cloudstand.
5. Gib höchstens zwei sinnvolle nächste Möglichkeiten passend zum Anliegen:
   etwa Stundenplan ansehen oder Lernfenster mit einem selbst genannten
   Zeitbudget finden. Nutze anschließend den verpackten `student-assistant`-Skill.

Wenn eine Aufgabe vorbereitet wird, prüft und bestätigt der Student die genauen
Angaben in der bestehenden Karte. Die angemeldete SemBan-App übernimmt sie beim
nächsten sicheren Abgleich und synchronisiert anschließend. Eine gespeicherte
Bestätigung ist noch kein Nachweis der Aufgabenübernahme. Das Modell ruft
`decide_task_proposal` niemals auf.

Zum Widerrufen führt der reguläre Weg zu
https://semban.de/oauth/verbindungen. Nimm keine Migration, Veröffentlichung
oder Änderung an persönlichen Kontodaten vor.
