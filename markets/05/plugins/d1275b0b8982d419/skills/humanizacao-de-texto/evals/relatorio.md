# Resultado da validação inicial

Data: 8 de setembro de 2026.

## Verificações executadas

- Validador oficial `quick_validate.py` do skill-creator: aprovado.
- Metadados: nome de exibição, tamanho da descrição curta, invocação explícita no prompt e seleção implícita habilitada verificados.
- Links relativos dos arquivos Markdown: todos resolvem para arquivos existentes.
- Verificador de invariantes: 11 casos positivos aprovados.
- Testes do próprio verificador: seis versões deliberadamente adulteradas foram rejeitadas (percentual alterado, proibição invertida, termo técnico removido, numeração alterada, marca inventada e booleano modificado).

## Revisão editorial dos resultados

Ensaio realizado pelo próprio autor da skill, sem avaliador independente. Notas na escala 0–2 do protocolo:

| Caso | Fidelidade | Naturalidade | Adequação | Evidência |
|---|---:|---:|---:|---|
| ritmo | 2 | 2 | 2 | Remove transição vazia e preserva contraste com “Mas”. |
| fatos-ressalvas | 2 | 2 | 2 | Mantém atribuição, data, percentual, amostra e ausência de conclusão causal. |
| bloco-protegido | 2 | 2 | 2 | Mantém as duas proibições literalmente e conserva “pode”. |
| tecnico-citacao | 2 | 2 | 2 | Preserva regressão robusta, óleo essencial e fala citada. |
| lista-formula | 2 | 2 | 2 | Mantém diagnóstico e plano, três itens e a sequência de ações. |
| sem-exemplo-novo | 2 | 2 | 2 | Corta apenas o aquecimento e não cria exemplos. |
| neutralidade | 2 | 2 | 2 | Mantém ausência de preferência e condição orçamentária. |
| ja-natural | 2 | 2 | 2 | Não modifica texto que já atende. |
| json | 2 | 2 | 2 | Muda só o texto; mantém tipos, chaves e data. |
| restricao-briefing | 2 | 2 | 2 | Não inventa benefício comercial nem publica o briefing. |
| sem-texto | 2 | 2 | 2 | Pede o material necessário, sem inventar conteúdo. |

Os quatro pedidos negativos (resumo, ortografia isolada, voz de marca e tradução) foram confrontados com os limites da descrição, que os exclui explicitamente. Isso é revisão de escopo, não teste de seleção automática.

## Limites

Não foi executado um teste de descoberta/ativação em nova sessão do Codex. A instalação e a configuração permitem essa avaliação, mas não garantem seleção em toda formulação de pedido. Não foi avaliada voz de marca, que está fora do escopo por solicitação do usuário.

O primeiro ensaio revelou uma checagem literal sensível à maiúscula inicial (“marcas” versus “Marcas”); o caso foi corrigido para aceitar a capitalização inicial da frase, sem alterar os testes de blocos protegidos. PyYAML foi obtido apenas na pasta temporária de trabalho para executar o validador oficial; a skill instalada não depende dele para funcionar. O verificador incluído usa somente a biblioteca padrão do Python.
