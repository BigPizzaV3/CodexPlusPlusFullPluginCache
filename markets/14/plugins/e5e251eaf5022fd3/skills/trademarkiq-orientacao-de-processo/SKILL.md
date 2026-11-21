---
name: trademarkiq-orientacao-de-processo
description: Explica em que ponto está um processo de marca no INPI e o que cabe fazer, com os dados do conector TrademarkIQ e fundamento no Manual de Marcas do INPI e na Lei 9.279/1996: o que o despacho significa, o prazo que abriu, as opções, o que cada uma exige e o que acontece se nada for feito. Use quando perguntarem o que significa um despacho, o que fazer com um indeferimento, exigência, oposição, sobrestamento ou arquivamento, até quando dá para recorrer, renovar, pedir caducidade ou nulidade.
---

# TrademarkIQ: orientação de processo

Nota curta que diz onde o processo está, o que o INPI decidiu, o prazo que corre e os caminhos possíveis, cada um com a base no manual e na lei. É a resposta que um bom procurador daria ao cliente por escrito. Escreva no idioma do usuário, em linguagem direta; o leitor pode não ser da área.

## 1. O que perguntar antes (só o que faltar)

O número do processo (ou a marca e o titular, para localizá-lo); o que o usuário quer (manter o pedido, desistir, atacar a marca de um terceiro); se ele é o titular, o procurador ou um terceiro interessado.

## 2. Dados: sempre pelas ferramentas do TrademarkIQ

1. `trademark_details` com o número: situação, datas, classe, especificação, titular, procurador e a sequência de despachos, com a data da RPI de cada um. Se só houver o nome, `search_trademarks` primeiro.
2. `rpi_issues`, se for preciso confirmar a data da edição que publicou o despacho: é dela que o prazo conta.
3. `manual_and_law`, sempre, em três passos:
   - o despacho: "despachos aplicáveis <nome do despacho>" (indeferimento, exigência, sobrestamento, deferimento, arquivamento);
   - a medida cabível: "recurso", "oposição", "manifestação oposição", "cumprimento de exigência", "processo administrativo de nulidade", "caducidade", "prorrogação", "restauração", "desistência";
   - os artigos que o trecho do manual citar, pelo parâmetro `article`.
4. Indeferimento por marca anterior: `trademark_details` na anterioridade citada (situação e vigência; marca extinta ou a vencer muda a estratégia) e `analyze_collision` para a força da colidência.
5. `ip_case_law` quando a tese depender de entendimento dos tribunais, com 1 a 3 decisões.

Fundamento: antes de explicar um procedimento, um prazo, um motivo de recusa ou de recomendar uma medida (oposição, manifestação, recurso, nulidade administrativa, caducidade, prorrogação, cessão), chame `manual_and_law` com palavras-chave curtas ("oposição prazo", "recurso indeferimento", "caducidade", "prorrogação") ou com o número do artigo. Escreva o prazo e a regra como vêm no trecho devolvido e cite o item do Manual de Marcas e o artigo da Lei 9.279/1996. Não afirme prazo, valor, requisito ou número de artigo de memória. Se a ferramenta não trouxer o ponto, diga que ele deve ser conferido no Manual de Marcas do INPI.

## 3. Formato (texto, ou PDF de 1 a 2 páginas se pedirem)

1. **Onde o processo está.** Uma frase: marca, processo, classe, situação e o último despacho com a data da RPI.
2. **O que isso significa.** O despacho em linguagem simples e, em seguida, o trecho do manual que o define, com o item.
3. **Prazo.** O prazo, de onde conta e a data-limite, com a conta mostrada e o artigo ou item que o fixa. Se o prazo já passou, diga isso primeiro e o que ainda resta.
4. **Caminhos.** Tabela: caminho, o que exige, base (item do manual e artigo), prazo, risco. Inclua sempre "não fazer nada" e a consequência.
5. **O que eu faria primeiro.** Um parágrafo com a sequência sugerida e o que precisa ser conferido antes.
6. **Histórico.** Os despachos em ordem, com data.

No PDF, use o visual das outras skills do TrademarkIQ: páginas de 828 x 1170 px; fundo #f4f5f8; cartões brancos com borda #e1e5ee e cantos de 12 px; navy #1b3a6b; dourado #c28a2d (linha de destaque #e6b85c sobre navy); azul #2f5faa; cinza-azulado #b9c2d6; texto #1d2433 e secundário #5d667a. Fontes: Inter no texto, DejaVu Serif em títulos e números. Cabeçalho com o logotipo do TrademarkIQ à esquerda e, à direita, "Em parceria com <escritório>" quando houver. Abertura em bloco navy: linha pequena em caixa alta e dourada, título em serifa escrito como conclusão, e uma linha com o escopo e a data.

## 4. Regras

1. Logotipo: use sempre o logotipo oficial, nunca um desenho próprio nem o nome em texto. Com esta skill instalada, os arquivos estão em `assets/` (`trademarkiq-logo-fundo-claro.png` para fundo branco ou claro, `trademarkiq-logo-fundo-escuro.png` para fundo navy ou escuro, `trademarkiq-icone.png`); copie-os para o diretório de trabalho, porque o ambiente de código não tem rede. Sem a skill, chame `trademarkiq_logo`. Mantenha a proporção, não recolora e não peça o logotipo ao usuário.
2. Endereço: o site é sempre `https://trademarkiq.com.br`. Use só os links que as ferramentas devolvem e cite o número de cada processo.
3. Só entra no relatório o que veio de uma ferramenta. Se um dado não veio, escreva que não está disponível; não estime nem complete de memória.
4. Contagens: todo número de destaque tem de bater com as linhas das tabelas. Se a ferramenta devolveu uma página de um total maior, diga quantos itens existem e quantos estão listados.
5. Uma ferramenta que responde que a área não se aplica à conta, que o plano não a inclui ou que a cota do dia acabou não é falta de dados: omita a seção e diga ao usuário, fora do relatório, o que ficou de fora e por quê.
6. Não explique como as análises são calculadas nem cite fontes internas.
7. Rodapé em todas as páginas: "Fonte: TrademarkIQ (trademarkiq.com.br). Consulta em <data>.", o aviso de que o material usa dados públicos e não é parecer jurídico nem garantia de resultado, e o número da página.
8. Prazo vencido, extinção e arquivamento definitivo são ditos sem rodeios, na primeira frase.
9. Toda data-limite mostra a conta: data da RPI, prazo e resultado. Se a contagem depender de regra que a ferramenta não trouxe (dias úteis, feriados, prorrogação), diga que a data deve ser confirmada.
10. Nunca diga que falta pagar taxa de concessão nem cite valores de retribuição de memória: descreva só o que o trecho do manual trouxer e mande conferir a tabela de retribuições do INPI.
11. A nota orienta; não substitui o procurador. Para peças (recurso, oposição, nulidade), entregue os fundamentos e recomende a redação por profissional habilitado.

## 5. Construção

Texto direto na conversa por padrão. PDF só se pedirem: HTML com SVG embutido, convertido em PDF por um navegador sem interface, com `@page` em 828 x 1170 px. Antes de entregar, abra as páginas renderizadas e confira: número de páginas, nada cortado pelo rodapé, tabelas sem texto sobreposto, logotipo nítido. Se o usuário pedir só a análise, entregue o mesmo conteúdo em texto, na mesma ordem.
