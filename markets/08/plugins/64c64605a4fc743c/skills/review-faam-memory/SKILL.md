---
name: review-faam-memory
description: Ověřuje úplnost FAAM Project Memory, odkazy, připravenost k uzavření a tvoří review, blueprinty a milníkové výstupy z doložených podkladů.
---

# Review a výstupy FAAM

Využij get_analysis_context tohoto kola a podle potřeby stránkovaný list_documents
a read_document. Chybějící část ohraničeného výpisu není důkazem nepřítomnosti.

validate_memory má tři odlišné úrovně:
- structure: přítomnost povinných souborů;
- contract: také tvar stavu a rozpoznaných metadat;
- references: také existence a význam kontrolovaných vazeb.
Před potvrzením etapy použij references a řeš errors/missing; warnings o staré evidenci
znamenají neověřené podklady. Překročení limitu není úspěch. Validátor neprokazuje
věcnou pravdivost ani plnění business acceptance; to musí posoudit review a člověk.

write_artifact podporuje blueprint, architecture, review, report, prototype a other.
Blueprint a architekturu opři o potvrzenou baseline a doložená rozhodnutí. Výslovně
odděl varianty a otevřené hypotézy. Požadavek na změnu mimo scope vrať do analýzy.

Pro baseline nebo dokončení analýzy ulož review s kontrolou cíle, evidence, otázek,
rozhodnutí a acceptance. Potom bez dalšího mezilehlého zápisu proveď odpovídající
transition_analysis_state nebo close_epic. Stará review server odmítne;
po konfliktu znovu posuď změněný obsah a ulož aktualizované review.

Milestone Report: write_artifact(artifact_type=report, milestone=...) odkazuje na
existující checkpoint_id, related_decisions a případně epic_id. U Vision-backed delta
Epicu po promote_epic_to_current nejprve vytvoř nový checkpoint a z něj confirmed
milestone_type=epic-close; až potom lze Epic uzavřít. Tím historická podoba zůstane
připnutá a nový obsah je jediná Current Truth. Zvol milestone_type
baseline/analysis/solution-mvp/delivery-readiness/contracted-baseline/epic-close,
status draft/confirmed/superseded a audience internal/client. Klientské confirmed
výstupy mají confirmed_at a confirmed_by pouze na základě skutečného potvrzení.
Existence reportu sama nemění stav analýzy. Výstup pro klienta přizpůsob jeho cíli;
technické údaje MCP do něj patří jen tehdy, když jsou pro něj relevantní.

Na konci ulož append_session_log a commit_checkpoint dle run-faam-analysis a uveď
provedené kontroly, neověřené věci a další krok. Neoznačuj hotový návrh za nasazený systém.

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
