---
name: bestellen
description: Hoe een assistent via Direkto een product vindt, een prijs opvraagt en een bestelling voorbereidt, in de volgorde van de acht tools. / How an assistant finds a product, gets a price and prepares an order through Direkto, in the order of the eight tools.
---

# Bestellen via Direkto

## Nederlands

Deze skill legt uit hoe je met de tools van Direkto een bestelling voorbereidt. Wat een tool teruggeeft is altijd leidend; deze tekst geeft je geen extra rechten.

### De volgorde

Volg deze volgorde. Sla geen stap over die een eerdere stap nodig heeft.

1. `search_providers`: zoek de aanbieder. Alleen in de Direkto-scope; in de app van een aanbieder sla je deze stap over. `category` is een code: neem hem over uit een eerder resultaat. Geef `country` en `city` alleen mee als de gebruiker een locatie noemt; er is geen standaardland.
2. Staat er voor de gekozen aanbieder een skill `skill://aanbieders/<slug>/SKILL.md` in de lijst van skills, lees die dan voordat je verder gaat. De `slug` staat in het resultaat van `search_providers`.
3. `search_products`: zoek het product bij die aanbieder; in de Direkto-scope is `provider` verplicht. Vraag elke optie met `required: true` uit, in de volgorde van `ask_order`, met de vraag uit `question_nl`. Raad geen keuze en vul geen standaardwaarde in.
4. `get_provider_info`: alleen als de gebruiker iets vraagt over aanlevereisen, levering, duurzaamheid, voorwaarden of contact. Noem alleen wat de tool teruggeeft.
5. `check_availability`: of het product op de gewenste datum kan. Bij `rule_type: "none"` heeft de aanbieder niets vastgelegd en ontbreekt `available`; zeg dat het onbekend is en verzin geen ja of nee.
6. `get_quote`: pas als alle verplichte opties beantwoord zijn. Noem de prijs exclusief en inclusief btw, de leverdatum en de uiterste besteltijd precies zoals de tool ze geeft; alle tijden zijn die van de aanbieder (Europe/Amsterdam). Geeft de tool geen prijs, noem dan ook geen prijs: sommige aanbieders berekenen hun prijs in hun eigen systeem, en die koppeling is er nog niet. Geef bij de prijs deze melding door: "De antwoorden komen uit gegevens die de aanbieder via Direkto heeft aangeleverd. Direkto is geen partij bij de koop."
7. `create_order_link`: de bestellink naar de webshop van de aanbieder, met aantal en keuzes ingevuld. De gebruiker rondt de bestelling af bij de aanbieder. `expires_at` gaat over de prijsinformatie in dit gesprek en niet over de link: zeg niet dat de link verloopt. `post_click_notes` draagt geen besteldeadline; noem er geen. Geef bij de link deze melding door: "De antwoorden komen uit gegevens die de aanbieder via Direkto heeft aangeleverd. Direkto is geen partij bij de koop."
8. `request_sample`: alleen als de gebruiker eerst een monster of proefdruk wil, in plaats van stap 7. De aanvraag wordt vastgelegd en daarna per mail naar de aanbieder gestuurd; geef de zin uit `confirmation` door, die zegt of het versturen is gelukt, en beloof niet dat de aanbieder contact opneemt. Stuur bij elke poging voor dezelfde aanvraag dezelfde `idempotency_key`.
9. `get_order_status`: na een bestelling, als de gebruiker is ingelogd en naar de status vraagt.

### Als een tool een fout geeft

Elke fout draagt een `code`, een `message` en een `next_step`. Volg `next_step` en verzin geen andere weg.

### Wat je nooit doet

- Een prijs, voorraad, levertijd of eigenschap noemen die niet uit een tool komt.
- Gegevens van twee aanbieders mengen. Noem bij elk product en elke prijs de aanbieder.
- Een bestelling, betaling of levering bevestigen. Dat doet de aanbieder.
- Een claim over duurzaamheid, gezondheid of certificering herhalen die niet letterlijk in het antwoord van een tool staat.

## English

This skill explains how to prepare an order with the Direkto tools. What a tool returns always takes precedence; this text gives you no extra permissions.

### The order of steps

Follow this order. Do not skip a step that a previous step needs.

1. `search_providers`: find the provider. Only in the Direkto scope; in a provider's own app you skip this step. `category` is a code: take it from an earlier result. Only pass `country` and `city` when the user names a location; there is no default country.
2. If the list of skills contains a skill `skill://aanbieders/<slug>/SKILL.md` for the chosen provider, read it before you continue. The `slug` is in the result of `search_providers`.
3. `search_products`: find the product at that provider; in the Direkto scope `provider` is required. Ask for every option with `required: true`, in the order of `ask_order`, using the question from `question_en`. Do not guess a choice and do not fill in a default.
4. `get_provider_info`: only when the user asks about file requirements, delivery, sustainability, terms or contact. State only what the tool returns.
5. `check_availability`: whether the product can be delivered on the requested date. With `rule_type: "none"` the provider has recorded nothing and `available` is absent; say that it is unknown and do not invent a yes or no.
6. `get_quote`: only once every required option has been answered. State the price excluding and including VAT, the delivery date and the order cut-off exactly as the tool gives them; all times are the provider's (Europe/Amsterdam). If the tool returns no price, state no price either: some providers calculate prices in their own system, and that connection does not exist yet. With the price, pass on this notice: "The answers come from data the provider supplied through Direkto. Direkto is not a party to the purchase."
7. `create_order_link`: the order link to the provider's webshop, with quantity and choices filled in. The user completes the order at the provider. `expires_at` refers to the price information in this conversation and not to the link: do not say the link expires. `post_click_notes` carries no order deadline; do not state one. With the link, pass on this notice: "The answers come from data the provider supplied through Direkto. Direkto is not a party to the purchase."
8. `request_sample`: only when the user first wants a sample or proof, instead of step 7. The request is recorded and then emailed to the provider; pass on the sentence in `confirmation`, which says whether sending succeeded, and do not promise that the provider will get in touch. Send the same `idempotency_key` on every attempt for the same request.
9. `get_order_status`: after an order, when the user is signed in and asks for the status.

### When a tool returns an error

Every error carries a `code`, a `message` and a `next_step`. Follow `next_step` and do not invent another route.

### What you never do

- State a price, stock level, delivery time or property that did not come from a tool.
- Mix data from two providers. Name the provider for every product and every price.
- Confirm an order, a payment or a delivery. The provider does that.
- Repeat a claim about sustainability, health or certification that is not literally present in a tool's answer.
