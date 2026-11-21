---
name: get-started
description: How to get a live Cargors pallet freight rate with this plugin. Use when the user first asks about Cargors shipping costs or how the plugin works.
---

# Get started with Cargors

Cargors is a European road-freight platform for pallet transport.

## What this plugin does

- Gets a **live** Cargors all-in freight rate (EUR, excl. VAT)
- Returns how many options exist and the cheapest price
- Never books, never creates an RFQ, never names carriers

## What you need from the user

1. Pickup location (city + country or postcode + country)
2. Delivery location (same format)
3. Number of pallets (default 1)
4. Total weight in kg if known (otherwise the API assumes 250 kg per pallet)

Use city or postcode plus country for the shipment route. Do not ask for names, email addresses, phone numbers, exact street addresses, device location, payment details, or login credentials. Do not send conversation transcripts or unrelated personal information to the tool.

The current tool supports euro, block, and mini pallets, an optional height and pickup date, and standard dry transport without special equipment. Do not claim that it supports a dedicated FTL service, custom pallet length/width, or special transport requirements. Explain the supported inputs if asked.

Then call the MCP tool `get_freight_rate`.

## How to answer

Repeat only the option count and cheapest all-in price, for example:

> Cargors has 2 options for this route. The cheapest all-in rate is €272.98 excl. VAT.

To book, send them to https://portal.cargors.com/#/public/public-quotes

## Do not

- Invent a price if the tool fails
- Name or guess carriers
- Book or create a shipment for the user
