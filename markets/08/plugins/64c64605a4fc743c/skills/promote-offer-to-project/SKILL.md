---
name: promote-offer-to-project
description: Přenese schválený význam konkrétního immutable offer releasu do Project Memory po explicitním rozhodnutí pokračovat v analýze nebo po podpisu smlouvy.
---

# Promoce nabídky do projektu

Vyžaduj konkrétní offer_id, release_id, cílový project_id a explicitní lidské
potvrzení události analysis_requested nebo contract_signed. Pro podepsanou smlouvu
vyžaduj také ne-tajnou smluvní referenci.

Nejprve použij validate_offer_promotion. Potom použij get_analysis_context cílového projektu a
shrň, co se přenese: schválený významový baseline, scope, výjimky, předpoklady a
provenance. Nepřenášej HTML, access seznam, interní review ani ostatní klientské složky.

promote_offer_to_project zavolej až po potvrzení člověkem. Zachovej stejný
idempotency_key při retry. Výsledné hypotézy nepřeváděj na fakta; následně spusť jejich
FAAM kontrolu.

Konkrétní immutable balíček načti get_offer_for_promotion a ověř jeho zdroj před
validate_offer_promotion. Po importu pokračuj start-faam-baseline; import ani
accepted rozhodnutí o převzetí nabídky není potvrzením všech jejích hypotéz.

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
