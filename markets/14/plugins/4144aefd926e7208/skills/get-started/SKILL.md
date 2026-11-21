---
name: get-started
description: Connect a cubobase store and show the owner what they can ask for.
---

# Getting started with cubobase

cubobase is an online store for small businesses. When the owner connects it, they sign in to their store and tap
"Authorize"; there are no keys to copy.

Once connected:

1. Call `ver_tienda` to learn the store's name, currency and whether it is open, and greet the owner by the store's
   name.
2. Offer three things they can ask for right away: how sales are going (`ventas`), who still owes them money
   (`quien_debe`) and changing a price or stock (`buscar_productos`, then `cambiar_producto`).
3. Answer in the owner's language. Amounts are in the store's currency.
4. Before cancelling an order (`cambiar_pedido` with estado `cancelado`) or deleting a
   product (`borrar_producto`), ask the owner to confirm.
5. Design changes (`cambiar_diseno`) go to a draft: show the owner how it looks (`ver_como_queda`) and publish
   (`publicar_diseno` with confirmar=true) only after they say yes.

If the owner has no store yet, they can open one at https://cubobase.com/en/.
