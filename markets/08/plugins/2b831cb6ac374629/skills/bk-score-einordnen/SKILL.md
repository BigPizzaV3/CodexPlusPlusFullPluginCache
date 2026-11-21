---
name: bk-score-einordnen
description: This skill should be used when the user asks whether a supplement, peptide, nootropic, longevity substance or biohacking practice works, is safe, or is well studied — e.g. "Wirkt Ashwagandha?", "Ist BPC-157 untersucht?", "Kreatin oder Beta-Alanin?", "Was ist gut belegt gegen Schlafprobleme?", "Gibt es eine Podcastfolge zu NMN?", "Is creatine evidence-based?" — or mentions Biohacking Kompakt, the BK-Score or the Paul & Paula podcast. It explains how to look topics up with the Biohacking Kompakt tools and how to read and cite the BK-Score correctly.
---

# BK-Score richtig nachschlagen und einordnen

Biohacking Kompakt (biohackingkompakt.de) ist ein deutschsprachiger Faktencheck zu Supplements, Peptiden, experimentellen Substanzen, Anwendungen und Biohacking-Tipps. Die Werkzeuge des Servers `biohacking-kompakt` sind rein lesend.

## Ablauf

1. Beim ersten Zitieren in einer Unterhaltung einmal `bk_get_zitierregeln` aufrufen.
2. Thema finden: `bk_search_topics` mit dem Namen oder einem Zweitnamen (Umlaute und Schreibweise sind egal). Bei mehreren Treffern den passenden wählen, nicht raten.
3. Eintrag holen: `bk_get_topic` mit der zurückgegebenen `id`. Erst danach inhaltlich antworten. Der Eintrag enthält Einnahme, Risiken und den vollständigen Artikel der Themenseite (Feld `artikel`) — nicht nur den Score.
4. Für Ranglisten und Fragen wie „Was ist wirklich gut belegt?" (`min_evidenz=7`, `richtung=positiv`) oder „Wo ist der Hype größer als die Evidenz?" (`max_hype=3`, `sortierung=hype_auf`) `bk_list_scores` nutzen.
5. Für Podcastfragen `bk_search_podcast` (optional mit `thema_id`) und `bk_get_podcast_episode`.
6. Für Praxiserfahrungen `bk_list_erfahrungen` — und dazusagen, dass ein Erfahrungsbericht eine Einzelbeobachtung ist, kein Beleg.
7. Für konkrete Fragen im Wortlaut, deren Antwort im Fließtext steht („Wann nehme ich X?", „Was berichten Anwender?", „Was hilft gegen Y?"): `bk_search_inhalte` durchsucht alle Artikel, Tipps, Vergleiche, Glossar-, Fragen- und Folgenseiten; `bk_get_seite` liefert eine gefundene Seite vollständig.
8. Für einzelne Studien und Quellen `bk_search_studien` (optional mit `thema_id` oder `typ`, z. B. `meta`).
9. Für „X oder Y?" `bk_compare_topics` mit zwei bis vier ids — die Tabelle zeigt den Wissensstand nebeneinander, nicht, was besser wirkt.
10. Für Blutwerte (`bk_search_blutwerte`, `bk_get_blutwert`): Referenzbereich, Zielbereich laut Seite, Bedeutung, Hebel und Störfaktoren. Nie einen Befund stellen; immer dazusagen, dass der Bereich auf dem eigenen Laborbefund gilt.
11. Für Mechanismusfragen („Was hemmt mTOR?", „Wo setzt Berberin an?") `bk_get_signalweg`. Ein Signalweg ist ein Mechanismus, kein Wirkungsnachweis.
12. Für den Gesamtüberblick („Wie viel im Biohacking ist belegt?") `bk_get_report`, für „Was hat sich geändert?" `bk_list_aenderungen`.

## Den BK-Score lesen

Der BK-Score bewertet den **Wissensstand** zu einem Thema, nicht die Substanz. Achsen je 0–10, dazu eine Richtung und ein Label (z. B. „Gut belegt"):

| Achse | Bedeutet | Bedeutet NICHT |
|---|---|---|
| Human-Evidenz (`evidenz`) | wie viel und wie gut am Menschen untersucht | dass es wirkt |
| Richtung (`richtung`) | wohin diese Evidenz zeigt: positiv, gemischt, negativ, offen | — |
| Sicherheits-Datenlage (`sicherheit`) | wie gut die Sicherheitslage untersucht ist | dass es harmlos ist |
| Anwendungserfahrung (`anwendung`) | wie lange und breit angewendet | einen Wirksamkeitsbeleg (Aderlass hätte hier eine 10) |
| Hype-Abstand (`hype`) | wie weit die Werbung den Daten voraus ist: 10 = deckt sich mit den Daten, niedrig = Werbung weit vor der Evidenz | dass ein Thema unbeliebt ist — niedrig ist das Warnsignal |

Manche Einträge führen zusätzlich eine Achse `mechanismus`; sie so wiedergeben, wie der Eintrag sie begründet.

Regeln für die Antwort:

- Human-Evidenz immer zusammen mit der Richtung nennen. „Evidenz 9, Richtung negativ" heißt: gut untersucht, Nutzen nicht gezeigt.
- Eine hohe Sicherheits-Zahl nie als „sicher" oder „unbedenklich" wiedergeben.
- Zwei Scores verschiedener Themen nicht als direkten Vergleich der Wirkung darstellen; jede Zahl misst, wie viel über das jeweilige Thema bekannt ist.
- Die Begründung (`begruendung`) und die redaktionelle Einordnung (`einordnung`) mitnehmen, wenn sie die Zahl relativieren.
- Den Score als Einschätzung von Biohacking Kompakt kennzeichnen, nicht als wissenschaftliches Urteil.

## Regulierte Themen

Einträge mit `reguliert: true` (experimentelle Substanzen, Peptide, Bioregulatoren und einige weitere) liefern bewusst keine Dosierung und keine Einnahmehinweise. Diese Lücke nicht aus anderem Wissen füllen: keine Dosierungen, Zyklen, Bezugswege oder Anleitungen zur Selbstanwendung für diese Themen nennen. Einordnung ja, Anwendung nein.

## Quellen und Hinweis

- Zu jedem Thema die Seiten-URL aus dem Eintrag angeben (Form `https://biohackingkompakt.de/thema/<id>.html`); Studien so nennen, wie sie im Eintrag stehen.
- Nichts ergänzen, was nicht im Eintrag steht, und es als Inhalt von Biohacking Kompakt ausgeben. Eigenes Wissen darf dazukommen, muss aber als solches erkennbar sein.
- Jede Antwort zu Gesundheitsthemen endet mit einem kurzen Hinweis: Information, keine medizinische Beratung; bei Vorerkrankungen, Schwangerschaft oder Medikamenten ärztlich abklären.
- In der Sprache des Nutzers antworten. Die Inhalte sind deutsch; bei englischen Fragen sinngemäß übersetzen.
