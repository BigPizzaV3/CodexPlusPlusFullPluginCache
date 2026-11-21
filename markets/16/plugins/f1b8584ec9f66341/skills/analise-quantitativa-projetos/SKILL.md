---
name: analise-quantitativa-projetos
description: Use para calcular, conferir ou interpretar indicadores de valor agregado (EVM), cronograma CPM e PERT, estimativas de custos, riscos quantitativos e simulação de cenários em projetos.
---

# Análise quantitativa de projetos — DIGG.IA

Não invente observações. Solicite dados essenciais ausentes somente se impedirem o cálculo pedido; se o usuário pede um exemplo, use dados hipotéticos claramente rotulados. Use a skill geral `gestao-projetos` para governança e comunicação dos resultados, quando disponível.

## Earned Value Management
Dados obrigatórios: PV (planned value), EV (earned value), AC (actual cost), mesma moeda, mesmo instante de corte, critérios de medição de EV e unidade. Se disponível, BAC (budget at completion). Definições:
- CV = EV − AC; SV = EV − PV.
- CPI = EV / AC, se AC > 0; SPI = EV / PV, se PV > 0.
- EAC pode seguir BAC / CPI **somente como hipótese de permanência do desempenho**, com BAC e CPI válidos. Alternativas: AC + (BAC − EV) para ETC a custo orçado; AC + (BAC − EV)/CPI para extrapolar CPI. Justifique a fórmula; não escolher automaticamente.
- ETC = EAC − AC; VAC = BAC − EAC. Projeções não são resultados observados.
- Se denominador 0 ou dados incompatíveis, indicar não calculável, sem substituir valores arbitrários.
- Indicadores de cronograma baseados em valor não representam por si só atraso em unidades de tempo; EVM não demonstra risco, causa ou performance futura sem evidência.

## CPM
Exija atividades, durações não negativas, calendário, relações e predecessoras coerentes. Para rede acíclica FS sem defasagens: ES = máximo(EF dos predecessores), EF = ES + duração; backward pass LF = mínimo(LS dos sucessores), LS = LF − duração. Folga total = LS − ES; caminho crítico tem folga nula dentro do modelo. Quando houver múltiplos caminhos, calendários especiais e lags, explicite a complexidade. Não afirmar datas reais sem calendário e data de início.

## PERT
Para estimativas three-point: E=(O+4M+P)/6 e variância=((P−O)/6)^2, com O≤M≤P, mesmo conjunto de unidades. Cálculos de probabilidade pressupõem condições adicionais; não declarar prazo garantido nem distribuições sem premissas.

## Monte Carlo
Só declarar simulação executada quando de fato houver ferramenta de cálculo e registro de amostragem, hipóteses, correlação, distribuições, número de iterações e semente (se aplicável). Caso contrário, fornecer **plano de simulação**, fórmula, pseudocódigo ou cenário ilustrativo, marcado não executado. Não inventar percentis P50/P80 nem probabilidades.

## Entrega
Mostrar fórmulas, substituição, unidades e arredondamento; apresentar interpretação e ao menos uma limitação material; distinguir resultado observado de prognóstico. Conferir consistência dimensional e financeira antes da conclusão.
