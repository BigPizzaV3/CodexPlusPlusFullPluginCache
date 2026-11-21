# Localizar cadastros antes de consultar movimentos

> Versão 0.4.0: os exemplos podem ser adaptados e executados com SQL livre de leitura. Todas as filiais da empresa do login estão autorizadas; TODAS tem esse escopo. O catálogo não exige cadastro de cada SQL. Confirme o esquema real e os critérios do relatório.

Fontes: API v2 `src/modules/sygecom/cadastros/sql/cadastros.sql.ts:24` e `:68`; produtos em `src/modules/sygecom/produtos/sql/produtos.sql.ts:30` e `src/core/interfaces/produto.interface.ts:2`; nomes de fornecedor/cliente/produto também conferidos no corpo de `syg_movimento_pesos` em `source/sagi_plsql.prg`.

Os termos `RECICLAGEM` e `SUCATA` são ilustrativos e devem ser substituídos pelo pedido. Validar os literais; apóstrofo vira `''`. Em buscas por texto literal, tratar `%` e `_` como caracteres escapados se o usuário não pediu curingas. Estes exemplos usam apenas palavras sem curingas internos.

Não aplicar status `ATIVO`, `A` ou outro código sem confirmar o domínio da coluna e o pedido. Os exemplos retornam o status armazenado. As permissões de cadastros e suas regras de acesso por empresa/filial devem ser aplicadas pelo MCP; estar na base da empresa não torna todo cadastro visível ao usuário.

## C01 — Encontrar fornecedor por parte do nome

Pergunta: “Qual o código dos fornecedores com RECICLAGEM no nome?” `codfor` pode ser usado no parâmetro 5 da pesagem de `ENTRADA`; não substituir por `orides_codigo`.

```sql
SELECT f.codfor AS fornecedor_codigo,
   f.fornecedor AS nome, f.cidade, f.uf, f.status
FROM cag_for f
WHERE f.fornecedor ILIKE '%RECICLAGEM%'
ORDER BY f.fornecedor, f.codfor, f.sr_recno
LIMIT 100
```

## C02 — Encontrar cliente por parte do nome

Pergunta: “Localize clientes com RECICLAGEM no nome para consultar suas vendas.” Se houver mais de um cadastro, apresentar os candidatos; não escolher automaticamente uma pessoa por nome parecido. `codcli` vai na posição 5 da pesagem de `SAIDA` e em `medicao_codcli` no Serviço 3.0.

```sql
SELECT c.codcli AS cliente_codigo,
   c.cliente AS nome, c.cidade, c.uf, c.status
FROM cag_cli c
WHERE c.cliente ILIKE '%RECICLAGEM%'
ORDER BY c.cliente, c.codcli, c.sr_recno
LIMIT 100
```

## C03 — Localizar código e subcódigo de produto

Pergunta: “Quais produtos de compra têm SUCATA na descrição e qual a unidade de cada um?” A chave de produto inclui código e subcódigo. Não usar preços ou estoques de uma coluna isolada como saldo de estoque por filial sem regra documentada.

```sql
SELECT p.codpro, p.subcod, p.produto,
   p.un AS unidade, p.status
FROM cag_pro p
WHERE p.produto ILIKE '%SUCATA%'
ORDER BY p.produto, p.codpro, p.subcod, p.sr_recno
LIMIT 100
```

O catálogo de produtos de venda também existe na API (`cag_prov`), mas não presumir o mesmo esquema/descrição. Estes exemplos usam apenas `cag_pro`, conferido na função de pesagens. Não foi criado exemplo de estoque: saldo por filial e unidade requer fonte e regra próprias.

Permissões por submenu: consulte `sagi_contexto.permissoes.areas` para identificar Clientes, Fornecedores, Credores, Funcionários, Produtos e demais cadastros autorizados. Um submenu de Clientes não autoriza Fornecedores. SQL com JOIN, UNION ou view envolvendo ambos exige os dois acessos; não substitua a fonte recusada por outra tabela/relatório.
