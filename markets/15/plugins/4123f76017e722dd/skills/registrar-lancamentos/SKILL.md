---
name: registrar-lancamentos
description: Cria, corrige e remove lançamentos de um cliente da Rica Pro, incluindo parcelados e recorrentes, sempre mostrando os dados antes de gravar. Use quando o planejador pedir para lançar, corrigir valor ou categoria, parcelar, criar recorrência ou apagar um lançamento de um cliente.
---

# Registrar lançamentos

Precisa da permissão de alteração (`clientes:write`).

## Criar

1. Confirme o cliente com `listar_clientes`.
2. Encontre a conta com `listar_contas_cliente` (ou `listar_cartoes_cliente`). A conta define a pessoa e o projeto.
3. Confira a categoria com `listar_categorias_cliente`. Ela precisa existir na estrutura do cliente.
4. Mostre ao planejador: cliente, conta, pessoa, projeto, nome, valor, tipo, data e categoria. Espere o ok.
5. `criar_lancamento_cliente` com `dados.contaId`, `nome`, `valor` (número) e `tipo`. Use `dataCompra` para a data.

Séries:

- parcelado: de 2 a 48 parcelas;
- recorrente: informe `dataFimRecorrencia`; sem ela, a Rica gera até um ano a partir do primeiro vencimento, no máximo 1.000 lançamentos;
- escolha parcelamento **ou** recorrência, nunca os dois;
- séries vão sem juros ou multa; ajuste encargos depois, no lançamento individual;
- a configuração da série só existe na criação.

## Corrigir

1. Encontre o lançamento com `listar_lancamentos_cliente`, filtrando por período (`dataInicio`, `dataFim`).
2. Mostre o lançamento atual e a mudança.
3. `atualizar_lancamento_cliente` só com os campos que mudam e com a `versaoEsperada` que veio na leitura.

Se a resposta for "O lançamento mudou durante a operação…", leia de novo e refaça. Se for "O lançamento está em categorização e tipagem…", espere alguns minutos.

## Remover

Mostre qual lançamento sai e peça confirmação. Só então chame `remover_lancamento_cliente` com `confirmar: true`. Numa série, sai só a ocorrência indicada.

## Conferir

Os lançamentos aparecem em Estúdio → Lançamentos, com origem "Rica MCP" no histórico. Se o cliente tem agentes de Novo lançamento, eles reagem ao lançamento criado.
