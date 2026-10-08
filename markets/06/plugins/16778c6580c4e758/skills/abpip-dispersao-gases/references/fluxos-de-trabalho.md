# Fluxos de trabalho do caderno

Esta referência transforma dois fluxos visuais em sequências textuais rastreáveis. Ela não cria automação decisória nem substitui as condições detalhadas das seções correspondentes.

## Fluxo geral das quatro etapas

```text
Etapa I - Identificar a necessidade do estudo
   |
   v
Etapa II - Desenvolver o estudo de dispersão
   |
   v
Etapa III - Avaliar e posicionar detectores de gás
   |
   v
Etapa IV - Definir tecnologias e boas práticas de configuração
```

Localizador: [Seção 1.2, p. 10; PDF p. 6].

### Interpretação

- **Entrada:** demanda relacionada à dispersão ou ao sistema fixo de detecção.
- **Etapa I:** verificar os gatilhos apresentados no capítulo 3.
- **Etapa II:** definir documentos, dados, cenários, abordagem de modelagem, condições meteorológicas, taxas, contornos e relatório.
- **Etapa III:** usar os resultados para avaliar proteção de áreas de processo, sensíveis e congestionadas.
- **Etapa IV:** selecionar tecnologia e tratar alarmes, mitigação, votação, comissionamento e manutenção segundo a filosofia da operadora.
- **Saída:** subsídios rastreáveis para decisão profissional; não uma certificação automática.

O desenho é sequencial, mas a aplicabilidade de cada etapa depende do caso. Para condições `Sim/Não`, use o Anexo B.

## Fluxo dos nove passos da avaliação semiquantitativa

```text
1. Selecionar o modelo de liberação de hidrocarbonetos
   |
2. Aplicar o fator do material de processo
   |
3. Aplicar o fator de probabilidade de ocupação
   |
4. Aplicar o fator de probabilidade de ignição
   |
5. Aplicar o fator das condições de pressão do processo
   |
6. Aplicar o fator de congestionamento/confinamento da nuvem inflamável
   |
7. Aplicar o fator de congestionamento/confinamento da nuvem de gás tóxico
   |
8. Identificar o grau de desempenho do FGS
   |
9. Obter a meta de desempenho de detecção de gases
```

Localizadores: a ordem e os rótulos vêm da [Anexo A, Figura 1, p. 39; PDF p. 20]; a síntese explicativa também usa o detalhamento dos passos nas [pp. 40-46; PDF pp. 21-24].

### Entradas e saída

- **Entradas:** equipamento, fase/material, ocupação, fontes de ignição, pressão, congestionamento/confinamento e concentração tóxica aplicável.
- **Processamento descrito:** pontuações de probabilidade e consequência são ajustadas conforme as tabelas do Anexo A.
- **Saída:** classificação relativa e meta de cobertura conforme as Tabelas 9 e 10.

### Cautelas

- O fluxograma apresenta ordem, não autoriza cálculo autônomo pela skill.
- A validade depende da consistência entre condições reais e premissas da avaliação.
- Os fatores inflamáveis e tóxicos não são intercambiáveis.
- A Figura 1 chama o passo 7 de ajuste por congestionamento/confinamento, mas a seção detalhada e a Tabela 7 tratam de concentração de gás tóxico. Preserve e sinalize essa inconsistência editorial; não combine os critérios por inferência.
- O passo 1 é rotulado na figura como seleção do modelo de liberação, enquanto a seção detalhada começa pela seleção do equipamento e sua pontuação. Use a seção detalhada para explicar o conteúdo, sem rebatizar a figura.
- Os valores tabulares e as fronteiras não resolvidas estão em [tabelas-do-anexo-a.md](tabelas-do-anexo-a.md); o contexto do método permanece em [anexo-a-avaliacao-semiquantitativa.md](anexo-a-avaliacao-semiquantitativa.md).
