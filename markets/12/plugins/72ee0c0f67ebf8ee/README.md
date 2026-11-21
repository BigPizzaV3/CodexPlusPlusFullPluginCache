# NEMOweby 1.0.3

Vzdálený plugin s přihlášením OAuth přes https://www.nemoweby.cz/api/mcp.
Nevyžaduje lokální server, klíč AI ani zapnutý Mac. Balíček neobsahuje přihlašovací údaje.

## První připojení
1. Plugin musí být registrovaný a dostupný ve vašem účtu ChatGPT. Samotný ZIP ani lokální marketplace nezaručují mobilní dostupnost.
2. Nainstalujte NEMOweby a zvolte připojení účtu.
3. Přihlaste se na webu NEMOweby. Vyberte oprávnění a potvrďte propojení.
4. V novém chatu napište „Ukaž moje nemovitosti“.
5. Na telefonu ve stejném účtu otevřete Live, pokud jej váš plán a verze aplikace podporují. Ověřte, že je NEMOweby mezi dostupnými pluginy.
6. Řekněte „Shrň moje nové poptávky“ nebo „Připrav změnu ceny ukázkového bytu na 5 290 000 Kč“.
7. Změnu potvrďte na https://www.nemoweby.cz/ucet/agenti. Agent může následně ověřit výsledek. Hlasový souhlas sám změnu neprovede.

## Soukromí a omezení
Každý používá vlastní účet a vlastní oprávnění. Připojení lze kdykoliv odpojit. Ve výchozím stavu změny vyžadují schválení. Majitel může pro každé připojení povolit vybrané samostatné akce, nastavit souhrnný limit změny ceny a limit AI požadavků za 24 hodin a kdykoliv je vypnout. Mazání a změny přístupů vždy čekají na potvrzení. Výslovná žádost o návrh nikdy změnu neprovede. Funkce účtu se pluginem neodemykají.
Plugin zpřístupňuje existující MCP funkce; nepřidává propojení Meta ani video.

## Stav vydání
Balíček je připraven pro nahrání do portálu OpenAI. Registrace, autorizovaný test v ChatGPT a test na skutečném telefonu jsou samostatné kroky; nejsou tvrzené jako dokončené.
Veřejné vydání vyžaduje ověření vydavatele, ověření domény, kontrolu serveru, izolovaný recenzentský účet, demo video a schválení OpenAI.

Oficiální postup: https://developers.openai.com/plugins/deploy/submission
Live: https://help.openai.com/en/articles/20001274-chatgpt-voice
