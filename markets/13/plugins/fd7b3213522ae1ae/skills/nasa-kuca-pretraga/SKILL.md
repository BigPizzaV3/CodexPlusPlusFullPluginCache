---
name: nasa-kuca-pretraga
description: Koristi kada korisnik traži proizvode, proizvođače, događaje, restorane, smještaj ili druge ponude na platformi Naša kuća.
---

# Pretraga Naše kuće

Koristi MCP server `nasa-kuca` za informacije o ponudama na platformi Naša kuća.

- Za opšta pitanja o ponudi prvo koristi `search_catalog`.
- Za detalje poznatog proizvoda, proizvođača, događaja ili profila koristi odgovarajući alat za detalje.
- Navodi samo podatke dobijene iz alata i priloži link konkretne ponude uz tvrdnju.
- Ne izmišljaj cijene, termine, zalihe, kapacitet, kontakte ili dostupnost.
- Ne prikazuj polje slike ako nije ispravan apsolutni HTTPS link; uvijek priloži link stranice ponude.
- Ponude iz kataloga Naše kuće ne predstavljaju sve ponuđače na tržištu.
- Kod smještaja i događaja ne tvrdi da je nešto rezervisano ili slobodno, osim ako alat to izričito potvrdi.
- `request_inquiry` šalje stvarni upit oglašivaču. Prije poziva pribavi ime, email i izričit pristanak korisnika za slanje tih podataka. Poziv nije rezervacija; odgovor daje oglašivač.
- Upit se šalje samo organizaciji čiju je ponudu korisnik odabrao. Objasni da su ime i email obavezni, a telefon, datum, vrijeme, broj osoba i poruka opcionalni; podaci iz upita čuvaju se 30 dana.
- Dodatak ne obavlja kupovinu, ne prima uplatu i ne potvrđuje narudžbu, rezervaciju ili prijavu.
- Za narudžbu proizvoda uputi korisnika na stvarni link proizvoda koji je alat vratio. Narudžba se završava na sajtu Naše Kuće uz plaćanje pouzećem. Ne šalji narudžbu kroz `request_inquiry` i ne tvrdi da je potvrđena.
