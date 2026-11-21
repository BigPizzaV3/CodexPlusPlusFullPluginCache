# SAGI Consultas: MCP + skill

Pacote de submissao 0.4.2 para o diretorio oficial de plugins do ChatGPT. Servidor remoto em producao: https://mcp.sagierp.com.br/mcp. O servidor permanece na versao 0.4.0.

O ZIP inclui plugin.json, mcp.json, o logotipo Sygecom e a skill com exemplos por area. OAuth usa CIMD e escopo sagi:read; o usuario autentica com seu acesso existente da API SAGI na pagina de autorizacao da Sygecom. Nao incluir senhas, tokens ou x-secret neste pacote.

O MCP permite somente leitura da empresa autenticada. Respeita menus SAGI por area e submenus de Cadastros, validacao de SQL e limites de creditos por usuario. Chamadas de negocio bem-sucedidas consomem creditos SAGI; login, falhas e verificacoes internas nao debitam. Nao realiza cobranca nem checkout dentro do ChatGPT.

O servidor oferece estoque fisico com preco/custo medio por filial, consultas de pesagens, fiscal, Financeiro 3.0 e Servico 3.0, contexto, catalogo, descoberta de fontes, SQL de leitura e consulta de creditos. A skill orienta dashboards por area autorizada, filtros, paginacao, unidades e criterios de comparacao, sem inventar valores.

Guia para clientes: https://mcp.sagierp.com.br/docs/. Suporte: https://sygecom.com.br/contato-suporte/. Termos: https://mcp.sagierp.com.br/docs/termos-de-uso.html.

A conexao manual foi homologada pelo BDI. A listagem publica depende da verificacao da Sygecom, ambiente ficticio de revisao, video, scans, submissao e aprovacao OpenAI. O executor de SQL livre precisa ser avaliado frente as diretrizes de ferramentas individualmente expostas; a preparacao deste pacote nao restringe funcionalidades autorizadas pelo BDI.

Credenciais de revisao e instrucoes privadas devem ser fornecidas somente nos campos privados do portal de submissao, nunca no ZIP.
