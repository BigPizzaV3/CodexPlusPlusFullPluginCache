---
name: preparar-atendimento
description: Prepara a pauta de uma reunião com um cliente da Rica Pro, busca dados durante a conversa e monta o resumo depois. Use quando o planejador pedir pauta, preparação de reunião, resumo de atendimento ou mensagem de acompanhamento para um cliente.
---

# Preparar e conduzir um atendimento

## Antes da reunião

1. Encontre o cliente com `listar_clientes` e confirme o nome com o planejador.
2. Descubra o ciclo: pergunte ou use o mês corrente. Diga o período usado na pauta.
3. Busque, sem alterar nada:
   - `analisar_fluxo_caixa_cliente`: entradas e saídas do período;
   - `analisar_distribuicao_cliente` e `listar_metas_cliente`: caixas comparadas com as metas do ciclo;
   - `listar_objetivos_cliente`: objetivos financeiros e comportamentais em andamento;
   - `analisar_patrimonio_cliente`: patrimônio por instituição;
   - `listar_openfinance_cliente` e `listar_b3_cliente`: conexões desatualizadas, que a família precisa renovar antes da reunião.
4. Monte a pauta em três blocos: **fatos** (com os números da Rica), **interpretações** e **perguntas para a família**. Cite valores como "Essenciais: R$ 8.940,00 de R$ 9.800,00".

Em `analisar_distribuicao_cliente`, `valorMovimentado` é volume bruto: não use como consumo nem como progresso de meta.

## Durante a reunião

- Responda pedidos curtos com uma consulta só. Para lançamentos, use `listar_lancamentos_cliente` com `dataInicio` e `dataFim` e `formato=compacto` quando o período for longo.
- Se a família decidir um ajuste, anote. Para gravar na hora, siga a skill `registrar-lancamentos` ou `objetivos-e-metas`, mostrando os dados antes.

## Depois da reunião

Com as decisões que o planejador passar, monte:

1. decisões da família;
2. ajustes que o planejador vai fazer na Rica Pro, com a tela de cada um (Estúdio → Lançamentos, Estúdio → Objetivos, Estrutura);
3. mensagem de acompanhamento pronta para copiar;
4. pauta do próximo encontro.

A Rica Pro não envia mensagens. Entregue o texto para o planejador mandar pelo canal dele.

## Antes de entregar

Para cada número, saiba dizer qual consulta trouxe o dado. Se um número não veio de nenhuma consulta, diga que não encontrou em vez de estimar.
