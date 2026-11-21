---
name: gconnect-merchant-ecommerce-audit
description: Analisi Merchant Center per e-commerce, feed, offerte, idoneità Shopping, benchmark prezzo e opportunità a catalogo.
---
# Merchant Center — Audit commerciale e tecnico

## Procedura obbligatoria
1. Identificare il cliente con `whoami`/`list_clients` e la sorgente Merchant con `list_sources`. Recuperare problemi account, prodotti elaborati, stato delle offerte e origini dei dati tramite `merchant_account_issues`, `merchant_products`, `merchant_data_sources` e `google_read_query` **solo con risorse supportate**. Paginare sino al completamento o dichiarare campione e limiti.
2. Controllare qualità del feed: ID stabili, duplicati/varianti, brand, GTIN/MPN, titolo, descrizione, immagini, disponibilità, prezzi, sale_price, shipping, resi, categorie, condizioni, link landing, refresh/errori, scadenze e allineamento fra landing/checkout/feed; distinguere errori che bloccano Shopping da avvisi.
3. Controllare prodotti disapprovati, limitati, non eleggibili, in attesa, fuori target paese, mancanti dal feed e non inclusi nelle campagne. Confrontare set Merchant vs SKU del gestionale **solo quando quest'ultimo è connesso e autorizzato**. Non assumere che «presente nel Merchant» significhi «attivo in Shopping».
4. Opportunità di mercato: se disponibili e idonei, interrogare `price_competitiveness_product_view`, bestseller di prodotti/marchi, `price_insights_product_view` e report su visibilità competitiva. Distinguere benchmark esterno dalla concorrenza reale del medesimo EAN/variante, paese, prezzo effettivo e spedizione. Non inventare domanda, vendite dei concorrenti o prezzo ottimale senza metriche.
5. Identificare SKU con domanda potenzialmente elevata (bestseller per categoria/brand o query GSC pertinenti) ma non idonei Shopping; etichettare **opportunità da verificare**, non «volume garantito».
6. Proporre correzioni prezzo solo con analisi di margine e unit economics: confrontare *riduzione prezzo* vs *aumento spesa Ads* con simulazioni, non con promesse di rendimento. Considerare resi, IVA, commissioni, spedizione, sconti e disponibilità.
7. Separare performance delle schede gratuite da Ads a pagamento. Non sommare clic/ordini dei due canali senza controllo di attribuzione.

## Output
Tabella prioritaria: SKU / problema / fonte / spesa Ads (se mappata) / differenza prezzo verificata / domanda proxy / intervento / urgenza / livello di confidenza. Aggiungere totali delle offerte idonee/non idonee e la copertura del dataset. No modifiche al feed senza consenso e strumenti di scrittura.

Riferimenti: https://developers.google.com/merchant/api/guides/reports/understand-the-market ; https://developers.google.com/merchant/api/guides/reports/overview
