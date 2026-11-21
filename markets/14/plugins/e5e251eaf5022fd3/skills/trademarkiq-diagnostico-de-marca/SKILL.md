---
name: trademarkiq-diagnostico-de-marca
description: Monta o relatório de diagnóstico de viabilidade de uma marca (PDF de 3 páginas) com os dados do conector TrademarkIQ, para o Brasil ou para outro país (Portugal, União Europeia, Estados Unidos e outros). Use quando pedirem diagnóstico, viabilidade, parecer de risco ou relatório para cliente sobre o registro de uma marca.
---

# TrademarkIQ: relatório de diagnóstico de marca

Relatório para entregar a um cliente que quer registrar uma marca. Responde a três perguntas: há marca igual ou parecida, qual o risco, o que fazer. Escreva no idioma do usuário (para Portugal, português europeu: "registo", "logótipo").

## 1. O que perguntar antes (só o que faltar)

Nome exato da marca; o que o negócio vende ou presta, para quem e por qual canal; país ou países do registro; nome do cliente e de quem elabora o relatório (escritório), se for para terceiros.

## 2. Dados: sempre pelas ferramentas do TrademarkIQ

Brasil:
1. `classify_activity` com a descrição do negócio; mostre as classes e as especificações e peça a confirmação do usuário.
2. `viability_diagnosis` (ou `analyze_collision`) com as classes confirmadas: dá a viabilidade de 0 a 100 por classe.
3. `search_trademarks` para as anterioridades concretas e `trademark_details` nas que importam (especificação, datas, titular, despachos).

Outro país:
1. `classify_activity` do mesmo modo (a Classificação de Nice vale em todos os países).
2. `international_analysis` com o código do país. Para país da União Europeia, acrescente `EM` (marcas da União Europeia, que valem em todos os Estados-membros) e `WO` (registros de Madri). Busque o nome completo e também o termo principal sem artigo ("O Leopoldo", "Leopoldo", "Leopold").
3. `trademark_details` em cada marca relevante: especificação da classe, data de concessão, validade e, nos registros de Madri, se o país está entre os designados.
4. `data_freshness_by_country` quando for útil dizer até quando vão os dados daquele país.

Nunca responda que só o Brasil é coberto. Fora do Brasil não há nota de 0 a 100: o resultado é um levantamento de anterioridades com leitura qualitativa de risco, e o relatório diz isso.

## 3. Formato (PDF, 3 páginas de 828 x 1170 px)

Página 1, resumo:
1. Cabeçalho com o logotipo do TrademarkIQ à esquerda e, à direita, "Em parceria com <escritório>" quando houver.
2. Bloco de abertura em navy: linha pequena em caixa alta ("TRADEMARKIQ · DIAGNÓSTICO DE VIABILIDADE · <PAÍS>"), título em serifa escrito como conclusão ("<Marca> tem espaço em <país>, mas <marca anterior> pede cautela em <setor>.") e uma linha com serviços, classe, registros consultados e data.
3. Faixa com: preparado para, marca analisada, serviços e classe, elaborado por.
4. Quatro números: marcas registradas iguais ou próximas no país, pedidos em andamento, registros regionais válidos no país, registros idênticos.
5. Dois cartões: "Leitura do diagnóstico" (frase de conclusão e escala baixo, médio, médio-alto, alto, com a posição marcada) e "Onde estão os N registros próximos" (barras por situação).
6. Cartão com os motivos do principal ponto de atenção e o que joga a favor.
7. Destaque "O que isso sugere." em 2 a 4 linhas.

Página 2, as marcas:
- Tabela 1: todas as marcas válidas no país, ordenadas pelo risco. Colunas: marca (titular e tipo), registro e classes, situação, serviços protegidos na classe, risco.
- Tabela 2: as demais contadas (inativas, ou registros internacionais que não designam o país), com a observação que explica por que não bloqueiam.

Página 3, o que fazer: caminhos recomendados numerados, especificação sugerida para o pedido e próximo passo.

Rodapé em todas as páginas: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", o aviso de que é análise de risco com dados públicos, não parecer jurídico nem garantia de registro ou de recusa, e o número da página.

Visual: fundo da página #f4f5f8; cartões brancos com borda #e1e5ee e cantos de 12 px; navy #1b3a6b; dourado #c28a2d (linha de destaque #e6b85c sobre navy); azul #2f5faa; cinza-azulado #b9c2d6; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em títulos e números.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial, nunca um desenho próprio nem o nome em texto. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png` para fundo branco ou claro, `trademarkiq-logo-fundo-escuro.png` para fundo navy ou escuro, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Mantenha a proporção, não recolora, não redesenhe, e não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`, para qualquer país. Use só os links que as ferramentas devolvem.
3. Contagens: toda marca contada num número de destaque aparece numa tabela. Se alguma ficar de fora, diga quantas e por quê.
4. Datas: a mesma informação em todas as linhas. Validade ("válida até dd/mm/aaaa") quando o registro a traz; só na falta dela, a data de concessão ou de depósito.
5. Só afirme data de concessão, países designados ou serviços protegidos que venham do resultado de uma ferramenta. Se a ferramenta não trouxe, diga que não está disponível.
6. Risco: no Brasil, a viabilidade é a que a ferramenta devolve. Fora do Brasil, a leitura por marca (médio-alto, médio, médio-baixo, baixo) é qualitativa, pela proximidade dos nomes e pela afinidade dos serviços, e o relatório a apresenta assim.
7. Não explique como as análises são calculadas nem cite fontes internas. Cite o número de cada processo.
8. Caminhos recomendados no Brasil (depósito, oposição, recurso, nulidade, caducidade da marca anterior, convivência): antes de escrevê-los, chame `manual_and_law` e cite o item do Manual de Marcas do INPI e o artigo da Lei 9.279/1996 que sustentam cada um. Não afirme prazo nem requisito de memória.
9. Todo relatório leva o aviso: análise de risco com dados públicos, não é parecer jurídico nem garantia; recomenda-se revisão por profissional de propriedade industrial antes do depósito.

## 5. Construção

HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px. Antes de entregar, abra as páginas renderizadas e confira: número de páginas, nada cortado pelo rodapé, tabelas sem texto sobreposto, logotipo nítido.
