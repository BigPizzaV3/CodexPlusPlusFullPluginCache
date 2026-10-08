---
name: lexplorer-tax
description: Schweizer Steuerrecht-Recherche mit dem Lexplorer Tax MCP. Nutzen für JEDE Schweizer Steuerfrage: DBG, MWSTG, StHG, VStG, Verrechnungssteuer, Emissions-/Stempelabgaben, kantonale Steuergesetze und Steuerbücher, ESTV-/SSK-Kreisschreiben, MWST-Infos, Lehre/Kommentare (ILE-HSG), §-Lookups wie «Was sagt § 31 StG ZH?», interkantonale Vergleiche. Der Skill plant die Recherche (Lehre → Rechtsprechung → Gesetz + Verwaltungspraxis → kantonale Normen), führt die Suchen selbst aus und schreibt eine strukturierte deutsche Antwort mit verifizierten, klickbaren Zitaten.
---

# Lexplorer Tax — Schweizer Steuerrecht-Recherche

## Wann dieser Skill greift

Bei jeder Schweizer Steuerfrage — von der punktuellen §-Frage bis zum
offenen Rechtsgutachten. Datenquelle ist der **Lexplorer Tax MCP**
(`mcp-tax.lexplorer.ch`): Gesetzestexte (Bund + 26 Kantone), komplette
Verwaltungspraxis (ESTV/SSK-Kreisschreiben, MWST-Publikationen,
Stempelabgaben-Praxis), Steuerbücher, Kommentierungen und die ILE-HSG-Lehre.

## Arbeitsweise

1. Lies `methodology/tax.md` — sie definiert die Prüfreihenfolge
   (gezielt vs. offen; Lehre → Rechtsprechung → Gesetz + Verwaltungspraxis →
   kantonale Normen) und die Abgrenzungsregeln (DBG vs. StHG vs. MWSTG vs.
   VStG vs. kantonales Recht).
2. Für die Tool-Mechanik (Navigation, Suchfilter, Kategorien, Zitier-Links)
   lies `tools/tax-mcp.md`.
3. Antworte auf Deutsch, strukturiert, mit Fundstelle zu jeder tragenden
   Aussage. Keine Aussage ohne gelesene Quelle; `preview` allein genügt nie.

## Iron Rules

- **Norm-First**: Gesetzestext vollständig lesen, bevor Praxis/Lehre
  eingeordnet wird; bei kantonalen Fragen IMMER `filter_kanton` setzen.
- **Ebenen trennen**: DBG (direkte Bundessteuer) · StHG (Harmonisierung) ·
  MWSTG · VStG · kantonales StG — nie vermischen; Kreisschreiben haben
  Indizwirkung, binden Gerichte nicht.
- **Offene Fragen**: mindestens eine interpretative Quelle (Lehre,
  Verwaltungspraxis oder Rechtsprechung) — nie Gesetzestext allein.
- Urteils-Recherche (BGer/BVGer/kantonal) läuft über den separaten
  **Lexplorer Legal**-Connector, falls verbunden; sonst Web-Verifikation
  nur auf offiziellen Domains (bger.ch, bvger.ch, estv.admin.ch).
