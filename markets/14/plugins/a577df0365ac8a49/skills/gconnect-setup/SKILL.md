---
name: gconnect-setup
description: Aiuta un cliente BitHub a collegare e verificare GConnect in ChatGPT, senza credenziali in chat e senza configurare manualmente URL MCP.
---

# GConnect — Attivazione per i clienti BitHub

Scopo: ridurre il più possibile i passaggi necessari al nuovo cliente.

1. Controlla se il server GConnect incluso nel plugin è collegato e se i suoi strumenti sono utilizzabili. Non asserire che lo sia soltanto perché il plugin risulta installato.
2. Se manca l'autorizzazione, invita l'utente a premere **Collega / Connect** per GConnect e ad autenticarsi nella pagina sicura con le credenziali fornite da BitHub. Non richiedere né ripetere username, password, token o codici OTP nella conversazione.
3. Se l'OAuth richiede conferma/autorizzazione, lascia che sia l'utente ad approvare nel flusso del proprio account.
4. Quando la connessione è pronta, usa nell'ordine gli strumenti **whoami**, **list_clients**, **list_sources** (o gli equivalenti effettivamente disponibili) per confermare identità autorizzata, clienti visibili e fonti abilitate.
5. Mostra in italiano l'elenco dei siti che quell'utente può vedere e le sorgenti collegate. Non mostrare né cercare clienti fuori autorizzazione.
6. Proponi una sola prova immediata pertinente, come "mostrami le campagne degli ultimi 7 giorni" o "riassumi traffico e ordini"; eseguila soltanto quando l'utente la richiede.
7. Se non ci sono siti visibili, spiega che l'attivazione dei permessi deve essere verificata da BitHub. Se la connessione non è disponibile per il piano o workspace ChatGPT, dillo chiaramente.

GConnect è un servizio commerciale BitHub con attivazione dei clienti e dei permessi gestita esternamente: **non promettere accesso gratuito o automatico a dati non autorizzati**. Non eseguire scritture o modifiche. Non dire "connessione riuscita" senza risposta positiva di uno strumento.

## Onboarding Google Ads obbligatorio, se presente
Dopo `list_sources`, se Google Ads è connesso e non risultano preferenze pubblicitarie già confermate, attiva `gconnect-ads-onboarding` (`../gconnect-ads-onboarding/SKILL.md`). Chiedi tipologia di attività, obiettivi desiderati e indesiderati, canali/posizionamenti graditi o esclusi e cosa conta come conversione utile. Solo dopo le risposte esegui l'audit `gconnect-google-ads-audit` (`../gconnect-google-ads-audit/SKILL.md`). Non affermare di conservare preferenze fra chat senza supporto storage verificato; se esistono, confermale senza ripetere inutilmente le domande.

## Check-up e-commerce alla prima connessione
Per negozi online con fonti abilitate eseguire o proporre subito audit Shopping per SKU, Merchant, GA4, GSC e cronologia Ads, con limiti espliciti. Se l'utente ha autorizzato più sorgenti, incrociarle solo mediante identificatori di prodotto e periodi verificati. Evitare questionari lunghi: iniziare da tipo sito, obiettivi desiderati/indesiderati e strategia bidding, poi analizzare.
