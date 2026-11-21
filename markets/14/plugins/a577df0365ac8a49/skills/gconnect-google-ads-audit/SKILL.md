---
name: gconnect-google-ads-audit
description: Audit indipendente e in sola lettura della coerenza tra obiettivi del cliente, campagne Google Ads, conversioni, canali, asset e attribuzione.
---

# GConnect — Audit immediato dell'account Google Ads

## Principio
Quando Google Ads è collegato e il cliente ha indicato cosa desidera e cosa **non desidera**, effettuare subito l'analisi disponibile in sola lettura. Non promettere accesso a risorse non esposte dal server MCP. Non modificare campagne, budget, conversioni, asset o targeting.

## Strumenti dedicati
Dopo `list_clients` e `list_sources`, usare `ads_conversion_configuration` con
`section=actions`, `customer_goals`, `campaign_goals`, `custom_goals` e
`campaign_config`. Incrociare i riferimenti delle risorse senza dedurre il bidding
soltanto dall'etichetta primaria/secondaria.
Per l'inventario usare `ads_assets`: `scope=asset` legge testi e riferimenti media;
`customer_asset`, `campaign_asset`, `ad_group_asset`, `asset_group_asset` leggono i
collegamenti. Questi risultati non dimostrano spesa per canale o approvazione.
Se `row_cap_reached` è vero, il risultato può essere incompleto: restringere la
query con `google_read_query` sulla stessa fonte oppure dichiarare il limite.

## Procedura
1. `list_clients` e `list_sources`, selezionare il solo account autorizzato; riportare periodo/date/fuso/valuta e latenza dei dati.
2. Leggere l'inventario delle campagne (abilitate, in pausa, tipo: Search, Shopping standard, PMax, Demand Gen, Display, Video, Local dove disponibili); confrontare impostazioni, budget, strategia d'offerta, obiettivi, spesa, conversioni e valore conversioni. Distinguere campagne attive da storiche.
3. **Audit obiettivi**: recuperare, se disponibili, conversion actions (nome, origine, categoria, primarie/secondarie, valore, `include_in_conversions_metric`, stato, conteggio e fonte), account-default goals, campaign-specific goals e custom goals. Determinare quali conversioni vengono davvero usate da ciascuna campagna per il bidding. Le azioni secondarie incluse in custom goals possono essere usate per l'ottimizzazione: non basta etichettarle «secondarie». Segnalare acquisti duplicati, eventi di micro-conversione come principali, chiamate/indicazioni/visite indesiderate, importazioni GA4 e Ads che misurano lo stesso acquisto. Quando mancano dati dire «non verificabile via API attuale».
4. **Audit canali e posizionamenti**: verificare Search Partners e Display Network nelle campagne Search ove applicabile; per PMax/Demand Gen esaminare il report per canale (Search, Shopping dove applicabile, YouTube, Display, Discover, Gmail, Maps, Search Partners), se la versione API e i permessi lo consentono. Il solo tipo PMax non prova quanto budget vada a YouTube o Display. Rapportare spesa e conversioni per canale con la granularità realmente disponibile; se il reporting non permette una ripartizione affidabile, dichiararlo e richiedere verifica nella UI.
5. **Audit asset**: controllare asset group/asset (titoli, descrizioni, immagini, video, loghi, call, location, sitelink, lead form e asset creati automaticamente) e stato/disapprovazioni dove l'API lo permette; evidenziare asset fuori dagli obiettivi del cliente o destinati a reti non desiderate. Non assumere che un asset generi automaticamente spesa in quel canale.
6. **Audit qualità delle conversioni**: distinguere ordini gestionali, eventi acquisto GA4 e conversioni Ads attribuite; controllare transaction ID e deduplicazione dove possibile, `Conversions` vs `All conversions`, conversion action breakdown, click-date vs conversion-date, finestre di attribuzione e stato del tracking. Non chiamare «ordini» telefonate, percorsi Maps o add_to_cart.
7. **Audit economico**: mostrare costi, ordini attribuiti, valore, CPA/ROAS e limiti; il ROAS positivo non equivale a profitto senza margine, resi, shipping e incrementalità. Per canali brand-awareness valutare metriche appropriate agli obiettivi dichiarati: un canale non è spreco solo perché non genera acquisti last-click.
8. Incrociare le preferenze del cliente con quanto osservato e produrre una tabella: **«Richiesto» / «Riscontrato» / «Evidenza» / «Rischio» / «Azione suggerita»**. Priorità alta a spesa su reti non desiderate, ottimizzazione su conversioni non pertinenti o tracciamento duplicato. Usare etichette «confermato», «sospetto», «dato non disponibile».

## Vincoli e tono
- Nessuna accusa personale o affermazione che Google o un consulente «truffino» il cliente senza evidenze. L'obiettivo è rendere trasparente la configurazione e mostrare eventuali disallineamenti con le sue istruzioni.
- Non affermare che YouTube/Display siano *sempre* uno spreco o che le conversioni siano false: distinguere chiaramente natura delle azioni, attribuzione e risultati.
- Nessun cambio automatico: prima dell'eventuale intervento va chiesta l'approvazione e uno strumento con permessi di scrittura (il MCP attuale è read-only).
- Se il cliente non ha autorizzato Ads, non interrogare altri account o fonti per aggirare il permesso.

## Esito sintetico
1. Tipo attività e obiettivo principale.
2. Campagne e canali attivi oggi.
3. Azioni di conversione realmente usate per il bidding, separate da quelle osservate soltanto.
4. Asset e posizionamenti non coerenti o non verificabili.
5. Elenco ordinato di correzioni proposte con impatto atteso, livello di confidenza e dati mancanti.

## Documentazione di riferimento
- https://support.google.com/google-ads/answer/10995103
- https://support.google.com/google-ads/answer/9143218
- https://developers.google.com/ads/blog/posts/2026/01/introducing-channel-level-reporting-for

## Audit e-commerce obbligatorio (dopo onboarding)
Se il cliente è un negozio online, invocare anche `../gconnect-shopping-sku-economics/SKILL.md`, `../gconnect-merchant-ecommerce-audit/SKILL.md`, `../gconnect-ga4-ecommerce-audit/SKILL.md`, `../gconnect-gsc-ecommerce-audit/SKILL.md` e `../gconnect-ads-account-governance/SKILL.md` quando le rispettive sorgenti sono collegate. Il benchmark prioritario del cliente può essere **Shopping-only**. Non sostituirlo con «Search-only». Identificare esplicitamente le strategie di bidding e distinguere `target_roas` configurato dal ROAS osservato.

## Spesa per tipo di conversione e avvertimenti
Usare `ads_conversion_performance` sul periodo e sulla fonte Ads selezionati.
Mostrare prima la spesa effettiva per campagna, inclusa quella senza conversioni,
poi la tabella delle azioni: categoria/nome, Conversions, All conversions, valore,
spesa delle campagne associate (condivisa, non additiva), rapporto spesa/conversione.
La stessa campagna può produrre chiamate e acquisti: non attribuire a ciascun tipo
un budget esclusivo, non sommare la colonna condivisa, non ricostruire spesa totale
come CPA × conversioni o ripartirla arbitrariamente. Valuta e periodo devono essere
espliciti. `exclusive_spend` nullo significa non disponibile, non spesa zero.
Se `complete=false`, non calcolare totali, CPA complessivi o allocazioni dalle righe
troncate: restringere date/campagna o dichiarare il limite.

Verificare inoltre gli obiettivi configurati con tutte le sezioni di
`ads_conversion_configuration`, anche se una categoria non ha ancora conversioni.
Incrociare azioni, default account, goal campagna, livello di configurazione e custom
goal per distinguere le azioni usate nel bidding da quelle soltanto osservate.
Quando obiettivi commerciali diversi (per esempio acquisti e chiamate/microeventi)
concorrono insieme all'ottimizzazione, segnalare come possibile cattiva configurazione
rispetto alla finalità concordata: il CPA aggregato può nascondere il risultato utile.
Non dichiarare universalmente scorretto avere più azioni per lo stesso obiettivo.
I `warnings` del report segnalano categorie diverse nella colonna Conversions;
non provano da soli la configurazione corrente, specialmente dopo modifiche nel periodo.
Esempio di avviso: «101 conversioni = 100 chiamate + 1 acquisto. Il CPA aggregato
non è il costo per acquisto: verificare gli obiettivi di bidding e leggere i tipi separati».
Il numero di conversioni può essere frazionario e non dimostra ordini unici.
