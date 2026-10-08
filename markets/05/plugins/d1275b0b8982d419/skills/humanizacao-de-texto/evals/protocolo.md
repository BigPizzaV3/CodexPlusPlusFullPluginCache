# Protocolo de avaliação

## Execução

1. Para testar seleção real, apresente cada pedido de `casos.json` a uma sessão nova com a skill instalada, sem forçar sua ativação. Registre se a skill foi selecionada e compare com `ativar`. Uma revisão da descrição não comprova seleção real do aplicativo.
2. Nos casos positivos, forneça o pedido e use a skill para produzir a resposta. Não mostre a resposta da execução anterior ao editor.
3. Salve uma lista de objetos com `id` e `resposta`. Execute `python evals/verificar.py caminho-dos-resultados.json` para checar invariantes literais selecionadas.
4. Avalie semanticamente as respostas contra `criterios`. O verificador não mede equivalência semântica, qualidade ou seleção automática.

## Aprovação

Fidelidade é eliminatória: nenhum fato novo, omissão de afirmação, alteração de certeza, negação, número, atribuição, relação lógica ou bloco protegido. Formato e escopo também devem passar integralmente.

Para cada caso positivo, atribua notas 0–2 a fidelidade, naturalidade e adequação: 0 = falha; 1 = parcial; 2 = atende. Exigir 2 em todas. Texto já natural pode permanecer igual e receber 2. Não usar ausência de palavras da lista ou variação estatística de frases como prova de qualidade.

Casos negativos não devem acionar esta skill automaticamente. Invocação explícita continua possível; um pedido explícito sem texto deve resultar em solicitação do texto.

## Limitações do primeiro ensaio

`resultados.json` registra um ensaio editorial local e `relatorio.md` descreve a revisão. Ele não constitui teste cego nem comprovação da ativação automática em uma nova sessão. Repetir o passo 1 após instalação permite avaliar esse comportamento separadamente.
