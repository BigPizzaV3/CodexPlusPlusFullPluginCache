---
name: revisar-carteira
description: Revisa a carteira inteira do planejador na Rica Pro, com clientes sem movimento, metas estouradas, pipeline, atendimentos, lembretes e indicadores do Office, e transforma a revisão em tarefas da semana. Use quando o planejador pedir visão geral, prioridades da semana ou situação dos clientes.
---

# Revisar a carteira

## Passos

1. `listar_clientes` para a lista completa. Avise quantos clientes vieram.
2. Escolha só as consultas que a pergunta pede. Para cada cliente, use o `clienteUsuarioId` dele:
   - metas do ciclo com uso alto: `listar_metas_cliente` e `analisar_distribuicao_cliente`;
   - clientes sem movimento: `listar_lancamentos_cliente` com `dataInicio` dos últimos 30 dias e `limite` pequeno, olhando `totalEncontrado`;
   - lembretes próximos: `listar_lembretes_cliente`;
   - conexões paradas: `listar_openfinance_cliente`.
3. Para a consultoria como um todo:
   - `listar_pipeline_consultoria`, `listar_contatos_consultoria` e `listar_atendimentos_consultoria`: quem está no funil e quem espera resposta;
   - `listar_lembretes_consultoria` e `listar_agentes_consultoria`: acompanhamentos combinados;
   - Office: `obter_indicadores_atividade_office` e `listar_afiliados_office` (afiliados e filiadas).
4. Entregue uma ficha curta por cliente, ordenada pelo que pede ação primeiro.

Carteiras grandes: diga quantos clientes faltam e pergunte antes de seguir, em vez de consultar todos de uma vez.

## Transformar em tarefas

Converta a revisão numa lista para a semana, por cliente: o que fazer, por que, e a tela da Rica Pro onde fazer (Nexo para abrir o cliente, Estúdio, Acompanhamento).

## Limites

- A Rica Pro não envia convites nem mensagens: proponha o texto e o planejador envia.
- Criar ou pausar agentes e lembretes é feito na Rica Pro.
- Assinaturas vêm sem dados de pagamento.
