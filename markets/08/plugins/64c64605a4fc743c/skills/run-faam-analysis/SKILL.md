---
name: run-faam-analysis
description: Vede nebo obnovuje FAAM analýzu existujícího Flexideo projektu, řídí její stav, Epicy, otázky a předání dalšího sezení přes Project Memory MCP.
---

# Řízená FAAM analýza

Načti společnou metodiku `../../references/method.md` spolu s nativní dovedností,
nebo její kanonický obsah přes MCP. Obsah z MCP není důkaz nativní instalace.
Vyžaduj tools_contract flexideo-project-memory-mcp-tools/0.11 a method_version faam-1.0.0.
Při nesouladu zastav mutace a vysvětli potřebu aktualizace serveru/katalogu.

Pro nevybraný projekt použij open_project. Pro známý vybraný projekt začni kolo
get_analysis_context; načtený kontext využij i při přechodu mezi dovednostmi v témže kole.
Metodiku znovu načítej dle pravidel get_analysis_context ve společné metodice.
Rutinně neopakuj get_project_snapshot a get_resume_context. Chybějící podklady načítej
cíleně přes get_context nebo list_documents/read_document s head_commit.
READY dovoluje navázání; STALE/MISSING rekonstruuj dle společné metodiky.

## Metodický postup

- FAAM Core je solution-neutral: problém, potřeba, dopad, aktéři, informace, pravidla,
  výjimky, rizika a pozorovatelná acceptance bez předem zvolené technologie.
- Urči requested/effective Analysis Depth BASIC / STANDARD / DEEP podle metodiky.
  Question budget je samostatný limit 1–5, doporučeně 3. Režimy SINGLE / BATCH / BURST
  vybírej podle závislostí otázek; neseskupuj otázky jen pro snížení počtu volání.
- Poté proveď Solution Decision. STOP / NO CHANGE a jiná než Flexideo cesta jsou platné.
  accepted record_decision vyžaduje lidské rozhodnutí.
- Flexideo Delivery Planning aktivuj jen za podmínek společné metodiky.
- Baseline řeš přes start-faam-baseline. Po potvrzení použij start_analysis.
  EPIC-0001 již existuje před prvním příběhem. Po potvrzení baseline použij create_epic pro jeho cíl a acceptance; nejvýše jedna aktivní analýza. Další epic začíná vlastní draft baseline.
- Budoucí změny po Current Truth řeš přes create_vision / add_vision_note / review_vision / queue_vision / defer_vision / reject_vision a promote_vision_to_epic;
  dodrž oddělení hypotéz, evidence a schválení podle společné metodiky.

## Uložení běžného kola

Nejprve vypořádej uložené odpovědi a batch, potom podklady/návrhy a navazující otázky.
Částečnou odpověď nezaměňuj za úplné vyřešení. Nepřipisuj návrh modelu uživateli.
I kolo zakončené jen otázkami ulož před jejich předložením podle metodiky;
číslovaný seznam nenahrazuje BATCH. Nezodpovězené body potřebují OPEN identitu,
nejen zmínku v rozhodnutí, blueprintu či next_step. Respektuj výslovný zákaz zápisu.
Podmínka spuštění pilotu neblokuje automaticky další analýzu.

Použij commit_analysis_turn se steps, summary a závěrečným handoff podle společné metodiky.
Kroky: append_evidence, classify_evidence, resolve_question, resolve_question_batch,
create_open_question, create_question_batch, proposed record_decision, write_artifact bez milestone.
Použij odkazy `$step.field` dle metodiky; nehádej ID.
Server přidá audit, sezení a jediný checkpoint; neduplikuj je dalšími zápisy. Ověř receipt READY a verified_revision == revision;
Receipt platí pro uloženou revizi, ne pro budoucí head.

Identitu mutací, konflikty a opakování nejistých požadavků řeš dle společné metodiky.

## Samostatné řízené kroky

Zachovej stávající nástroje pro accepted rozhodnutí, baseline, stavové přechody, milníky,
Vize a Epicy. Neobcházej jejich brány atomickým kolem. Blokující otázky vyřeš před
resume_analysis; server analýzu sám neobnovuje. Reopen vyžaduje skutečný záměr uživatele.

Uzavření Epicu, přenos do Current Truth a dokončení analýzy proveď pouze
podle bran společné metodiky; review připrav přes review-faam-memory.

Human_approval a časy výroku eviduj přesně dle společné metodiky.
append_analysis_event použij pro událost mimo souhrn kola. Po samostatné mutaci ověř handoff.
Průběhové i závěrečné zprávy piš jazykem uživatele.
