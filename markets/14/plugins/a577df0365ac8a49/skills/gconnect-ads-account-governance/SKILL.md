---
name: gconnect-ads-account-governance
description: Verifica come è stato gestito Google Ads negli ultimi 90 giorni, separando modifiche verificabili e attività di monitoraggio non visibili.
---
# Gestione account Ads — controlli 30/90 giorni

- `change_event`: dettagli di modifiche **ultimi 30 giorni**, inclusi prima/dopo e tipo client ove disponibili. `change_status`: risorse modificate **ultimi 90 giorni**, ma solo ultimo stato della risorsa e non ogni intervento. Non affermare che siano 90 giorni completi di cronologia eventi. Storico locale GConnect o export UI consentito per completare i tre mesi.
- Inventariare cambi budget e bidding, ROAS/CPA target, attivazioni/pausa, gruppi prodotti ed esclusioni SKU, feed labels, negativi, asset, conversion goals, obiettivi personalizzati e tracking; annotare data, autore se visibile, risorsa, prima/dopo e cambiamento di performance nelle finestre compatibili.
- Distinguere modifiche manuali, script/API automatizzate e modifiche automatiche; evitare attribuzioni di merito/colpa senza attore verificato.
- Un account può essere seguito senza modifiche (controlli, analisi, decisione di mantenere impostazioni). **Non usare assenza di edit come prova di abbandono**. Per rilevare gestione reale confrontare: report, log operativi, comunicazioni con il gestore e storico di controlli forniti dall'utente.
- Verificare quando sono state **rivalutate** le liste prodotti dannosi: solo se esiste un log del controllo, uno snapshot schedulato o una modifica di esclusione documentata. «Ultima esclusione» non equivale a «ultima analisi». Se non esiste log, «data ultimo monitoraggio prodotti non accertabile».
- Presentare un riepilogo per mese con limiti della fonte, e un giudizio trasparente: evidenze di ottimizzazione / assenza di evidenze / configurazioni incoerenti / elementi da chiedere all'agenzia.

Riferimenti: https://developers.google.com/google-ads/api/docs/change-event ; https://developers.google.com/google-ads/api/docs/change-status

## Strumento stato risorse
Usare `ads_change_status(client_id, source_id, start, end)` con date YYYY-MM-DD
entro gli ultimi 90 giorni di calendario. Riporta soltanto l'ultima modifica per
risorsa, senza autore o dettaglio prima/dopo. Per gli eventi dettagliati usare
`ads_change_history` entro 30 giorni. Dichiarare il limite quando
`row_cap_reached` è vero; nessuno dei due tool prova ogni decisione del gestore.
