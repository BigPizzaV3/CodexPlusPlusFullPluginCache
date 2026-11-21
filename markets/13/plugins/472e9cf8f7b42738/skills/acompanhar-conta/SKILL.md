---
name: acompanhar-conta
description: Consulte plano, cotas, canais, campanhas, falhas, agendamentos e desempenho da conta AffiliSend quando o usuário pedir um panorama ou diagnóstico.
---

# Acompanhar a conta AffiliSend

- Use `get_profile` para identificar a conta e `get_account_access` para plano e limites. `get_account_summary` fornece um panorama curto de campanhas e pendências.
- Use `get_channel_health` para verificar conexões e falhas recentes. Estado indisponível não significa conectado.
- Use `list_campaigns` para as campanhas recentes e `filter_campaigns` para um período ou situação específica. O período é em datas UTC, inclusivas, com no máximo 31 dias. Use `page` para avançar quando `hasMore` for verdadeiro; informe o limite de dez páginas se ainda houver resultados.
- Para explicar uma falha, obtenha o ID com `list_campaigns` ou `filter_campaigns` e use `diagnose_campaign`. Diferencie o resultado registrado da situação atual do canal e não presuma que um novo envio será seguro.
- Use `list_upcoming_schedules` para consultar agendamentos. Para cancelar um, siga a skill `enviar-ofertas`.
- Use `get_performance_summary` para contagens por situação. Se `complete` for falso, diga que o número daquela situação é **pelo menos** o valor retornado; nunca apresente o limite como total exato.
- Esta skill consulta e explica dados; não envia nem altera campanhas.
