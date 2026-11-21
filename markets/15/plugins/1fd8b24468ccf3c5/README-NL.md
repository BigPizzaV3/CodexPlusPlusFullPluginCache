# All-School Simulation – openbaar pluginpakket (concept, versie 0.1.3)

Dit pakket bevat de openbare pluginmanifesten, de Nederlandstalige ontwerpskill, de MCP-koppeling en vijf positieve plus drie negatieve reviewscenario’s.

## Inhoud
- `plugin.json`: plugin-identiteit en openbare presentatiegegevens.
- `mcp.json`: koppeling met de publieke Render MCP-server.
- `skills/simulation-design/SKILL.md`: volledige Nederlandstalige ontwerpskill.
- `assets/icon.png` en `assets/icon.svg`: producticonen.
- `review/test-cases.md`: vijf positieve en drie negatieve scenario’s; nog niet formeel door OpenAI uitgevoerd.
- `RELEASE-NOTES.md`: eerste release.

## Status vóór formele indiening
1. De privacyverklaring en gebruiksvoorwaarden zijn bijgewerkt voor de externe MCP-server en hosting via Render.
2. De MCP-server is publiek gehost; de OpenAI-toolscan moet nog in het indieningsportaal worden uitgevoerd en eventuele bevindingen moeten worden opgelost.
3. De acht reviewscenario’s zijn opgesteld, maar moeten tegen de uiteindelijke portal-scan en live integratie worden uitgevoerd en bevestigd.
4. De uitgeversidentiteit moet in OpenAI Platform zijn geverifieerd en overeenkomen met de gekozen uitgeversnaam.
5. De domeinverificatie kan pas worden afgerond nadat OpenAI in het portaal de exacte challenge-token heeft verstrekt. Stel die token daarna in Render in als `OPENAI_APPS_CHALLENGE`.
6. Selecteer Nederland bij de land-/regio-instellingen in het indieningsportaal.
7. Voor een remote MCP-inzending is een demo-opname-URL vereist. Maak een korte demonstratie van de belangrijkste workflow en tools.

De ZIP is een voorbereid inzendpakket, geen bewijs van succesvolle OpenAI-validatie of goedkeuring. Er zijn geen verificatietokens of geheimen opgenomen. Dien pas ter beoordeling in nadat de resterende portalstappen en tests zijn afgerond.
