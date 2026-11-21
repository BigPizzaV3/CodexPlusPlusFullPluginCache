---
name: start-faam-baseline
description: Vytvoří nebo zkontroluje FAAM baseline, když projekt potřebuje potvrdit výchozí příběh, kontext, evidenci a otevřené otázky.
---

# FAAM baseline

Použij get_analysis_context, nebo již načtený kontext tohoto kola; nejprve
obnov nebo rekonstruuj uložený úkol dle společné metodiky. Další kontext dočti
přes get_context nebo read_document. Rozděl informace na:

- potvrzená fakta a jejich zdroje;
- uživatelské předpoklady;
- modelové inference;
- otevřené otázky.

Import nabídky je imported_hypothesis, dokud jej člověk samostatně nepotvrdí. Nabídka ani orientační řešení nejsou automaticky Analysis Model ani Solution Decision. Baseline zachycuje problém a kontext; sama neaktivuje Flexideo Delivery Planning.

Evidenci ukládej přes append_evidence, otázky přes create_open_question, souvislý
výchozí příběh přes update_context do baseline_story a rozhodnutí pouze přes
record_decision. Každá mutace musí mít stabilní idempotency key, aktuální revision,
skutečný důvod a metodickou verzi z kontextu.

Baseline neoznačuj za potvrzenou bez explicitního lidského potvrzení. Podklady a předání běžného kola ulož přes commit_analysis_turn dle společné metodiky;
update_context a schvalovací přechody zůstávají samostatné. Question budget je 1–5, doporučeně 3. Pro nezávislé otázky stejného kontextu můžeš použít BATCH 2–5; jinak SINGLE nebo BURST. Po dosažení budgetu vyhodnoť dostatečnost kola;
Souhrn kola zaznamená výsledek a důvod dalšího kola; append_session_log je potřebný jen
mimo atomický turn.

## Serverem řízené potvrzení

Ověř tools_contract flexideo-project-memory-mcp-tools/0.11. Evidence má explicitní typ;
append_evidence ji vytváří unverified. Pro potvrzení použij classify_evidence až po
skutečném souhlasu dle manage-faam-evidence. Zodpovězené otázky uzavři resolve_question.

Baseline je připravena k review, když je doložen problém, dopad, cílový výsledek,
rozsah a jeho hranice, hlavní aktéři, známá omezení a pozorovatelná kritéria úspěchu.
Neznámé nepřepisuj na fakta: pojmenuj je a rozliš, zda blokují smysluplnou baseline,
nebo mohou zůstat explicitní neblokující otázkou pro detailní analýzu. Nesnaž se
vyčerpat všechny implementační otázky před potvrzením příběhu.

Po doplnění baseline proveď validate_memory(level=references) a skutečné review,
ulož write_artifact(artifact_type=review) a bez mezilehlého zápisu zavolej
transition_analysis_state(action=review_baseline, review_document=<vrácená cesta>).
Teprve po explicitním lidském potvrzení použij confirm_baseline s human_approval
(statement, confirmed_at). Pak lze start_analysis. Textové „potvrzeno“ bez úspěšného
stavového nástroje není potvrzená baseline. Pokud se kontext změní, server baseline
vrátí do draft; proveď nové review a potvrzení. Podrobné pokračování: run-faam-analysis.

## Načtení metodiky podle hostitele

Společná metodika: `../../references/method.md`. Načti ji s nativní dovedností,
nebo použij obsah dodaný přes get_analysis_context; MCP obsah není důkaz nativní instalace.
Pro známý projekt načti na začátku kola get_analysis_context. Již načtený kontext téhož
kola využij i při přechodu do této dovednosti. known_guidance_revision a known_skill
předej jen pro skutečně načtený obsah; po ztrátě kontextu je vynech.
Další potřebnou dovednost dočti přes get_faam_guidance. Rutinně neopakuj snapshot/resume.
Běžné podporované kroky ulož přes commit_analysis_turn dle společné metodiky;
server přidá souhrn sezení a checkpoint. Samostatné schvalovací a stavové operace zachovej.
Průběhové i závěrečné zprávy piš jazykem uživatele.
