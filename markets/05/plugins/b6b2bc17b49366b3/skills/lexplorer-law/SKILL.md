---
name: lexplorer-law
description: "Schweizer Rechtsrecherche mit dem Lexplorer Law MCP: Rechtsprechung (BGer, BGE, BVGer, BStGer, kantonale Gerichte, EGMR), das geltende Bundesrecht (SR), kantonale Erlasse und Botschaften. Nutzen für jede Frage zu Schweizer Recht: Normauslegung, Urteilssuche ('BGE 140 III 86', '4A_123/2024', 'Leitentscheid zu …'), Erwägungen lesen, 'noch gültig?', Rechtsprechung zu Art. X OR/ZGB/StGB, kantonale Gesetze und Urteile, Prüfungs- und Mandatsantworten. Der Skill plant die Recherche, führt die Suchen selbst aus und schreibt eine strukturierte Antwort mit verifizierten, klickbaren Zitaten."
---

# Lexplorer Law — Schweizer Rechtsrecherche

## Wann dieser Skill greift

Bei jeder Frage zu Schweizer Recht, von der punktuellen Artikel- oder
Urteilsfrage bis zum offenen Gutachten oder zur mehrteiligen Prüfungsantwort.
Datenquelle ist der **Lexplorer Law MCP** (`law.lexplorer.ch`): rund eine
Million Urteile von über 100 Gerichten und Behörden (Bund, alle 26 Kantone,
EGMR), das gesamte geltende Bundesrecht (SR), ein Katalog der kantonalen
Erlasse mit Artikeltext, Botschaften und ein Zitationsgraph.

## Aufbau

- `methodology/` sagt, *was* in welcher Reihenfolge zu suchen ist, je Rechtsgebiet.
  Lies nur die Datei, die zur Frage passt.
- `tools/lexplorer-law.md` sagt, *wie* die Tools bedient werden. Lies sie, bevor
  du das erste Tool aufrufst.
- `synthesis.md` regelt die Antwort, `review.md` die Quellenprüfung auf Wunsch.

## Klassifizieren und leiten

- **Bundesrecht** (OR, ZGB, StGB, BGG, öffentliches Bundesrecht, „was sagt
  Art. X“) → `methodology/federal.md`
- **Rechtsprechung** (bekannte Referenz, offene Rechtsprechungsfrage, „noch
  gültig?“, Richter/Besetzung, Trends) → `methodology/case-law.md`,
  `methodology/composite.md`
- **Prüfungs- oder Mandatsantwort** (mehrteiliger Sachverhalt, „prüfen Sie die
  Ansprüche von …“) → `methodology/exam-answer.md`, bei mehrteiligen
  Sachverhalten zwingend
- **Kantonal** (Verwaltungsrecht, Bau/Planung, Gemeinden, kantonale Urteile) →
  `methodology/cantonal.md`
- **Steuerrecht**: Steuerurteile (BGer, BVGer, kantonal) und die
  Bundessteuergesetze (DBG, MWSTG, StHG, VStG) findest du hier. Kantonale
  Steuergesetze im Wortlaut, Kreisschreiben, Verwaltungspraxis und Lehre deckt
  das separate Plugin „Lexplorer Swiss Tax Research“ ab. Ist es nicht verbunden,
  sag das offen und arbeite mit dem, was dieser Server liefert.
- **Unklar**: eine gezielte Rückfrage; bleibt es offen, mit dem
  wahrscheinlichsten Gebiet beginnen und ausweiten.

Danach `synthesis.md` für die Antwort.

## Flexibel statt starr

Die Methodik-Dateien geben die Reihenfolge für **offene** Fragen vor. Gezielte
Fragen springen direkt zum passenden Schritt:

- „Was sagt Art. 336a OR?“ → `get_article`, keine Rechtsprechungs-Kaskade.
- „Finde den BGE zu X“ / „gibt es einen Leitentscheid zu Y?“ →
  `find_leading_cases` bzw. `nav_find`.
- „Urteile des Obergerichts Zürich zu Z“ → Gerichtscode aus `nav_tree()`
  (`courts`), dann Suche mit `court="zh_obergericht"`.

Brich ab, sobald die Antwort steht. Eine offene oder dogmatische Frage braucht
aber immer mindestens eine auslegende Quelle (Leitentscheid, Botschaft), nie
nur den Gesetzestext.

## Eiserne Regeln

- **Norm zuerst**: Vor jeder Rechtsprechungsrecherche den massgebenden Artikel
  vollständig mit `get_article` lesen, inklusive zweitem Halbsatz, weiterer
  Absätze und der Nachbarartikel (`nav_law_toc`). Die Rechtsgrundlagen in der
  Antwort ausdrücklich nennen.
- **Nur Gelesenes zitieren**: Wörtliche Zitate, E.-Nummern, Dossiernummern und
  Daten stammen ausschliesslich aus `read_chunk`- oder `read_section`-Ausgaben,
  nie aus einer Vorschau (`preview`) oder aus dem Gedächtnis.
- **„Noch gültig?“** nur mit `get_citing_decisions(id, since_date=…)`. Fehlen
  spätere Zitierungen, heisst das „keine späteren Zitierungen im Korpus“,
  nicht „bestätigt“.
- **Keine Rechtsprechungsantwort ohne verifiziertes Zitat.** Findet die direkte
  Suche nichts, zuerst `find_leading_cases(topic=…)` und
  `get_article_case_law` auf die massgebende Norm.
- **Leitentscheid-Hop**: Ein passender Treffer ist selten der zu zitierende
  Fall. Über `get_case_brief(id)` (`citation_impact`) und
  `get_cited_decisions(id)` zum Leitentscheid gehen.
- **Schluss-Check**: `verify_citations([...])` über jedes Zitat im Entwurf. Nicht
  gefundene Referenzen streichen, die kanonische Zitierform übernehmen
  (BGE-Form, wenn publiziert).

## Zitate

Jede Quelle ist ein klickbarer Markdown-Link an der Stelle, wo sie verwendet
wird. Link ist immer das Feld `lexplorer_url` des Tool-Resultats: Es steht bei
Urteilen, Bundesgesetzesartikeln und kantonalen Erlassen und führt auf eine
öffentliche Lexplorer-Quellseite mit Stand und Link zur amtlichen Quelle.
Fehlt es, wird ohne Link zitiert. Nie URLs erfinden. Details und
Quellenverzeichnis in `synthesis.md`.

## Arbeitsweise

Vor der ersten Suche einen kurzen Plan festhalten: Einordnung, die geplanten
Schritte (offene Frage) oder den einen gezielten Schritt. Nach jeder Suche
Trefferzahl und die wichtigsten Quellen notieren, bei zentralen Urteilen
Dossier, Ergebnis und Kernaussage in einem Satz.

Sind die Tools des Lexplorer Law MCP nicht aufrufbar, ist der Connector nicht
verbunden. Sag das, statt Gesetzes- oder Urteilstext aus dem Gedächtnis zu
rekonstruieren.
