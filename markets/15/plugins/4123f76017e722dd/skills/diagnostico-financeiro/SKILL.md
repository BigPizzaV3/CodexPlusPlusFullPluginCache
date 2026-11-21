---
name: diagnostico-financeiro
description: Monta o diagnóstico financeiro de um cliente da Rica Pro a partir da estrutura, do fluxo de caixa, das categorias, do patrimônio, dos investimentos, das projeções e da previdência cadastrada. Use quando o planejador pedir diagnóstico, raio-x, análise de gastos, patrimônio ou proteção de renda de um cliente.
---

# Diagnóstico financeiro de um cliente

## 1. Estrutura

Confirme o cliente com `listar_clientes`. Depois:

- `obter_sessao_cliente`: resumo da estrutura;
- `listar_pessoas_cliente`, `listar_projetos_cliente`, `listar_contas_cliente` e `listar_cartoes_cliente`: quem é quem e onde o dinheiro passa.

## 2. Fluxo e gastos

- `analisar_fluxo_caixa_cliente`: entradas e saídas mês a mês;
- `analisar_categorizacao_cliente`: onde o dinheiro vai, por categoria;
- `analisar_distribuicao_cliente`: saldo líquido por caixa. Entrada, investimento e provisão somam; saída desconta; circular e excluído ficam fora.
- Para abrir uma categoria ou um mês, `listar_lancamentos_cliente` com `dataInicio`, `dataFim` e `formato=compacto`. A resposta traz `totalEncontrado` e `quantidadePorMes`; pagine com `proximoDeslocamento` em vez de carregar tudo.

## 3. Patrimônio

- `analisar_patrimonio_cliente`: patrimônio consolidado;
- `listar_investimentos_cliente`: posições, inclusive as importadas da B3;
- `listar_projecoes_cliente`: projeções já cadastradas.

## 4. Previdência e proteção

`listar_previdencia_social_cliente` diz quais análises previdenciárias estão cadastradas (matriz, CNIS, restituição, pró-labore). Para proteção de renda, use `analisar_patrimonio_cliente` junto com essa lista. Os cálculos completos ficam no Estúdio: indique a análise e onde abrir, sem refazer contas previdenciárias por conta própria.

## Entrega

Organize em: situação atual (dados), pontos de atenção (interpretação, sempre ligada a um dado), perguntas para o cliente e próximos passos para o planejador. Recomendação de produto e decisão previdenciária ficam com o planejador.
