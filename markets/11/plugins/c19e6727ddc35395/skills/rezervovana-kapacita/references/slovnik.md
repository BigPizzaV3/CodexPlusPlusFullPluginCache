# Slovník pojmů pro vyhodnocení energií

| Pojem | Význam pro vyhodnocení |
|---|---|
| OM (odběrné místo) | Místo připojení s EAN (elektřina) nebo EIC (plyn). Všechny nástroje pracují s identifikátorem OM (GUID), ne s EAN. |
| EAN / EIC | Identifikační kód odběrného místa elektřiny (EAN, 18 číslic) a plynu (EIC). Zobrazuje se jen při úrovni detailu, kterou povolil správce organizace. |
| Komodita | `electricity` (elektřina), `gas` (plyn) nebo `heat` (teplo). Hodnoty různých komodit se nikdy nesčítají. |
| Teplo (CZT) | Dodávka tepla z teplárny (centrální zásobování teplem). V portálu jen po měsících, z odečtů a faktur; `get_consumption(commodity=heat)` vrací jen celé měsíce. |
| GJ | Gigajoule, jednotka tepla z faktur teplárny: 1 GJ = 277,77778 kWh. Spotřebu tepla v GJ vrátí `get_consumption(unit=GJ)`. |
| Stálý plat | Měsíční platba teplárně za sjednaný příkon, nezávislá na spotřebě; `get_costs(commodity=heat)` ji uvádí jako samostatnou složku nákladů bez DPH. |
| Napěťová hladina | NN (nízké napětí, domácnosti a menší firmy), VN (vysoké napětí), VVN (velmi vysoké napětí). Určuje strukturu distribučních plateb. |
| Rezervovaná kapacita (RK) | U odběru z VN a VVN smluvní maximum 15minutového příkonu v kW. Překročení se penalizuje podle cenového rozhodnutí ERÚ. Roční a měsíční RK se mohou kombinovat. |
| Hlavní jistič | U odběru z NN určuje velikost platby za příkon v distribuci (např. 3×25 A). Jeho orientační výkon je v kVA. |
| Denní rezervovaná kapacita (plyn) | Rezervovaná denní kapacita v m³/den u větších odběrů plynu; porovnává se s maximálním denním odběrem. |
| Čtvrthodinové maximum | Nejvyšší průměrný příkon za 15 minut (kWh za čtvrthodinu × 4 = kW). Z faktury distributora nebo z 15minutových dat. |
| Průběhové měření | Měření s 15minutovým průběhem (typ A, B, případně C s chytrým elektroměrem). |
| TDD | Typový diagram dodávky: odhad průběhu spotřeby tam, kde se průběh neměří. U plynu se značí `tdd_estimate`. |
| Původ spotřeby elektřiny | Ze zdrojů, které portál opravdu sečetl: `distributor_measured`, `supplier_measured`, `measured` (průběhové měření), `meter_readings` (odečty), `invoice` (faktura), `monthly_import` (měsíční tabulka). U odečtů a faktur je množství skutečné, jen průběh v čase je rozpočítaný (`basis: estimated`). `unknown` znamená, že původ nelze určit; nikdy ho nevydávej za měření. |
| Úplnost dat | Podíl dnů s daty v hodnoceném období (0–1). Pod 95 % nelze čísla bez výhrady potvrdit. |
| Podíl odhadů | Podíl spotřeby bez naměřeného průběhu (odečty, faktury, odhad TDD; 0–1). Nad 10 % je nutné na to upozornit. |
| Základní odběr | Spotřeba mimo provoz (noc, víkend, neprovozní dny). Vysoký základní odběr je typický ukazatel plýtvání. |
| Neprovozní den | Den, kdy podle provozního kalendáře organizace neběží provoz (svátek, odstávka, celozávodní dovolená). |
| Anomálie | Den s neobvykle vysokou spotřebou nebo špičkou oproti očekávání. Závažnost `low`, `medium`, `high`; stav nevyřízená nebo vzatá na vědomí. |
| EnPI | Ukazatel energetické náročnosti podle ISO 50001 (např. kWh na jednotku výroby nebo na m² a denostupeň). |
| Metodika výpočtu | Jeden platformní dokument, který popisuje, jak portál počítá EnPI, výkon vůči počasí, základní odběr a úspory. Výsledek nese blok `methodology`: větu pro klienta, číslo verze metodiky platné v době výpočtu (u uloženého výsledku ta, se kterou byl spočten, ne dnešní) a odkaz do portálu na stránku Metodika výpočtu v té verzi. Když blok chybí, organizace metodiku v portálu zapnutou nemá; větu nepřepisuj vlastními slovy a metodiku nedomýšlej. |
| Denostupně (HDD) | Míra potřeby vytápění podle venkovní teploty. Slouží k normalizaci spotřeby na počasí. |
| Očekávaná spotřeba při normálním počasí | Spotřeba, kterou regresní model OM vypočte pro dlouhodobě průměrné počasí (dříve „normalizovaná spotřeba“). Uváděj ji vedle naměřené spotřeby, nikdy ji s naměřenou nesčítej a nevydávej za hodnotu EnB ani za úsporu. Použitelná jen při dostatečné kvalitě modelu (R²). |
| Účiník (cos φ) | Poměr činného a zdánlivého výkonu. Nedodržení hranice stanovené distributorem znamená přirážku za jalovou energii. |
| Silová elektřina / komoditní část | Cena za samotnou energii od dodavatele (fix nebo spot + marže). Neobsahuje distribuci, poplatky ani daně. |
| Distribuce | Regulovaná platba distributorovi za přenos energie a za příkon (RK nebo jistič). Ceny stanovuje ERÚ. |
| Regulované složky | Distribuce, systémové služby, podpora OZE (POZE), poplatek OTE, u plynu i další regulované platby. Ceník vydává ERÚ na každý rok. |
| POZE | Podpora obnovitelných zdrojů energie, regulovaná položka faktury za elektřinu. |
| Daň z elektřiny / plynu | Spotřební daň z energie; u plynu samostatná položka. |
| ERÚ | Energetický regulační úřad; vydává cenová rozhodnutí pro regulované složky ceny. |
| OTE | Operátor trhu s elektřinou a plynem; zveřejňuje spotové ceny (denní trh). |
| Spot | Nákup za spotové ceny OTE (15minutové nebo hodinové ceny elektřiny, cena plynárenského dne) plus marže dodavatele. |
| Fix | Pevná cena komoditní části na smluvní období. |
| Forward | Termínový produkt na budoucí dodávku (měsíc, kvartál, rok) s cenou zúčtování. |
| Plynárenský den | Obchodní den plynu od 6:00 do 6:00 následujícího dne. |
| Záporná cena | Spotová cena pod nulou; odběr v takovém intervalu je pro spotového odběratele výhodný. |
| Výpovědní lhůta | Poslední den, kdy lze smlouvu vypovědět, aby skončila k datu konce. Po jejím uplynutí se smlouva s automatickým prodloužením prodlouží. |
| Automatické prodloužení | Smluvní doložka, která smlouvu bez včasné výpovědi prodlouží o další období, často za horších podmínek. |
| Bez DPH / s DPH | Přehledy nákladů v portálu jsou bez DPH. Faktura bývá s DPH. Vždy uveď základ. |
| Potvrzený rozpis faktury | Faktura, jejíž položky byly v portálu zkontrolovány a potvrzeny. Náklady v portálu vycházejí jen z potvrzených rozpisů. |
| Faktura čekající na zpracování | Faktura nahraná do portálu, která ještě nebyla potvrzena (čeká na ruční kontrolu nebo potvrzení). Do nákladů se nepočítá. |
| Konflikt odečtů | Dva zdroje dat hlásí pro stejné období různé hodnoty; do vyřešení je číslo nejisté. |
| figure_id | Identifikátor čísla z nástroje ES Zone (`fig_…`). Nástroj `verify_figures` s ním přepočítá přesně stejný dotaz. |
| portalUrl | Odkaz do portálu ES Zone, kde uživatel uvidí totéž číslo se stejnými filtry. |
