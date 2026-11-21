---
name: gconnect-ads-onboarding
description: Raccoglie le preferenze pubblicitarie di un cliente GConnect dopo la prima connessione, confrontando obiettivi desiderati e indesiderati con la configurazione reale Google Ads senza modifiche.
---

# GConnect — Onboarding commerciale e obiettivi Google Ads

## Quando attivarla
- Alla **prima connessione riuscita** di un utente con Google Ads abilitato, prima di proporre un giudizio sulle campagne.
- Quando il cliente cambia obiettivi, tipologia di attività o preferenze di posizionamento.
- Se le preferenze non sono note o non sono state confermate, chiedile; NON inferirle dal tipo di campagne.
- Non ripetere il questionario ad ogni conversazione se le preferenze sono già state confermate e accessibili. Se non esiste uno storage autorizzato per salvarle, non fingere persistenza: puoi fornire un riepilogo riutilizzabile, chiedere a BitHub di registrarne la configurazione o richiedere conferma in una sessione successiva.

## Connessione e confini
1. Confermare `whoami`, `list_clients`, `list_sources` e selezionare solo il cliente autorizzato. Non rivelare informazioni sugli altri clienti.
2. Se Google Ads è disponibile, avviare una breve conversazione sull'attività e i risultati desiderati.
3. Se non è disponibile Google Ads, chiedere solo tipologia di sito e obiettivi generali pertinenti, senza promettere un audit Ads.

## Le domande iniziali (brevi e non ripetitive)
In un solo scambio, in linguaggio semplice, chiarire:
- **Che attività è?** (a) negozio online/e-commerce, (b) sito aziendale o di servizi, (c) attività locale o negozio fisico, (d) altro: specificare. Consentire più categorie.
- **Quali risultati vuoi che le campagne producano?** Acquisti/ordini online, richieste preventivo/lead, chiamate telefoniche, richieste di indicazioni stradali o visite in negozio, prenotazioni/appuntamenti, iscrizioni, riconoscibilità del marchio, altri obiettivi. Chiedere sia **priorità** sia **obiettivi da escludere dalle offerte**.
- **Dove desideri comparire?** Shopping (prioritario per e-commerce); Search separata; YouTube; siti/app della Rete Display e partner Google; Discover/Gmail/Maps, dove applicabili. Esplicitare per ogni rete: **sì**, **no** oppure **solo se dimostri un ritorno economico sostenibile**.
- **Che cosa consideri una conversione valida?** Per e-commerce: acquisto pagato/confermato, valore ordine attendibile, resi/cancellazioni se disponibili. Distinguere eventi di assistenza (add_to_cart, begin_checkout, view_item) da obiettivi su cui fare bidding.
- **Vincoli economici** (facoltativo): budget, CPA/ROAS desiderato, margine o valore lead, se disponibili. Non calcolare la redditività se non si conoscono costi e margini.

### Spiegazione chiara e non promozionale sui canali
Prima della scelta, spiegare al cliente:
«YouTube, Display e gli altri posizionamenti esterni alla ricerca possono essere utili per far conoscere un marchio, fare remarketing o acquisire clienti, ma possono assorbire budget significativo e produrre risultati meno diretti delle ricerche ad alta intenzione. Per un negozio online che vuole soprattutto ordini redditizi non li attiveremo per impostazione predefinita senza una verifica dei risultati. Non esiste però una regola per cui siano sempre costosi o in perdita: lo stabiliscono i dati di spesa, acquisti attribuiti, incremento reale e redditività».

Spiegare inoltre: «Google Ads può mostrare numeri di conversioni più elevati se sono configurati obiettivi come chiamate, indicazioni, contatti o altri eventi. Non significa automaticamente ordini aggiuntivi. È essenziale controllare quali azioni entrano nelle conversioni primarie, nelle offerte automatiche e nella colonna Tutte le conversioni».
NON attribuire malafede a Google o a un'agenzia senza prove.

## Attività immediata dopo la risposta
Richiamare l'audit Google Ads (vedi `../gconnect-google-ads-audit/SKILL.md`): controllare campagne, reti, obiettivi effettivamente usati per il bidding, asset e risultati. Se i dati API sono insufficienti, segnalarlo e richiedere una verifica dalla UI, senza inventare informazioni.

## Sintesi da consegnare
Restituire un **profilo preferenze pubblicitarie** con tipo di attività, obiettivi desiderati, obiettivi esclusi, canali consentiti/esclusi, obiettivo principale di bidding e vincoli dichiarati. Separare preferenze espresse e dati verificati. Nessuna modifica ad Ads: proposte soltanto.

## Regola prioritaria negozio online
Se il sito è un e-commerce, chiedere esplicitamente se l’obiettivo è **solo Shopping** oppure anche Search, YouTube, Display, PMax e altre reti. Chiedere quale strategia di offerta il cliente desidera o utilizza (ROAS target, massimizza valore di conversione, CPA target, massimizza conversioni, CPC manuale), se ha un target numerico e quale metrica economica considera valida. Non inferire da sola che Shopping standard sia sempre la scelta migliore.
