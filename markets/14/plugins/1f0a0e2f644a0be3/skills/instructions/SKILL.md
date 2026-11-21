---
name: instructions
description: How to answer questions about a Finikos short-term rental workspace (bookings, guests, prices, competitors, cleanings, revenue, invoices) with the read-only Finikos tools. Use when the user asks about their own rentals managed in Finikos.
---

# Finikos: how to use the tools

Finikos is a property-management platform for Italian short-term rentals. The connected user is
signed in to one Finikos organization (tenant) and every tool reads only that organization's data.
Users usually write in Italian: answer in the user's language.

## Ground rules

- **Read-only.** Every tool is a read. If the user asks to change something (prices, bookings,
  cleanings, settings, messages to guests), say that the plugin can only read data and that the
  change is made in the Finikos app. Do not pretend a change was made.
- **One organization only.** The tools cannot see other companies, competitors' bookings or other
  Finikos customers. Competitor *prices* come from the `concorrenti` tools, which describe public
  listings, not other organizations' data.
- **Never invent data.** If a tool returns nothing, say so. Do not fill gaps with estimates.
- **Use totals as returned.** Revenue and invoice totals are already computed by the backend: report
  them as they are, without recalculating or summing them again.
- **Find the property first.** Most tools need a property id. When the user names an apartment,
  call `lista_proprieta` (or `proprieta_gestionale`) and match the name, then call the specific tool.
  If more than one property matches, ask which one.
- **Dates.** Resolve "today", "this week", "next 14 days" from the current date and pass explicit
  dates in the format the tool asks for.
- **Large answers.** If a tool says the response is too large, narrow the date range or the property
  and call it again. Never present a partial result as complete.
- **Channel copies.** Some Airbnb and Booking.com settings are served from a saved copy; when a tool
  returns `_copiaZodomusDel`, tell the user the date of that copy.
- **Guest data.** Guest identity details (documents, dates of birth, addresses) are personal data.
  Show them only when the user explicitly asks for them, and only the fields needed.

## Which tool for which question

| Question | Tools |
|---|---|
| What happens today: arrivals, departures, cleanings | `riepilogo_oggi`; for another day `riepilogo` |
| Arrivals or departures of a day | `arrivi_oggi`, `partenze_oggi`, `arrivi`, `partenze` |
| Bookings of a property or a period | `cerca_prenotazioni`, `prenotazioni_periodo` |
| One booking in full (guest, amounts, cleanings) | `dettaglio_esteso_prenotazione`, `importi_prenotazione` |
| Who is staying on a given night | `prenotazione_della_notte` |
| Nightly prices per channel, availability, sold price | `calendario_prezzi`; several properties: `calendario_prezzi_multiplo` |
| Competitors and market | `concorrenti`, `report_concorrenti_settimanale`, `disponibilita_mercato` |
| What moves demand | `eventi_citta`, `meteo_citta`, `minimo_notti_citta` |
| Pricing rules | `preferenze_prezzi`, `configurazione_last_minute`, `regole_durata_soggiorno` |
| Revenue | `incassi_totali`, `incassi_proprieta`, `incassi_proprieta_mensili`, `guadagni_mensili_proprieta` |
| Cleanings | `pulizie_gestionale`, `pulizie_da_fare`, `pulizie_oggi`, `agenda_colf` |
| Police registration (Alloggiati) | `alloggiati`, `ricevute_alloggiati` |
| Online check-in status of a booking | `riepilogo_ospiti_prenotazione` |
| Invoices | `fatture`, `fatture_elettroniche`, `richieste_fattura_in_attesa` |
| Direct booking site | `sito_diretto`, `annunci_sito_diretto`, `tariffe_sito_diretto`, `ordini_sito_diretto` |

## Presenting results

- Prices and nights: a compact table, one row per night, with the channels as columns.
- Money: euro with two decimals, as returned.
- Lists of people or apartments: name first, then the detail the user asked for.
- Keep the answer focused on the question; offer a follow-up instead of dumping every field.
