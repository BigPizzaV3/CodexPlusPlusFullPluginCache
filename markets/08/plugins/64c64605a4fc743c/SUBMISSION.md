# Flexideo Průvodce — veřejná registrace

Stav 2026-10-06: dílčí živé PROD testy doloženy; úplná acceptance není uzavřena.
Kandidát 0.5.1 (OpenAI review remediation), metoda faam-1.0.0, tools contract 0.11. O vydání rozhoduje
produktový SHA a release-manifest.json, ne samotné číslo verze.

Aktuální podklady, konkrétní 5+3 scénáře, evidence, účet a video:
[Review readiness](../../tests/e2e/flexideo-guide/review/README.md).
Reviewer flow outcomes jsou USER_REPORTED_PASS; finální přesný replay je NOT_RUN,
video NOT_RECORDED a registrace původního 0.5.0 již byla odeslána; nový kandidát 0.5.1 dosud NEODESLÁN. Workspace rozcestník je docs/chatgpt-review/.

## Dvě odlišné distribuce

- `*-chatgpt.zip`: aktualizace osobního pluginu. Obsahuje `.app.json` se skutečným
  ChatGPT app ID pro zvolené prostředí; neobsahuje `.mcp.json`.
- `*-chatgpt-submission.zip`: kandidát pro veřejné review, pouze production.
  Obsahuje `.mcp.json` s `https://projects.flexideo.cloud/mcp`, sedm stejných
  skills a metodu. Neobsahuje `.app.json` ani odkaz `apps`. OAuth a scan serveru
  se dokončí v OpenAI dashboardu. Není určen k aktualizaci osobního DEV pluginu.

Production Prepare vytvoří oba balíčky. Development Prepare veřejný balíček
nevytváří. Samostatně lze kandidát sestavit:

```bash
python toolkit/projects/package_faam_plugin.py --environment production --target chatgpt-submission --output /tmp/flexideo-submission
```

Úspěšné balení není potvrzením přijetí OpenAI validátorem ani dokončeného E2E.
Před odesláním ověřit aktuální pravidla a všechny cílové stránky:
https://developers.openai.com/plugins/deploy/submission
https://developers.openai.com/plugins/deploy/app-review

## Podmínky odeslání

1. Uzavřít DEV a PROD acceptance z E2E.md; zapsat skutečné runy, SHA, guidance hash
   a výsledky. Původní hashovaný kit nepřepisovat. Žádný NOT_RUN nepřevádět na PASS.
2. Ověřit vydavatele, oprávnění v OpenAI organizaci a produkční OAuth. GitHub App ID
   není ChatGPT app ID. Nezakládat duplicitní produkční registraci bez kontroly
   existujícího dashboardu; návaznost na osobní testovací registraci ověřit tam.
3. Zkontrolovat veřejný popis a skutečně dostupné funkce. Manifest má website,
   support, privacy a terms URL; zkontrolovat jejich dostupnost i obsah pro MCP.
   Přibalená čtvercová ikona používá existující brand wordmark; zkontrolovat náhled.
4. V dashboardu provést scan produkčního MCP, ověřit tool schemas, annotations,
   OAuth a případné UI resources/CSP. Použít stabilní produkční endpoint.
5. Připravit přesně pět pozitivních a tři negativní reprodukovatelné review scénáře.
   Minimální lokální review sada: pozitivní P01–P05; negativní N01–N03.
   P05 nyní ověřuje review, lidské potvrzení a zahájení analýzy; plný Vize/delta
   průchod není součástí tohoto výběru. ID nepřečíslovávají širší E2E.
   Doplnit konkrétní prompty, skutečné názvy volaných tools a očekávaný výsledek;
   doložit otestované projekty/role. Tento výběr sám není výsledkem testů.
6. Doplnit reviewer-accessible video, release notes a země dostupnosti.
   Testovací přístup a instrukce zadat do zabezpečeného dashboardu; žádné přihlašovací
   údaje, tokeny, OTP ani soukromá projektová data nepatří do ZIP/Gitu.
7. Odeslání ke schválení a následné publikování jsou samostatné ruční kroky.

Claude a cross-host acceptance zůstávají součástí plánu prvního vydání, dokud
vlastník výslovně nezmění rozsah. Tento soubor nic nepublikuje.
