---
name: trademarkiq-estudo-de-mercado
description: Monta um estudo de mercado de marcas (país, setor, classe, América Latina ou escritórios) em PDF editorial de uma página, com opção de carrossel de 3 imagens, a partir dos dados do conector TrademarkIQ. Use quando pedirem estudo, relatório setorial, análise de país ou um material com números de depósitos de marcas.
---

# TrademarkIQ: estudo de mercado em formato editorial

Uma página que defende uma tese com números. Escreva no idioma do usuário.

## 1. Entregas

1. PDF de uma página, 828 x 1170 px.
2. Opcional, se pedirem material para redes: carrossel de 3 imagens de 1080 x 1350 px no mesmo visual, com letras grandes (30 px ou mais no corpo, 60 px ou mais no título) e poucas palavras por imagem.

## 2. Formato do PDF (ordem fixa)

1. Bloco de abertura em navy #1b3a6b, cantos de 14 px: linha pequena em caixa alta e dourada (#e6b85c) "TrademarkIQ · Inteligência de mercado · <tema>"; título em serifa, no máximo 2 linhas, escrito como tese com o número central; subtítulo de 1 a 2 linhas dizendo o que foi medido, a janela e os países.
2. Quatro números em cartões brancos (borda #e1e5ee, cantos de 12 px): número em serifa, navy; legenda cinza de 2 a 3 linhas com o contexto e a janela.
3. Linha de dois cartões: à esquerda um gráfico de barras horizontais; à direita "Dinâmicas que chamam atenção", com 3 a 4 parágrafos curtos que começam por uma frase-resumo em negrito.
4. Cartão de tabela: cabeçalho pequeno em caixa alta, números alinhados à direita, linhas finas. Destaque a linha do foco do estudo.
5. Cartão de série temporal: barras mensais, 12 meses anteriores em cinza-azulado #b9c2d6, os 12 meses atuais em azul #2f5faa, rótulos só em 3 a 5 pontos.
6. Destaque "O que isso sugere.": fundo #eef1f8, borda esquerda dourada, 2 a 4 linhas, com o fecho "Mesma leitura por país, classe, setor ou porte: https://trademarkiq.com.br".
7. Rodapé: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", a janela usada, o mês de referência de cada país, as ressalvas de cobertura, o aviso de que não é aconselhamento jurídico e o logotipo do TrademarkIQ.

Visual: fundo #f4f5f8; azul #2f5faa; cinza #b9c2d6; dourado #c28a2d; navy #1b3a6b; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em título e números.

## 3. Dados: sempre pelas ferramentas do TrademarkIQ

- `market_by_country`: série mensal, soma dos últimos 12 meses, variação, acumulado do ano e classes de qualquer escritório nacional; sem país, a matriz de todos. Leia os avisos de cobertura e omita ou sinalize os países afetados.
- Brasil em detalhe: `query_tiq_index`, `tiq_ranking`, `market_report`; procuradores em `attorney_ranking`; relações entre escritórios do Brasil e do exterior em `international_relations`.
- Prefira a soma móvel dos últimos 12 meses completos a comparações de ano fechado. No ano em curso, compare o acumulado com o mesmo período do ano anterior, nunca o ano parcial com um ano fechado.
- O último mês publicado costuma estar incompleto: use o último mês completo, ou estime e diga que estimou. Ao comparar países, informe o mês de referência de cada um.
- Projeção é cenário, não previsão: rotule assim e só projete quando houver série mensal.
- Causas entram como hipótese, a menos que venham de fonte oficial citada.
- Nunca invente números. Se a ferramenta não devolver o dado, diga que não está disponível.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png`, `trademarkiq-logo-fundo-escuro.png`, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Não recolora, não redesenhe, não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`.
3. Cite TrademarkIQ (trademarkiq.com.br) com a data da consulta em toda página.
4. Não explique como os números são calculados nem cite fontes internas.
5. Use vírgula nos decimais e o sinal "−" nos negativos.

## 5. Construção

HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px; confira que o PDF tem 1 página. Formate os números antes de montar o SVG. Em linhas de dois cartões, deixe os gráficos menores que a célula. Rótulos que se sobrepõem devem ser cortados. Abra as imagens renderizadas e confira sobreposição, cortes e transbordo antes de entregar.
