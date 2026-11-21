# DIGG.IA: Assistente de Gestão de Projetos — 1.1.3

Plugin portátil **skills-only**, formato Agent Plugins 1.0. O nome oficial é **DIGG.IA: Assistente de Gestão de Projetos**; o título abreviado `DIGG.IA: Gestão de Projetos` satisfaz o limite técnico de 30 caracteres da listagem. Não há MCP server, aplicativo embutido, Python executável em runtime ou persistência automática.

## Sete skills, ativação condicional
1. `gestao-projetos`: núcleo de governança e roteamento.
2. `goal-finish-line` (GFL 0.1.1): definição estável de objetivos, aceites e conclusão verificada.
3. `zero-to-goal` (0TG 0.1.1): Marco 0, plano progressivo, evidências e handoff à GFL.
4. `loop-graph-engineering` (LGE 2.10.2): arquitetura mínima suficiente, loops, grafos, segurança e limites de execução.
5. `ask-user-question` (AUQ 2.1.2): perguntas proporcionais para lacunas materiais, sem UI obrigatória.
6. `analise-quantitativa-projetos`: EVM, CPM, PERT e cálculos gerenciais.
7. `pmbok8-rastreabilidade`: especialização com exigência de fonte primária para atribuições PMI.

## Integração
- Entrada geral: `skills/gestao-projetos/SKILL.md`.
- Contrato de divisão de responsabilidades: `skills/gestao-projetos/references/orquestracao-competencias.md`.
- Versões originais, SHA-256 e ressalvas de compatibilidade: `integration/provenance.json`. A suíte `integration/casos-aceitacao.yaml` registra 14 cenários para testes futuros, não executados.
- Cada skill nova contém uma adaptação `SKILL.md` e a **especificação YAML original integral** em `references/source.yaml`.
- A GFL é responsável pela decisão terminal; o 0TG não declara FINISH. LGE não redefine metas, AUQ não presume autorização.

## Testes, status e limitações
A validade de empacotamento, parse de YAML/JSON e verificações de integridade podem ser testadas offline; isso **não** comprova que o modelo escolhe skills corretamente em execução. GFL/0TG estão em `pilot_observation`, LGE/AUQ em `implementation_candidate`. A compatibilidade cruzada LGE 2.10.2/AUQ 2.1.2 com contratos históricos do 0TG exige avaliação comportamental. Não alegar execução de motor Python local, interfaces JS, ações externas, validação humana ou funcionamento de MCP inexistente.

## Licenças
O pacote mantém o índice do PMBOK® 8 sem incluir o PDF do manual, tradução ou a biblioteca `livros.zip`. Estes materiais têm restrições de redistribuição não resolvidas. As especificações adicionais foram fornecidas pelo usuário para incorporação; antes de publicar publicamente, confirmar titularidade e autorizações aplicáveis. PMBOK® e PMI pertencem aos respectivos titulares; este plugin não é afiliado ao PMI.

## Publicação
A estrutura técnica do ZIP não substitui validação da OpenAI Platform. Os quatro URLs institucionais estão declarados no manifesto. Para publicação pública, permanecem pendentes a verificação do publisher e a avaliação do conteúdo de suporte, privacidade e termos quanto à cobertura específica desta ferramenta. A instalação por conta privada também depende de aceitação do pacote no serviço.

## Conferência da LGE 2.10.2 — release 1.1.2
A referência `skills/loop-graph-engineering/references/source.yaml` já estava integrada na versão 1.1.1 e é **idêntica byte a byte** ao arquivo `skill_LGE_v2_10_2.yaml` apresentado para esta atualização. Não há duplicação nem substituição de instruções.

- SHA-256 do YAML preservado: `bc42f3f95432bffd8fa54fd2de1c6f26880b34ee8f3bfde096919fcb60db10da`.
- A skill é descoberta em `skills/loop-graph-engineering/SKILL.md` e acionada condicionalmente; GFL mantém Goal/Finish Line, 0TG governa marcos, AUQ trata apenas lacunas materiais.
- Versão do pacote: **1.1.2**. As sete skills e as respectivas bases de referência continuam com os mesmos bytes das versões anexadas.
- Os 14 cenários de aceitação permanecem **NOT_RUN**: sua existência não comprova efetividade operacional nem aprovação pela OpenAI Platform.

## Atualização 1.1.3 — prompt inicial
A revisão atual utiliza como fonte o arquivo ZIP v1.1.2 fornecido, cujo `plugin.json` já contém o `defaultPrompt` atualizado pelo usuário. A versão 1.1.3 preserva **exatamente** esse texto, inclusive em `extensions.com.openai.review.prompts`. Não foi fornecido um pacote anterior distinto para comprovar a diferença textual em relação à versão pré-alteração. Todas as sete Skills, as bases em `references/` e o ícone permanecem inalterados. Os 14 cenários de aceite seguem declarados, não executados. A validação não abrange a aceitação pela OpenAI Platform nem testes comportamentais de runtime.
