---
name: open-flexideo-project
description: Otevře existující Flexideo projekt a obnoví práci z autoritativního Project Memory snapshotu.
---

# Otevření Flexideo projektu

Pokud uživatel uvedl project_id, otevři právě tento projekt. Jinak použij open_project
bez ID a nech jej vybrat, pokud je výsledků více.

Načti get_analysis_context; současně získáš metodiku i úplný kontext obnovy z jednoho headu. Pouze další
potřebné části dočti přes get_context nebo read_document se stejným headem. Nečti celý
repozitář a neodvozuj stav z historie chatu. Sděl aktuální revizi, stav baseline, stav
analýzy a doporučený krok.

Před pokračováním rozliš resume_status READY / STALE / MISSING podle společné
metodiky. Načtený vision_index je zásobník budoucích záměrů, nikoli další verze
Current Truth; recent_work_log je pouze chronologie pro orientaci při navázání. U READY obnov goal, task, done_when, presentation_mode, pending_question_ids, pending_batch_id a rozpočet kola;
stav projektu a skutečné blokace mají přednost před textem next_step. U STALE/MISSING
nejprve rekonstruuj rozpracovanou práci z uložených podkladů, bez domnělého souhlasu.
Samotné otevření projektu nic nezapisuje. Ohlášení revize není dokončená obnova.

Před každou mutací použij revision z kontextu jako expected_revision. Po mutaci pracuj
s novou vrácenou revision. Při konfliktu znovu načti get_analysis_context; nepřepisuj souběžnou změnu.

Ověř tools_contract flexideo-project-memory-mcp-tools/0.11. Při neúplném snapshotu
stránkuj list_documents s vráceným head_commit a načti relevantní read_document;
nevyvozuj nepřítomnost objektů z částečného seznamu. Pro řízení pokračování použij
run-faam-analysis, pro klasifikaci manage-faam-evidence a pro validace/výstupy
review-faam-memory. ANALYSIS_COMPLETED neznamená výzvu k automatickému znovuotevření.

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
