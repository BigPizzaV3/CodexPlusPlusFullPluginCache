# Validação da versão 0.1.12

A versão 0.1.12 preserva o título e o nome do arquivo XML-base e ajusta as seções do INI.

A versão 0.1.11 separa a criação completa da edição segura de um dashboard existente. Quando os campos vêm de uma fonte MyBI existente, exige o XML atual como base, preserva a fonte, consulta ou procedure, parâmetros, cálculos e itens existentes, e acrescenta somente os novos componentes. Também preserva o nome real das medidas
e inclui um prompt inicial pertinente em português. O comportamento visual deve ser conferido após carregar a atualização.

Verificado localmente em 2026-09-13:

- Validador oficial do scaffold de plugin: aprovado.
- Validador oficial de SKILL.md: aprovado.
- 26 testes automatizados Python: aprovados, incluindo preservação do XML-base, fonte dinâmica, esquema, fórmulas,
  moeda, percentual, aparência e rejeições.
- Colunas explícitas e ResultSchema no formato serializado pelo DevExpress 24.2.5.
  Confirmados cinco tipos (String, Int64, Double, DateTime, Boolean) em source.Result
  após carga offline; esquema e colunas preservados na regravação. Referência de
  serialização obtida de tabela SQLite sintética vazia, sem acessar dados de clientes.
- CalculatedFields preservados na carga/regravação DevExpress 24.2.5 com expressão,
  DataType e DataMember; sintaxe analisada por CriteriaOperator. Sem consulta ao banco.
- Pacote com três componentes separados (card, EChartsGradientBar e grid): carregado
  e reserializado pelo DevExpress 24.2.5 sem acessar banco de dados.
- Pacote cobrindo os 15 componentes do catálogo: carregado e reserializado, preservando
  contagem de itens, fonte, DataItems, metadados customizados e séries/medidas dos cards.
- Estrutura do ZIP: DashboardWeb/dashboard1.xml e formatacao.ini mínimo na raiz.
  Leitores de aparência conferidos no código MyBI. Aparência final ainda requer teste web.
- Oito pacotes de teste carregados e regravados pelo DevExpress 24.2.5, incluindo
  NumericFormat Currency/Percent e esquema tipado.

Esses testes não executaram o MyBI web, o JavaScript dos gráficos ou uma importação no
servidor. Não comprovam qualidade visual, dados do cliente, instalação no ChatGPT Work
ou compatibilidade com Claude. A validação de sintaxe JavaScript não executa o código.

O modo padrão é components: componentes separados, não Dashboard HTML. Itens HTML
exigem mode html explícito. CalculatedFields numéricos suportados conforme calculos.md;
outras opções fora do catálogo não são ignoradas.
Próxima validação: instalar o plugin em ambiente de teste e importar um ZIP gerado no
MyBI de teste, vinculando uma fonte sintética compatível, antes de distribuição pública.
