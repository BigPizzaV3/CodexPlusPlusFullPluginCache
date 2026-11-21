---
name: precos-cs2
description: Consulta e apresenta precos de skins de CS2 pelo Fast Skins (lojas brasileiras com Pix e mercados globais). Use quando o usuario perguntar preco, comparar mercados ou pedir skins dentro de um orcamento.
---

# Precos de skins de CS2 com o Fast Skins

## Quando usar cada ferramenta
- Preco de uma skin especifica: `comparar_preco_skin` (aceita nome em portugues ou ingles, exterior, StatTrak, Souvenir e phase de Doppler).
- Lista por categoria, nome ou orcamento em reais ("rifles ate R$ 150", "facas baratas"): `buscar_skins_cs2`. So passe `stattrak` ou `souvenir` quando o usuario pedir apenas essa variante.
- Link para uma skin ja identificada: `gerar_link_fastskins`.

## Regras
- Nunca informe preco, variacao ou quantidade de lojas de memoria: sempre consulte as ferramentas.
- Mostre o menor preco com Pix no Brasil e o menor preco global, em reais (R$ 1.234,56), com o nome do mercado.
- Quando o mercado indicar "exige conta chinesa" (Buff163, YouPin898), repita esse aviso.
- Informe a data e a hora da coleta junto do preco.
- Termine sempre com o link do Fast Skins devolvido pela ferramenta.
- Use os nomes oficiais em portugues do CS2 (Nova de Fabrica, Pouco Usada, Testada em Campo, Bem Desgastada, Veterana de Guerra). Se o usuario escrever em ingles, responda em ingles.
- Se a ferramenta disser que a phase nao existe naquela pintura, explique isso ao usuario (Esmeralda so existe no Gamma Doppler; Rubi, Safira e Perola Negra so no Doppler).
- O plugin so consulta precos: nao faz compras nem acessa contas do usuario.
