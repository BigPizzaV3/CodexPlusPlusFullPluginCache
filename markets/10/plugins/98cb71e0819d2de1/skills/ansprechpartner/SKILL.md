---
name: ansprechpartner
description: Findet Ansprechpartner bei einem Unternehmen, das die Website besucht hat, und zeigt E-Mail oder Rufnummer nur auf ausdrückliche Anfrage. Nutzen bei "wen kann ich dort anrufen", "Ansprechpartner bei", "E-Mail von", "Entscheider bei". / Finds contacts at a company that visited the website and reveals e-mail or phone only when explicitly requested. Use for "who can I call there", "contacts at", "e-mail of", "decision makers at".
---

# Ansprechpartner

Webmetic identifiziert Unternehmen. Ansprechpartner gibt es nur für
Unternehmen, die die Website besucht haben, und nur wenn der Nutzer
ausdrücklich danach fragt.

## Vorgehen

1. **Unternehmen bestimmen.** `find_contacts` nimmt den Namen, die
   `company_id` oder die Website-Domain eines Besuchers und löst ihn über
   die Besucherdaten des Zeitraums auf. Kommt „kein identifizierter
   Besucher", den Zeitraum weiten (`from_date="-365 days"`) oder den Namen
   aus `list_visiting_companies` übernehmen. Ein Unternehmen, das nie da
   war, hat keine Ansprechpartner in Webmetic.
2. **Suchen** mit `find_contacts`, ein Unternehmen pro Aufruf. Ohne Filter
   gelten Abteilungen und Seniorität aus dem Ansprechpartner-Profil des Kontos;
   `departments` und `seniority` nur setzen, wenn der Nutzer sie nennt.
   Die Tabelle zeigt Name, Position und welche Daten vorliegen
   („available") oder bereits freigeschaltet sind.
   Meldet das Tool, dass die Ansprechpartner noch nicht freigeschaltet
   sind, geschieht das hier im Chat: die drei Zustimmungen aus
   `enable_contacts` zeigen, das Tool erst nach dem ausdrücklichen Ja des
   Nutzers aufrufen und danach die Suche wiederholen.
3. **Freischalten nur auf ausdrücklichen Wunsch** mit `reveal_contact`, ein
   Kontakt pro Aufruf. `reveal="email"` liefert E-Mail und LinkedIn,
   `"phone"` Direktwahl und Mobil, `"both"` beides. Nur den vom Nutzer
   verlangten Datentyp anfordern. Bereits offengelegte Daten können auch in
   späteren `find_contacts`-Tabellen erscheinen.
4. **Ergebnis ausgeben:** Person, Position und die ausdrücklich angeforderten
   Kontaktdaten. Nicht verfügbare Daten sachlich benennen.

## Regeln

- Nie über eine Besucherliste schleifen und für jedes Unternehmen
  Ansprechpartner holen. Ein Unternehmen, das der Nutzer nennt.
- Nichts freischalten, was der Nutzer nicht verlangt hat; „Ansprechpartner
  zeigen" heißt suchen, nicht freischalten.
- Ist unklar, ob E-Mail, Rufnummer oder beides gewünscht ist, vor dem
  Freischalten nachfragen.
- Kontaktdaten nur wiedergeben, wie das Tool sie liefert. Keine E-Mails
  aus Namensmustern erraten.
- In der Sprache des Nutzers antworten. Auf Deutsch: „Unternehmen" statt
  „Firma".
