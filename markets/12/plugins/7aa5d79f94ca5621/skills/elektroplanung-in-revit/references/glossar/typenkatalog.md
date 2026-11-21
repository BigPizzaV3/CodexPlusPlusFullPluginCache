---
titel: "Was ist ein Typenkatalog in Revit?"
quelle: https://bimwired.com/landing/wissen/glossar/typenkatalog.html
stand: 2026-08-25
art: glossar
---

# Was ist ein Typenkatalog in Revit?

Ein Typenkatalog ist eine Textdatei, die neben einer Revit-Familie (.rfa) liegt und deren Typvarianten mit ihren Parameterwerten auflistet. Beim Laden der Familie zeigt Revit daraus eine Auswahlliste, und nur die tatsächlich benötigten Typen kommen ins Projekt. Das hält Projekte schlank und macht Familien mit vielen Varianten, etwa Typserien eines Herstellers, überhaupt erst pflegbar.

Abbildung: Das Dateipaar Steckdose.rfa und Steckdose.txt im selben Ordner, daneben der Aufbau der Textdatei mit Kopfzeile aus Parametern samt Datentyp und Einheit und je einer Zeile pro Typ sowie die Auswahlliste beim Laden. Die Verbindung entsteht allein über den Dateinamen; stimmen Name, Endung oder Ordner nicht, lädt Revit die Familie ohne jede Typauswahl.

Bewährte Praxisregeln für Typenkataloge:

- Die Datei trägt denselben Namen wie die Familie, mit der Endung .txt, und liegt im selben Ordner; nur dann verbindet Revit beides beim Laden.
- Die Werte sind durch Kommas getrennt; der Spaltenkopf nennt je Parameter in der Praxis auch Datentyp und Einheit, damit Revit die Werte korrekt interpretiert.
- Gespeichert wird am besten als UTF-8 mit BOM, sonst kommen Umlaute in Typnamen verstümmelt an.

Probleme entstehen vor allem, wenn jemand Parameter an der Familie ändert und den Katalog nicht nachzieht: Dann passen Spalten und Parameter nicht mehr zusammen, das Laden schlägt fehl oder liefert leere Werte. Der Typenkatalog erzeugt weder Geometrie noch Parameter; er füllt nur Werte in Parameter, die die Familie bereits hat.

In BimWired führt jede Familie ihren Typenkatalog mit bis zu 60 Typen direkt im Browser.

## Weiterführend

- [Revit-Familienbibliothek fürs TGA-Büro aufbauen](https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/glossar/typenkatalog.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
