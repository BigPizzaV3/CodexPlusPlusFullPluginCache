---
name: create-flexideo-project
description: Založí nový Flexideo projektový prostor, když uživatel chce začít projekt nebo analýzu a ještě nemá připravené Project Memory.
---

# Založení Flexideo projektu

Nejprve rozliš, zda už uživatel má projekt nebo self-service draft. Dostupné projekty
ověř přes open_project bez project_id; pro existující projekt použij jeho skutečné project_id.
Nevytvářej náhradní projekt, pokud jde o pokračování nebo obnovu.

Ve veřejném self-service režimu začíná nový projekt na Projects portálu stejného
prostředí jako připojené MCP (produkce https://projects.flexideo.cloud/,
vývoj https://projects-dev.flexideo.cloud/). Uživatel tam dokončí přihlášení,
přijetí podmínek a založení draftu. Server přidělí project_id; nikdy jej nevymýšlej.
Na webu může rovnou dokončit přípravu a otevřít projekt. Potom převezmi stejné ID
nebo jej ověř přes open_project bez project_id a pokračuj open-flexideo-project.

Pokud už draft existuje a uživatel chce dokončit přípravu v chatu, použij
start_project_provisioning se skutečným project_id, source=self_service a
ownership_mode=FLEXIDEO_MANAGED. Vytvoř stabilní idempotency_key a při opakování
stejného pokusu jej zachovej. Přímé založení bez draftu používej pouze v prostředí,
které tuto cestu výslovně podporuje. DRAFT_PROJECT_REQUIRED znamená návrat na
Projects portál, nikoli opakované pokusy s novým klíčem.

První veřejné vydání používá úložiště spravované Flexideem. Nenabízej uživateli
CLIENT_OWNED jako dostupnou alternativu, dokud není pro konkrétní prostředí
výslovně povolena. V povolené CLIENT_OWNED cestě předej bezpečný authorization_url,
po dokončení vybírej jen repository_id z ověřeného seznamu přes
select_project_repository. Nikdy nevyžaduj GitHub token, repository URL ani heslo.
Pokud uživatel výslovně určí název repozitáře, předej repository_name přesně;
jinak ponech výchozí odvození služby.

Stav ověř přes get_provisioning_status; přerušený tok obnov přes
resume_project_provisioning. Při ztrátě přístupu použij reconnect_project_repository
pro stejný repozitář. Po READY načti get_analysis_context stejného project_id a
pokračuj open-flexideo-project a start-faam-baseline. Požadovaný tools contract
je 0.11. FAAM analýza se tímto vstupním postupem nemění.

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
