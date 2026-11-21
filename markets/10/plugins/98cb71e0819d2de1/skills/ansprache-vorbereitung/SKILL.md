---
name: ansprache-vorbereitung
description: Bereitet die Ansprache eines besuchenden Unternehmens vor — holt Besuchskontext und Profil und liefert belegte Gesprächsaufhänger, aus denen sich eine Nachricht schreiben lässt. Schreibt die Nachricht nicht selbst. Nutzen bei "wie spreche ich [Unternehmen] an", "Gesprächsaufhänger für", "bereite die Ansprache vor", "was schreibe ich [Unternehmen]", "Aufhänger für den Erstkontakt". / Prepares outreach to a visiting company — pulls visit context and profile and returns grounded talking points to write a message from. Does not write the message. Use for "how do I approach [company]", "talking points for", "prep outreach to", "what do I say to [company]".
---

# Ansprache vorbereiten

Liefert Gesprächsaufhänger, keine fertige Nachricht. Die Aufhänger sind das
Rohmaterial, die Formulierung bleibt beim Nutzer. So bleibt der Ton seiner und
jede Aussage belegt.

## Sprache

Antwort in der Sprache des Nutzers. Unternehmensnamen, Domains und Seitenpfade
bleiben unverändert. Auf Deutsch „Unternehmen" statt „Firma".

Die Sprache der späteren Nachricht kann davon abweichen: Wer auf Deutsch arbeitet,
schreibt dem Gegenüber vielleicht auf Englisch. Sagt der Nutzer nichts dazu, die
Sprache der Unterhaltung annehmen und einmal anbieten, es anders zu machen.

## Wann diese Skill greift

Der Nutzer nennt ein Unternehmen und will wissen, womit er herangeht. Auch nach
einem `unternehmens-brief`, wenn er den nächsten Schritt wählt. Nicht auslösen bei
„schreib mir eine Kaltakquise-Mail" ohne benanntes Unternehmen: Dafür gibt es
keine Datengrundlage.

## Ablauf

1. **Unternehmen und Besuche holen** mit `get_company_profile` und
   `get_company_activity`, Zeitraum 90 Tage, wenn nichts anderes gesagt wird.
2. **Verdichten:** Welche Seiten und Themen, wie oft, wie lange, über welche
   Quelle, welche Ereignisse (Formular, Download, Kontaktklick), und wie sich das
   über die Zeit entwickelt hat.
3. **Zwei bis vier Aufhänger ableiten.** Ein Aufhänger ist keine Rohzahl, sondern
   eine Deutung: was angesprochen wird und warum es beim Gegenüber ankommt. Je
   stärker ein Aufhänger ein Verhalten mit einem Anlass verbindet, desto besser.
   Trägt die Datenlage nur einen Aufhänger, ist einer die richtige Zahl.
4. **Ausgeben** nach dem Format unten.

**Abbruchgründe:** kein identifizierter Besuch im Zeitraum (dann sagen, dass es
keine Grundlage gibt, statt allgemeine Vertriebstipps zu geben); im Free-Plan
verborgen; Unternehmen nicht gefunden.

## Regeln für die spätere Nachricht

Diese Regeln gelten, sobald aus den Aufhängern eine Nachricht wird. Sie sind der
wichtigste Teil dieser Skill und werden mit ausgegeben.

- **Keine Beobachtungen zitieren.** Keine Verweildauer, keine Seitenpfade, keine
  Besuchszahlen, kein „Sie waren dreimal auf unserer Preisseite". Genau das
  Nacherzählen, wer was wie lange getan hat, macht eine Nachricht unheimlich.
- **Keine Person unterstellen.** Webmetic erkennt Unternehmen, keine Personen.
  Niemandem schreiben, er persönlich sei auf der Website gewesen. Das wäre nicht
  nur übergriffig, es ist durch die Daten auch nicht gedeckt.
- **Über das Thema einsteigen, nicht über die Messung.** Nicht „Sie haben sich
  unsere Preise angesehen", sondern der Anlass dahinter: die Aufgabe, die Branche,
  der Zeitpunkt.
- **Zuerst der Nutzen für das Gegenüber**, dann das eigene Angebot.
- Lässt sich ein Aufhänger nur formulieren, indem man Tracking-Details nennt,
  gehört er nicht in die Nachricht.

## Ausgabeformat

Bei jedem Lauf gleich, auch wenn die Skill in derselben Unterhaltung schon lief.
Abschnitte ohne Daten weglassen.

```
## Ansprache — {Unternehmen}

**Warum jetzt:** {Ein Satz, der stärkste Anlass, belegt aus den Daten.}

### Besuchskontext (letzte {N} Tage)
- **Besuche:** {Anzahl}
- **Erster / letzter Besuch:** {Datum} / {Datum}
- **Themen und Seiten:** {Pfade}
- **Quellen:** {Direkt, Google, LinkedIn …}
- **Kaufsignale:** {Formular, Download, Kontaktklick mit Datum — oder "keine"}
- **Datenlage:** {✅ tragfähig / ⚠️ dünn / ❌ keine Besuche im Zeitraum}

### Gesprächsaufhänger
1. **{Aufhänger}** — {Ein Satz: was angesprochen wird und warum es ankommt.}
2. **{Aufhänger}** — …

### Für die Nachricht
{Die Regeln oben in zwei bis drei Zeilen, auf diesen Fall gemünzt: was hier
ausdrücklich nicht in die Nachricht gehört.}

Zum Weiterarbeiten kopieren:

Schreib daraus eine kurze E-Mail an {Unternehmen}
```

## Quellenregel

Jeder Aufhänger lässt sich auf eine konkrete Antwort der Werkzeuge zurückführen:
eine Seite, ein Ereignis, ein Datum. Nichts erfinden, auch keine Branchenanekdote.
Zahlen in Aufhängern und Besuchskontext müssen übereinstimmen: Eine genannte Zahl
entspricht den aufgezählten Einträgen. Ist die Datenlage dünn, sind weniger
Aufhänger die richtige Antwort.

## Was nicht zu tun ist

- Die Nachricht nicht selbst schreiben. Diese Skill liefert Aufhänger.
- Keine Ansprechpartner suchen und nichts freischalten. Das ist `ansprechpartner`
  und wird ausdrücklich verlangt.
- Keine allgemeinen Vertriebstipps, wenn die Daten dünn sind. Dann lieber sagen,
  dass das Unternehmen kalt ist.
- Keine Kaufabsicht behaupten, die die Besuche nicht hergeben.
