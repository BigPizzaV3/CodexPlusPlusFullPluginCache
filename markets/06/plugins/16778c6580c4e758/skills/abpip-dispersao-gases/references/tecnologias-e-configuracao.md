# Tecnologias e configuração

## Tecnologias

- Eletroquímico: voltado principalmente a gases tóxicos e oxigênio; alta sensibilidade, porém vida útil e interferências ambientais/químicas exigem atenção.
- Oxidação catalítica: gases inflamáveis; baixo custo, mas exige oxigênio, calibração e cuidado com envenenamento do catalisador.
- IR pontual: hidrocarbonetos; boa estabilidade e vida útil, com limitações de cobertura pontual e obstrução óptica.
- IR de visada: concentração média ao longo de um caminho; útil em perímetros/áreas abertas, exige alinhamento e tem custo maior.
- Acústico/ultrassônico: detecta ruído de vazamento pressurizado, não concentração; requer pressão mínima indicada como geralmente `> 2 bar` e pode sofrer interferência de ruído ultrassônico.

[Seções 6.1.1-6.1.6 e Tabela 2, pp. 28-30; PDF pp. 15-16]

A Tabela 2 compara aplicação, CAPEX, OPEX/manutenção e vida útil. Consulte [tabelas-do-corpo.md](tabelas-do-corpo.md) para as células e a ambiguidade da aplicação mesclada. Use-a como comparação qualitativa do caderno; não faça seleção comercial final sem condições ambientais, alvo, geometria, manutenção e análise de risco.

## Alarmes

Exemplos de configuração apresentados:

- inflamáveis: alarme alto em 10-20% do LII; muito alto em 25-50% do LII;
- H2S: alarme alto em 8-15 ppm; muito alto em 50 ppm (50% do IDLH).

O caderno ressalta que o nível de ação não deve ser 100% do LII. Trate as faixas como exemplos/recomendações e confronte-as com filosofia da operadora e requisitos aplicáveis. [Seções 6.2.1-6.2.2, pp. 30-31; PDF p. 16]

## Mitigação e intertravamento

Possíveis ações: shutdown/intertravamento, controle de fontes de ignição, alarmes para evacuação e dilúvio. A decisão de intertravamento deve ser apoiada por análise de risco; não deduza automaticamente uma ação a partir de um único detector ou limiar. [Seção 6.3, pp. 31-32; PDF pp. 16-17]

## Disponibilidade

O caderno aborda comissionamento, testes de aceitação, manutenção/inspeção, documentação em listas de elementos críticos e tarefas de manutenção e lógica de votação. A votação pode reduzir trips espúrios, mas deve ser compatível com a capacidade da nuvem de alcançar detectores distintos e com as consequências da indisponibilidade. [Seção 6.4, pp. 32-33; PDF p. 17]

Checklist preliminar: tecnologia e gás-alvo; princípio e limitações; faixa/nível de alarme; posição e cobertura; ação associada; votação; comissionamento; teste funcional; manutenção/calibração; registro e rastreabilidade.
