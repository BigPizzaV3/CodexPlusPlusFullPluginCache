---
name: urbit-analise-imobiliaria
description: Analisa mercado imobiliário, preços de venda e aluguel, infraestrutura, perfil territorial e potencial de terrenos com as ferramentas MCP da Urbit. Use para comparar imóveis e localizações, estudar oferta e demanda ou apoiar viabilidade preliminar; não para alterar cadastros, publicar anúncios ou administrar o servidor MCP.
---

# Análise imobiliária com Urbit

Transforme os dados da Urbit em uma análise que ajude o usuário a entender um imóvel, terreno ou mercado. Responda no idioma do usuário. Ajuste a profundidade à decisão solicitada; uma consulta pontual não exige um estudo completo.

## Delimitar a análise

Identifique localização, finalidade (venda, aluguel, aquisição, desenvolvimento ou comparação) e tipo de imóvel. Peça apenas informações ausentes que mudem a consulta ou a interpretação. Não invente atributos para completar uma avaliação.

Use as ferramentas Urbit disponíveis na sessão. Os nomes podem aparecer com prefixos do conector e sublinhados: resolva pelo nome e descrição reais do catálogo, sem presumir que um nome histórico esteja disponível. Se não houver conexão, explique o impedimento e prepare a análise com dados fornecidos pelo usuário, sem simular resultados.

Quando necessário, converta o endereço com `get-geocoder` e confirme ambiguidades de cidade ou logradouro. Coordenadas devem representar o imóvel ou área objeto da análise, não a localização pessoal do usuário. Use `cidade` sem acentos e com hífens nas consultas municipais. Latitude e longitude não são intercambiáveis.

As informações do MCP Urbit funcionam melhor para o mercado residencial. Para estudos logísticos, corporativos e salas comerciais, apresente disclaimer ao usuário.

## Escolher consultas pela pergunta

| Objetivo                                                        | Ferramentas e uso                                                                                                                                                                                               |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Precificar venda                                                | `get-avm` para estimativa; `get-listing` para ofertas concorrentes; `get-transacoes-itbi` para evidências de transações quando disponíveis                                                                      |
| Analisar aluguel                                                | `get-listing` com finalidade aluguel; separar aluguel, condomínio, IPTU e custo total                                                                                                                           |
| Entender lançamentos ou estudos do mercado primário residencial | `get-launches-typologies-mcp` e `get-estatisticas-lancamentos-vendas` para tipologias, preços, estoque e vendas                                                                                                 |
| Conhecer terreno e potencial construtivo                        | `get-lote-fiscal`, `get-zoneamento-parametros` e, quando pertinente, `get-operacoes-intervencoes-urbanas`                                                                                                       |
| Avaliar acessibilidade e serviços                               | `get-mobilidade-urbana`, `get-escolas-shoppings-hospitais`, `get-amenities`, `get-parques` e `get-feiras`                                                                                                       |
| Entender demanda territorial                                    | `get-sociodemografico-mcp` para análises socioeconômicas consolidadas; use `get-sociodemografico-setor-mcp` somente quando a pergunta exigir abertura das informações por setor censitário, individualmente     |
| Investigar restrições e riscos                                  | Selecione entre `get-areas-contaminadas`, `get-area-alagamento`, `get-risco-geologico`, `get-patrimonio-cultural`, `get-melhoramento-viario`, `get-decreto-desapropriacao` e `get-infra-dutos-gasodutos-torres` |
| Complementar contexto                                           | `get-altitude`, `get-divisao-adm-mun`, `get-vilas`, `get-area-vulnerabilidade`, `get-ivs` e `get-supply-location-quality-index`, conforme a pergunta                                                            |

Consulte apenas os serviços úteis à decisão. Prefira o raio padrão de cada ferramenta, salvo recorte explícito ou necessidade analítica justificada. Informe o raio usado; se ampliar por escassez de dados, explique a mudança. Envie `limit` somente quando o usuário solicitar um limite, conforme os descritores atuais. Resultados limitados não representam necessariamente todo o mercado.

As permissões e a cobertura variam. Diante de `permission_denied`, informe a limitação e continue com dados disponíveis; não repita chamadas para contornar o acesso nem transforme a análise em oferta comercial. Não refaça consultas idênticas sem motivo.

Diante dos custos por requisição, faça um planejamento antes de cada análise com os endpoints a serem consultados e a estimativa do custo. Para consultas do `get-launches-typologies-mcp`, pergunte ao usuário antes se deseja prosseguir.

## Precificar e comparar

Para `get-avm`, obtenha área privativa, quartos, vagas, suítes, banheiros e localização. Confira o schema atual para tipo, subtipo e região do modelo. A implementação atual estima venda para apartamentos; não use seu resultado como estimativa de aluguel e não use para casas.

O modelo atual considera lançamento quando o ano de construção está ausente, mesmo com `lancamento=0`. Para imóvel usado, procure obter o ano antes de chamar o AVM. Se desconhecido, prefira comparáveis ou explicite a hipótese e sua limitação. Não estenda a região padrão `rmsp` a outras cidades sem confirmar suporte.

Separe sempre três evidências: preço pedido em anúncio, valor registrado de transação e estimativa do modelo. Elas não são equivalentes. Compare imóveis com finalidade, tipologia, área, padrão, idade, localização e data compatíveis; explique diferenças relevantes.

Calcule preço por m² usando área compatível e positiva, preferencialmente privativa. Remova duplicatas identificáveis antes de agregar; não elimine observações apenas por divergirem da conclusão. Mostre quantidade de comparáveis, período, recorte geográfico e dispersão. Em amostras pequenas, apresente faixa indicativa e incerteza em vez de precisão artificial. Não aplique descontos ou prêmios percentuais sem evidência ou premissa explícita.

No AVM, apresente os valores mínimo, central e máximo quando disponíveis, sem chamar essa faixa de intervalo de confiança se a fonte não o definir assim. Para lançamentos, diferencie preço de lançamento, preço de estoque, valores corrigidos por índice e suas datas. Só calcule velocidade de vendas ou absorção quando houver período e denominador conhecidos.

Quando for usar os serviços `get-listing` e `get-transacoes-itbi`, dê preferência para raios pequenos, de 100 a 200m. Raios grandes tendem a sobrecarregar a consulta. Informe o usuário da limitação de anúncios conforme descrição do serviço.

## Infraestrutura, demanda e viabilidade

Conecte cada indicador a uma implicação verificável: proximidade a transporte, oferta de serviços, concorrência por tipologia ou adequação do produto à composição domiciliar. Distância geográfica não é tempo de caminhada nem prova de acesso por via pública. Diferencie infraestrutura existente de planejada.

Use dados sociodemográficos como agregados territoriais: registre ano da fonte, raio ou setor e unidade do indicador. Não atribua renda ou características de moradores a uma pessoa ou imóvel específico. Não confunda presença de vulnerabilidade com criminalidade ou qualidade individual dos residentes.

A informação de renda do serviço é renda do responsável, e não domiciliar. Deixe isso evidente para o usuário, e sugira uma estimativa da renda domiciliar conforme características do local e pertinência do estudo.

Em terrenos, diferencie área do lote, área construída, área ocupada (de projeção do lote) e área privativa. Um cálculo como área do lote × coeficiente de aproveitamento é um cenário teórico de área computável, não área vendável aprovada. Explicite condicionantes disponíveis, como taxa de ocupação, permeabilidade, recuos, gabarito, patrimônio e intervenções. Não conclua aprovação ou regularidade apenas com a consulta espacial.

## Análise do mercado primário

Use o serviço `get-launches-typologies-mcp` com parcimônia. Prefira sempre o serviço `get-estatisticas-lancamentos-vendas`, pois é mais barato e trás dados agregados.

## Interpretar respostas e entregar

Leia `structuredContent` quando disponível; registros podem estar em `value` ou diretamente no objeto. Preserve o significado de erros, ausência de cobertura e campos nulos. `nada consta` significa ausência de registros na consulta, não inexistência comprovada de risco, oferta ou restrição.

Retorne somente os dados necessários. Para análise de mercado, omita nomes de contribuintes e contatos de anunciantes; não reproduza dados pessoais desnecessários que apareçam na resposta. Identificadores cadastrais de imóveis podem servir à rastreabilidade quando pertinentes. Nunca peça tokens ou senhas na conversa.

Apresente primeiro a conclusão que os dados sustentam, seguida das evidências e limitações que alteram a decisão. Em comparações, use uma tabela com métricas equivalentes. Identifique serviços consultados, datas dos dados quando retornadas, recorte e premissas; não invente links de fontes. Distinga resultados observados, cálculos próprios e hipóteses. Proponha próximos passos proporcionais às lacunas encontradas, sem prometer valorização, retorno, venda ou aprovação.

O app consulta e estima. Pedidos para alterar cadastro na prefeitura, publicar anúncio, contatar compradores ou executar transações estão fora deste fluxo; explique a limitação sem acionar ferramentas como se realizassem essas ações.
