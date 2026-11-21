# Resultados e geografia

`arvor_eleicoes_municipios`: `ano` (2022/2026), `uf` opcional, `busca`,
`offset` e `limite` (1–20). Descubra o município pelo catálogo do ano; o código
TSE tem cinco dígitos e deve preservar zeros. Não é o código IBGE.

`arvor_eleicoes_resultados`: `ano`, `turno` (1/2), filtros opcionais `uf`,
`municipio`, `zona`, `secao`, `local`, `incluir_exterior`, `offset`, `limite`.
Município e zona exigem UF; seção/local exigem UF, município e zona.
UF é a sigla maiúscula; zona, seção e local são inteiros, município é string.
Para `ZZ`, use `incluir_exterior=true`. O exterior é excluído por padrão.

Os totais somam TODAS as seções do recorte. `limite` controla somente a amostra
de seções retornada; não some novamente esses totais ao percorrer páginas.
Brasil e UF usam resumos e podem não trazer amostra de seções. Para extrair
seções, aplique recorte detalhado e siga `proximo_offset` quando disponível.
Encerre quando for null. Uma página ou o ranking não são todo o universo.

Ao calcular participação, explicite se o denominador é votos válidos nominais,
comparecimento ou eleitorado. Brancos, nulos e abstenção são categorias distintas.
Verifique cobertura e campos ausentes antes de reconciliar totais. A cobertura
corresponde aos BUs disponíveis no snapshot, não automaticamente a todas as
seções cadastradas. Compare eleições preservando diferenças de universo.

Exemplo de fluxo: para Rio Branco/AC, encontre o município no ano desejado;
use o código retornado com UF, ano e turno na consulta de resultados. Compare
os totais dos candidatos retornados, não apenas os votos das seções da amostra.
