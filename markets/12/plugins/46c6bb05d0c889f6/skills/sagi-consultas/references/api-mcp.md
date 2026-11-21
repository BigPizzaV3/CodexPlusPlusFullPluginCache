# Contrato MCP SAGI de leitura — 0.4.0

Servidor: https://mcp.sagierp.com.br/mcp. OAuth/PKCE e login externo existente da API SAGI. O Worker envia internamente POST /api/v1/generic com {"sql":"SELECT ..."}, Bearer individual e header interno de conexão. As credenciais não aparecem nas ferramentas.

## Ferramentas

| Ferramenta | Entradas principais | Resultado |
|---|---|---|
| sagi_contexto | nenhuma | Empresa do login, todas as filiais, tabelas 3.0 existentes, data/fuso e limite |
| sagi_tabelas | busca, deslocamento | Tabelas/views de negócio por trecho literal do nome; 100 por página |
| sagi_esquema | tabelas, 1 a 20 nomes | Colunas, tipos, nulabilidade, comentários, definições PK/FK/unique; sem credenciais |
| sagi_catalogo | nenhuma | Exemplos adaptáveis; não é lista de autorização |
| sagi_consultar | sql, deslocamento=0, limite=100 | SQL livre de leitura; registros, quantidade, próximo deslocamento e data da consulta |
| sagi_pesagens | datas, movimento, filiais, pessoa/produto/subcódigo/boleto/unidade e flags | Pesagens de qualquer período/filial, lista ou mês/produto |
| sagi_notas_fiscais | datas, filial e os 18 filtros fiscais, status/destinatário | Notas fiscais com colunas explícitas |
| sagi_financeiro30 | datas/campo_data, P/R, filiais, pessoa/módulo/documento e saldo | Parcelas Financeiro 3.0, saldo de listagem declarado |
| sagi_servico30 | datas, filiais, cliente, status e aprovada | Cabeçalhos de medição Serviço 3.0 |
| sagi_pesagens_compra_mensal | deslocamento múltiplo de 100 | Referência FILIAL2/2026, todos os grupos; outros recortes usam pesagens/SQL |

O contrato JSON acompanha o plugin. Argumentos opcionais e defaults são descobertos em tools/list. Datas: YYYY-MM-DD; data_final inclusiva nas ferramentas de relatório. Filiais de pesagens/serviço usam nomes; financeiro usa IDs reais do cadastro. Unidade da filial na pesagem não é KG/UN do produto.

## Permissões e validação

Qualquer login externo válido acessa os dados de negócio de sua própria empresa e todas as suas filiais, conforme liberação BDI. Não escolhe empresa em argumento. Política enabled:false pode suspender acesso. Não há cadastro de cada SELECT, lista fixa de SQL nem corte obrigatório em FILIAL2/2026.

SQL livre aceita SELECT, CTE de leitura, JOIN, UNION, subconsulta, agrupamento, janelas e comentários válidos, com colunas explícitas e aliases únicos. COUNT(*) é permitido. Escrita, bloqueios, comandos administrativos, funções perigosas, registros inteiros e segredos são recusados. Views são analisadas recursivamente. Funções de relatório verificam a definição instalada e validam argumentos dinâmicos; outras funções customizadas exigem garantia de leitura. Parser cobre um subconjunto do PostgreSQL e recusa sintaxe não reconhecida.

`readOnlyHint` e demais anotações ajudam o cliente; a proteção real está no Worker antes da chamada de negócio. A conexão da API não foi alterada para role de leitura. Não executar funções arbitrárias só porque começam com syg_ ou são declaradas STABLE/IMMUTABLE.

## Paginação e resposta

sagi_consultar e relatórios livres retornam até 100 registros, quantidade, deslocamento, proximo_deslocamento (null ao terminar), limite_linhas e consultado_em. A página é aplicada após filtros/agregações. LIMIT no SQL limita o conjunto antes da paginação externa: para percorrer a lista completa, retire LIMIT do SQL e use limite do MCP. Totais devem vir de SUM/COUNT da fonte completa filtrada, nunca soma de uma página.

Use ORDER BY com chave de desempate. Fonte pode mudar entre páginas; não há snapshot entre chamadas. A ferramenta de referência fixa retorna total_grupos porque já carrega aquele relatório inteiro, dentro do limite de transporte; isso não implica total conhecido nas outras ferramentas.

## Erros

Falha é resposta MCP isError, não registros vazios. Token expirado: reconectar pelo OAuth. Tabela inexistente: descobrir o nome real. Sintaxe recusada: reescrever como leitura suportada. Função instalada mudou: consultar diretamente a fonte tabular ou solicitar revisão da função; não contornar a proteção. Estouro de bytes/timeout: reduzir período ou detalhe. Nenhuma mensagem inclui senha, Bearer ou diagnóstico SQL interno da API.

Fontes: [API Explorer](https://api.sagierp.com.br/api-explorer/), [dicionário](https://sagierp.com.br/devel/uteis/sagi_dicionario_dados.pdf), [guia público](https://mcp.sagierp.com.br/docs/).


## Créditos por usuário

`sagi_creditos` não recebe argumentos e mostra plano, limite diário, usados/reservados, créditos disponíveis hoje, saldo mensal quando aplicável, reinícios ISO e mensagem legível. Não consome créditos e permanece disponível no bloqueio. As respostas das demais ferramentas incluem `uso`. Bloqueio retorna `isError: true` com `erro` e `uso`; apresente a mensagem ao usuário e pare as consultas. Consultas de negócio bem-sucedidas consomem um crédito por chamada à API, inclusive cada página. Metadados internos, contexto, esquema, catálogo, login e falhas não debitam. Cotas são por empresa+usuário autenticados e compartilhadas entre sessões/dispositivos.
