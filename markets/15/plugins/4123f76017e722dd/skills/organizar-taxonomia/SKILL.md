---
name: organizar-taxonomia
description: Organiza categorias, conceitos e caixas de um cliente da Rica Pro e o catálogo da consultoria (categorias, caixas e templates), respeitando limites e o que muda ao remover. Use quando o planejador pedir para criar, juntar, renomear ou remover categorias, caixas, conceitos ou templates, ou padronizar a taxonomia entre clientes.
---

# Categorias, conceitos, caixas e templates

A taxonomia vive em dois lugares. Pergunte em qual mexer quando o pedido não disser:

| Onde | Consultar | Alterar |
| --- | --- | --- |
| Cliente | `listar_categorias_cliente`, `listar_conceitos_categoria_cliente`, `listar_caixas_cliente`, `obter_uso_taxonomia_cliente` | `criar_/atualizar_/remover_` + `categoria_cliente`, `conceito_categoria_cliente`, `caixa_cliente` |
| Catálogo da consultoria | `listar_catalogo_categorias_planejador`, `listar_conceitos_categoria_catalogo_planejador`, `listar_catalogo_caixas_planejador`, `listar_catalogo_templates_planejador` | `criar_/atualizar_/remover_` + `categoria_catalogo_planejador`, `conceito_categoria_catalogo_planejador`, `caixa_catalogo_planejador`, `template_catalogo_planejador` |

## Limites

Cliente: 130 categorias e 30 caixas. Os dois lugares: 100 conceitos por categoria, nome do conceito com até 80 caracteres e definição com até 300. Estruturas antigas acima do limite podem reduzir, nunca aumentar.

## Mudar a taxonomia de um cliente

1. `obter_uso_taxonomia_cliente` para ver quanto falta para o limite.
2. Liste o que existe e proponha a mudança.
3. Confirme uma mudança por vez e leia de novo o item alterado.

Use só identificadores devolvidos pela Rica nas relações entre categoria e caixa. Uma categoria pode estar em mais de uma caixa. No cliente, criar com um nome que já existe atualiza o item existente.

## Catálogo

Crie na ordem categoria e conceitos → caixa → template, pedindo confirmação em cada etapa. Mudanças no catálogo valem para clientes novos; os atuais ficam como estão.

## Antes de remover

Remoções exigem `confirmar: true` e não são bloqueadas por uso. Antes, mostre o impacto:

| Remover | Efeito |
| --- | --- |
| Categoria do cliente | lançamentos ficam sem categoria, caixas perdem a categoria, condições de agentes deixam de citá-la |
| Caixa do cliente | metas perdem a caixa |
| Categoria do catálogo | caixas do catálogo perdem a categoria |
| Caixa do catálogo | templates perdem a caixa |
| Template | sai do catálogo; estruturas já criadas continuam iguais |

Para medir o uso de uma categoria, consulte `listar_lancamentos_cliente` por período e `listar_caixas_cliente`.

## Erros

`limite_taxonomia_excedido`, `limite_caracteres_conceito_excedido`, `nome_duplicado` e `referencia_fora_escopo` não gravam parte da mudança. Explique a causa, consulte de novo e só então repita.
