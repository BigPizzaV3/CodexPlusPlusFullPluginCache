---
name: gconnect-ga4-ecommerce-audit
description: Analizza funnel, qualità degli ordini, canali, dispositivi, landing, abbandoni, anomalie e affidabilità del tracking GA4 per e-commerce.
---
# GA4 — Audit e-commerce orientato alle vendite

1. Selezionare proprietà autorizzata e periodo esplicito (7/30/90 giorni e confronto con periodo precedente ove fattibile). Specificare proprietà, fuso, valuta, latenza e eventuali limiti/thresholding.
2. Funnel acquisto: `view_item` → `add_to_cart` → `begin_checkout` → `add_shipping_info` → `add_payment_info` → `purchase`, **solo per eventi realmente implementati**. Spiegare differenze di denominatore, utenti vs eventi e funnel aperto/chiuso; gli step mancanti non equivalgono ad abbandoni.
3. Analizzare acquisizione per `sessionDefaultChannelGroup`, source/medium, campaign, landing page, device, paese; distinguere attribuzione GA4 da quella Google Ads e non forzare join per sessione/click non disponibile.
4. Validare revenue, currency, `transactionId`, duplicati, ordini cancellati/rimborsati, valore di spedizione/tasse e disallineamenti; deduplicazione solo con verifiche e riconciliazione gestionale se connesso. Ricordare differenze tra conteggio eventi e ordini distinti.
5. Rilevare funnel per dispositivo, checkout mobile, errore di pagamento solo se esistono eventi verificati, prodotti con molte visite ma poche aggiunte al carrello, carrelli abbandonati, repeat purchase e nuovi vs ricorrenti solo se la definizione è attendibile.
6. Identificare pagine di ingresso ad alto traffico ma bassa conversione, traffico referral/payment gateway auto-riferito e landing ads fuori assortimento.
7. Se tecnicamente disponibile: confrontare acquisti GA4 con conversioni Ads per data clic e data conversione, non dare per scontata parità dei totali; controllo di duplicati Google Tag/GTM, eventi purchase emessi più volte, utm/gclid, Consent Mode, cross-domain.
8. Evidenziare dati mancanti/inattendibili prima di trarre conclusioni economiche; non dichiarare causa UX senza replay/RUM o evidenza tecnica.

Output: qualità tracking (alta/media/bassa), 5 maggiori frizioni quantificate, opportunità per pagina/prodotto, test consigliati, con metodi e limiti. Nessuna modifica a tag o configurazioni.
Riferimenti: https://developers.google.com/analytics/devguides/reporting/data/v1 ; https://support.google.com/analytics/answer/9267735
