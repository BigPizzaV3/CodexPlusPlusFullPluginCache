# Labelsol — candidatura pubblica 1.1.13

Aggiornamento richiesto dal titolare per correggere gli URL legali mancanti
nella versione 1.1.12. Il pacchetto consolida logo e informazioni
commerciali/legali; non costituisce una candidatura completa o approvata.
Manca ancora il collegamento a un video accessibile ai revisori.
Il copione completo è nel progetto in `docs/labelsol-video-revisione.md`.

Nuova candidatura pubblica autorizzata dal titolare dopo il rifiuto OpenAI
di modificare i server MCP della precedente candidatura.
Nuovo nome interno: `labelsol`.
Nome visibile: Labelsol. Autore dichiarato: Solespress; l'identità verificata
nel portale deve essere coerente e non è modificata dallo ZIP.

## Contenuto

- `.codex-plugin/plugin.json`: nuova identità pubblica, versione incrementata,
  metadati e casi di review nei campi documentati da OpenAI.
- `.mcp.json`: un solo server, `https://labelsol.org/mcp/public-shipping`.
- `skills/labelsol/SKILL.md` e `ISTRUZIONI-CHATGPT.md`: istruzioni operative
  identiche alla fonte del pacchetto esistente.
- `assets/logo.png`: nuova immagine fornita dal titolare, centrata su tela
  quadrata trasparente 89 × 89 senza tagli, deformazioni o ridisegno.
  È usata sia per il logo sia per l'icona del compositore.

Nessun riferimento a un'app registrata, hook, credenziale, account demo,
ordine o documento cliente. Nessun sorgente o strumento amministrativo
TMS/Carrier Gateway.

## Caricamento nella candidatura pubblica `labelsol`

1. Aprire https://platform.openai.com/plugins con l'account autorizzato del titolare.
2. La nuova candidatura `labelsol` è già riconosciuta dal portale: scegliere
   **Upload new version / Upload plugin to make changes** su QUELLA candidatura.
   NON creare un terzo plugin e NON aggiornare la vecchia candidatura `dev-…`.
   Solo se `labelsol` non fosse ancora stata creata, il primo caricamento
   deve essere With MCP, mai Skills only.
3. Caricare questo ZIP completo senza estrarlo. In Metadata & Skills verificare
   versione 1.1.13, nome interno `labelsol`, logo, skill e metadati importati.
4. In **MCPs → Connect**, usare l'URL sopra e **Authentication: None**.
   Nessuna OAuth o chiave amministrativa è necessaria per il server pubblico.
   Le autorizzazioni ai singoli ordini restano gestite dal server.
5. Il titolare ha riportato dominio verificato e connessione configurata.
   Mantenere quella connessione: questo aggiornamento non cambia il server MCP
   né richiede di sostituire la challenge.
6. Attendere la scansione e controllare strumenti e Issues; usare Reconnect
   o Rescan se indicato. Non dichiarare operazioni di scrittura come letture.
7. Controllare Review details: cinque casi positivi e tre negativi sono
   scenari attesi, non attestazioni di collaudo. La registrazione ricevuta
   mostra un blocco della conferma, non un pagamento riuscito, e non è
   inclusa nello ZIP né collegata come dimostrazione completa.
8. Non premere **Submit for review** finché i requisiti mancanti non sono
   completati e il titolare non ha dato l'autorizzazione distinta.

L'identità precedente non è modificata o cancellata da questo ZIP. Le sue
installazioni non migrano automaticamente: gli utenti dovranno collegare il
nuovo plugin quando sarà disponibile. Prima di cancellare la vecchia
candidatura, verificare connessione e disponibilità della nuova. La cancellazione
non è necessaria per generare questo ZIP e non è stata eseguita dall'agente.

## Requisiti ancora aperti

- Privacy specifica Labelsol e termini commerciali sono implementati a
  `/privacy` e `/termini`, con NIR SRL e condizioni fornite dal titolare.
  Entrambi gli URL sono stati verificati sul dominio pubblico con HTTP 200.
  I testi legali devono essere verificati dal titolare e da un professionista
  competente; la generazione del pacchetto non certifica conformità legale.
- Video accessibile della funzionalità reale, con dati controllati e senza segreti.
- Controllare che il portale conservi dominio verificato e connessione configurata.
  Il titolare ha riportato una scansione MCP senza findings.
- Esecuzione documentata dei casi di review che preparano/confermano MOS,
  avviano pagamenti o recuperano documenti. Nessuna operazione reale viene
  autorizzata dalla semplice presenza dei casi nello ZIP.
- Valutazione OpenAI dell'ammissibilità commerciale del servizio MOS-first
  e del percorso di checkout esterno. `commerce: true` non equivale ad approvazione.

Il contatto pubblico dichiarato è https://solespress.it/contatti/.
La privacy pubblica del vecchio sito Solespress non è stata riciclata come
privacy Labelsol: il testo consultato riguarda WordPress, Stripe e PayPal,
non descrive adeguatamente il percorso Labelsol/SumUp/TMS.

Questo ZIP non pubblica il backend, non aggiorna le installazioni ChatGPT
automaticamente e non sblocca eventuali dinieghi di sicurezza.
L'effettiva importazione e approvazione OpenAI non è verificata localmente.

## Rigenerazione

`python3 scripts/package-labelsol-plugin.py --submission`

La build di candidatura usa lo stesso sorgente delle istruzioni ma un nuovo
nome interno esplicitamente autorizzato. Non sostituisce il download operativo
del sito con la candidatura pubblica. La 1.1.9 respinta non va ricaricata per tentativi. I successivi
aggiornamenti della NUOVA candidatura devono mantenere `name: labelsol`
e la stessa dichiarazione MCP del suo primo caricamento.

La 1.1.11 aggiorna la skill al nome descrittivo
`submit_paid_shipping_order_for_review`. La chiave MCP `labelsol` e il suo URL
restano identici alla 1.1.10, quindi non si sostituisce il server MCP.
Le correzioni agli schemi e alle annotazioni sono sul server: diventano
visibili a OpenAI soltanto dopo il Publish del codice dell'app e Rescan.
I metadati legali e video non sono inventati per eliminare gli avvisi.

La 1.1.12 sostituisce soltanto l'immagine del logo e aggiorna queste note.
Il server MCP e le istruzioni operative restano invariati.

La 1.1.13 consolida NIR SRL, pagamento anticipato del servizio di spedizione
e URL delle pagine legali implementate. Conserva il logo della 1.1.12.
Non viene dichiarata pronta per l'invio finché manca il video reale.

Fonti:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors
- https://developers.openai.com/plugins/plugin-guidelines
