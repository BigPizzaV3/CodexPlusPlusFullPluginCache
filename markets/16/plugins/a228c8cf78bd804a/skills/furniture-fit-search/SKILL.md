---
name: furniture-fit-search
description: Use when someone wants ready-made furniture that fits a measured niche or free wall.
---

# Sizely: passende fertige Möbel finden

Sizely sucht fertige Möbel, die in eine Nische oder an eine Wand passen. Sizely ist keine Suche nach Möbeln nach Maß.

## Suche

- Sobald der Nutzer Maße nennt, rufe sofort `search_furniture_by_size` auf, sofern Breite und gegebenenfalls Nischentiefe vorliegen.
- Verwende `type: "niche"` für eine Nische und `type: "wall"` für eine freie Wand.
- Übergib `width` in Zentimetern. Bei einer Nische übergib auch `depth` in Zentimetern.
- `height` ist optional und wird nur übergeben, wenn der Nutzer eine Höhe nennt.
- Übergib `category` nur, wenn der Nutzer eine Möbelart nennt. Leite keine Möbelart aus Kontext oder Beispielen ab.
- Übergib `max_price` nur, wenn der Nutzer ein Budget nennt.
- Wenn Breite fehlt oder bei einer Nische die Tiefe fehlt, frage kurz nur nach den fehlenden Maßen. Frage nicht nach Möbelart oder Budget, um die Suche zu starten.

## Treffer

- Zeige die zurückgegebenen Treffer mit Titel, Maßen, Preis und dem `buy_url`-Link von Sizely.
- Verwende ausschließlich die vom MCP-Server zurückgegebenen Werte und Links. Erfinde keine Händler, Produkte, Maße, Preise oder Links.
- Wenn keine Treffer zurückkommen, sage kurz, dass Sizely keine passenden Treffer gefunden hat.
- Antworte in der Sprache des Nutzers.
