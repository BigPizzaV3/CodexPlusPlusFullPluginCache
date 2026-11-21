# Siesta AI 1.0.1

Tento balíček zachovává identitu pluginu `siesta-ai` a produkční MCP připojení
z funkčního RC balíčku. Nahraj celý `siesta-ai-codex-plugin-1.0.1.zip` jako
novou verzi do odpovídajícího existujícího draftu. Verze 1.0.1 přidává vysvětlení
nástrojů pro review; nemění backend, OAuth ani chování skillu.

## Soubory v ZIPu

- `.codex-plugin/plugin.json`: identita, verze, katalogové údaje a review scénáře.
- `.mcp.json`: produkční MCP server a deklarace OAuth.
- `chatgpt-app-submission.json`: samostatný import do pole **Use Codex to fill
  this form more quickly** v MCP formuláři. Obsahuje odůvodnění anotací včetně
  14 označených nástrojů. Přítomnost v ZIPu nenahrazuje import ani nenastavuje OAuth.
- `skills/siesta-ai/SKILL.md`: instrukce pro práci se Siesta AI.
- `assets/icon.png` a `LICENSE`: ikona a licence.

**Finder skrývá názvy začínající tečkou.** Po rozbalení stiskni **Cmd + Shift + .**.
Pro upload použij původní ZIP; zabalením pouze viditelných souborů by se ztratily
manifest a MCP konfigurace.

Balíček používá Codex compatibility formát. Manifest odkazuje na `.mcp.json`
pomocí `"mcpServers": "./.mcp.json"`; soubor nepřejmenovávej na `mcp.json`.

## OAuth a review

- MCP server a resource: `https://api.siesta.ai/mcp`.
- Server key: `siesta`.
- Deklarace OAuth: `extensions.com.openai.auth.type: "oauth"` v `.mcp.json`.
- Siesta scope: `mcp`; `offline_access` umožňuje refresh při nastavení připojení.

Client ID, secret, tokeny ani hesla nejsou součástí balíčku. Konkrétní připojení
a OAuth discovery spravuje klient a portál.

Podrobná anglická vysvětlení a žádost o ruční posouzení jsou v doprovodném
`siesta-ai-openai-submission-kit-1.0.1.zip`, souboru
`docs/submission/reviewer-notes.md`. Žádost lze zkopírovat do dostupného pole
pro review/appeal nebo použít při kontaktování podpory. Není automaticky
importovaná a nemění serverové anotace ani výsledek scanu.

Dne 13. 10. 2026 uživatel hlásil připojený účet a stav „No scan has finished
since this connection.“ Připravený ZIP nepotvrzuje dokončený scan, úspěšné
review ani publikaci. Schvalování akcí s neověřitelně úplnými argumenty
nadále patří do Siesta AI podle přiloženého skillu.
