---
name: gerenciar-buscadores
description: Consulte buscadores configurados e importações pendentes do AffiliSend; pause ou retome somente um buscador escolhido pelo usuário após confirmação.
---

# Gerenciar buscadores

- Use `list_offer_searches` para mostrar estado, loja, motivo da pausa e próximo horário. Use `get_offer_search` para confirmar a identidade e o estado de um buscador específico.
- Use `list_pending_offer_imports` para mostrar importações da extensão ou do ChatGPT que ainda aguardam revisão. O link retornado abre o painel; esta consulta não publica ofertas.
- Para pausar ou retomar, mostre o nome, a loja, o estado atual e o ID do buscador escolhido. Peça confirmação explícita para **essa ação nesse buscador** antes de chamar `pause_offer_search` ou `resume_offer_search`.
- Se o estado mudar, leia novamente e explique o conflito. A retomada revalida plano, loja, capacidade e destinos; não contorne uma recusa da API.
- Não crie, edite, exclua ou reinicie buscadores automaticamente.
