# REALITY / EvO / QChronon / EMO — agent bootstrap v3 deep map

Tato vrstva je veřejně bezpečná, offline a bez závislosti na LLM/API.

## Rozsah
- uzly: 362
- hrany: 2136
- V_semantic: (362, 4096) float32
- V_control: (362, 24) float32
- V_emo: (362, 10) float32
- V_frequency: (362, 48) float32
- A_direct/A_weight: (362, 362)
- zdroje textových chunků: 13

## Hlavní pravidlo agenta
1. Nejprve rozliš realitu, záznam, model, interpretaci, fikci, důkaz a rozhodnutí.
2. Potom určuj lokální realitu, historii, omezení, možnost pokračování a nulový stav.
3. Pokud dotaz míří do chráněného jádra, neodpovídej technicky. Vrať veřejnou hranici.
4. Pokud chybí dost reality, vrať nulový stav / požadavek na kontext.

## Chráněné
EMQCP, těžební filtr, kryptoměnové optimalizace, nonce/difficulty/hash postupy, orbitální testy, backendová validace, implementační rovnice, parametry a cokoliv reprodukovatelného nejsou součástí této mapy.

## Jednověté jádro
EvO není kalkulačka výsledků. EvO je evoluční operátor přípustnosti, který v lokální gravitační realitě rozlišuje, který stav smí projít z možnosti do děje.
