---
name: objetivos-e-metas
description: Monta e mantém objetivos, realizações e metas de um cliente da Rica Pro, financeiros ou de hábito, e acompanha o andamento. Use quando o planejador falar em objetivo, sonho, reserva, meta mensal, hábito da família ou acompanhamento de metas de um cliente.
---

# Objetivos, realizações e metas

A Rica segue a cadeia **objetivo → realização (resultado e processo) → meta**.

## Consultar

- `listar_objetivos_cliente`: cada objetivo traz `financeiro: true` (valores, caixas, ciclos) ou `false` (comportamental: hábito, saúde, estudo; nota de 0 a 5 e marcações);
- `listar_realizacoes_cliente`: resultados e processos;
- `listar_metas_cliente`: metas e o andamento do ciclo atual;
- `listar_ciclos_cliente`: ciclos gravados das metas financeiras.

## Criar

1. Confirme o cliente e as pessoas (`listar_pessoas_cliente`). Para meta financeira, confirme as caixas (`listar_caixas_cliente`).
2. Proponha a cadeia inteira e mostre cada etapa antes de gravar:
   - `criar_objetivo_cliente`: nome e pessoas. `financeiro` é definido aqui e não muda depois;
   - `criar_realizacao_cliente`: o resultado (ex.: juntar R$ 60.000,00) e o processo (ex.: guardar R$ 1.000,00 por mês);
   - `criar_meta_cliente`: financeira precisa de processo, nome, valor e caixas; comportamental, de processo, nome e vezes por ciclo.
3. Frequências: diária, semanal, quinzenal, mensal, bimestral, trimestral, semestral, anual e uma vez.

Editar uma meta financeira refaz os ciclos. Avise antes.

A Rica Pro não marca hábito como feito: quem marca é a pessoa, no app ou na conversa com a Rica.

## Remover

Diga o que sai junto e espere o ok antes de enviar `confirmar: true`:

| Remoção | Sai junto |
| --- | --- |
| Objetivo | realizações e metas ligadas; no comportamental, as marcações |
| Realização | as metas do processo dela |
| Meta financeira | ciclos e avisos |
| Meta comportamental | as marcações |

Erros de validação voltam com `codigo` e `mensagem`. Corrija o campo indicado e tente de novo.
