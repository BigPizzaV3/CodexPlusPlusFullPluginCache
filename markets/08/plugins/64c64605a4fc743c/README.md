# Flexideo Průvodce — kandidát 0.5.1

Jeden kanonický zdroj poskytuje sedm řídicích dovedností, společnou metodu
`faam-1.0.0` a aktuální MCP tools contract `flexideo-project-memory-mcp-tools/0.11`.
ChatGPT a Claude Code používají odlišné obaly, ale stejné soubory skills/metodiky.
Jde o připraveného kandidáta, nikoli doklad schválení ve veřejných katalozích.

## Připravit jeden testovací kit

V Product repository na `main` ručně spusťte **Prepare Flexideo Guide release candidate**
(`prepare-project-mcp-development.yml`). Zvolte development/production, plný
`expected_commit` a skutečné `chatgpt_app_id` příslušné registrace.
Workflow nic nenasazuje, neinstaluje ani nepublikuje. Produkční app ID se nesmí
nahradit vývojovým; skript umí ověřit formát, nikoli skutečnou vazbu registrace.

Lokálně z kořene Product repository (ve workspace přidejte `product/` před cestu skriptu):

```bash
python toolkit/projects/prepare_guide_release.py --environment development \
  --source-commit "$PRODUCT_COMMIT" --chatgpt-app-id "$CHATGPT_APP_ID" \
  --output /tmp/flexideo-guide-candidate
```

`PRODUCT_COMMIT` musí označovat checkout, z něhož balíte. `CHATGPT_APP_ID` je
`asdk_app_…` (podporován je i starší `plugin_asdk_app_…`), nikoli OAuth client ID.
Výstupní složka musí být prázdná. `release-manifest.json` obsahuje identity vydání,
endpoint, guidance_revision a SHA-256 souborů. Veškeré E2E začíná jako NOT_RUN.

## ChatGPT

1. Zaregistrujte MCP endpoint pro prostředí a dokončete OAuth:
   development `https://projects-dev.flexideo.cloud/mcp`,
   production `https://projects.flexideo.cloud/mcp`.
2. Převezměte `*-chatgpt.zip` ze stejného kitu. Obsahuje `.codex-plugin/plugin.json`,
   `.app.json` s vaší registrací, sedm skills a `references/method.md`.
   Neobsahuje druhé `.mcp.json` připojení.
3. V podporovaném ChatGPT Work/Codex klientu správce připojí rozbalený balík do
   osobního zdroje pluginu. Při aktualizaci upraví stávající zdroj, nevytváří druhý
   plugin ani další MCP registraci. Ověřte novou verzi a všech sedm skills.
4. V novém chatu proveďte [společný E2E](../../cloudflare/project-mcp/WEB-CHAT-TEST.md).

Osobní instalace není univerzální upload ZIP do libovolného webového chatu.
Veřejné vydání se podává přes OpenAI plugin submission portal jako MCP + skills;
registrace serveru bez skills není kompletní vydání Průvodce. Připravte produkční
registraci a samostatný `*-chatgpt-submission.zip` z production kitu. Ten používá
`.mcp.json` místo `.app.json`. Osobní `*-chatgpt.zip` nelze odeslat k veřejnému review.
Konkrétní podmínky a zbývající kroky: [SUBMISSION.md](SUBMISSION.md).
Upload a zveřejnění jsou pozdější krok po akceptaci, nikoli součást Prepare.

## Claude Code

`*-claude.zip` obsahuje `.claude-plugin/plugin.json`, `.mcp.json`, všech sedm skills
a společnou metodiku. ChatGPT `.app.json` ani `.codex-plugin` do něj nevstupují.
Kit obsahuje také kompletní lokální katalog `claude-marketplace/`, který lze
předat testerovi bez přístupu k soukromému zdrojovému repozitáři.

```text
/plugin marketplace add /absolutni/cesta/claude-marketplace
/plugin install flexideo-faam-development@flexideo-guide-development
/mcp
```

Dokončete OAuth. Ověřte endpoint, namespaced skills a otevřete nové sezení.
Produkční jména jsou `flexideo-faam@flexideo-guide-production`.
Alternativa pro vývojáře: rozbalený samotný plugin lze testovat přes
`claude --plugin-dir /absolutni/cesta/pluginu`; tím se neověřuje instalace z katalogu.
Pokud je CLI dostupné, proveďte `claude plugin validate /absolutni/cesta/pluginu`.

Pro aktualizaci nahraďte distribuční složku novým ověřeným kitem, aktualizujte katalog
přes `/plugin marketplace update flexideo-guide-development`, poté plugin přes
`/plugin update flexideo-faam-development@flexideo-guide-development` a ověřte nové
sezení. Při každé obsahové změně zvýšit verzi; neaktualizovat obsah vydané verze.
Veřejná distribuce použije samostatně publikovaný katalog a balíky s dosažitelnými
zdroji; soukromý orchestrátor není veřejný instalační zdroj. Lokální katalog je
připravený pro test a pro převzetí do veřejné distribuce po produkční acceptance.

## Metodika a hranice

Samotné MCP URL neinstaluje nativní skills. MCP-only fallback `get_faam_guidance`
poskytuje stejný obsah a otisk; vykazuje delivery=mcp-guidance, nikoli nativní instalaci.
`get_resume_context` obnovuje jeden Git head. READY/STALE/MISSING rozlišují aktuální,
zastaralé a chybějící předání. READY není souhlas ani doklad pravdivosti evidence.

Server ověřuje autorizaci, revize, idempotenci a stavové brány. Volný chat musí
skutečně volat MCP a dodržovat metodiku; chování ověřuje E2E. AI nenahrazuje lidskou
odpovědnost za rozhodnutí. Návod po nasazení je veřejně dostupný na `/guide/`
příslušného Projects hostu a nepotřebuje přístup k soukromému GitHubu.

## Oficiální reference ověřené 2026-09-23

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/plugin-marketplaces


## Metodická hranice 0.4.4

Průvodce používá jeden tok:

    FAAM Core → Solution Decision → volitelné Flexideo Delivery Planning

Core je solution-neutral. STOP / NO CHANGE i jiná než Flexideo cesta jsou platným výsledkem. Native Coverage, Architecture Placement a Work Graph se aktivují až po decision gate. Analysis Depth BASIC / STANDARD / DEEP je jiný koncept než question budget pracovního kola.


## Question presentation 0.4.4

Question Engine používá `SINGLE / BATCH / BURST`. Question budget je 1–5 (doporučeně 3). BATCH má 2–5 samostatných otázek, preferovaně 2–3; každá zůstává vlastním `OPEN-*` objektem a společný `QB-*` slouží pouze k prezentaci a resume. Tools contract 0.9 používá handoff 0.2 s `pending_question_ids` a `pending_batch_id`; legacy handoff 0.1 zůstává čitelný jako SINGLE.

## Question persistence 0.4.5

Question-only turns persist OPEN/QB identities and final handoff before presentation. Partial batches retain unanswered members; accepted decisions and drafts do not replace open-question records. Explicit read-only requests remain read-only. V době verze 0.4.5 byl tools contract 0.10; aktuální vydání 0.5.1 používá 0.11. Update both the remote plugin and any personal native installation actually selected by the host.

## Self-service 0.4.6

Založení ve veřejném režimu začíná na Projects portálu. Wizard i Průvodce
pokračují se stejným draft ID; první veřejné vydání používá FLEXIDEO_MANAGED.
Sedm dovedností a společná FAAM metodika zůstávají zachované.
