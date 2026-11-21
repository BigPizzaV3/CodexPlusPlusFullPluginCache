---
name: manage-faam-evidence
description: Ukládá a posuzuje důkazy, předpoklady, inference, rozhodnutí a otevřené otázky ve FAAM Project Memory, včetně zdrojů a lidských potvrzení.
---

# Evidence a rozhodnutí

Využij get_analysis_context načtený pro toto kolo a dočti jen chybějící dokumenty. Respektuj aktuální revision, project_id a
method_version; pravidla konfliktů a idempotence jsou v run-faam-analysis.

append_evidence ukládá title, source, content, volitelné confidence/rationale a evidence_type:
fact, user_assumption, model_inference nebo imported_hypothesis. I fact vzniká jako
unverified. Nevolej následnou klasifikaci jen pro stejné označení inference či doplnění skóre, které lze uložit rovnou. Při klasifikaci použij classify_evidence s evidence_id, evidence_type,
confirmation_status, rationale a volitelným confidence 1–10. Skóre vyjadřuje odhad
jistoty, není kalibrovanou pravděpodobností a samo nic nepotvrzuje.

confirmed vyžaduje evidence_type=fact a explicitní human_approval(statement,
volitelný confirmed_at). Čas výroku předej jen ze známého zdroje s pásmem; neznámý čas vynech, neodhaduj. Serverový recorded_at znamená čas záznamu, nikoli čas výroku. Zaznamenej, co přesně člověk potvrdil a z jakého zdroje. Změnu původní
hypotézy na fakt vysvětli v rationale; původní obsah a historie musí zůstat dohledatelné.
rejected použij pro vyvrácený podklad. Důkaz bez metadata je legacy/unverified.
Pro čtení použij list_documents a read_document; načti obsah i .metadata.json.

Rozhodnutí zapisuj record_decision se status proposed/accepted/rejected/superseded a
rationale. Accepted vyžaduje skutečné doložené lidské rozhodnutí; technické oprávnění
zápisu nenahrazuje business souhlas. Nahrazení accepted rozhodnutí proveď novým accepted
záznamem s supersedes; server ověří předchůdce a označí jej superseded v témže commitu.

Chybějící informace řeš create_open_question(question, why_it_matters, blocking).
Blokaci zvol pouze pokud bez odpovědi nelze pokračovat v analýze. Podmínky budoucího pilotu či nasazení ukládej neblokující, lze-li dál analyzovat. Po zjištění odpovědi
použij resolve_question(answered) s odpovědí a zdrojem. Pro uzavření bez odpovědi použij
closed a doložený důvod změny relevance. Pouhé rozhodnutí otázku automaticky neuzavírá.
Nesnižuj blokaci ani nevytvářej náhradní otázku jen kvůli obejití stavové brány.

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
