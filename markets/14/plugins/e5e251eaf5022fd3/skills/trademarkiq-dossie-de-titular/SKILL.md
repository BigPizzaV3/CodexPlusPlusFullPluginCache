---
name: trademarkiq-dossie-de-titular
description: Monta o dossiê de propriedade intelectual de uma empresa ou pessoa (cliente em prospecção, concorrente, alvo de aquisição ou parte contrária) com os dados do conector TrademarkIQ: marcas, patentes, desenhos, quem a representa, litígios, presença no exterior e domínios. Use quando pedirem dossiê, perfil de PI, due diligence de marcas, análise de concorrente ou o que uma empresa tem registrado.
---

# TrademarkIQ: dossiê de titular

Retrato do que uma empresa ou pessoa tem em propriedade intelectual e de como cuida disso. Serve para preparar uma reunião, avaliar um concorrente ou conferir ativos antes de um negócio. Escreva no idioma do usuário.

## 1. O que perguntar antes (só o que faltar)

Nome ou CNPJ do titular; a finalidade (prospecção, concorrência, aquisição, litígio), porque muda a ênfase; se interessa o grupo econômico ou só aquela pessoa jurídica.

## 2. Dados: sempre pelas ferramentas do TrademarkIQ

1. `search_trademarks` com o titular: as marcas, por situação e classe. Pagine até cobrir tudo ou diga quantas ficaram de fora. `trademark_details` nas principais (especificação, vigência, procurador, despachos) e `get_trademark_logo` para as figurativas que forem destaque.
2. `company_patents` (por CNPJ ou nome), com `patent_details` nas relevantes; `designs_by_holder` para desenhos industriais.
3. `search_ip_cases` e `ip_case`: ações judiciais em que o titular é parte; `case_law_statistics` quando ajudar a dar contexto.
4. Exterior: `international_analysis` com o nome das marcas principais nos países de interesse e `WO` para registros de Madri; `international_relations` para os escritórios estrangeiros ligados.
5. `digital_presence` para os domínios das marcas principais.
6. Contexto de mercado, se pedido: `query_tiq_index` e `tiq_ranking` no setor do titular.

Nomes de titular variam na base (razão social, abreviações, grafias antigas). Busque as variações e diga quais foram consideradas a mesma pessoa e por quê (CNPJ igual, ou nome idêntico).

Fundamento: antes de explicar um procedimento, um prazo, um motivo de recusa ou de recomendar uma medida (oposição, manifestação, recurso, nulidade administrativa, caducidade, prorrogação, cessão), chame `manual_and_law` com palavras-chave curtas ("oposição prazo", "recurso indeferimento", "caducidade", "prorrogação") ou com o número do artigo. Escreva o prazo e a regra como vêm no trecho devolvido e cite o item do Manual de Marcas e o artigo da Lei 9.279/1996. Não afirme prazo, valor, requisito ou número de artigo de memória. Se a ferramenta não trouxer o ponto, diga que ele deve ser conferido no Manual de Marcas do INPI.

## 3. Formato (PDF, 3 páginas)

Página 1, retrato: abertura com o título como conclusão ("<Titular> protege N marcas em M classes; K vencem em 12 meses."); quatro números (marcas em vigor, pedidos em andamento, patentes e desenhos, ações judiciais); gráfico de barras das marcas por classe; cartão "Quem cuida": procuradores que constam nos processos, com a contagem de cada um.

Página 2, os ativos: tabela das marcas principais (marca, processo, classe, situação, vigência, procurador) e tabela de patentes e desenhos (título, número, situação).

Página 3, riscos e oportunidades: vigências a vencer, pedidos indeferidos ou arquivados, classes do negócio sem proteção, litígios em curso, países onde a marca não aparece. Cada ponto com o dado que o sustenta.

Visual: páginas de 828 x 1170 px; fundo #f4f5f8; cartões brancos com borda #e1e5ee e cantos de 12 px; navy #1b3a6b; dourado #c28a2d (linha de destaque #e6b85c sobre navy); azul #2f5faa; cinza-azulado #b9c2d6; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em títulos e números. Cabeçalho com o logotipo do TrademarkIQ à esquerda e, à direita, "Em parceria com <escritório>" quando houver. Abertura em bloco navy: linha pequena em caixa alta e dourada, título em serifa escrito como conclusão, e uma linha com o escopo e a data.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial, nunca um desenho próprio nem o nome em texto. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png` para fundo branco ou claro, `trademarkiq-logo-fundo-escuro.png` para fundo navy ou escuro, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Mantenha a proporção, não recolora e não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`. Use só os links que as ferramentas devolvem e cite o número de cada processo.
3. Só entra no relatório o que veio de uma ferramenta. Se um dado não veio, escreva que não está disponível; não estime nem complete de memória.
4. Contagens: todo número de destaque tem de bater com as linhas das tabelas. Se a ferramenta devolveu uma página de um total maior, diga quantos itens existem e quantos estão listados.
5. Uma ferramenta que responde que a área não se aplica à conta, que o plano não a inclui ou que a cota do dia acabou não é falta de dados: omita a seção e diga ao usuário, fora do relatório, o que ficou de fora e por quê.
6. Não explique como as análises são calculadas nem cite fontes internas.
7. Rodapé em todas as páginas: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", o aviso de que o material usa dados públicos e não é parecer jurídico nem garantia de resultado, e o número da página.
8. Patente arquivada ou extinta é uma situação publicada pelo INPI, não uma conclusão de que a tecnologia é livre para uso. Marca ausente num país significa que não foi encontrada na base daquele país, não que o titular não tenha direitos lá.
9. O procurador que consta no processo é o que o INPI publicou; não afirme que há contrato vigente nem o motivo de uma troca de representante.
10. Dossiê de pessoa física: só dados de registros públicos de PI; não inclua endereço, documento nem contato.

## 5. Construção

HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px. Antes de entregar, abra as páginas renderizadas e confira: número de páginas, nada cortado pelo rodapé, tabelas sem texto sobreposto, logotipo nítido. Se o usuário pedir só a análise, entregue o mesmo conteúdo em texto, na mesma ordem.
