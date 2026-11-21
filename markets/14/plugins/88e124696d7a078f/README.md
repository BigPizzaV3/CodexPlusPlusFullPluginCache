# Integrarea LowCostSolar

Serverul remote MCP oferă catalog, comparații, calculator și ghiduri pentru echipamente fotovoltaice în România. Endpoint: https://lowcostsolar.ro/mcp. Documentație publică: https://lowcostsolar.ro/asistent-fotovoltaic.

Pachetul este pregătit pentru evaluare, nu reprezintă o listare aprobată. Nu afirmăm afiliere OpenAI sau distribuire proactivă. Identitatea publicatorului, verificarea domeniului, categoria și materialele vizuale cerute trebuie validate în portal înainte de publicare.

## Comportamentul așteptat

Căutarea și calculul nu cer contact. Datele lipsă pentru estimare se solicită. Prețurile folosesc sursa comercială reală și cursul verificat. Costul estimat privește panouri, invertor și baterie, separat de instalația completă. Stocul necunoscut nu este promis.

Toate cele cinci instrumente sunt doar pentru citire și calcul: search_solar_products, get_solar_product, compare_solar_products, estimate_solar_system și get_solar_guidance. Nu cer nume, telefon, email, adresă exactă sau istoricul conversației. Nu pregătesc și nu trimit cereri de contact, nu notifică firma și nu plasează comenzi. Agentul nu trebuie să ofere aceste acțiuni. Numai dacă utilizatorul întreabă explicit cum contactează firma sau cumpără, poate primi un link public pe care să îl deschidă personal. Formularele site-ului rămân separate de MCP.

Serverul nu folosește persistența de leaduri sau serviciul de email. Conexiunea nu necesită cont LowCostSolar. Parametrii tehnici sunt prelucrați pentru răspuns; hostingul poate prelucra date tehnice de acces, conform politicii de confidențialitate.

## Verificare

Testele automate sunt în tests/mcp.test.mjs și verifică protocolul, calculele și respingerea vechilor instrumente de contact. Nu trimite cereri reale de test în producție. Un test de calculator folosește valori explicit ipotetice și nu reprezintă profilul utilizatorului. Setul de întrebări pentru evaluare este în docs/growth/evaluation-prompts.json.

Selecția instrumentelor instalate, găsirea în director și sugestiile proactive sunt trei lucruri diferite. Se măsoară distinct și nu se garantează niciun volum de trafic.

## Măsurarea funcționării

Versiunea 1.2.0 păstrează cele cinci instrumente numai pentru citire. Serverul salvează totaluri zilnice pe funcție, rezultat, versiune, categorie de trafic și interval de durată, fără argumente, rezultate complete, conversații, IP-uri sau identificatori personali. Testele automate proprii folosesc o semnătură verificabilă și sunt raportate separat. Nu se identifică persoane, instalări sau recomandări proactive.

Linkurile către produse, calculator și ghiduri au marcaje publice de campanie: sursa lowcostsolar_mcp, mediul referral și campania solar_assistant. Nu includ parametrii calculului sau identificatori de utilizator. Deschiderea lor este opțională, iar site-ul aplică preferințele existente de consimțământ. Detalii: https://lowcostsolar.ro/confidentialitate.

## Pachet pentru review 1.3.0

Publicator: MIHAI BACILA, ales explicit și verificat ca persoană fizică; METROLINK SRL rămâne comerciant/operator. Pachet engleză cu traducere română, categoria Other, cinci scenarii pozitive și trei negative. Acestea sunt rezultate așteptate, nu dovada executării tuturor testelor. Draftul 1.3.0 este încărcat în portal, cu domeniu verificat și metadate/scanare MCP fără constatări. Aprobarea/publicarea nu au avut loc. Video real trebuie adăugat înainte de submit, fără URL fictiv.

Toate instrumentele 1.3.0: readOnlyHint=true, destructiveHint=false, idempotentHint=true, openWorldHint=false. MCP citește catalogul, ghidurile și cursul din baza proprie; nu accesează BNR sau linkurile citate. Cron autentificat separat, zilnic, pentru curs. Lipsa/expirarea produce eroare fără fetch de rezervă. Calculatorul returnează ID și model exact; modelul nu trebuie să substituie imagini/specificații ale variantelor similare.

Atribuirea 1.3.0 gestionează rescrierea observată a sursei ChatGPT doar când campania/medium/content MCP valide sunt păstrate. Testele manuale și scanările reprezintă evaluări neclasificate, nu adopție demonstrată. Stadiul exact și dovezile sunt în docs/growth/state.json.

## Estimare simplă 1.4.0

monthly_bill_ron + supplier sunt suficiente pentru prima recomandare; se acceptă și monthly_kwh + supplier sau tarife explicite. Nu solicita kWh/acoperiș/zonă/racord înaintea rezultatului când există factura și furnizorul. Folosește contextul returnat: ofertă de referință datată, consum derivat după scăderea abonamentului fix, referință Cluj dacă zona lipsește, suprafață necesară și scenarii mono/trifazat dacă racordul nu este cunoscut. Datele reale pot rafina rezultatul ulterior. Ofertele expirate sunt marcate; furnizorii necunoscuți nu sunt înlocuiți arbitrar cu un tarif inventat. Contractele nu sunt verificate de instrument. Același motor și aceleași tarife ca pe site, fără acces public suplimentar sau colectare de contact.
