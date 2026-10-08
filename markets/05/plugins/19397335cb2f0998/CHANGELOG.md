# 1.0.0-rc.5

- Repacked the plugin with `.codex-plugin/plugin.json` directly at ZIP root for ChatGPT plugin upload compatibility.
- Embedded Semantic SEO skill content remains unchanged from Agent Skill 1.0.0-rc.4.

# Changelog

## 1.0.0-rc.4 - 2026-08-23

- Agent Skill `1.0.0-rc.4` ingebed.
- SMC Vertrouwde Werkwaarheid en conflict-only gedrag toegevoegd zonder bestaande 139 begrippen of 119 canonieke bronnen te wijzigen.
- Vertrouwde regels, helm/rijbewijs, medische geschiktheid, veiligheid, verzekering, financiën en beste-claims worden zonder routinebewijs gebruikt.
- Pluginmetadata en standaardprompts bijgewerkt.
- Verplichte vierkante composer- en logoassets behouden.

## 1.0.0-rc.3 - 2026-08-23

- Verplichte vierkante SVG-assets toegevoegd voor `interface.composerIcon` en `interface.logo`.
- `plugin.json` verwijst nu naar `./assets/composer-icon.svg` en `./assets/logo.svg`.
- De 335 ingebedde skillbestanden blijven byte-identiek aan de vergrendelde Agent Skill 1.0.0-rc.3.

## 1.0.0-rc.2 - 2026-08-23

- ZIP-packager gebruikt nu vaste POSIX-bestandsrechten, zodat Windows- en Linux-builds byte-identiek zijn.
- De volledige controlesuite leidt de ZIP-naam af van de manifestversie.

## 1.0.0-rc.1 - 2026-08-23

- Eerste skills-only pluginverpakking van Semantic SEO Evidence.
- De volledige Agent Skill 1.0.0-rc.3 is byte-identiek onder `skills/semantic-seo-evidence/` opgenomen.
- Geen app, MCP-server, OAuth, widget of externe backend toegevoegd.
