# KI-Tutor Grundlagen der ET

Ein deutschsprachiges Codex-Plugin für Studierende im ersten Semester. Der enthaltene Skill unterstützt bei Verständnisfragen und Übungen zu den Grundlagen der Elektrotechnik, prüft Lösungswege und beantwortet inhaltliche Fragen zur Vorlesung.

## Inhalt

- ein Tutor-Skill unter `skills/ki-tutor-et/`
- interne Referenzmaterialien für Übungen und Vorlesungsinhalte
- Verweise auf passende öffentlich erreichbare Vorlesungsvideos

Das vollständige Vorlesungstranskript ist in thematische Abschnitte gegliedert und mit den inhaltlich passenden Übungsaufgaben verknüpft. Aufgaben ohne hinreichend passende Stelle erhalten keinen pauschalen Videoverweis.

Nummerierte Aufgaben liegen als einzelne Dateien mit den jeweils passenden Videoabschnitten vor. So muss der Tutor für eine Frage nach Aufgabe 1.4 nicht den gesamten Transkriptindex durchsuchen.

## Nutzung

Beispielanfragen:

- „Gib mir einen Ansatz für die Aufgabe 1.4“
- „Prüfe meinen Lösungsweg und erkläre mir meine Fehler.“
- „Erkläre mir den mehrfachen Spannungsteiler Schritt für Schritt.“

Der Tutor gibt bevorzugt Hilfestellungen statt fertiger Endergebnisse. Ein Endergebnis wird ausgegeben, wenn ausdrücklich danach gefragt wird.

Vor der Nutzung muss der Thinking-Modus („Nachdenken“) aktiviert werden; sonst kann der Zugriff auf die mitgelieferten Wissensdateien ausbleiben.

## Veröffentlichung

Die erforderlichen Rechte und Freigaben für die enthaltenen Lehrmaterialien und das verwendete Logo wurden vom Herausgeber bestätigt. Das einreichbare Archiv wird unter `dist/` erzeugt; Angaben für das OpenAI-Einreichungsportal stehen unter `submission/`.

Das Plugin ist als reines Skills-Plugin aufgebaut. Es enthält keinen MCP-Server, keine App-Konfiguration und keine eigene Benutzeroberfläche.

Das Veröffentlichungs-ZIP enthält die 140 Aufgaben-Einzeldateien, die benötigten Abbildungen und die gegliederten Vorlesungsabschnitte. Die Gesamtsammlung der Aufgaben, das Rohtranskript, die separate Aufgaben-Video-Zuordnung und die Erzeugungs- und Prüfscripts bleiben nur im Entwicklungsordner.

Die Übungsdaten liegen in mitgelieferten Referenzdateien. Ob der Tutor sie in einer Sitzung lesen kann, hängt von den dort verfügbaren Dateiwerkzeugen ab. Ein installiertes Plugin allein garantiert keinen Zugriff auf diese Dateien. Wenn der Zugriff fehlt, benötigt der Tutor den Aufgabentext und bei bildabhängigen Aufgaben auch die Skizze von der nutzenden Person.
