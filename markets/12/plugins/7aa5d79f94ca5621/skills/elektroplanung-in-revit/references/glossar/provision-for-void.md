---
titel: "Was ist ein Provision for Void?"
quelle: https://bimwired.com/landing/wissen/glossar/provision-for-void.html
stand: 2026-08-25
art: glossar
---

# Was ist ein Provision for Void?

Ein Provision for Void ist ein Durchbruchsvorschlag in der modellbasierten Schlitz- und Durchbruchsplanung: ein Platzhalterkörper, mit dem die TGA-Planung anmeldet, wo Wand, Decke oder Träger für Trassen und Leitungen durchdrungen werden sollen. Nach dem frei verfügbaren Leitfaden „einfach bim" reisen solche Vorschläge im IFC-Modell als IfcBuildingElementProxy mit der Klassifikation „ProvisionForVoid", mit Verortung, geschlossenem Körper und Attributen. Erst nach Prüfung und Freigabe durch Objekt- und Tragwerksplanung wird aus dem Vorschlag eine tatsächliche Öffnung.

Abbildung: Eine Wand im Schnitt, in der ein gestrichelter Platzhalterkörper um eine durchlaufende Trasse liegt, daneben der Weg von der TGA-Planung über Objekt- und Tragwerksplanung bis zur Öffnung im Bauteil. Der gestrichelte Körper ist der Antrag, nicht das Loch: Ob daraus eine Öffnung wird, entscheiden Objekt- und Tragwerksplanung.

Warum das geregelt gehört, begründet der VDI in einer Meldung zur Richtlinie VDI/bS 2552 Blatt 11.2 (2022): Bei Planung und Ausführung von Aussparungen arbeiten viele Beteiligte zusammen, unklare Kommunikation ist deshalb ein hohes Fehlerrisiko; das BIM-Modell verringert Fehlinterpretationen.

Ein häufiger Fehler sind Vorschläge ohne saubere Klassifikation und Attribute: Der Empfänger kann sie nicht automatisiert filtern, und sie fallen aus dem Freigabe-Workflow heraus. Wichtig für die Rollen: Der Provision for Void hat Antragscharakter; über die Öffnung entscheiden Objekt- und Tragwerksplanung.

## Weiterführend

- [Elektroplanung in Revit: der Leitfaden](https://bimwired.com/landing/wissen/elektroplanung-in-revit.html)

## Quellen

- einfach bim: Anwendungsfall Schlitz- und Durchbruchsplanung (Version 4.7, 05.11.2022), https://www.einfachbim.de/files/2022/11/einfach-bim-anwendungsfall-schlitz-und-durchbruchsplanung.pdf (abgerufen am 25.08.2026)
- VDI: Mehr Sicherheit und Effizienz durch Informationsaustausch (13.07.2022), https://www.vdi.de/news/detail/mehr-sicherheit-und-effizienz-durch-informationsaustausch (abgerufen am 25.08.2026)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/glossar/provision-for-void.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
